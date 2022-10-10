from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime
import config

# OLD WAY
# driver_path = "C:/Users/RA135GG/OneDrive - EY/Documents/.02_Personal/VidingBot/chromedriver.exe"
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# option = webdriver.ChromeOptions()
# option.binary_location = brave_path

# browser = webdriver.Chrome(executable_path=driver, options=option)

# WEBDRIVER_MANAGE WAY
browser = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

browser.get("https://vidingcenter.provis.es/Login")
browser.maximize_window()

# Save time variables
# today = datetime.now()
# day = today.day + 1
# month = datetime.today()

# Wait for the page to fully load
browser.implicitly_wait(20)

username_keys = config.username
password_keys = config.password

# Login
username = browser.find_element(By.NAME, "Username")
password = browser.find_element(By.NAME, "Password")

username.send_keys(username_keys)
password.send_keys(password_keys)
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
desired_day = 2
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

# When the desired date is selected, zoom out and scroll to bottom
browser.execute_script("document.body.style.zoom='70%'")
time.sleep(2)
browser.execute_script("window.scrollTo(0, 100);")
browser.execute_script("window.scrollTo(100, 200);")
browser.execute_script("window.scrollTo(200, 300);")
browser.execute_script("window.scrollTo(300, 500);")
browser.execute_script("window.scrollTo(500, 700);")
browser.execute_script("window.scrollTo(700, document.body.scrollHeight);")
browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

# Find right time Reservation button
## Reservation button id="136(YYYY)(MM)(DD)(HHHH)"
## Reservation button class="btn btn-lg pull-right vistaContenidoT  btn-success "
# #29/08/2022 
# 136202208291030
# 136202208291230
# 136202208291630
# #30/08/2022
# 136202208301030

book_buttons = browser.find_elements(By.XPATH, "//*[@class = 'btn btn-lg pull-right vistaContenidoT  btn-success ']")

for slot in book_buttons:
    if str(desired_time) in slot.get_attribute("id"):
        slot.click()
        break


button = browser.find_element(By.ID, "136202209021030")
button.is_displayed()
button = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[3]/div/ol/li[1]/div[2]/div/div[3]/button")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "136202208311030")))