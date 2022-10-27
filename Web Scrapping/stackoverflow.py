from bs4 import BeautifulSoup
import requests

URL = "https://insights.stackoverflow.com/survey/2021"
id = ""
req = requests.get(url=URL)
soup = BeautifulSoup(req.text, "html.parser")

def most_popular_lang():
    id = "most-popular-technologies-language"
    wrapper = soup.find("figure", id=id).find("table")
    items = wrapper.find_all("tr")

    for item in items:
        for i in item.find_all("td"):
            print(i.text.strip(), end="\t")
        print()

