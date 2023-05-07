from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
opt=Options()

@pytest.fixture()
def driverfix():
    opt.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(r"F:\Selenium\chromedriver_win32\chromedriver.exe"),options=opt)
    driver.get("https://login.salesforce.com/?locale=in")
    yield driver
    driver.close()

def test_editlead(driverfix):
    driverfix.find_element(By.ID, "username").send_keys("sayanbcroy@gmail.com")
    time.sleep(3)
    driverfix.find_element(By.ID, "password").send_keys("*Sales123#")
    time.sleep(3)
    driverfix.find_element(By.ID, "Login").click()
    time.sleep(20)
    driverfix.maximize_window()
    time.sleep(10)
    # till here logging in is done
    v = "https://d5g00000jsr79eah-dev-ed.develop.my.salesforce.com/home/home.jsp"
    urll = driverfix.current_url
    if (v != urll):
      driverfix.get("https://d5g00000jsr79eah-dev-ed.develop.my.salesforce.com/home/home.jsp")
      time.sleep(10)

    driverfix.find_element(By.ID, "phSearchInput").send_keys("Nath")
    time.sleep(2)
    driverfix.find_element(By.ID, "phSearchButton").click()
    time.sleep(5)
    # click edit
    driverfix.find_element(By.LINK_TEXT, "Edit").click()
    time.sleep(2)
    driverfix.find_element(By.NAME, "name_lastlea2").clear()
    time.sleep(2)
    driverfix.find_element(By.NAME, "name_lastlea2").send_keys("Guru")
    time.sleep(2)
    #save
    driverfix.find_element(By.XPATH, "//td[@class='pbButton']/input[2]").click()
    time.sleep(5)

    # logging out section
    driverfix.find_element(By.ID, "userNav").click()
    time.sleep(10)
    driverfix.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(5)