import json
import time
# import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.close()
