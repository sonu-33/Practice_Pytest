from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pdb
import time
import selenium.webdriver.common.keys
from selenium.webdriver.support.expected_conditions import _find_element



driver = webdriver.Chrome(executable_path="C:/Users/srout/eclipse-workspace/Test_Python_21_Mar/chromedriver.exe")

driver.maximize_window()
driver.get("file:///C:/Users/srout/Desktop/SONALI/Personal/Self%20Learning/HTML/Example_DropDown.html")

driver.set_page_load_timeout(3)

dropdown_select= driver.find_element_by_xpath('//*[@id="princess"]')
#dropdown_select.select_by_visible_index(1)
dropdown_select.select_by_value("Elsa")
pdb.set_trace()

driver.implicitly_wait(5)
dropdown_select.select_by_value("Avg. Customer Review")
driver.implicitly_wait(5)
#pdb.set_trace()
all_options = dropdown_select.options

for i in all_options:
    print(i.text)