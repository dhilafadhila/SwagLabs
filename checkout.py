import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import element
from data import inputan
import baseLogin

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_chart_tilpayment(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.base_Login(driver)

        driver.find_element(By.ID,element.add_chart).click()
        time.sleep(1)
        # validasi1
        response_data = driver.find_element(By.XPATH,element.number_cart).text
        self.assertIn(inputan.number_cart, response_data)

        # validasi2
        response_data = driver.find_element(By.ID,element.remove_button).text
        self.assertEqual(response_data, inputan.remove_button)

        driver.find_element(By.XPATH,element.btn_cart).click()
        time.sleep(1)
        
        response_data = driver.find_element(By.XPATH,element.header_cart).text
        self.assertIn(inputan.header_cart, response_data)

        driver.find_element(By.ID,element.btn_checkout).click()
        time.sleep(1)

        response_data = driver.find_element(By.XPATH,element.btn_continue).text
        self.assertIn(inputan.header_confirm, response_data)

        #inputan form valid 
        driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Lalisa")
        time.sleep(1)
        driver.find_element(By.ID,"last-name").send_keys("Manoban")
        time.sleep(1)
        driver.find_element(By.ID,"postal-code").send_keys("12345")
        time.sleep(1)
        driver.find_element(By.ID,"continue").click()
        time.sleep(1)

        response_data = driver.find_element(By.XPATH,element.header_overview).text
        self.assertIn(inputan.header_overview, response_data)

        driver.find_element(By.ID,element.btn_finish).click()
        time.sleep(1)

        response_data = driver.find_element(By.XPATH,element.header_complete).text
        self.assertIn(inputan.header_complete, response_data)

        driver.find_element(By.ID,element.btn_back_to_home).click()
        time.sleep(1)

        response_url = driver.current_url
        self.assertIn(response_url, inputan.product_url)

        driver.find_element(By.ID,element.btn_menu).click()
        time.sleep(1)

        driver.find_element(By.ID,element.btn_logout).click()
        time.sleep(1)

        response_url = driver.current_url
        self.assertIn(response_url, element.base_url)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()