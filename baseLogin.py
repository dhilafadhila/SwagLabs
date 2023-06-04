import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import element
from data import inputan

def base_Login(driver):
    driver.get(element.base_url) # buka situs
    driver.maximize_window()
    driver.find_element(By.ID,element.username).send_keys(inputan.username) # isi email
    time.sleep(1)
    driver.find_element(By.ID,element.password).send_keys(inputan.password) # isi password
    time.sleep(1)
    driver.find_element(By.ID,element.btn_login).click()
    time.sleep(1)