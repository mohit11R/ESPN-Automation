from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import Basic_Functions as f
import Stats_Functions as s

# Defining the path of chrome driver 
PATH  = "C:\Program Files (x86)\chromedriver.exe"

# telling webdriver which chrome driver you have to use 
driver = webdriver.Chrome(PATH)


website = driver.get("https://www.espn.in/")
# driver.maximize_window()
driver.implicitly_wait(20)

print("Enter the Choice: ")
print("1. Login Functionality") 
print("2. Feature_Event")
print("3. top_events")
print("4. top_headlines")
print("5. search_Box")
print("6. AddFavorite")
print("7. checking_Sports_Link")
print("8. InfoAboutIndividualSport")
print("9. Quit")

personChoice = int(input("Enter : "))

while  personChoice != 9:
    
    if personChoice == 1:
        f.login(driver)
        
    if personChoice == 2:
        f.Feature_Event(driver)
        
    if personChoice == 3:
        f.top_events
        
        
    if personChoice == 4:
        f.top_headlines(driver)
        
    if personChoice == 5:
        SearchValue = str(input("What u want to search? -- "))
        print("What U want TOP RESULT -- press 1 or ARTICLES -- press 2?")
        Choice = str(input("Enter the Choice"))
        f.search_Box(driver,SearchValue,Choice)
        
        
    if personChoice == 6:
        f.AddFavorite(driver,"basketball")
        f.checking_Sports_Link(driver)
        
    if personChoice == 7:
        f.checking_Sports_Link(driver)
        
    if personChoice == 8:
        s.InfoAboutIndividualSport(driver)
    else:
        print("Enter Valid Number")
    