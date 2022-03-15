from selenium import webdriver
# Below code is not a pytest. It can be run using Eclipse editor


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(5)
   

def test_login(test_setup):
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_name("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    driver.implicitly_wait(5)
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[3]/a").click()
    driver.implicitly_wait(2)
    titleName = driver.title
    print(titleName)

def test_teardown():
    driver.close()
    driver.quit()     
    

result = test_setup()
test_login(result)
test_teardown()

print("******** Test Completed Successfully *********")

