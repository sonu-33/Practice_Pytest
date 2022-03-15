from selenium import webdriver
import time
import unittest
import HtmlTestRunner


class LoginTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/chromedriver.exe")
        cls.driver.maximize_window()

    #def testLoginValidation(self):
    def testloginValidation(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(5)    
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("welcome").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[3]/a").click()
        titleName = self.driver.title
        print(titleName)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls): 
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/Practice_POM'),verbosity=2)
