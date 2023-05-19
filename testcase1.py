from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys



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
   
   #lowercase search
   search_l = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
   admin_fill = 'admin' 
   pim_fill = 'pim'
   leave_fill ='leave'
   time_fill = 'time'
   recruitment_fill = 'recruitment'
   myinfo_fill = 'my info'
   performance_fill = 'performance'
   dashboard_fill = 'dashboard'
   directory_fill = 'directory'
   maintenance_fill = 'maintenance'
   buzz_fill = 'buzz'
   
   #uppercase search
   admin_fil = 'ADMIN'
   pim_fil = 'PIM'
   leave_fil = 'LEAVE'
   time_fil = 'TIME'
   recruitment_fil = 'RECRUITMENT'
   myinfo_fil = 'MY INFO'
   performance_fil = 'PERFORMANCE'
   dashboard_fil = 'DASHBOARD'
   directory_fil = 'DIRECTORY'
   maintenance_fil = 'MAINTENANCE'
   buzz_fil = 'BUZZ'
 


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
   def search(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.search_l).click()
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.admin_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.pim_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.leave_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.time_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.recruitment_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.myinfo_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.performance_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.dashboard_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.directory_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.maintenance_fill)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.buzz_fill)
        print('lowercase MENU options are working on searchbox')
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).click()
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.admin_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.pim_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.leave_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.time_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.recruitment_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.myinfo_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.performance_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.dashboard_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.directory_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.maintenance_fil)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.driver.find_element(by=By.XPATH, value=self.search_l).send_keys(self.buzz_fil)
        print("UPPERCASE MENU OPETIONS ARE WORKING ON SEARCHBOX")
        
Nivetha().Browsing()
Nivetha().login()  
Nivetha().search()
