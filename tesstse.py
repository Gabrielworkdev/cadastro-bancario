from requests import requests
from bs4 import BeautifulSoup
import time

def check_website_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para códigos de resposta HTTP diferentes de 2xx
        return True
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return False

def monitor_website_changes(url):
    previous_content = None

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()

            current_content = response.content

            if current_content != previous_content:
                print("Detetada uma alteração na página!")

                # Aqui você pode adicionar a lógica para enviar um alerta (por exemplo, e-mail, notificação, etc.)

            previous_content = current_content

        except requests.RequestException as e:
            print(f"Erro ao acessar o site: {e}")

        time.sleep(60)  # Espera por 60 segundos antes de verificar novamente

if __name__ == "__main__":
    website_url = "https://www.central.rj.gov.br/"

    if check_website_status(website_url):
        print("O site está online. Iniciando monitoramento de alterações...")
        monitor_website_changes(website_url)
    else:
        print("O site está offline.")
