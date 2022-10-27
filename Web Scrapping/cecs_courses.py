from bs4 import BeautifulSoup
import requests
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
    
    return result