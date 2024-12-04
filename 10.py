from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do navegador
driver = webdriver.Chrome()

try:
    # Passo 1: Acessa a página de login
    driver.get("https://the-internet.herokuapp.com/login")

    # Passo 2: Preenche o formulário com as credenciais
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    # Passo 3: Clica no botão de login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Passo 4: Espera até o site carregar a mensagem de sucesso
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.success")))

    # Passo 5: Verifica se a mensagem de sucesso apareceu
    success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
    if "You logged into a secure area!" in success_message.text:
        print("Login feito com sucesso!")
        
        # Passo 6: Faz uma captura de tela pra mostrar que deu certo
        driver.save_screenshot("login_prova.png")
        print("Captura de tela salva como 'login_proof.png'.")
    else:
        print("Algo deu errado no login.")

finally:
    # Passo 7: Fecha o navegador
    driver.quit()
