import csv
import os
import requests
from bs4 import BeautifulSoup

def get_Images_from_tag(list_tag):
    for tag in list_tags:
        index = 1
        while index < 11:
            with open(os.path.join('cat_pics', f'{tag}_{index}.jpg'), 'wb') as file:
                response = requests.get('https://cataas.com/cat/' + tag)
                file.write(response.content)
            index += 1
    print("Done.")

def write_to_csv(list_tag):
    for tag in list_tags:
        cat_list = []
        link = 'https://cataas.com/cat/' + tag
        cat_list.append(tag)
        cat_list.append(link)
        list.append(cat_list)

    with open('cat_tags.csv', 'w', newline='', encoding='utf-8') as f:
        try:
            writer = csv.writer(f)
            writer.writerow(['Tag', 'Link'])
            writer.writerows(list)
        except:
            pass

if __name__ == "__main__":
    try:
        os.mkdir('cat_pics')
    except FileExistsError:
        pass
    r = requests.get("https://cataas.com/api/tags")
    list_tags = r.json()
    list_tags = list_tags[3:]
    list = []
    get_Images_from_tag(list_tags)
    write_to_csv(list_tags)


