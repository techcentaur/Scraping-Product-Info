import requests
from lxml import html
from time import sleep

class Ebay:
    def __init__(self):
        print("okay")
        pass

    def ebay_parser(self, link):
        print("okay2")
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
        page = requests.get(link, headers=headers)
        print("okay3")
        try:
            doc = html.fromstring(page.content)
            TITLE = '//h1[@id="itemTitle"]//content()'
            CAT = '//td[@id="vi-VR-brumb-lnkLst"]//text()'
            SHIPPING_COST = '//span[@id="fshippingCost"]//text()'
            SHIPPING_SVC = '//span[@id="fShippingSvc"]//text()'
            PAY = '//div[@id="payDet1"]//text()'
            SOLD = '//span[@class="w2b-sgl"]//text()'

            RAW_TITLE = doc.xpath(TITLE)
            RAW_CAT = doc.xpath(CAT)
            RAW_SHIP_COST = doc.xpath(SHIPPING_COST)
            RAW_SHIP_SVC = doc.xpath(SHIPPING_SVC)
            RAW_PAY = doc.xpath(PAY)
            RAW_SOLD = doc.xpath(SOLD)

            _title = RAW_TITLE[1]
            for i in RAW_CAT:
                if (not i.startswith('\n')) or (not i.startswith('\t')):
                    _cat.append(i)
            _cat = " ".join(_cat)

            _ship_cost = ' '.join(''.join(RAW_SHIP_COST).split()) if RAW_SHIP_COST else None
            _ship_svc = ' '.join(''.join(RAW_SHIP_SVC).split()) if RAW_SHIP_SVC else None
            
            _paystr = "".join(RAW_PAY)
            for i in ['\n', '\t', '\xa0']:
                _paystr = _paystr.replace(i, '')

            _sold = " | ".join(RAW_SOLD)

            data = {
            'title': _title,
            'category': _cat,
            'ship':{
                    'cost': _ship_cost,
                    'service': _ship_svc
                    },
            'payment': _paystr,
            'sold': _sold
            }

            print(data)

        except Exception as e:
            print(e)
        return True

if __name__=="__main__":
    e = Ebay().ebay_parser("https://www.ebay.in/itm/portable-rugby-wireless-bluetooth-mini-stereo-speaker-fm-radio-usb-microsd/292105966607?hash=item4402df540f")