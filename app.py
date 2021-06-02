## import dependents

from bs4 import BeautifulSoup
import requests
import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_indy import scrapper

