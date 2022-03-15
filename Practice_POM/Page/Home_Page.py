class HomePage():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.welcome_link_id = "welcome"
        self.logout_link_text = "Logout"
        
    def clickWelcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
    
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()