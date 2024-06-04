import requests
from bs4 import BeautifulSoup
import os


def download_pdf(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)
    print(f"Download complete. Saved as {destination}")


html = r''' 

'''

links = []
soup = BeautifulSoup(html, 'html.parser')

note_elements = soup.find_all('li', class_='note')
for note_element in note_elements:
    link_element = note_element.find_all('a')[1]
    if link_element:
        link = link_element['href']
        url = "https://openreview.net" + link
        links.append(url)
print(links)
print(len(links))

i = 0

for url in links:
    start_index = url.find("?id=") + len("?id=")
    id = url[start_index:]
    folder_name = str(id)
    i += 1
    print(str(i) + ". ID:" + str(id))

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    save_as = f"{id}\ICLR2022-{id}.pdf"
    download_pdf(url, save_as)
