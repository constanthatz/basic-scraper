import requests
from bs4 import BeautifulSoup
import sys
import re


DOMAIN = 'http://info.kingcounty.gov'
PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
PARAMETERS = {'Output': 'W',
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
    url = DOMAIN + PATH
    parameters = PARAMETERS.copy()
    for key, val in kwargs.items():
        if key in PARAMETERS:
            parameters[key] = val
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.encoding, response.content


def load_inspection_page(file):
    with open('inspection_page.html', "r") as fo:
        html = fo.read()
    return html


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed


def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        # you will likely have something different here, depending on how
        # you implemented the load_inspection_page function.
        html, encoding = load_inspection_page('inspection_page.html')
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    print doc.prettify(encoding=encoding)
