from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime

# driver_path = "C:/Users/RA135GG/OneDrive - EY/Documents/.02_Personal/VidingBot/chromedriver.exe"
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver_path = r"C:\Users\RJ855MF\Documents\MIO\VidingBot\VidingBot\chromedriver.exe"
brave_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, options=option)

browser.get("https://vidingcenter.provis.es/Login")
browser.maximize_window()

# Save time variables
today = datetime.now()
day = today.day + 1
month = datetime.today()

# Wait for the page to fully load
browser.implicitly_wait(20)

# Login
username = browser.find_element(By.NAME, "Username")
password = browser.find_element(By.NAME, "Password")

username.send_keys("pablochaure@gmail.com")
password.send_keys("Maricarmenes13.")
password.send_keys(Keys.RETURN)

# Navigate to 'Reservar actividades libres'
actividades_libres = browser.find_element(By.XPATH, "/html/body/section/div[1]/aside/div[2]/div[1]/nav/ul/li[4]/a/div/div/i")
reservar_actividades_libres = browser.find_element(By.XPATH, "/html/body/section/div[1]/aside/div[2]/div[1]/nav/ul/li[4]/ul/li[1]/a")

actividades_libres.click()
reservar_actividades_libres.click()

# Click for weekdays pool
entre_semana = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/section/div/div/div/div/div[1]/div[1]")
fin_de_semana = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/section/div/div/div/div/div[2]/div[1]")

entre_semana.click()
#fin_de_semana.click()

# Select desired date
date_picker = browser.find_element(By.XPATH, "//*[@class = 'form-control datetimepicker']")
date_picker.click()
#print(date_picker.get_attribute("value")) #25 de agosto de 2022

month_title = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[2]/div[2]/div[1]/div/div/div/div[1]/div/ul/li[1]/div/div[1]/table/thead/tr[1]/th[2]")
next_month = browser.find_element(By.CSS_SELECTOR, "*[class = 'next']")

#today_activate_date = browser.find_element(By.XPATH, "//*[@class = 'day active today']")
#today_date = browser.find_element(By.XPATH, "//*[@class = 'day today']")
#print('The current selected date is: {}'.format(today_date.text)) #25
#print(today_date.get_attribute("data-day")) #25/08/2022

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
desired_month = 9
desired_day = 5
desired_time = 1030

while meses.get(desired_month) not in month_title.text:
    next_month.click()

available_days = browser.find_elements(By.XPATH, "//*[@class = 'day']")
for i in available_days:
    if int(i.text) == desired_day:
        i.click()
        browser.implicitly_wait(15)
        #print("Clicked on {day}-{month}".format(day = int(i.text) , month = month_title.text))
        break
    else:
        print("I could not find your desired booking date")




from selenium.webdriver.common.action_chains import ActionChains

book_buttons = browser.find_elements(By.XPATH, "//*[@class = 'btn btn-lg pull-right vistaContenidoT  btn-success ']")
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(book_buttons[0]).click(book_buttons[0]).perform()