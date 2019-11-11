import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, fr, es")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\nrussian language for test..")
        language = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
        return language
    elif language == "fr":
        print("\nfrance language for test..")
        language = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207"
        return language
    elif language == "es":
        print("\nspanish language for test..")
        language = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207"
        return language
    else:
        raise pytest.UsageError("--language should be ru, fr, es")
    
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()