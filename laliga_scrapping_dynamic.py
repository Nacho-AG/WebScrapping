#!/usr/bin/env python
# -*- coding: 850 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Web we want to scrape into
URL = 'https://www.marca.com/movil/tabla_marcadores.html?c=futbol_1adivision'
# Location of the previously installed chromedriver
PATH = 'chromedriver.exe'

def has_class(web_element, elem_class):
    return elem_class in web_element.get_attribute('class').split(' ')

def main():
    # Open a browser that we can control with selenium
    browser = webdriver.Chrome(executable_path=PATH)
    # Look for the URL we want to scrap
    browser.get(URL)

    # WEB-DRIVING

    # Go through every week of the ligue and get the results
    with open('results.txt','w', encoding='utf-8') as file:
        last_week = False
        week=0
        file.write("LOCAL_TEAM, LOCAL_SCORE, VISITING_SCORE, VISITING_TEAM\n")
        while(not last_week):
            week += 1
            print('Ready for week: ' + str(week))
            # Get the matches from this week
            # Wait for the results to be loaded 
            matches = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'final')))
            # Go throught the week matches
            for match in matches[::2]:
                info = match.find_elements_by_tag_name('a')
                teams, score = info
                teams = teams.text.split(' - ')
                score = score.text.split('-')
                file.write('{},{},{},{}\n'.format(teams[0], score[0], score[1], teams[1]))
            # Check if it is the last week of the ligue
            prev_btn = browser.find_elements_by_class_name('bloque-prev')
            last_week = has_class(prev_btn[0], 'disabled')
            # If there are more weeks go for the next one
            if (not last_week):
                prev_btn[0].click()

    browser.close()

if __name__ == "__main__":
    main()