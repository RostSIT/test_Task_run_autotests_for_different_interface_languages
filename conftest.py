import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    if language == 'fr':
        print('\nlanguage fr')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)
    elif language == 'es':
        print('\nlanguage es')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('\nChoose language es or fr')
    yield browser
    print('quit browser')
    time.sleep(30)
    browser.quit()
