from importlib.metadata import metadata

import pytest_html
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on. Supported: chrome, firefox")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

def pytest_html_report_title(report):
    report.title = "My Custom Test Report"

# Hook to add environment info to the HTML report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([pytest_html.extras.html("<p>Department: QA</p>")])
    prefix.extend([pytest_html.extras.html("<p>Release: 1.2.3</p>")])
    prefix.extend([pytest_html.extras.html("<p>Project Name:nopcommerce</p>")])
    prefix.extend([pytest_html.extras.html("<p>Module Name = Login</p>")])




