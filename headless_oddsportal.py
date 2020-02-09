#!/usr/bin/env python
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import time
from text_to_file import text_to_file

output_file = "Output.txt"

def epl_results_page(i):
    return f"https://www.oddsportal.com/soccer/england/premier-league/results/#/page/{i}/"
    
next_url = "https://www.oddsportal.com/soccer/england/premier-league/"

options = FirefoxOptions()
options.add_argument("--headless")
#options.add_argument("--incognito")
driver = webdriver.Firefox(options=options)
driver.get(next_url)
driver.find_element_by_xpath("//a[@id='user-header-timezone-expander']/span").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='timezone-content']/a[75]/span").click()


open(output_file,"w").close()

for i in range(8,0,-1):
    url = epl_results_page(i)
    driver.get(url)
    time.sleep(3)
    el = driver.find_element_by_xpath('//*[@id="tournamentTable"]').text
    if "No data available" in el:
        continue
    text_to_file(url)
    text_to_file(el)

driver.get(next_url)
el = driver.find_element_by_xpath('//*[@id="tournamentTable"]').text
text_to_file(el)

driver.close()


