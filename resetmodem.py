from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# Modem yönetim arayüzü URL'si ve kullanıcı bilgilerini burada ayarlayın
modem_url = "http://192.168.1.1"  # Modem yönetim arayüzünün URL'sini ayarlayın
username = "admin"  # Modem yönetim kullanıcı adınızı ayarlayın
password = "admin"  # Modem yönetim şifrenizi ayarlayın

# Chrome WebDriver'ı başlatın
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Modem yönetim arayüzüne gidin
driver.get(modem_url)
alert = Alert(driver)
wait = WebDriverWait(driver, 20)
# Kullanıcı adı ve şifre alanlarına verileri girin ve giriş yapın
wait.until(EC.visibility_of_element_located((By.ID, 'userName')))
driver.find_element("id", "userName").send_keys(username)
wait.until(EC.visibility_of_element_located((By.ID, 'pcPassword')))
driver.find_element("id","pcPassword").send_keys(password)
driver.find_element("id","loginBtn").click()
time.sleep(1)
wait.until(EC.visibility_of_element_located((By.ID, 'skipBtn')))
driver.find_element("id","skipBtn").click()
time.sleep(1)
alert.accept()
time.sleep(1)
driver.find_elements(By.CLASS_NAME,"btnText")[1].click()
wait.until(EC.visibility_of_element_located((By.ID, 'menu_tools')))
driver.find_element("id","menu_tools").click()
wait.until(EC.visibility_of_element_located((By.ID, 'menu_restart')))
driver.find_element("id","menu_restart").click()
wait.until(EC.visibility_of_element_located((By.ID, 'button_reboot')))
driver.find_element("id","button_reboot").click()
time.sleep(1)
alert.accept()
# Modem sıfırlama işlemi tamamlandıktan sonra, bekleyin (zamanı ihtiyaca göre ayarlayın)
time.sleep(40)

# Tarayıcıyı kapatın
driver.quit()