import json
from bs4 import BeautifulSoup
import requests

URL = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80" \
      "%D1%81%D1%82%D0%B2 "
res = requests.get(URL)
print(res)
if res:
    print('Response OK')
    soup = BeautifulSoup(res.text, "lxml")

    # country_names = []
    # country_full_names = []
    # country_img = []
    # same_letter_count = []
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
            # country_full_names.append(country_tds[3].text.rstrip('\n'))
            # country_names.append(country_tds[2].text.rstrip('\n'))
            # country_img.append(country_tds[1].find('img').get('src'))

    # print(country_list)
    # print(f"Full name:{country_full_names} ")
    # print(f"Name:{country_names} ")
    # print(country_img)
    # print(country_list[1]['country'])
    for item in country_list:
        letter_count = 0
        for item_count in country_list:
            if item['country'][0] == item_count['country'][0]:
                letter_count += 1
        item['same_letter_count'] = letter_count
    print(country_list)

    with open(f"country.json", 'w', encoding='utf-8') as file:
        json.dump(country_list, file, indent=4, ensure_ascii=False)


    def search(contr):
        for search_item in country_list:
            if search_item['country'] == contr:
                print(search_item)
                return
        print('Nothing found')


    search(input('Enter country name: '))

else:
    print('Response Failed')
    # for name in country_names:
    #     for full_name in country_full_names:
    #         for count in same_letter_count:
    #             for url in country_img:
    #                 country_list.append({"country": name,"country_full_names":full_name,"same_letter_count":count,"country_img":url})

    # country_list.append({name :"country"for name in country_names})

    # country_list.append({"Country": item_name,
    #                     "count":item_count,
    #                     "img":item_img})

    # print(allCountries)
    # coutry_names = soup.find('table', class_='wikitable').find_all('a',class_=None)
    # coutry_full_names = soup.find('table', class_='wikitable').find_all('td',string=True)

    # for item in coutry_full_names:
    #
    #     print(item.text)
    # for item in coutry_names:
    #     print(item.text)

    # allImg = soup.find('table',class_='wikitable').findAll('img')
    # allCoutry = soup.find('table',class_='wikitable').findAll('a',class_=None)
    # # print(allImg)
    # Coutry_list = []
    # for item in allImg:
    #     item_img = item.get('src')
    #     item_name = item.get('alt')
    #     item_count = len(item_name)
    #     Coutry_list.append({"Country":item_name,
    #                     "count":item_count,
    #                     "img":item_img})
    #
    # print(Coutry_list)