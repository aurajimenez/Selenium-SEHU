import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class UserModule(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Opera(executable_path = r"operadriver.exe")
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
		username = element.find_element_by_xpath('//*[@id="id_username"]')
		username.send_keys("juanprueba")
		nombres = element.find_element_by_xpath('//*[@id="id_first_name"]')
		nombres.send_keys("Juan alberto")
		apellidos = element.find_element_by_xpath('//*[@id="id_last_name"]')
		apellidos.send_keys("Cifuentes")
		correo_electronico = element.find_element_by_xpath('//*[@id="id_email"]')
		correo_electronico.send_keys("juancif@gmail.com")
		cargo = Select(element.find_element_by_xpath('//*[@id="id_cargo"]'))
		cargo_options = ['Administrador','Integrante','Manager']
		act_options = []
		for option in cargo.options:
			act_options.append(option.text)
		#self.assertListEqual(cargo_options,act_options)
		cargo.select_by_visible_text('Integrante')

		skills =  element.find_element_by_xpath('//*[@id="id_skills"]')
		skills.send_keys("Git,github")
		enfoque = Select(element.find_element_by_xpath('//*[@id="id_enfoque"]'))
		enfoque_options = ['BACKEND','FRONTEND','FULLSTACK','QA','CEO']
		act_options2 = []
		for option in enfoque.options:
			act_options.append(option.text)
		#self.assertListEqual(enfoque_options,act_options2)
		enfoque.select_by_visible_text('BACKEND')

		#foto = element.find_element_by_xpath('//*[@id="id_foto_perfil"]')
		contrasena = element.find_element_by_xpath('//*[@id="id_password1"]')
		contrasena.send_keys("contrasena111")
		confirmacion_contrasena = element.find_element_by_xpath('//*[@id="id_password2"]')
		confirmacion_contrasena.send_keys("contrasena111")
		register_button = element.find_element_by_xpath('//*[@id="main-wrapper"]/div[4]/div[2]/div/div/div/div/div/form/div[2]/div/button[1]')
		register_button.send_keys(Keys.ENTER)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()