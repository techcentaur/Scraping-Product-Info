from flask import Flask
from flask import flash, redirect, render_template, request, session, abort

from scraper import Scraper

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/info", methods=['GET'])
def info(link):
    s = Scraper(link)
    data = s.get_data()

    return render_template('product.html', data = data)

@app.route("/error", methods=['GET'])
def error():
    
    return render_template('error.html')


if __name__=="__main__":
    app.run(debug=True)
