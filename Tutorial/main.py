from msilib.schema import Billboard
from bs4 import BeautifulSoup
import requests

Billboard_URL = "https://www.billboard.com/charts/hot-100/"
URL = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2023/By_Subject/CECS.html"
def get_all_cecs_courses():
    wrapper_id = "pageContent"
    course_code_id = "courseCode"
    course_title_id = "courseTitle"
    
    result = []
    
    res = requests.get(URL) # HTML doc
    
    obj = BeautifulSoup(res.content, 'html.parser')

    wrapper = obj.find(id=wrapper_id)

    courseCodes = wrapper.find_all("span", {"class": course_code_id})
    courseTitles = wrapper.find_all("span", {"class": course_title_id})

    for i in range(len(courseCodes)):
        result.append( (courseCodes[i].text, courseTitles[i].text) )
    
    print(result)

def scrape_billboard():
    html = requests.get(Billboard_URL)
    obj = BeautifulSoup(html.content, 'html.parser')
    wrapper_class_name = "chart-results // lrv-a-wrapper lrv-u-padding-lr-00@mobile-max"
    item_class = "o-chart-results-list-row-container"
    obj = obj.find("div", {"class": wrapper_class_name})
    items = obj.find_all("div", {"class": item_class})

    for item in items:
        list_items = item.find("ul").find_all("li", recursive=False)
        rank = list_items[0].find("span").text.strip()
        title = list_items[-1].find("h3").text.strip()
        artist = list_items[-1].find("span").text.strip()
        print(rank, end="\t")
        print(title, end="\t")
        print(artist)

def main():
    scrape_billboard()

main()