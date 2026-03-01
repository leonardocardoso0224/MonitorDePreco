Meu Monitor de Preços
Criei este bot em Python para monitorar o preço de uma placa de vídeo que eu quero comprar. Assim, não preciso ficar abrindo o site toda hora; o bot faz o trabalho pesado e me avisa no Telegram.

O que ele faz:
Acessa o link do produto automaticamente. 

Procura o preço atual na página. 

Compara com o meu "preço alvo". 

Me manda uma mensagem no Telegram se o preço baixar ou mudar. 

O que usei:
Python: Linguagem principal.

BeautifulSoup: Para conseguir ler as informações do site.

Requests: Para conversar com o site e com o Telegram.

Time: Para o bot esperar um tempo antes de olhar o site de novo.

O que instalar
Abra o terminal e instale as bibliotecas necessárias: pip install requests beautifulsoup4

Como configurar
No arquivo buscador.py, você só precisa mudar essas duas linhas:

Token: Em token = "Seu Token Aqui", coloque o código que o @BotFather te deu.

Chat ID: Em chat_id = "Seu Chat ID Aqui", coloque o seu ID do Telegram. 🆔

Como funciona
O robô está programado para conferir o preço a cada 3 horas. ⏳

Para mudar o tempo, altere o número em time.sleep(10800) (o valor é em segundos).

Como rodar
Abra a pasta no VS Code e clique no Play ou digite no terminal: python buscador.py