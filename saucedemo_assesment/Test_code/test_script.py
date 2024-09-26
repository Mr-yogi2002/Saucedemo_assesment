import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Test_data.test_user_data import saucedemo_data
from Test_locators.test_locator import saucedemo_locat
from selenium.webdriver.common.action_chains import ActionChains

class Test_Saucedemo:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    # first testcase
    def test_login(self, boot):
        self.driver.get(saucedemo_data.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 8)
        # positve scenarios
        id_name = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().id)))
        id_name.send_keys(saucedemo_data().user_id)

        id_pass = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().pass_word)))
        id_pass.send_keys(saucedemo_data().password)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, saucedemo_locat().button)))
        login_button.click()
        

        assert self.driver.current_url == saucedemo_data().dash_url
        print(self.driver.current_url)

    # # Second testcase    
    def test_add_product(self, boot):
        self.driver.get(saucedemo_data.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 8)
        # positve scenarios
        id_name = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().id)))
        id_name.send_keys(saucedemo_data().user_id)

        id_pass = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().pass_word)))
        id_pass.send_keys(saucedemo_data().password)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, saucedemo_locat().button)))
        login_button.click()
        

        assert self.driver.current_url == saucedemo_data().dash_url
        print(self.driver.current_url)

        product_1 = wait.until(EC.presence_of_element_located((By.LINK_TEXT, saucedemo_locat().text)))
        product_1.click()
       
        add_cart = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().add)))
        add_cart.click()

        add_check = wait.until(EC.presence_of_element_located((By.XPATH, saucedemo_locat().add_box)))
        add_check.click()
        
        add_remove = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().remove)))
        add_remove.click()

        continue_shop = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().return_shop)))
        continue_shop.click()
       
        side_click = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().side_button)))
        side_click.click()
        
        button_logout = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().logout)))
        button_logout.click()
        
        assert self.driver.current_url == saucedemo_data().url
        print(self.driver.current_url)
    # # third testcase
    # negative scenarios
    def test_negative_(self, boot):
        self.driver.get(saucedemo_data.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 8)
        id_name = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().id_2)))
        id_name.send_keys(saucedemo_data().user_id_2)

        id_pass = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().pass_word_2)))
        id_pass.send_keys(saucedemo_data().password_2)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, saucedemo_locat().button_2)))
        login_button.click()

        screen = wait.until(EC.presence_of_element_located((By.XPATH, saucedemo_locat().shot)))
        screen.screenshot("error.png")
    
        assert self.driver.current_url == saucedemo_data().url
        print(self.driver.current_url)
    # four testcase
    def test_low_high_price(self, boot):
        self.driver.get(saucedemo_data.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 8)
        # positve scenarios
        id_name = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().id)))
        id_name.send_keys(saucedemo_data().user_id)

        id_pass = wait.until(EC.presence_of_element_located((By.ID, saucedemo_locat().pass_word)))
        id_pass.send_keys(saucedemo_data().password)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, saucedemo_locat().button)))
        login_button.click()

        name_a_z = wait.until(EC.presence_of_element_located((By.XPATH, saucedemo_locat().a_z)))
        name_a_z.click()
       
        low_high = wait.until(EC.presence_of_element_located((By.XPATH, saucedemo_locat().l_h)))
        low_high.click()

        assert self.driver.current_url == saucedemo_data().dash_url
        print(self.driver.current_url)
