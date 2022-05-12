from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
import random
import maskpass


# Establishes drivers and opens Instagram

def ChromeDriver():
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])
        global driver
        driver = webdriver.Chrome(options=options,
                                  executable_path=r"C:\Program Files (x86)\chromedriver.exe"
                                  )
        driver.get('https://www.instagram.com/?hl=en')
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
    UserUsername = input('Please Enter Your Instagram Username: ')
    print('\n')

# When the user types their password, it will appear as asterisks

    UserPassword = \
        maskpass.askpass(
            prompt='Please Enter Your Instagram Password: ', mask='*')
    print('\n')
    global HashTag
    HashTag = input('What HashTag Would you Like to Search: #')
    print('\n')
    global Likes
    Likes = int(input('How Many Photos do you Want to interact with? '))
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

time.sleep(2)


# Clicks Not now on the instagram pop ups

def IgnorePopUp():
    NotNow = WebDriverWait(driver,
                           20).until(EC.element_to_be_clickable((By.XPATH,
                                                                 "//button[contains(text(), 'Not Now')]")))
    NotNow.click()


IgnorePopUp()

time.sleep(5)

IgnorePopUp()

time.sleep(5)


# Enters the user-specific hashtag

def Search(HashTag):
    search = WebDriverWait(driver,
                           20).until(EC.element_to_be_clickable((By.XPATH,
                                                                 '//input[@placeholder="Search"]')))
    search.send_keys('#' + HashTag + ' ')
    time.sleep(5)
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    search.send_keys(Keys.ENTER)
    time.sleep(5)


Search(HashTag)

Counter = 0

# Poteinal comments (randomly selected for every post)

ListofComments = ['Nice!', 'Good Post!', 'Cool!', 'Amazing!']


# Clicks the first image in the hashtag, likes and comments

def FirstImage():
    Image = WebDriverWait(driver,
                          20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                    '_9AhH0')))
    Image.click()
    ImageLike = WebDriverWait(driver,
                              20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                    'fr66n')))
    ImageLike.click()
    Comment = WebDriverWait(driver,
                            20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                  'PUqUI.Ypffh')))
    Comment.click()
    time.sleep(4)
    Comment = WebDriverWait(driver,
                            20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                  'PUqUI.Ypffh')))
    Comment.click()
    Comment.send_keys(random.choice(ListofComments))
    Comment.submit()
    global Counter
    Counter = Counter + 1


FirstImage()


# After an image is liked and commented on, the bot will click the right arrow key and like and comment on each new post
# until the desired amount of photos is completed or reaches the end of the hashtag.

def LikeAndCommentCycle(Likes):
    global Counter
    while Likes > Counter:
        try:

            driver.find_element(By.XPATH,
                                "//button[@class='wpO6b  ']//*[@aria-label='Next']"
                                ).click()
            ImageLike = WebDriverWait(driver,
                                      20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                            'fr66n')))
            ImageLike.click()
            Counter = Counter + 1
            Comment = WebDriverWait(driver,
                                    20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                          'PUqUI.Ypffh')))
            Comment.click()
            time.sleep(4)
            Comment = WebDriverWait(driver,
                                    20).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                          'PUqUI.Ypffh')))
            Comment.click()
            Comment.send_keys(random.choice(ListofComments))
            Comment.submit()
        except Exception as e:
            print(
                'An error occured, may be caused by no other posts existing in the hashtag')

            driver.find_element(By.XPATH,
                                "//button[@class='wpO6b  ']//*[@aria-label='Next']"
                                ).click()
            pass


LikeAndCommentCycle(Likes)

time.sleep(10)

driver.quit()
