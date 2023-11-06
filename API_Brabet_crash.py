import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sqlite3


def brabetcrash():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--mute-audio")
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.maximize_window()

    while True:
        try:
            navegador.get("https://tipminer.com/brabet-gaming/crash")
            time.sleep(5)
            identify = 70
            while True:
                try:
                    if identify >= 1000:
                        identify = 0
                    id0 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(1) > div > div').text.replace(
                        "X", ""))
                    id1 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(2) > div > div').text.replace(
                        "X", ""))
                    id2 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(3) > div > div').text.replace(
                        "X", ""))
                    id3 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(4) > div > div').text.replace(
                        "X", ""))
                    id4 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(5) > div > div').text.replace(
                        "X", ""))
                    id5 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(6) > div > div').text.replace(
                        "X", ""))
                    id6 = float(navegador.find_element(By.CSS_SELECTOR,
                                                       '#crash > div > div > div:nth-child(7) > div > div').text.replace(
                        "X", ""))
                    identify = identify + 1
                    conexão = sqlite3.connect('api.db')
                    cursor = conexão.cursor()
                    comando = f"UPDATE api SET valor1={id0}, valor2={id1}, valor3={id2}, valor4={id3}, valor5={id4}, valor6={id5}, valor7={id6}, identify={identify} WHERE casa='crash_brabet'"
                    cursor.execute(comando)
                    conexão.commit()
                    print(f'({id0}),({id1}),({id2}),({id3}),({id4}),({id5}),({id6}),')
                    ul = navegador.find_element(By.CSS_SELECTOR,
                                                '#crash > div > div > div:nth-child(1) > div.time').text
                    while True:
                        ul1 = navegador.find_element(By.CSS_SELECTOR,
                                                     '#crash > div > div > div:nth-child(1) > div.time').text
                        if ul == ul1:
                            pass
                        else:
                            break
                except:
                    print('erro brabet crash')
                    break
        except:
            print('erro de conexão brabet crash')
            pass
    navegador.quit()


if __name__ == "__main__":
    brabetcrash()

