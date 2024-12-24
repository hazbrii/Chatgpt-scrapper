from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Set up Chrome options
options = Options()
options.add_argument(r"user-data-dir=C:\Users\Hazbri\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Profile 6")
# options.add_argument("--disable-extensions")




# Initialize the WebDriver with user profile
driver = webdriver.Chrome(options=options)


url = 'https://chatgpt.com/c/67484daa-f0fc-8003-ac1b-b520c7531fd1'


# Open the TikTok video URL
driver.get(url)
time.sleep(20)
# Use the XPath to find the element
try:
    
    for i in range(5):
        input_element = driver.find_element(By.XPATH,'//*[@id="prompt-textarea"]/p')
        input_element.send_keys("more 20")
        submit_button = driver.find_element(By.XPATH, '//*[@id="composer-background"]/div[2]/button')
        submit_button.click()
        time.sleep(40)
        print("done",i)
    
    # question_response_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[2]/div/div/div[2]/div/div[1]/div/div/div/p[2]')
    # for question_response in question_response_elements:
    #       print(question_response.text)
    
    
    print("done")


except Exception :
        print("Error:")


# Close the browser
driver.quit()
