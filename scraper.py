import requests
from lxml import html

from scraper_config import rank_xpath as rx
import parse_functions as pf

def to_dict(company_tuple):
    '''Change tuple to dict'''
    # necessary?
    pass

def Request_Gainers():
    '''Later add params for getting rank range of values'''
    
    request_settings = rx()

    response = requests.get(request_settings.url)
    tree = html.fromstring(response.content)

    rows = tree.xpath(request_settings.rows)
    
    data_array = []
    
    for row in rows[1:]:
        company = row.xpath(request_settings.stock_row)
        data = row.xpath(request_settings.data)
#        link = row.xpath(request_settings.link)
        
        data_tuple = pf.parse_row(company, data)
#        data_array += link
        data_array.append(data_tuple)

    return data_array




