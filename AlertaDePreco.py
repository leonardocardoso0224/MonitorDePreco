import requests
import time
from bs4 import BeautifulSoup
contagem = 0
while contagem < 1:
    time.sleep(10800)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    url = "https://www.kabum.com.br/produto/463543/placa-de-video-rx-7600-series-graphics-cards-xfx-amd-radeon-8gb-gddr6-rx-76pqickby"

    def enviar_alerta(menssagem):
        token = "Seu Token aqui"
        chat_id = "Seu Chat ID Aqui"
        url_telegram = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={menssagem}"
        requests.get(url_telegram) 

    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")
    precotexto = soup.find("h4", string=lambda t: "R$" in t if t else False)

    if precotexto:
        # --- Repare nos 4 espaços de recuo nestas linhas abaixo ---
        precotexto_limpo = precotexto.text.strip()
        print(f"Preço Encontrado: {precotexto_limpo}")

        valorLimpo = precotexto_limpo.replace("R$", "").replace(".", "").replace(",", ".").strip()
        precoFinal = float(valorLimpo)

        precoFinal = float(valorLimpo)

        titulo = soup.find("h1").text.strip()
        print(f"Produto Encontrado: {titulo}")

        if precoFinal == 1499.99:
            print(f"O produto Esta: {valorLimpo} O Preço Esta Estavel")
        if precoFinal < 1499.99:
            print(f"O Preço Do Produto Abaixou! Agora Esta: {precoFinal}")

        if precoFinal > 1499.99:
            print(f"O Preço Do Produto Aumentou... Agora Esta: {precoFinal}")



        preco_alvo = 1500.00

        if precoFinal < preco_alvo:
            msg = f"ALERTA DE PREÇO!\n{titulo}\n Agora Esta: R$ {precoFinal}\nLink: {url}"
            enviar_alerta(msg)
            print("Alerta Enviado Para O Telegram")

        elif precoFinal > 1499.99: 
            msg = f"Aumentou! O Produto:\n{titulo}\n Aumentou para Valor de: R$ {precoFinal}\nLink: {url}"
            enviar_alerta(msg)
            print("Alerta Enviado Para O Telegram")
    contagem += 1
    