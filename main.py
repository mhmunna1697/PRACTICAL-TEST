#importing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import traceback



#webdriver
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.delete_all_cookies()
wait = WebDriverWait(driver, 30)



#variables
email = 'mehedi.hasan.munna@g.bracu.ac.bd'
password = 'mhmunna'
first_name = 'Mehedi Hasan'
last_name = 'Munna'



#visiting the given URL
def login():
    driver.get("http://automationpractice.com/index.php")



#Clicking on the signin link
def signin():

    try:
        driver.implicitly_wait(60)
        driver.find_element_by_xpath('/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a').click()

    except:
        print(traceback.format_exc())
        print('can not sign in or portal error')



#Creating account with valid email address
def createAccount():

    try:
        driver.implicitly_wait(30)

        #clearing the text field
        driver.find_element_by_xpath('//*[@id="email_create"]').clear()

        #putting email address
        driver.find_element_by_xpath('//*[@id="email_create"]').send_keys(email)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span').click()

    except:
        print(traceback.format_exc())
        print('can not create an account')



#providing personal information
def personalInfo():

    try:
        driver.implicitly_wait(30)

        #select gender
        driver.find_element_by_xpath('//*[@id="id_gender1"]').click()

        #first name
        driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys(first_name)

        #last name
        driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys(last_name)

        #clearing the text field
        driver.find_element_by_xpath('//*[@id="email"]').clear()

        #email address
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)

        #password
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

        #Selecting given 'date of birth'
        #day
        try:   
            select = Select(driver.find_element_by_id('days')).select_by_value('10')
        
        except:
            print(traceback.format_exc())
            print('can not select the day')
        
        #month
        try:   
            select = Select(driver.find_element_by_id('months')).select_by_value('8')
        
        except:
            print(traceback.format_exc())
            print('can not select month')

        #year
        try:   
            select = Select(driver.find_element_by_id('years')).select_by_value('1985')
        
        except:
            print(traceback.format_exc())
            print('can not select year')

        #Signup for our newsletter!
        driver.find_element_by_xpath('//*[@id="newsletter"]').click()

        #YOUR ADDRESS
        #clearing the text field & putting first name
        driver.find_element_by_xpath('//*[@id="firstname"]').clear()
        driver.find_element_by_xpath('//*[@id="firstname"]').send_keys(first_name)

        #clearing the text field & putting last name
        driver.find_element_by_xpath('//*[@id="lastname"]').clear()
        driver.find_element_by_xpath('//*[@id="lastname"]').send_keys(last_name)

        #Company
        driver.find_element_by_xpath('//*[@id="company"]').send_keys('BS21')

        #Address
        driver.find_element_by_xpath('//*[@id="address1"]').send_keys('S 16th Ave ')

        #Address 2
        driver.find_element_by_xpath('//*[@id="address2"]').send_keys('F2')

        #City
        driver.find_element_by_xpath('//*[@id="city"]').send_keys('Tucson')

        #State
        try:
            select = Select(driver.find_element_by_id('id_state')).select_by_value('3')

        except:
            print(traceback.format_exc())
            print('can not select State')
        
        #Zip code
        driver.find_element_by_xpath('//*[@id="postcode"]').send_keys('85701')

        #Country
        try:
            select = Select(driver.find_element_by_id('id_country')).select_by_value('21')

        except:
            print(traceback.format_exc())
            print('can not select Country')

        #Additional information
        driver.find_element_by_xpath('//*[@id="other"]').send_keys('I Love Shopping!')

        #Home phone
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys('01681964716')

        #Mobile phone
        driver.find_element_by_xpath('//*[@id="phone_mobile"]').send_keys('01681964716')

        #Assigning an address alias for future reference
        driver.find_element_by_xpath('//*[@id="alias"]').clear()
        driver.find_element_by_xpath('//*[@id="alias"]').send_keys('E 33rd St, South Tucson')

    
    except:
        print(traceback.format_exc())
        print('can not fill up personal information')




def register():

    try:
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button/span').click()

    except:
        print(traceback.format_exc())
        print('can not register')



def verify():

    try:
        driver.implicitly_wait(30)
        
        login()

        signin()

        #Email address
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)

        #Password
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

        #Sign in
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span').click()

    except:
        print(traceback.format_exc())
        print('can not sign in')



login()
signin()
createAccount()
personalInfo()
register()
verify()