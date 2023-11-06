import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--mute-audio")

    with webdriver.Chrome(service=ChromeDriverManager().install(), options=options) as navegador:
        navegador.maximize_window()
        navegador.get("https://www.betbry.com/game/rowDouble")

        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gbRoot")))
        navegador.find_element(By.CSS_SELECTOR, "#gbRoot").click()

        while True:
            roll_and_update_db(navegador)


def roll_and_update_db(navegador):
    rolou = 'Rolled'
    identify = 0

    try:
        WebDriverWait(navegador, 40).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                             "#gbRoot > div > div.MainLayout_bodyContainer__P0jkj > div > div.RowDoubleGame_game__g5wEe > div.RowDoubleGame_running__FW8Na"),
                                                                            rolou))
        if identify >= 100:
            identify = 0
        values = []

        for i in range(2, 9):
            try:
                value = navegador.find_element(By.XPATH, f'//*[@id="gbRoot"]/div/div[1]/div/div[2]/span[{i}]/div').text
                values.append(value)
            except:
                values.append('0')

        identify += 1

        update_database(values, identify)
        print(','.join(values))
        time.sleep(5)
    except:
        print('Erro')
        pass


def update_database(values, identify):
    try:
        conexão = sqlite3.connect('api.db')
        cursor = conexão.cursor()
        comando = f"UPDATE api SET valor1=?, valor2=?, valor3=?, valor4=?, valor5=?, valor6=?, valor7=?, identify=? WHERE casa='double_betbry'"
        cursor.execute(comando, values + [identify])
        conexão.commit()
    except:
        print('Erro ao atualizar o banco de dados')
    finally:
        conexão.close()


if __name__ == "__main__":
    main()

