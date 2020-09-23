from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as W
from base_page import BasePage
from Locators import Locators

class LoginPage():
    username = "admin"
    contrasena = "historias"

    def __init__(self, driver):
        title = "Login"
        self.driver = driver
        self.wait_time_out = 5
        self.wait_variable = W(self.driver, self.wait_time_out)
        
        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.contrasena_textbox_xpath = Locators.contrasena_textbox_xpath
        self.ingresar_button = Locators.ingresar_button

    def test_title(self, title):
        assert self.title in self.driver.title

    def enter_username(self):
        username_textbox_xpath = self.driver.find_element_by_xpath('//*[@id="usernameInput"]').clear()
        username_textbox_xpath.send_keys(username)
    
    def enter_contrasena(self):
        self.driver.find_element_by_xpath('//*[@id="passwordInput"]').clear()
        self.driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(contrasena)

    def click_button_registrar(self):
        self.driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div/div/div/div/div/form/button').click()