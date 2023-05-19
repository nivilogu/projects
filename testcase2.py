from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import Select

class Nivetha:
   url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   username = 'Admin'
   password = 'admin123'
   # username_locator is a TagName
   username_locator = 'username'
   # password_locator is a TagName
   password_locator = 'password'
   # Submit Button Locator as XPATH
   submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

   Admin_l = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
#    usersmgmt_l = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i'
#    users_l = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
   userrole_l ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
   status_l ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'


   # Browsing function for Selenium Automation
   def Browsing(self):
       self.driver.maximize_window()
       self.driver.get(self.url)

   # Method for login 
   def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        print('the user is logged in successfully')
   def adminpage(self):
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.Admin_l).click()
        # self.driver.find_element(by=By.XPATH, value=self.usersmgmt_l).click()
        sleep(4)
        # self.driver.find_element(by=By.XPATH, value=self.users_l).click()
        self.driver.find_element(by=By.XPATH, value=self.userrole_l).click()
        self.driver.find_element(by=By.XPATH, value=self.status_l).click()
        print('user role dropdown and status dropdown are working')

Nivetha().Browsing()
Nivetha().login()
Nivetha().adminpage()
