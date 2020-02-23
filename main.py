from bottle import route, request, response, run, template, Bottle, static_file, HTTPError
import requests
from bs4 import BeautifulSoup as bs
import jsonfeed as jf

BASE_URL = "https://atlasofplaces.com/"
ERROR_MESSAGES = {
    404: "This category could not be resolved in Atlas of Places."
}

# NOTE: typical structure:
# <a href="/cinema/dr-strangelove/">
#   <div>
#     <em></em>
#     <img
#       alt="Stanley Kubrick: Dr. Strangelove"
#       class="lazy"
#       data-src="https://www.atlasofplaces.com/atlas-of-places-thumbnails/_thumbnail/ATLAS-OF-PLACES-STANLEY-KUBRICK-DR-STRANGELOVE-IMG-5.jpg"
#     />
#   </div>
#   <span>
#     <small>Stanley Kubrick</small>
#     <br/>
#     Dr. Strangelove
#   </span>
# </a>
def toItem(link):
    url = link["href"]
    text = link.find("span").text.split("\n")
    image = link.find("img")
    return jf.Item(
        id=url,
        url=BASE_URL+url,
        title=text[1],
        author=jf.Author(name=text[0]),
        content_html=link.prettify().replace("data-src", "src"),
        image=image["data-src"],
        tags=text
    )

# TODO: cache.
def getRecentItems(category=""):
    specific_url = BASE_URL + category
    page = requests.get(specific_url)
    soup = bs(page.text, 'html.parser')
    if not page.ok:
        raise HTTPError(
            status=page.status_code,
            body=ERROR_MESSAGES.get(page.status_code)
        )
    links = soup.findAll("section", class_="overview")[0].findAll("a")
    recentLinks = links[:20]
    # Render the output feed.
    res = jf.Feed(
        title="Atlas of Places" if len(category) == 0 else "Atlas of Places: %s" % category,
        home_page_url=BASE_URL+category,
        feed_url="https://atlas-feed-dot-arxiv-feeds.appspot.com",
        items=[toItem(l) for l in recentLinks]
    )
    return res.toJSON()

app = Bottle()

@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./static', mimetype='image/x-icon')

# Serve index.
@app.route('/')
def entry():
    response.content_type = 'application/json'
    return getRecentItems()

# Serve Atlas of Places categories. Supported categories at this time:
#   academia, architecture, cartography, cinema, essays, painting, photography,
#   research
@app.route('/<category>')
def subset(category):
    response.content_html = 'application/json'
    return getRecentItems(category=category)
