from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Nivetha:
   url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
   #url1 = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
   PIM = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
   

      
   username = 'Admin'
   password = 'admin123'
   # username_locator is a TagName
   username_locator = 'username'
   # password_locator is a TagName
   password_locator = 'password'
   # Submit Button Locator as XPATH
   submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

   PIM_locator =   '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
   Add_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'

   Addemployee_locator = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
   first_Name = 'nila'
   middle_Name = 'logu'
   last_Name = 'eswar'
   firstName_locator = 'firstName'
   middlename_locator = 'middleName'
   lastname_locator = 'lastName'
   createlogindetails_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
   save_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
   u_name = 'monikaa'
   pwd = 'Qwer@12345'
   c_pwd = 'Qwer@12345'
   u_locator ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
   p_locator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
   cp_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
   enable_l = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
  
   # Browsing function for Selenium Automation
   def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        

   def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        print('the user is logged in successfully')

   def PIM(self):
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
   def Add(self):
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.Add_locator).click()

   def Addemployee(self):
        sleep(4)
        self.driver.find_element(by=By.NAME, value=self.firstName_locator).send_keys(self.first_Name)
        self.driver.find_element(by=By.NAME, value=self.middlename_locator).send_keys(self.middle_Name)
        self.driver.find_element(by=By.NAME, value=self.lastname_locator).send_keys(self.last_Name)
        self.driver.find_element(by=By.XPATH, value=self.createlogindetails_locator).click()
        self.driver.find_element(by=By.XPATH, value=self.u_locator).send_keys(self.u_name)
        self.driver.find_element(by=By.XPATH, value=self.p_locator).send_keys(self.pwd)
        self.driver.find_element(by=By.XPATH, value=self.cp_locator).send_keys(self.c_pwd)
        self.driver.find_element(by=By.XPATH, value=self.enable_l).click()
        self.driver.find_element(by=By.XPATH, value=self.save_locator).click()
        sleep(4)

Nivetha().Browsing()       
Nivetha().login()
Nivetha().PIM()
Nivetha().Add()
Nivetha().Addemployee()
