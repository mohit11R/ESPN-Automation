import unittest
from selenium import webdriver
import testCases as tc



class BaseTesting(unittest.TestCase):
    
    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.espn.in/")
    
    
    def test_title(self):
        self.driver.implicitly_wait(5)
        mainPage = tc.MainPage(self.driver)
        assert mainPage.is_title_matches()
        print('Worked')
    
    def test_watch(self):
        self.driver.implicitly_wait(5)
        mainPage = tc.MainPage(self.driver)
        assert mainPage.is_Watch_video()
        print('Worked')
        
    def test_search(self):
        self.driver.implicitly_wait(5)
        mainPage = tc.MainPage(self.driver)
        assert mainPage.SearchSomething()
        print('Worked')
        
        
    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()