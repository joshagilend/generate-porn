import os
import requests
from bs4 import BeautifulSoup

cookies = { '_ga_EDLM4HZ2Q0': 'GS1.1.1682659074.4.1.1682659575.0.0.0', 
            '_ga': 'GA1.1.1014489337.1682632861' }

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def scrape_images(url, save_folder):
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if not img_url.startswith('http'):
            img_url = url + '/' + img_url
        img_name = img_url.split('/')[-1]
        save_path = os.path.join(save_folder, img_name)
        download_image(img_url, save_path)
        print(f'Downloaded {img_name} from {img_url}')

if __name__ == '__main__':
    url = 'https://pornpen.ai'  # Replace with the URL of the website you want to scrape images from
    save_folder = 'downloaded_images'
    scrape_images(url, save_folder)
