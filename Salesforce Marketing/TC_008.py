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


def test_verify_importloaddiff(driverfix):
    driverfix.find_element(By.ID, "username").send_keys("sayanbcroy@gmail.com")
    time.sleep(3)
    driverfix.find_element(By.ID, "password").send_keys("*Sales123#")
    time.sleep(3)
    driverfix.find_element(By.ID, "Login").click()
    time.sleep(10)

    driverfix.maximize_window()
    time.sleep(10)
    v = "https://d5g00000jsr79eah-dev-ed.develop.my.salesforce.com/setup/forcecomHomepage.apexp?setupid=ForceCom"
    urll = driverfix.current_url
    if (v != urll):
        driverfix.find_element(By.CLASS_NAME, "uiImage").click()
        time.sleep(10)

        driverfix.find_element(By.LINK_TEXT, "Switch to Salesforce Classic").click()
        time.sleep(10)
    driverfix.find_element(By.LINK_TEXT,"Setup").click()
    time.sleep(5)
    driverfix.find_element(By.ID,"setupSearch").send_keys("Assignment Rules")
    time.sleep(2)
    driverfix.find_element(By.LINK_TEXT,"Lead Assignment Rules").click()
    time.sleep(5)
    driverfix.find_element(By.XPATH, "//input[@value=' New ']").click()
    time.sleep(5)
    driverfix.find_element(By.ID,"name").send_keys("PPu")
    time.sleep(5)
    driverfix.find_element(By.XPATH,"//input[@value=' Save ']").click()
    time.sleep(3)
    driverfix.find_element(By.LINK_TEXT, "PPu").click()
    time.sleep(5)
    driverfix.find_element(By.XPATH, "//input[@value=' New ']").click()
    time.sleep(5)
    driverfix.find_element(By.ID,"SortOrder").send_keys("33")
    time.sleep(5)
    drop = Select(driverfix.find_element(By.XPATH, "//select[@id='FilterType']"))
    drop.select_by_index(0)
    time.sleep(5)
    drop1= Select(driverfix.find_element(By.XPATH, "//select[@id='critfld1']"))
    drop1.select_by_index(3)
    time.sleep(3)
    drop2 = Select(driverfix.find_element(By.XPATH, "//select[@id='critop1']"))
    drop2.select_by_index(1)
    time.sleep(3)
    driverfix.find_element(By.ID,"pVAL1").send_keys("123")
    time.sleep(3)
    drop3 = Select(driverfix.find_element(By.XPATH, "//select[@id='Assignee_mlktp']"))
    drop3.select_by_index(0)
    time.sleep(3)
    driverfix.find_element(By.ID,"Assignee").send_keys("Sunny Bhattacharya")
    time.sleep(5)
    driverfix.find_element(By.XPATH, "//input[@value=' Save ']").click()
    time.sleep(3)

    driverfix.find_element(By.ID, "userNav").click()
    time.sleep(10)
    driverfix.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(5)

