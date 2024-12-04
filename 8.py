# Em Selenium WebDriver com Python, escreva um código para realizar o seguinte:
# Abrir o navegador e acessar https://www.selenium.dev/.
# Navegar até a seção Downloads clicando no link correspondente.
# Extraia o texto do cabeçalho principal (h1 ou h2) da página e imprima no console.


from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do WebDriver (ajuste o caminho do driver se necessário)
driver = webdriver.Chrome()

try:
    # 1. Abrir o navegador e acessar https://www.selenium.dev/
    driver.get("https://www.selenium.dev/")

    # 2. Navegar até a seção Downloads clicando no link correspondente
    download_link = driver.find_element(By.LINK_TEXT, "Downloads")
    download_link.click()

    # 3. Extrair o texto do cabeçalho principal da página (h1 ou h2)
    header = driver.find_element(By.TAG_NAME, "h1")
    header_text = header.text
    print("Texto do cabeçalho principal:", header_text)

    # 4. Capturar uma captura de tela como prova
    driver.save_screenshot("selenium_downloads_prova.png")
    print("Captura de tela salva como 'selenium_downloads_prova.png'.")

finally:
    # 5. Fechar o navegador
    driver.quit()
