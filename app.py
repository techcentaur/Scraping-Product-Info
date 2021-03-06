from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request, session, abort

from scraper import Amazon, eBay

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/info", methods=['POST'])
def info():
    if request.method == 'POST':
        link = request.form['link']
    else:
        raise ValueError

    if link.find("amazon") != -1:
        data = Amazon().Amazon_parser(link)
    elif link.find("ebay") != -1:
        data = eBay().eBay_parser(link)

    if data:
        pass
    else:
        flash('Incorrect link! Please insert a correct one.')
        return redirect(url_for('index'))

    return render_template('product.html', data = data)

if __name__=="__main__":
    app.run(debug=True)
