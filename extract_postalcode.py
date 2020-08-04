import requests
from lxml import html

def extract_postalcode(URL):
    """
    URL: "http://www.geonames.org/postalcode-search.html?q=&country=NL"
    return: List of all the Postal codes
    Function scrape the URL and returns all The Netherlands Postal Code.
    """
    try:
        resp = requests.get(url=URL,
                            headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
                            })
    except requests.exceptions.ConnectionError as e:
        print(repr(e))
    else:
        resp = resp.text.encode('ascii', 'ignore').decode('utf-8')
        tree = html.fromstring(html=resp)
        postal_code = tree.xpath(
            "//table[@class='restable']//td/small[not(self::a)]/ancestor::td[1]/following-sibling::td[2]/text()")
        return postal_code
