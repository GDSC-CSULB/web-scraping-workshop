from bs4 import BeautifulSoup
import requests

billboard_url = "https://www.billboard.com/charts/hot-100/"

main_container_class = "chart-results-list"
each_row_class = "o-chart-results-list-row-container"

def extract_billboard(req, up_to):
    songs = []
    full_doc = req.find("div", {"class":main_container_class})
    result = full_doc.find_all("div", {"class": each_row_class})
    print(type(result))

    for r in result:
        data = r.find("ul", {"class":"o-chart-results-list-row"})
            
    return songs

req = requests.get(url=billboard_url, headers = {"User-Agent": "XY"} )
dict_result = extract_billboard(BeautifulSoup(req.text, "html.parser"), up_to=100)
