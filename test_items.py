import time
from selenium.webdriver.common.by import By


def test_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    time.sleep(5)
