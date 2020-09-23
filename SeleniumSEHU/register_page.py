from selenium.webdriver.common.keys import Keys, By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

class RegisterPage():
    title = "Registrar usuario"
    wait_time_out = 5
    username = "llorona"
    nombres = "Llorona Alicia"
    apellidos = "Gonzalez"
    correo_electronico = "llorona@mail.com"
    skills = "QA, Automation, React"
    enfoque = "Indeciso"
    contrasena = "Contrasena1234"
    confirmacion_contrasena = "Contrasena1234"

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = W(self.driver, self.wait_time_out)

    def test_title(self):
        assert self.title in self.driver.title
    
    def enter_username(self):
        input_username_element = self.find_element_by_xpath(*self.locator.USERNAME)
        input_username_element.send_keys(self.username)
        
	def enter_nombres(self):
		input_nombres_element = self.find_element_by_xpath(*self.locator.NOMBRES)
        input_nombres_element.send_keys(self.nombres)

	def enter_apellidos(self):
		input_apellidos_element = self.find_element_by_xpath(*self.locator.APELLIDOS)
        input_apellidos_element.send_keys(self.apellidos)

	def enter_correo_electronico(self):
		input_correo_electronico_element = self.find_element_by_xpath(*self.locator.CORREO)
        input_acorreo_electronico.send_keys(self.correo_electronico)

	def enter_cargo(self):
		input_cargo_element = self.find_element_by_xpath(*self.locator.CARGO)

	def enter_skills(self):
		input_skills_element = self.find_element_by_xpath(*self.locator.SKILLS)
        input_skills.send_keys(self.skills)

	def enter_enfoque(self):
		input_enfoque_element = self.find_element_by_xpath(*self.locator.ENFOQUE)
        input_enfoque.send_keys(self.enfoque)

	def enter_contrasena(self):
		input_contrasena_element = self.find_element_by_xpath(*self.locator.CONTRASENA)
        input_contrasena.send_keys(self.contrasena)

	def enter_confirmacion_contrasena(self):
		input_confirmacion_contrasena_element = self.find_element_by_xpath(*self.locator.CONFIRMACION_CONTRASENA)
        input_confirmacion_contrasena.send_keys(self.confirmacion_contrasena)

	def clic_boton_registrar(self):
		input_boton_registrar_element = self.find_element_by_xpath(*self.locator.BOTON_REGISTRAR)
        input_boton_registrar.submit()
