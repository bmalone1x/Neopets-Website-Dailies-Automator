######################################################
#   Neopets Dailies Automater 
#   Designed only for use with Microsoft Edge 
#
#   Developed by Bradley
##########################################################


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

## MS Edge Web Driver for Automation ##
path_to_msedgedriver = ".\\msedgedriver.exe"
s = Service(path_to_msedgedriver)

browser = webdriver.Edge(service=s)
browser.get("http://www.neopets.com")
browser.maximize_window()

time.sleep(3)

browser.find_element(By.CLASS_NAME, "nav-tab-button__2020").click() 

################## Your Login Info ################
username = ""
password = ""
browser.find_element(By.ID, "loginUsername").send_keys(username)
browser.find_element(By.ID, "loginPassword").send_keys(password)


browser.find_element(By.ID, "loginButton").click()

#Logged In



time.sleep(3)

#################### Fruit Wheel #########################
browser.execute_script("window.open('https://www.neopets.com/desert/fruit/index.phtml')")
browser.switch_to.window(browser.window_handles[1])

time.sleep(3)

try:
    fruit_wheel_submit = browser.find_element(By.XPATH, "//form/input[@value='Spin, spin, spin!']")
    fruit_wheel_submit.submit()
    time.sleep(5)
except:
    print("You already did your 1 allowed spin of the Fruit Wheel Today!")


################# Free Jelly #############################

browser.execute_script("window.open('http://www.neopets.com/jelly/jelly.phtml')")
browser.switch_to.window(browser.window_handles[2])

time.sleep(3)

try:
    jelly_submit = browser.find_element(By.XPATH, "//form/input[@value='Grab some Jelly']")
    jelly_submit.submit()
except:
    print("You already grabbed your slice of jelly today!")

############## Tombola ##################################

browser.execute_script("window.open('http://www.neopets.com/island/tombola.phtml')")
browser.switch_to.window(browser.window_handles[3])

time.sleep(3)

try:
    tombola_submit = browser.find_element(By.XPATH, "//form/input[@value='Play Tombola!']")
    tombola_submit.submit()
except:
    print("You already played tombola or it is temporarily closed!")

###########The Discarded Magical Blue Grundo Plushie of Prosperity########

browser.execute_script("window.open('http://www.neopets.com/faerieland/tdmbgpop.phtml')")
browser.switch_to.window(browser.window_handles[4])

time.sleep(3)

try:
    magical_plushie_submit = browser.find_element(By.XPATH, "//form/input[@value='Talk to the Plushie']")
    magical_plushie_submit.submit()
except:
    print("You already talked to the plushie today!")

########## Slorg Payout #########

time.sleep(3)

browser.execute_script("window.open('http://www.neopets.com/shop_of_offers.phtml?slorg_payout=yes')")
browser.switch_to.window(browser.window_handles[5])

########### Coltzan's Shrine ########


browser.execute_script("window.open('http://www.neopets.com/desert/shrine.phtml')")
browser.switch_to.window(browser.window_handles[6])

time.sleep(3)

try:
    shrine_submit = browser.find_element(By.XPATH, "//form/input[@value='Approach the Shrine']")
    shrine_submit.submit()
except:
    print("You already talked to Coltzan today!")

######### Anchor's Management #######


browser.execute_script("window.open('http://www.neopets.com/pirates/anchormanagement.phtml')")
browser.switch_to.window(browser.window_handles[7])

time.sleep(3)

try:
    anchor_submit = browser.find_element(By.XPATH, "//*[@id='btn-fire']/a")
    anchor_submit.click()
except:
    print("You already fired the harpoon earlier!")

########## Collect Daily Bank Interest ####

browser.execute_script("window.open('http://www.neopets.com/bank.phtml')")
browser.switch_to.window(browser.window_handles[8])

time.sleep(3)

try:
    interest_submit = browser.find_element(By.XPATH, "//form/input[@value='Collect Interest']")
    interest_submit.submit()
except:
    print("You already collected your bank interest")
    
    
    
###### Just Opening Links from here ######



######## Trudy's Surprise Slot Machine #######

time.sleep(3)

browser.execute_script("window.open('http://www.neopets.com/trudys_surprise.phtml')")  
browser.switch_to.window(browser.window_handles[9])


###### Stock Links ######

browser.execute_script("window.open('http://www.neopets.com/stockmarket.phtml?type=portfolio')")
browser.switch_to.window(browser.window_handles[10])

browser.execute_script("window.open('http://www.neopets.com/stockmarket.phtml?type=list&bargain=true')")
browser.switch_to.window(browser.window_handles[11])

