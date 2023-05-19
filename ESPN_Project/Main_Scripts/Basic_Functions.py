# Login Function
from selenium.webdriver.common.by import By


def login(driver):
    
    driver.find_element_by_xpath("/html/body/div[5]/section/section/div/section[1]/article[2]/button[2]").click()

    driver.implicitly_wait(5)

    Username = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/form/section/div[1]/div/label/span[2]/input")
    Username.send_keys("")
    driver.implicitly_wait(5)
    Password = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/form/section/div[2]/div/label/span[2]/input")
    Password.send_keys("")
    driver.implicitly_wait(10)
    Login_Button = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/form/section/div[3]/button")
    Login_Button.click()
    
    
def Feature_Event(driver):
    
    Feature_events = driver.find_elements_by_class_name("quicklinks_list__detail")
    event_type = []
    for Feature in Feature_events:
            event_type.append(str(Feature.text))
    with open("Main Events" , 'w') as file:
        i = 1 
        for event in event_type:
            file.write(str(i) + ") " + event + " \n")
            i+=1
        
def top_events(driver):
    
    topEventBn = driver.find_element_by_xpath("/html/body/div[5]/div[2]/section/div/div/div[1]/div[2]/button")
    topEventBn.click()
    
    topEventsName = driver.find_element_by_xpath("/html/body/div[5]/div[2]/section/div/div/div[1]/div[2]")
    print("TOP EVENTS LIST")
    print(topEventsName.text)
    
    
def top_headlines(driver):
    
    topHeadlines = driver.find_element_by_xpath("/html/body/div[5]/section/section/div/section[3]/div[1]")
    print(topHeadlines.text)
    

def search_Box(driver, input , choice):
    driver.implicitly_wait(5)
    searchBoxIcon = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/a")
    driver.implicitly_wait(5)
    searchBoxIcon.click()

    SearchInputBox = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/div/div/input[1]")
    SearchInputBox.send_keys(input)
    driver.implicitly_wait(5)
    
    submitButton = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[1]/div/div/input[2]")
    submitButton.click()
    
    driver.implicitly_wait(10)
    
    if choice == "1":
        topResult = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[2]/div/div/ul/li[1]/a")
        topResult.click()
    else:
        articles = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[2]/div/div/ul/li[2]/a")
        articles.click()
    
    
def AddFavorite(driver,searchValue):
    
    loginFun = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/div[2]/ul/li[2]/div")
    addFavFun = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/ul[2]/li/div/div/a")
    addFavFun.click()
    
    driver.implicitly_wait(5)
    
    findTOAdd = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div/div/section/div/section/div/div/div/input")
    findTOAdd.send_keys(searchValue)
    
    driver.implicitly_wait(5)
    follow = driver.find_element_by_relative_xpath('//*[@id="fittPortal_0"]/div/div/section/div/div/section/div/section/section[1]/div/ul/li[2]/div[2]/div/button')
    

def checking_Sports_Link(driver):
    print("Select the Sport You want to go.")
    print("1)Cricket \n2)Football \n3)Olympic Sports \n4)F1 \n5)NBA \n6)Tennis \n7)Boxing \n8)Hockey \n9)Athletics \n10)Badminton")
    SelectSports = input("Enter: ")
    
    if SelectSports == "1":
        cricketLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]")
        cricketLink.click()
    
    if SelectSports == "2":
        FootballLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[2]/a/span/span[1]")
        FootballLink.click()
    
    if SelectSports == "3":
        OlympicLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[3]/a/span/span[1]")
        OlympicLink.click()
    
    if SelectSports == "4":
        F1Link = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[4]/a/span/span[1]")
        F1Link.click()
    
    if SelectSports == "5":
        nbaLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[5]/a/span/span[1]")
        nbaLink.click()
    
    if SelectSports == "6":
        TennisLInk = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[6]/a/span/span[1]")
        TennisLInk.click()
    
    if SelectSports == "7":
        goToDot = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/a")
        goToDot.click()
        BoxingLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/div/ul/li[2]/a/span/span[1]")
        BoxingLink.click()
    
    if SelectSports == "8":
        goToDot = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/a")
        goToDot.click()
        HockeyLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/div/ul/li[5]/a/span/span[1]")
        HockeyLink.click()
    
    if SelectSports == "9":
        goToDot = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/a")
        goToDot.click()
        AthleticsLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/div/ul/li[8]/a/span/span[1]")
        AthleticsLink.click()
    else:
        goToDot = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/a")
        goToDot.click()
        BadmintonLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[7]/div/ul/li[9]/a/span/span[1]")
        BadmintonLink.click()

    

def InfoAboutIndividualSport(driver):
    
    print("Now WE only 2 Options")
    print("Press 1 for Cricket   or press 2 for NBA")
    
    choiceSport = input("Enter : ")
    
    if choiceSport == "1":
        cricketLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]")
        cricketLink.click()
        
        driver.implicitly_wait(8)
        
        print("Choice What you want to Know About Cricket")
        print("1)Scores \n2)Series \n3)Teams \n4)ICC Ranking \n5)Stats ")
        
        InfoCheck = input("Enter the number : ")
        
        if InfoCheck == "1":
            scoresInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[3]/a/span[1]")
            scoresInfo.click()
        
        if InfoCheck == "2":
            seriesInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[4]/a/span[1]")
            seriesInfo.click()
        
        if InfoCheck == "3":
            teamInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[5]/a/span[1]")
            teamInfo.click()
            
        if InfoCheck == "4":
            rankingInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[6]/a/span[1]")
            rankingInfo.click()
        
        else:
            statsInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[7]/a/span[1]")
            statsInfo.click()
    
    else:
            
        nbaLink = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[1]/ul/li[5]/a/span/span[1]")
        nbaLink.click()
        
        driver.implicitly_wait(8)
        
        print("Choice What you want to Know About NBA")
        print("1)Draft \n2)Scores \n3)Schedule \n4)Standings \n5)Stats \n6)Teams \n7)Players \n8)Daily Lines")
        
        InfoCheck = input("Enter the number : ")
        
        if InfoCheck == "1":
            draftInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[3]/a/span[1]")
            draftInfo.click()
        
        if InfoCheck == "2":
            scoresInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[4]/a/span[1]")
            scoresInfo.click()
        
        if InfoCheck == "3":
            scheduleInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[5]/a/span[1]")
            scheduleInfo.click()
        
        if InfoCheck == "4":
            standingInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[6]/a/span[1]")
            standingInfo.click()
        
        if InfoCheck == "5":
            statsInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[7]/a/span[1]")
            statsInfo.click()
        
        if InfoCheck == "6":
            teamsInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[8]/a/span[1]")
            teamsInfo.click()
        
        if InfoCheck == "7":
            playersInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[9]/a/span[1]")
            playersInfo.click()
        else:
            dailyInfo = driver.find_element_by_xpath("/html/body/div[5]/div[2]/header/nav[2]/div/ul/li[10]/a/span[1]")
            dailyInfo.click()
            
    
