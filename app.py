from flask import Flask
from flask import flash, redirect, render_template, request, session, abort

from scraper import Amazon

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/info/<link>", methods=['GET'])
def info(link):
    s = Scraper(link)
    data = s.get_data()

    if data.status:
        pass
    else:
        flash('Incorrect link! Please insert a correct one.')
        return redirect(url_for('index'))

    return render_template('product.html', data = data)

if __name__=="__main__":
    app.run(debug=True)
