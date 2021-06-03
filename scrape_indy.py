import os
from re import X
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

def scraper():
    indy_results_url = "https://www.racing-reference.info/race-results/2021-06/O/"

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(indy_results_url)

    html= browser.html

    soup = BeautifulSoup(html, 'html.parser')

    #identify the specific table needed
    results = soup.find_all('table', attrs={'class': 'tb race-results-tbl'})
    table = results[0]

    body = table.find_all('tr')
    
    tHead = body[0]
    bodyRows = body[1:]
    
    for rowNum in range(len(bodyRows)):
        columnArray = bodyRows[rowNum].find_all('td')
        x = 0
        print(f'Finishing Position: {columnArray[0].text}')
        print(f'Qualifying Position: {columnArray[1].text}')
        print(f'Car Number: {columnArray[2].text}')
        print(f'Driver Name: {columnArray[3].text}')
        #need to split string on ()
        print(f'Sponsor/Owner: {columnArray[4].text}')
        #need number between C/ and /F to find engine maker
        print(f'Engine: {columnArray[5].text}')
        print(f'Laps Completed: {columnArray[6].text}')
        print(f'Laps Lead: {columnArray[8].text}')
        print(f'Points Awarded: {columnArray[9].text}')
        print('=======================')

        #while x < len(columnArray):
         #   print(columnArray[x].text)
          #  x =x+1
scraper()