from bottle import route, request, response, run, template, Bottle
import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://atlasofplaces.com"

FEED_METADATA = {
    "version": "https://jsonfeed.org/version/1",
    "title": "Atlas of Places",
    "home_page_url": BASE_URL,
    "feed_url": "https://atlas-feed-dot-arxiv-feeds.appspot.com"
}

# <a href="/cinema/dr-strangelove/">
#  <div>
#   <em>
#   </em>
#   <img alt="Stanley Kubrick: Dr. Strangelove" class="lazy" data-src="https://www.atlasofplaces.com/atlas-of-places-thumbnails/_thumbnail/ATLAS-OF-PLACES-STANLEY-KUBRICK-DR-STRANGELOVE-IMG-5.jpg"/>
#  </div>
#  <span>
#   <small>
#    Stanley Kubrick
#   </small>
#   <br/>
#   Dr. Strangelove
#  </span>
# </a>
def toItem(link):
    url = link["href"]
    text = link.find("span").text.split("\n")
    image = link.find("img")
    return {
        "id": url,
        "url": BASE_URL + url,
        "title": text[1],
        "author": {"name": text[0]},
        "content_html": link.prettify().replace("data-src", "src"),
        "image": image["data-src"],
        "tags": text
    }

# TODO: cache.
def getRecentItems():
    page = requests.get(BASE_URL)
    # TODO: check page status.
    soup = bs(page.text, 'html.parser')
    links = soup.findAll("section", class_="overview")[0].findAll("a")
    recentLinks = links[:20]
    res = FEED_METADATA.copy()
    # TODO: error handling.
    res["items"] = [toItem(l) for l in recentLinks]
    return res

app = Bottle()

# Serve index.
@app.route('/')
def entry():
    response.content_type = 'application/json'
    return getRecentItems()
