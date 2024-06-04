from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import io
import os

# def download_pdf(url, destination):
#     response = requests.get(url)
#     with open(destination, 'wb') as file:
#         file.write(response.content)
#     print(f"Download complete. Saved as {destination}")

html = r''' 


'''

links = []
soup = BeautifulSoup(html, 'html.parser')

note_elements = soup.find_all('li', class_='note')
for note_element in note_elements:
    link_element = note_element.find('a')
    if link_element:
        link = link_element['href']
        links.append("https://openreview.net" + link)

print(links)
print(len(links))
i = 0

for url in links:
    # path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome()

    # url = "https://openreview.net/forum?id=NudBMY-tzDr"
    i += 1
    start_index = url.find("?id=") + len("?id=")
    id = url[start_index:]
    print(str(i) + ". ID:" + str(id))

    folder_name = str(id)

    # if not os.path.exists(folder_name):
    #     os.mkdir(folder_name)
    #     print(f"Folder '{folder_name}' created successfully.")
    # else:
    #     print(f"Folder '{folder_name}' already exists.")

    # save_as = f"D:\Riya\DJ Sanghvi\Extra\Internship\{id}\ICLR2022-{id}.pdf"
    # download_pdf(url, save_as)

    driver.get(url)
    # Wait for the dropdown to be visible
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "invitations"))
    )

    # Click on the dropdown to expand it
    dropdown.click()

    # Click on the "Select All" checkbox
    select_all_checkbox = driver.find_element(
        By.CLASS_NAME, "select-all-checkbox")
    select_all_checkbox.click()

    # Click on the "Official Review" checkbox
    official_review_checkbox = driver.find_elements(
        By.CLASS_NAME, "invitations-multiselector-checkbox")[0]
    official_review_checkbox.click()
    official_review_checkbox = driver.find_elements(
        By.CLASS_NAME, "invitations-multiselector-checkbox")[1]
    official_review_checkbox.click()

    time.sleep(15)
    print(driver.title)

    content = driver.find_element(By.ID, 'note_children')
    # print(content.text)

    j = -1
    notes = content.find_elements(By.CLASS_NAME, 'comment-level-odd')
    for note in notes:
        class_name = note.get_attribute("class")
        # print(class_name)
        if class_name == 'note_with_children comment-level-odd semi-collapsed':
            continue
        else:
            panels = note.find_elements(By.CLASS_NAME, 'panel')
            work = ""
            for panel in panels:
                note_contents = panel.find_elements(
                    By.CLASS_NAME, 'note_contents')

                for note_content in note_contents:
                    # print(note_content.text)
                    work += note_content.text + "\n\n\n"
            j += 1

            folder_path = f'{str(id)}'
            if j == 0:
                filename = f"ICLR2022-{id}-MetaReview.txt"
            else:
                filename = f"ICLR2022-{id}-R{j}.txt"
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(work)
                print(f"File created: {file_path}")
            except Exception as e:
                print(f"An error occurred while writing to {filename}: {e}")

            # with io.open(f"ICLR2022-{id}-R{j}.txt", "w", encoding="utf-8") as file:
            #     file.write(work)

    driver.close()
