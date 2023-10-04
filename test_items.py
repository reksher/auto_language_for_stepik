import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        basket = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        assert basket is not None
    except NoSuchElementException:
        assert False, "Basket button not found"
    time.sleep(30)
