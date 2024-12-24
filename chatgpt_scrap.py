import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# Setup ChromeDriver
options = Options()
options.add_argument(r"user-data-dir=C:\Users\****\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Profile 6")

driver = webdriver.Chrome(options=options)

csv_file = 'chat_data.csv'
csv_columns = ['Question', 'Response', 'Intention', 'Language', 'Topic']

def scrape_data_agronomie_kahlanzi(link,xpath_of_message):
    try:
        # Open the chat page directly using its URL
        driver.get(link)  # Replace with your actual URL
        time.sleep(10)  # Wait for the page to load fully
        # Scrap the chat messages
        chat_data = []  # To store scraped questions and responses

        messages = driver.find_elements(By.XPATH,xpath_of_message)
        language = "Français" 
        topic = "Gastronomie" # the topic you change it manually as it's entered in the input of the first message of the conversation 
        # here is also is going to be a little bit tricky because it depends on the reponse you gonna get and then you gonna find a way to split the data 
        # in my case :(example)
        # question : $var_question
        # response : $var_response
        # intention : $var_intention
        for message in messages : 
            message = message.text
            l = message.split(' : ')
            if (len(l) == 4):
                question = l[1][:-10]
                response = l[2][:-12]
                intention = l[3]
                chat_data.append([question ,response, intention, language, topic])
        # Write the data to a CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(csv_columns)  # Write the header
            writer.writerows(chat_data)  # Write the chat data
        #just to check that all the data has been scraped
        print(len(messages))
        print(f"Scraped data has been saved ")

    finally:
        driver.quit()
scrape_data_agronomie_kahlanzi("https://chatgpt.com/share/67490193-bdf0-800b-afcf-e80762231f74",'/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[*]/div/div/div[2]/div/div/div/div/div/ol/li[*]/p')