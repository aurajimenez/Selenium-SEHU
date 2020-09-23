from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage

executable_path = r"operadriver.exe"

driver = webdriver.Opera(executable_path=executable_path)
base_url ='http://localhost:8000/usuarios/login'

def setUp():
    driver.get(base_url)

def test_login_user():
    login = Login(driver)
    login.test_title()

def test_register_user():
    register_user = RegisterPage(driver)
    register_user.test_title()
    register_user.enter_username()
    register_user.enter_nombres()
    register_user.enter_apellidos()
    register_user.enter_correo_electronico()
    register_user.enter_cargo()
    register_user.enter_skills()
    register_user.enter_enfoque()
    register_user.enter_contrasena()
    register_user.enter_confirmacion_contrasena()
    register_user.clic_boton_registrar()