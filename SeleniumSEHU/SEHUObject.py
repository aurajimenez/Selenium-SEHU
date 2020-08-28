from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseSehu(object):
	def __init__(self, driver, base_url='http://localhost:8000/usuarios/login'):
		self.base_url= base_url
		self.driver = driver

	def find_element(self, *locator):
		return self.driver.find_element(*locator)

	def open(self, url):
		url = self.base_url + url
		self.driver.get(url)

	def get_title(self):
		return self.driver.title 

	def get_url(self):
		return self.driver.current_url

	def hoover(self, *locator):
		element = self.find_element(*locator)
		hover = ActionChains(self.driver).move_to_element(element)
		hover.perform()

	def wait_element(self, *locator):
		try:
			WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
		except TimeoutException:
			print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
			self.driver.quit()