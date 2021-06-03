## import dependents

from bs4 import BeautifulSoup
import requests
import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_indy import scrapper

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/indy500"
mongo = PyMongo(app)

@app.route("/")
def home():
    most_recent = mongo.db.indy_mongo.find({})
    return render_template("index.html",
        most_recent = most_recent)
    
@app.route('/scrape')
def scrape():
    indy_mongo = mongo.db.indy_mongo
    indy_info = scrapper()
    indy_mongo.update({}, indy_info, upsert=True)

if __name__ == "__main__":
    app.run(debug=True)