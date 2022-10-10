from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime
import sys
from config import *

def open_viding():
    driver_path = "C:/Users/RA135GG/OneDrive - EY/Documents/.02_Personal/VidingBot/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path

    browser = webdriver.Chrome(executable_path=driver_path, options=option)

    browser.get("https://vidingcenter.provis.es/Login")
    browser.maximize_window()

def login(worked, tryAgain):

    #worked = worked
    #tryAgain = tryAgain
    username_keys = credentials.username
    password_keys = credentials.password

    username = browser.find_element(By.NAME, "Username")
    password = browser.find_element(By.NAME, "Password")

    username.send_keys(username_keys)
    password.send_keys(password_keys)
    password.send_keys(Keys.RETURN)

def pool(month, day, time, week_day = 1):
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

    actividades_libres = browser.find_element(By.XPATH, "/html/body/section/div[1]/aside/div[2]/div[1]/nav/ul/li[4]/a/div/div/i")
    reservar_actividades_libres = browser.find_element(By.XPATH, "/html/body/section/div[1]/aside/div[2]/div[1]/nav/ul/li[4]/ul/li[1]/a")

    actividades_libres.click()
    reservar_actividades_libres.click()

    entre_semana = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/section/div/div/div/div/div[1]/div[1]")
    fin_de_semana = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/section/div/div/div/div/div[2]/div[1]")

    if week_day == 1:
        entre_semana.click()
        
        date_picker = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        date_picker.click()
        
        month_title = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[2]/div[2]/div[1]/div/div/div/div[1]/div/ul/li[1]/div/div[1]/table/thead/tr[1]/th[2]")
        next_month = browser.find_element(By.XPATH, "/html/body/section/div[1]/")

        while meses.get(month) not in month_title.text:
            next_month.click()

        #buscar el dia deseado
    
    else:
        fin_de_semana.click()

        date_picker = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        date_picker.click()
        
        month_title = browser.find_element(By.XPATH, "/html/body/section/div[1]/section/div[2]/div[2]/div[1]/div/div/div/div[1]/div/ul/li[1]/div/div[1]/table/thead/tr[1]/th[2]")
        next_month = browser.find_element(By.XPATH, "/html/body/section/div[1]/")

        while meses.get(month) not in month_title.text:
            next_month.click()

        #buscar el dia deseado




open_viding()
browser.implicitly_wait(10)
login()
browser.implicitly_wait(10)
#pool(month = , day = , time = )
