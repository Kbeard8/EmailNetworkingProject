from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("/Users/kobybeard/Desktop/EmailProj/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://www.google.com")