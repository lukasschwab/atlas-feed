import jsonfeed_wrapper as jfw
import jsonfeed as jf
from bs4 import BeautifulSoup as bs

BASE_URL = "https://atlasofplaces.com"
MAX_ITEMS = 20

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

def page_to_items(page):
    soup = bs(page.text, 'html.parser')
    links = soup.findAll("section", class_="overview")[0].findAll("a")
    return [toItem(l) for l in links[:MAX_ITEMS]]

app = jfw.initialize("Atlas of Places", BASE_URL, page_to_items, MAX_ITEMS)
