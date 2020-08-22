import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class UserModule(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Opera(executable_path = r"C:\Users\Dell\Documents\Proyectos - propio\Selenium-SEHU\code\SeleniumSEHU\operadriver.exe")
		driver = self.driver
		driver.maximize_window()
		driver.get('http://localhost:8000/usuarios/login')
		username = driver.find_element_by_xpath('//*[@id="usernameInput"]')
		username.send_keys("admin")
		password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
		password.send_keys("historias")
		button = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div/div/div/div/div/form/button')
		button.send_keys(Keys.ENTER)

	def test_register_user(self):
		element = self.driver
		menu_user = element.find_element_by_xpath('//*[@id="sidebarnav"]/li[3]/a/span').click()
		register_option = element.find_element_by_xpath('//*[@id="sidebarnav"]/li[3]/ul/li[1]/a').click()


	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()