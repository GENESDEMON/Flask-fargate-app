import requests

from flask import Flask, render_template
app = Flask(__name__)

API_KEY = "b775a8d75663454e923e385d9c6e518b"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=%s" % API_KEY

def get_news_articles():
    # fetch the news articles
    response = requests.get(NEWS_API_URL)

    # return the articles in json format
    return response.json()['articles']

@app.route("/")
def index():
    return str(get_news_articles())