from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class CbitLogin():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.binary_location = os.environ.get(
            "GOOGLE_CHROME_BIN")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), chrome_options=self.chrome_options)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        try:
            driver = self.driver
            driver.get("https://erp.cbit.org.in/")
            time.sleep(0)
            user_name = driver.find_element_by_id("txtUserName")
            user_name.send_keys(self.username)
            next_button = driver.find_element_by_id("btnNext")
            next_button.click()
            time.sleep(0)
            password = driver.find_element_by_id("txtPassword")
            password.send_keys(self.username)
            submit_button = driver.find_element_by_id("btnSubmit")
            submit_button.click()

            att = driver.find_element_by_id("ctl00_cpStud_lblTotalPercentage")
            time.sleep(0)

            print('Your attendance is :' + att.text)
            att_string = att.text
            self.closeBrowser()
            return att_string
        except:
            time.sleep(5)
            return "Server Down"


# login1 = CbitLogin("160118862006","160118862006")
# login1.login()


# id="ctl00_cpStud_lblTotalPercentage"

# id="ctl00_cpStud_lblTotalPercentage"
