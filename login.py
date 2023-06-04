import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import element
from data import inputan
import baseLogin
import pytest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.base_Login(driver)

        # validasi 
        # response_url = driver.current_url
        # self.assertEqual(response_url, inputan.url_success_login) #validasi 1

        response_data = driver.find_element(By.CLASS_NAME,element.title).text
        self.assertIn(inputan.header, response_data) #validasi 2

       # driver.find_element(By.CLASS_NAME,element.shopping_cart).click()
       # self.assertEqual(driver.current_url, inputan.url_shopping) #validasi 3

    def test_b_fail_username_empty(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(element.base_url) # buka situs
        driver.find_element(By.ID,element.password).send_keys(inputan.password)
        driver.find_element(By.ID,element.btn_login).click() 

         # validasi
        response_data = driver.find_element(By.XPATH,element.required_username).text
        self.assertEqual(response_data, inputan.req_username)

    def test_c_fail_password_empty(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(element.base_url) # buka situs
        driver.find_element(By.ID,element.username).send_keys(inputan.username) # isi username
        driver.find_element(By.ID,element.btn_login).click() 

         # validasi
        response_data = driver.find_element(By.XPATH,element.required_password).text
        self.assertEqual(response_data, inputan.req_password)
    
    def test_d_fail_username_invalid(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(element.base_url) # buka situs
        driver.find_element(By.ID,element.username).send_keys(inputan.invalid_username) # isi email
        driver.find_element(By.ID,element.password).send_keys(inputan.password) # isi password
        driver.find_element(By.ID,element.btn_login).click()

         # validasi
        response_data = driver.find_element(By.XPATH,element.invalid_button).text
        self.assertEqual(response_data, inputan.invalid_alert)

    def test_d_fail_password_invalid(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(element.base_url) # buka situs
        driver.find_element(By.ID,element.username).send_keys(inputan.username) # isi email
        driver.find_element(By.ID,element.password).send_keys(inputan.invalid_password) # isi password
        driver.find_element(By.ID,element.btn_login).click()

         # validasi
        response_data = driver.find_element(By.XPATH,element.invalid_button).text
        self.assertEqual(response_data, inputan.invalid_alert)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()