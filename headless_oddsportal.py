#!/usr/bin/env python
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

url = "https://www.oddsportal.com/soccer/england/premier-league/results/#/page/1/"
next_url = "https://www.oddsportal.com/soccer/england/premier-league/"

options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get(next_url)

#driver.find_element_by_xpath("//a[@id='user-header-timezone-expander']/span").click()
#driver.find_element_by_xpath("//div[@id='timezone-content']/a[75]/span").click()
#driver.get(next_url)


el = driver.find_element_by_xpath('//*[@id="tournamentTable"]').text

driver.close()
print(el)