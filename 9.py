# Durante a automação de testes, como você lidaria com pop-ups ou alertas usando
# Selenium WebDriver? Escreva um trecho de código em Python que feche um alerta
# assim que ele aparecer. (2 pontos)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configuração do WebDriver
driver = webdriver.Chrome()

try:
    # 1. Abra uma página de teste
    driver.get("https://www.example.com")

    # 2. Criar manualmente um alerta para teste
    driver.execute_script("alert('Teste de alerta!');")

    # 3. Aguardar o alerta aparecer e interagir com ele
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())  # Espera até 10 segundos
        alert = driver.switch_to.alert  # Alternar para o alerta
        print("Texto do alerta:", alert.text)  # Exibir o texto do alerta
        alert.accept()  # Fechar o alerta clicando em "OK"
        print("Alerta fechado com sucesso.")

        # Capturar uma captura de tela como prova
        driver.save_screenshot("alert_prova.png")
        print("Captura de tela salva como 'alert_proof.png'.")

    except TimeoutException:
        print("Nenhum alerta apareceu no tempo esperado.")

finally:
    # Fechar o navegador
    driver.quit()

