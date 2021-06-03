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
    x = 0
    for result in bodyRows:
        x = x+1
        print(x)
        print(result.text)


scraper()