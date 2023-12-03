# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
#sleep(3)

# completam username/ password in f de atribut = valoare; driver.//
chrome.find_element(By.XPATH, '//input[@name="username"]').send_keys('tomsmith')
#sleep(3)

# password

#chrome.find_element(By.XPATH, '//input[@name="password"]').send_keys('SuperSecretPassword!')
chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')  # cauta toate elementele cu ajutorul *
#//*[@id="login"]/button/i
#//*[@id="password"]
#sleep(3)

# inspect elementul selenium link in f de textul elementului
#sleep(1)
chrome.find_element(By.XPATH, '//a[text()="Elemental Selenium"]').click()
# login
#chrome.find_element(By.XPATH, '//i[text()=" Login"]').click()
chrome.find_element(By.XPATH, '//*[text()=" Login"]').click()
#sleep(3)

# verificam ca am ajuns pe pagina corecta
expected = 'https://the-internet.herokuapp.com/secure'
actual = chrome.current_url
assert expected == actual, 'Incorrect url, was expecting ' + expected

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCES - TEST PASSED')