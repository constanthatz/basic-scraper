import requests
from bs4 import BeautifulSoup
import sys
import re


INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {'Output': 'W',
                     'Business_Name': '',
                     'Business_Address': '',
                     'Longitude': '',
                     'Latitude': '',
                     'City': '',
                     'Zip_Code': '98103',
                     'Inspection_Type': 'All',
                     'Inspection_Start': '',
                     'Inspection_End': '',
                     'Inspection_Closed_Business': 'A',
                     'Violation_Points': '',
                     'Violation_Red_Points': '',
                     'Violation_Descr': '',
                     'Fuzzy_Search': 'N',
                     'Sort': '',
                     }


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    with open('inspection_page.html', "w") as fo:
        fo.write('%s\n%s' % (resp.encoding, resp.content))
    return resp.content, resp.encoding


def load_inspection_page(file):
    with open('inspection_page.html', "r") as fo:
        encoding = fo.readline()
        html = ''
        for line in fo:
            html += line
    return html, encoding


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed


def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def has_two_tds(elem):
    is_tr = elem.name == 'tr'
    td_children = elem.find_all('td', recursive=False)
    has_two = len(td_children) == 2
    return is_tr and has_two

if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = load_inspection_page('inspection_page.html')
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    listings = extract_data_listings(doc)
    print len(listings)
    print listings[0].prettify()
    print doc.prettify(encoding=encoding)
