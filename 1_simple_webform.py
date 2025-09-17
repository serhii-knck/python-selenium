# importing time module
import time

# importing webdriver from selenium module
from selenium import webdriver

# importing class By which allows to search for the element on the web page
from selenium.webdriver.common.by import By

# initializing Chrome webdriver
driver = webdriver.Chrome()

# waiting for 5 seconds for the browser to load
time.sleep(5)

# navigating to the specified web page
driver.get("https://suninjuly.github.io/text_input_task.html")
#waiting 5 seconds for the page to load
time.sleep(5)

# searching for textarea by CSS selector
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# entering phrase into textarea
textarea.send_keys("Hello Selenium")
time.sleep(5)

# searching for the 'Submit' button on the web page
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# clicking on the button 'Submit'
submit_button.click()

# closing webdriver
driver.quit()