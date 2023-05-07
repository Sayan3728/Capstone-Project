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

def test_newlead(driverfix):
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
    driverfix.find_element(By.ID,"createNew").click()
    time.sleep(5)
    driverfix.find_element(By.LINK_TEXT,"Lead").click()
    time.sleep(5)
    driverfix.find_element(By.NAME,"name_lastlea2").send_keys("Nath")
    time.sleep(2)
    driverfix.find_element(By.NAME, "lea3").send_keys("XYZ")
    time.sleep(3)
    #Lead status
    drop=Select(driverfix.find_element(By.XPATH,"//select[@id='lea13']"))
    drop.select_by_index(1)
    time.sleep(4)
    #save
    driverfix.find_element(By.XPATH, "//td[@class='pbButton']/input[2]").click()
    time.sleep(5)

    # logging out section
    driverfix.find_element(By.ID, "userNav").click()
    time.sleep(10)
    driverfix.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(5)