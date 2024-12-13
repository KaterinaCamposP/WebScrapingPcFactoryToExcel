from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText

#Librerias instaladas: selenium, pandas, smtplib

#Configuraciones del navegador
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

service = Service(executable_path="geckodriver.exe")
driver = webdriver.Firefox(service=service, options=firefox_options)

url = "https://www.pcfactory.cl/"
driver.get(url)

#Interaccion con buscador
search_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "search-input-desktop"))
)
search_box.click()
search_box.send_keys("tablet")
search_box.send_keys(Keys.ENTER)
time.sleep(10)

#Extrayendo data
nombres_elementos = driver.find_elements(By.XPATH, "//h2[contains(@class,'products__item__info__name pcf-text--sm pcf-fw-bold')]")
precios_elementos = driver.find_elements(By.XPATH, "//span[contains(@class,'pcf-price')]")

nombres = [nombre.text.strip() for nombre in nombres_elementos]
precios = [precio.text.strip() for precio in precios_elementos]

#Verificando data
print("Nombres encontrados:")
for nombre in nombres:
    print(nombre)

print("\nPrecios encontrados:")
for precio in precios:
    print(precio)

#Creando archivo con data
df = pd.DataFrame(list(zip(nombres, precios)), columns=['Nombre', 'Precio'])
df.to_excel('listado_tablets.xlsx', index=False)

driver.quit()

