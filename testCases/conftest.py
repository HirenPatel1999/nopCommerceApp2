import pytest
import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    browser = "chrome"
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox Browser........")
    else:
        print('plz pass the correct browser name' + browser)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")

######### PyTest HTML Report ##########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hiren'

# It is hook for delete/Modify environment info to HTML Report
@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)