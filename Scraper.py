from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains   
from selenium.webdriver.common.keys import Keys as Keys
from bs4 import BeautifulSoup
import json
import time

"""
Scraping linkedin: https://www.geeksforgeeks.org/scrape-linkedin-using-selenium-and-beautiful-soup-in-python/
https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
"""

#get password from json
with open("passwords.json") as file:
    data = json.load(file)
    pswd = data["linkedin"]
#pswd = input("What is your LinkedIn password?")

s = Service("/Users/kobybeard/Desktop/EmailProj/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://linkedin.com/uas/login")
time.sleep(5)
# entering username
username = driver.find_element(By.ID, "username")           
username.send_keys("kobybeard@gmail.com") 

# entering password
password = driver.find_element(By.ID, "password")
password.send_keys(pswd)

# clicking sign in button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

company_link = "https://www.linkedin.com/company/oracle"
company_link += "/people/?keywords=software%20engineer"

driver.get(company_link)

#Getting people names
src = driver.page_source
soup = BeautifulSoup(src, 'lxml')
#people = soup.find('div', {"class": "scaffold-finite-scroll__content"})
print(soup.prettify())





# # Searches company name and then hits enter
# search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
# search.send_keys("Oracle")
# actions = ActionChains(driver) 
# actions.send_keys(Keys.ENTER)
# actions.perform()

time.sleep(20)
