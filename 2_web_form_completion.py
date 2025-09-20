from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/simple_form_find_task.html")

first_name = browser.find_element(By.NAME, "first_name")
first_name.send_keys("John")
last_name = browser.find_element(By.NAME, "last_name")
last_name.send_keys("Doe")
city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
city.send_keys("San Francisco")
country = browser.find_element(By.ID, "country")
country.send_keys("US")

submit_button = browser.find_element(By.ID, "submit_button")
submit_button.click()

browser.quit()
