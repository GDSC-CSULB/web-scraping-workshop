import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
rows = soup.find_all("ul", {"class": "o-chart-results-list-row"})

for row in rows:
    list_items = row.find_all('li', recursive=False)

    rank = list_items[0].find("span")
    title = list_items[-1].find("h3")
    artist = list_items[-1].find("span")
    print(rank.text.strip(), title.text.strip(), artist.text.strip())