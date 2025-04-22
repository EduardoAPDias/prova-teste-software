#Este bloco importa todas as bibliotecas usadas posteriormente no código
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

#inicializa o chrome e maximiza janela
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try: #captura erros na execução 
    url = "https://www.hankeds.com.br/prova/login.html" #URL
    driver.get(url) #URL

    time.sleep(2) #Espera

    def digitar_lento(elemento, texto, delay=0.25): #delay na digitação
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(delay)

    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #acha username por ID
    senha = driver.find_element(By.ID, "password")#acha password por ID
    botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]") # acha o botão por xpath

    digitar_lento(usuario, "admin") #admin respeitando a espera
    time.sleep(1) #espera
    digitar_lento(senha, "admin123456") #digita senha respeitando a espera
    time.sleep(1)#espera

    botao.click() #clica no botão especificado
    time.sleep(4)#espera

    if "destino.html" in driver.current_url: #confirma o destino e se deu certo
        print(" Teste passou: redirecionado corretamente.")
    else:
        print(" Teste falhou: redirecionamento não ocorreu.")

    time.sleep(5)#espera

except Exception as e: #se teve erro no teste print do erro
    print(" Erro durante o teste:", str(e))

finally:
    driver.quit()