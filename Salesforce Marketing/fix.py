import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture()
def driverfix():
    driver = webdriver.Chrome(service=Service(r"F:\Selenium\chromedriver_win32\chromedriver.exe"))
    driver.get("https://login.salesforce.com/?locale=in")
    yield driver
    driver.close()