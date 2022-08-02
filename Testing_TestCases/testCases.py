# from locator import *
# from element import BasePageElement
from selenium import webdriver



class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        

class MainPage(BasePage):
    
    
    def is_title_matches(self):
        return  "ESPN: Serving sports fans. Anytime. Anywhere"  in self.driver.title
    
    
    def is_Watch_video(self):
        element = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/a/span/span[1]")
        print(element.text)
        return element.text == "Watch"
    
    
    def SearchSomething(self):
        value = input("Enter: ")
        self.driver.implicitly_wait(5)
        searchBoxIcon = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/a")
        self.driver.implicitly_wait(5)
        searchBoxIcon.click()

        SearchInputBox = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/div/div/input[1]")
        SearchInputBox.send_keys(value)

        submitButton = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/div/div/input[2]")
        submitButton.click()
        
        finalOutput = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[2]/div/div/div[3]/section/div/ul/div/div[1]/li/article/a/div/h2/span/span")
        print(finalOutput.text)
        
        return value in finalOutput.text
        
        
        
        
    
    