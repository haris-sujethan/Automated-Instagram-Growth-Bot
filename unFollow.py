from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
import random
import maskpass
#from secret import UserUsername
#from secret import UserPassword
# The below code gets the username and password manually
# If you would like to import your credentials you can remove the code which prompts you for your username and password

instagramURL = 'https://www.instagram.com/'

# Establishes drivers and opens Instagram


def ChromeDriver():
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])
        global driver
        driver = webdriver.Chrome(options=options,
                                  executable_path=r"C:\chromedriverTesting\chromedriver.exe"
                                  )
        driver.get(instagramURL)
    except Exception as e:
        # If an Exception occurs, prints the error message and quits the driver
        print('An error occured, may be caused by filename, or file location.', e)
        quit()


ChromeDriver()


# Asks the user for their credentials and how many photos they want to like under their specific hashtag

def UserSpecificInformation():
    print('\n')
    print('Hello and welcome to the Instagram bot! You should see a Chrome window containing Instagram, please enter your credentials below, and the bot will run.')
    print('\n')
    global UserUsername
    UserUsername = input('Please Enter Your Instagram Username: ')
    print('\n')

# When the user types their password, it will appear as asterisks

    UserPassword = \
        maskpass.askpass(
            prompt='Please Enter Your Instagram Password: ', mask='*')
    print('\n')
    Username(UserUsername)
    Password(UserPassword)


# Puts the username in ther username field

def Username(UserUsername):

    username = WebDriverWait(driver,
                             20).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//input[@name='username']")))
    username.send_keys(UserUsername)


# Puts the password in ther username field

def Password(UserPassword):
    password = WebDriverWait(driver,
                             20).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//input[@name='password']")))
    password.send_keys(UserPassword)


# Presses the login button
def Login():
    login = WebDriverWait(driver,
                          20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'button[type="submit"]')))
    login.click()


UserSpecificInformation()
Login()

time.sleep(5)


driver.get(instagramURL + UserUsername + '/' + 'following')

time.sleep(5)

unFollow = driver.find_elements(By.XPATH, '//*[text()="Following"]')

unFollowCount = 0

for i in unFollow:
    try:
        time.sleep(4)
        i.click()
        time.sleep(4)
        confirmUnfollow = driver.find_element(By.XPATH,
                                              """/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]""")
        confirmUnfollow.click()
        unFollowCount = unFollowCount + 1
        print('\n')
        print("User Unfollowed")
    except Exception as e:
        print('\n')
        print("Error occurred, moving to next user")

    time.sleep(5)

print('\n')
print("Finished! Unfollowed {} users".format(unFollowCount))
