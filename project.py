from pydoc import classname
from traceback import print_tb
from selenium.webdriver.common.by import By
from selenium import webdriver
import itertools 

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\\Users\HP\OneDrive\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get("https://www.careerguide.com/career-options")

subCat = []
subCat = driver.find_elements(By.TAG_NAME, 'h2')

val = []
for element in  subCat:
    val.append(element.text)


#linkdin
state = ['Maharashtra, India', 'Karnataka, India']

for job in val[:2]:
    print("Cat: ", job) 
    
    for st in state:
        
        print()
        print("State: ", st)
        print() 
        
        driver.get("https://www.linkedin.com/jobs/")
        driver.find_element(By.NAME, 'location').clear()
        driver.find_element(By.NAME, 'location').send_keys(st)
        ele = driver.find_element(By.NAME, 'keywords')
        ele.send_keys(job)
        ele.send_keys(Keys.RETURN)

        job_position = []
        company_name = []
        location = []


        job_position = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')
        company_name = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')
        location = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')


        temp = []
        for (element, cname, loc) in zip(job_position, company_name, location):
            print("Job position: ", element.text)
            print("Company Name: ", cname.text)
            print("Location: ", loc.text)
            print()
            print()
    print('--------------------------------')
    print()
