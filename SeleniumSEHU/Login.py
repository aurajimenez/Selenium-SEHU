import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Login_page import LoginPage
import time

class Login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = r"operadriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get('http://localhost:8000/usuarios/login')
        
    def test_login(self):
        login = self.driver
        login = LoginPage(login)
        login.enter_username()
        login.enter_contrasena()
        login.click_button_registrar()
        
    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()