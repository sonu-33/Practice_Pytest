class LoginPage():
    
    # mention all the locators in __init__ function
    def __init__(self,driver):
        self.driver = driver
        
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
    
    #Create separate function for User name entry action
    def enterUserName(self, userName):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(userName)
    
    #Create separate function for Password entry action    
    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    
    #Create separate function for Login button click action    
    def clickLogin(self):
        self.driver.find_element_by_id(self.login_button_id).click()
        
            
    