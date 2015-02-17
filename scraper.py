import requests
from bs4 import BeautifulSoup


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


def get_inspection_page(kwargs):
    url = DOMAIN + PATH
    parameters = PARAMETERS.copy()
    for key, val in kwargs.items():
        if key in PARAMETERS:
            parameters[key] = val
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.encoding, response.content


def read_html():
    with open('inspection_page.html', "w") as fo:
        html = fo.read()
    return html


def parse_source(html, encoding='utf-8'):
    souped = BeautifulSoup(html, from_encoding=encoding)
    return souped

def start():

    parameters = {'Zip_Code': '98103'}
    data = get_inspection_page(parameters)
    with open('inspection_page.html', "w") as fo:
        fo.write(data[1])

if __name__ == '__main__':
    start()
