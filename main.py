import json
from bs4 import BeautifulSoup
import requests

URL = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80" \
      "%D1%81%D1%82%D0%B2 "
try:
    res = requests.get(URL)
except Exception: res=None
print(res)
if res:
    print('Response OK')
    soup = BeautifulSoup(res.text, "lxml")
    country_list = []
    Countries = soup.find('tbody').find_all('tr')
    for _country in Countries:
        country_tds = _country.find_all('td')
        if len(country_tds) > 0:
            country_list.append({"country": country_tds[2].text.rstrip('\n'),
                                 "full_country_name": country_tds[3].text.rstrip('\n'),
                                 "same_letter_count": 0,
                                 "letter_count": country_tds[3].text.rstrip('\n').count(" ")+1,
                                 "flag_img": country_tds[1].find('img').get('src')})
    for item in country_list:
        letter_count = 0
        for item_count in country_list:
            if item['country'][0] == item_count['country'][0]:
                letter_count += 1
        item['same_letter_count'] = letter_count
    for item in country_list:
        print(item)

    with open(f"country.json", 'w', encoding='utf-8') as file:
        json.dump(country_list, file, indent=4, ensure_ascii=False)

    def search(contr):
        for search_item in country_list:
            if search_item['country'] == contr:
                print(str(search_item).replace(",","\n").replace("'","")[1:-1])
                return True
            elif contr == '0':
                return False
        print('Nothing found')
        return True

    while True:
        if not search(input('Enter country name: ')): break

else:
    print('Response Failed')