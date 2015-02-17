#!/usr/bin/env python
from __future__ import print_function
import request


DOMAIN = 'http://info.kingcounty.gov'
PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
PARAMETERS = {'Output': 'W',
              'Business_Name': '',
              'Business_Address': '',
              'Longitude': '',
              'Latitude': '',
              'City': '',
              'Zip_Code': '',
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
    parameters = {key: val for (key, val) in kwargs}
    response = request.get(url, parameters)
    return response.encoding, response.content
