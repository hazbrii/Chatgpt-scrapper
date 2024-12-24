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
 
options.add_argument(r"user-data-dir=C:\Users\****\AppData\Local\Google\Chrome\User Data")
# Here you must add your chrome Profile you wille find in the link above
options.add_argument("profile-directory=Profile 6")
# options.add_argument("--disable-extensions")




# Initialize the WebDriver with user profile
driver = webdriver.Chrome(options=options)
#Well here is the tricky step which is to create a new conversation with chatgpt
#prepare what kind of topic you want and ask him to generate 1 example of the data format you want 
#(so that the format doesn't change in the next responses of the conversation ) 
url = 'https://chatgpt.com/c/67484daa-f0fc-8003-ac1b-b520c7531fd1'


# Open the Chatgpt conversation URL
driver.get(url)
#wait for the page to load
time.sleep(20)
try:
    for i in range(5):
        # Use the XPath to find the element
        input_element = driver.find_element(By.XPATH,'//*[@id="prompt-textarea"]/p')
        # I used the input element to send a message contains more 20 (you can modify it)
        input_element.send_keys("more 20")
        submit_button = driver.find_element(By.XPATH, '//*[@id="composer-background"]/div[2]/button')
        #here I simply click the button (send the message) 
        submit_button.click()
        #waitong for the response to end
        time.sleep(40)
        #for the data I will get it later as I'm making a ressource for now and then I will get all the data 
        #(I know, I can find a better solution for that)
        print("done",i)
    print("done")
except Exception :
        print("Error:")
# Close the browser
driver.quit()
