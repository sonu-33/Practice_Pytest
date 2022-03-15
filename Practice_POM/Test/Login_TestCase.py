from Practice_POM.Page.Login_Page import LoginPage
from Practice_POM.Page.Home_Page import HomePage
from selenium import webdriver
import unittest
import HtmlTestRunner


class loginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome(executable_path="C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)
    
    def testloginVaidation(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver) # driver is used as an argument here because the same argument was mentioned in Loginpage class
        login.enterUserName("Admin")
        login.enterPassword("admin123")
        login.clickLogin()
        
        homepage = HomePage(driver)
        homepage.clickWelcome()
        homepage.clickLogout()

     
    @classmethod    
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/Practice_POM'),verbosity=2)
