from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_site_contains_add_to_basket_button(browser):
    try:
        browser.get(link)
        browser.execute_script('return arguments[0].scrollIntoView(true)',
                               browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'))
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add_to_basket_form"]/button')))
        return True
    except:
        return False


def test_function():
    assert test_site_contains_add_to_basket_button == True, 'No Such basket Element'
