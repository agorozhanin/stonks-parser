import requests
from bs4 import BeautifulSoup
import re


def get_parse_result() -> list:
    response = requests.get('https://smart-lab.ru/q/Shares/')
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('table', class_="simple-little-table trades-table")
    rows = table[0].find_all('tr')
    result_list = []
    for row in rows:
        attributes = row.find_all('td')
        try:
            result_list.append({
                'updateTime': attributes[1].text,  # в таймстеп
                'companyName': attributes[2].text,
                'tickerName': attributes[3].text,
                'lastPrice': float(attributes[7].text),
                'percentUpdate': float(attributes[8].text.split()[0][:-1]),
                'volumeInMillions': float(attributes[9].text),
                'percentUpdateWeek': float(attributes[10].text.split()[0][:-1]),
                'percentUpdateMonth': float(attributes[11].text.split()[0][:-1]),
                'percentUpdateStartYear': float(attributes[12].text.split()[0][:-1]),
                'percentUpdateYear': float(attributes[13].text.split()[0][:-1]),
                'capitalizationInBillionRUB': float(attributes[14].text),
                'capitalizationInBillionUSD': float(attributes[15].text),
            })
        except:
            ...
    return result_list


print(get_parse_result())
