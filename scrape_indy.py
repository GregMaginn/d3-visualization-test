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
        #for colNum in columnArray:
         #   print(columnArray[x].text)
          #  x =x+1

        while x < len(columnArray):
            print(columnArray[x].text)
            x =x+1
        #for result in bodyRows:
         #   print(f'Finishing Position: {result.text[0]}')
          #  print(f'Qualifying Position: {result.text[1]}')
           # print(f'Car Number: {result.text[2]}')
            #print(f'Driver Name: {result.text[3]}')
            #need to split string on ()
            #print(f'Sponsor/Owner: {result.text[4]}')
            #need number between C/ and /F to find engine maker
            #print(f'Engine: {result.text[5]}')
            #print(f'Laps Completed: {result.text[6]}')
            #print(f'Laps Lead: {result.text[8]}')
            #print(f'Points Awarded: {result.text[9]}')
            #print('=======================')
scraper()