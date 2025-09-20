# importing pytest, time module, webdriver module from selenium, and class By from webdriver module
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    """Function that initializes the browser and opens the specified link"""
    # initializing Chrome webdriver
    driver = webdriver.Chrome()
    # waiting for 5 seconds for the browser to load
    time.sleep(5)
    yield driver
    driver.quit()

def test_simple_web_form(browser):
    """Test that runs through a simple webform"""
    # opening specified link
    browser.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)
    # searching for textarea by CSS selector
    textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
    # entering phrase into textarea
    textarea.send_keys("Hello Selenium")
    time.sleep(5)
    # searching for the 'Submit' button on the web page
    submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    # clicking on the button 'Submit'
    submit_button.click()

def test_apply_find_element_method(browser):
    """Test that applies selenium find_element() method"""
    # opening specified link
    browser.get('http://suninjuly.github.io/find_link_text')
    # searching and clicking link with the exact text
    link = browser.find_element(By.LINK_TEXT, '224592')
    link.click()
    # searching for elements and completing the web-form
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("John")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Doe")
    city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    city.send_keys("San Francisco")
    country = browser.find_element(By.ID, "country")
    country.send_keys("US")
    # searching for submission button and clicking it
    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

def test_apply_find_elements_method(browser):
    """Test that applies selenium find_elements() method"""
    # opening specified link
    browser.get('http://suninjuly.github.io/huge_form.html')
    # searching for several elements by CSS selector
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        print("Found elements: ", element)
        element.send_keys("answ")
    # searching for submission button and clicking it
    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

def test_apply_searching_elements_by_xpath(browser):
    """Test that applies selenium find_element() method using XPath"""
    # navigating to the specified webpage
    browser.get('https://suninjuly.github.io/find_xpath_form')

    # searching for elements and completing the web-form
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("John")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Doe")
    city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    city.send_keys("San Francisco")
    country = browser.find_element(By.ID, "country")
    country.send_keys("US")

    # searching for Submit button by XPath and clicking it
    submit_button = browser.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    submit_button.click()
