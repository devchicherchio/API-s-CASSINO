import time
import requests
from bs4 import BeautifulSoup
import sqlite3

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

URL = "https://historicosblaze.com/br/blaze/crashes"
SESSION = requests.Session()

def fetch_data():
    try:
        response = SESSION.get(URL, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return None

def extract_data(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        values = []
        for i in range(1, 8):
            xpath = f'//*[@id="crashes"]/div[{i}]/div[3]/span'
            value = soup.select_one(xpath).text.strip().replace("X", "")
            values.append(float(value))
        return values
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return [0.0] * 7

def update_database(values, identify):
    try:
        conexão = sqlite3.connect('api.db')
        cursor = conexão.cursor()
        comando = f"UPDATE api SET valor1=?, valor2=?, valor3=?, valor4=?, valor5=?, valor6=?, valor7=?, identify=? WHERE casa='crash_blaze'"
        cursor.execute(comando, values + [identify])
        conexão.commit()
        conexão.close()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o banco de dados: {e}")

def main():
    identify = 0
    while True:
        if identify >= 100:
            identify = 0
        html = fetch_data()
        if html is not None:
            values = extract_data(html)
            identify += 1
            update_database(values, identify)
            print(values)
        while True:
            new_html = fetch_data()
            if new_html == html:
                time.sleep(1)
            else:
                break
        time.sleep(5)

if __name__ == "__main__":
    main()
