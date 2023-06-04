import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import element
from data import input
import baseLogin
import pytest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_one_product(self):
        # steps
        driver = self.browser 
        baseLogin.base_Login(driver)

        driver.find_element(By.ID,element.add_chart).click()
        time.sleep(1)
        # validasi1
        response_data = driver.find_element(By.XPATH,element.number_cart).text
        self.assertIn(input.number_cart, response_data)

        # validasi2
        response_data = driver.find_element(By.ID,element.remove_button).text
        self.assertEqual(response_data, input.remove_button)

    def test_b_add_and_remove(self):
        # steps
        driver = self.browser 
        baseLogin.base_Login(driver)

        driver.find_element(By.ID,element.add_chart).click()
        time.sleep(1)
        driver.find_element(By.ID,element.bike_light).click()
        time.sleep(1)
        driver.find_element(By.ID,element.t_shirt).click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,element.number_cart).text
        self.assertIn(input.number_add, response_data)

        driver.find_element(By.ID,element.remove_button).click()
        time.sleep(1)
        driver.find_element(By.ID,element.remove_bike_light).click()
        time.sleep(1)
     
        # validasi
        response_data = driver.find_element(By.XPATH,element.number_cart).text
        self.assertIn(input.number_cart, response_data)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()