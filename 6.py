# Crie um script em Python usando Selenium WebDriver que: (3 pontos)
# Abra o navegador e acesse o site https://www.google.com.
# Procure pela barra de pesquisa (search bar).
# Digite a palavra "Python Selenium" e pressione Enter.
# Faça uma captura de tela da página de resultados e salve como resultado.png

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configuração do WebDriver (ajuste o caminho do driver se necessário)
driver = webdriver.Chrome()

try:
    # 1. Abra o navegador e acesse o site Google
    driver.get("https://www.google.com")

    # 2. Procure pela barra de pesquisa
    search_bar = driver.find_element(By.NAME, "q")

    # 3. Digite a palavra "Python Selenium" e pressione Enter
    search_bar.send_keys("Python Selenium")
    search_bar.send_keys(Keys.RETURN)

    # 4. Espere um pouco para garantir que a página seja carregada
    driver.implicitly_wait(5)

    # 5. Faça uma captura de tela da página de resultados
    driver.save_screenshot("resultado.png")

    print("Captura de tela salva como resultado.png")

finally:
    # 6. Feche o navegador
    driver.quit()
