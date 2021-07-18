from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class User_accout:

    def __init__(self, login, password, user_agent):
        self.__login = login
        self.__password = password
        self.user_agent = user_agent
        self.__cookies = None
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"user-agent={self.user_agent}")
        self.driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

    def auth_and_set_cookies(self):
        self.driver.get("https://esia.gosuslugi.ru")
        element = WebDriverWait(self.driver, timeout=3).until(
            lambda d: d.find_element(By.ID, "loginByPwdButton"))
        login = self.driver.find_element(By.ID, "login")
        passd = self.driver.find_element(By.ID, "password")
        enter = self.driver.find_element(By.ID, "loginByPwdButton")

        login.send_keys(self.__login)
        passd.send_keys(self.__password)
        enter.click()

    def get_passport_data(self):
        self.driver.get("https://esia.gosuslugi.ru/profile/user/personal")
        elements = WebDriverWait(self.driver, timeout=3).until(
            lambda d: d.find_elements_by_class_name("span_6"))
        return self.driver.find_elements_by_class_name("span_6")[5].text
