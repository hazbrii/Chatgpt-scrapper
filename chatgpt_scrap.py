import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# Setup ChromeDriver
options = Options()
options.add_argument(r"user-data-dir=C:\Users\Hazbri\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Profile 6")

driver = webdriver.Chrome(options=options)

csv_file = 'chat_data_with_intention.csv'
csv_columns = ['Id','Question', 'Reponse', 'Intention', 'Langue', 'Topic']

def scrape_data_agronomie_kahlanzi(link,xpath_of_message):
    try:
        # Open the chat page directly using its URL
        driver.get(link)  # Replace with your actual URL
        time.sleep(10)  # Wait for the page to load fully

        # Scrape the chat messages
        chat_data = []  # To store scraped questions and responses

        # Keep scrolling and scraping until no more content is loaded
        messages = driver.find_elements(By.XPATH,xpath_of_message)
        language = "Français"
        topic = "Gastronomie"
        id = 0
        for message in messages : 
            message = message.text
            l = message.split(' : ')
            question = "question"
            response = "response"
            intention = "intention"
            if (len(l) == 4):
                question = l[1][:-10]
                response = l[2][:-12]
                intention = l[3]
            chat_data.append([id, question ,response, intention, language, topic])
            id+=1
            
        # Write the data to a CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(csv_columns)  # Write the header
            writer.writerows(chat_data)  # Write the chat data
        print(len(messages))
        print(f"Scraped data has been saved ")

    finally:
        driver.quit()
scrape_data_agronomie_kahlanzi("https://chatgpt.com/share/67490193-bdf0-800b-afcf-e80762231f74",'/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[*]/div/div/div[2]/div/div/div/div/div/ol/li[*]/p')