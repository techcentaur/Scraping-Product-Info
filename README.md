# Scraping-Product-Info

Flask app for scraping product information, given a link of product from Amazon or eBay.

### Usage
Run the flask app
```console
gavy42@jarvis:~$ export FLASK_APP=app.py
gavy42@jarvis:~$ flask run
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

On an example link -  https://www.ebay.com.au/itm/Oneal-2018-Sierra-Dual-Sport-Full-Face-Helmet-Sniper-Black-White-Motocross-Mx-Di/292151534808`

Output would be - 

![Web-output](https://github.com/techcentaur/Scraping-Product-Info/blob/master/static/prodinfoans.png)

### Scraper
`scraper.py` contains 2 separate classes for scraping from Amazon and eBay.

Sample command line usage would be like this - 

```console
>>> from scraper import (Amazon, eBay)
>>> a = Amazon().Amazon_parser(<link>)
>>> e = eBay().eBay_parser(<link>)
```

### Contribution

Sure. Why not?