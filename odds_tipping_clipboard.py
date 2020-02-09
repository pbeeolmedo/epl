#!/usr/bin/env python
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import time
import pickle
import pandas as pd

pickle_dest = "scores_string.bin"

def odds_scrape(out_file):   
    next_url = "https://www.oddsportal.com/soccer/england/premier-league/"

    options = FirefoxOptions()
    #options.add_argument("--headless")
    #options.add_argument("--incognito")
    driver = webdriver.Firefox(options=options)

    driver.get(next_url)
    driver.find_element_by_xpath("//a[@id='user-header-timezone-expander']/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='timezone-content']/a[75]/span").click()

    el = driver.find_element_by_xpath('//*[@id="tournamentTable"]').text

    #print(el)
    with open(out_file,'wb') as out_file: 
        pickle.dump(el,out_file,protocol = 1)
    
    driver.close()

def isfloat(value):
    try:
        float(value)
        if "." in value:
            return True
        else:
            return False
    except ValueError:
        return False

        
#odds_scrape(pickle_dest)

with open(pickle_dest,'rb') as in_file: 
    odds_str = pickle.load(in_file)

odds_str = odds_str.splitlines()
print(odds_str)

games = [s for s in odds_str if ( ":" in s or isfloat(s) )]
print(games)
print(games[0].split(" "))
print(games[0].split(" ").index("-"))
print(games[1].split(" "))

i = 0 
new_list = []
while games:
    list_item = games.pop(0)

    if i == 0:
        teams = list_item.split(" ")
        hyphen_index = teams.index("-")
        home = " ".join(teams[1:hyphen_index])
        away = " ".join(teams[hyphen_index+1:])
    elif i == 1:
        home_odds = float(list_item)
    elif i == 2:
        draw_odds = float(list_item)
    elif i == 3:
        away_odds = float(list_item)

        new_list.append((home,home_odds,draw_odds,away_odds,away))
        i = -1


    i += 1

print(new_list)

# Generate dataframe from list and write to xlsx.
df = pd.DataFrame(new_list)

#df.to_excel('output.xlsx',header=False, index=False)


df.to_clipboard(excel=True, header=False, index=False)








