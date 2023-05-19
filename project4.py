from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


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

   PIM_locator =   '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
   
   empname = 'nila'
   empname_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input' 
   
   empid = '2019'
   empid_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
   
   search_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
   editbutton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i'
   
   nation = 'Namibian'
   nation_l = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
   save_l ='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
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

   def PIM(self):    
        sleep(4)  
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.empname_locator).send_keys(self.empname)
     #    self.driver.find_element(by=By.XPATH, value=self.empid_locator).send_keys(self.empid)
        self.driver.find_element(by=By.XPATH, value=self.search_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.editbutton_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.nation_l).send_keys(self.nation)
     #    self.driver.find_element(by=By.XPATH, value=self.nation_l).click()
        self.driver.find_element(by=By.XPATH, value=self.save_l).click()

Nivetha().Browsing()
Nivetha().login()
Nivetha().PIM()