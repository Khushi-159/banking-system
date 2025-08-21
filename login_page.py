from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element(By.NAME, "uid")
        self.password = driver.find_element(By.NAME, "password")
        self.login_btn = driver.find_element(By.NAME, "btnLogin")
    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_btn.click()
