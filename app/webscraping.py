import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime


# webdriver config
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)

# Acessar o site da Globo
url = "https://www.globo.com/"
driver.get(url)

# Esperar um tempo para carregar os elementos
time.sleep(5)

# Encontrar os Titulo e Links das notícias
noticias = driver.find_elements(By.CSS_SELECTOR, "a.feed-post-link")

# Criando uma lista para armazenar os dados
dados = []
for noticia in noticias:
    titulo = noticia.text.strip()
    link = noticia.get_attribute("href").strip()
    if titulo and link:
        dados.append((titulo, link, datetime.now()))

# Fechar o navegador
driver.quit()

# Conectar ao banco PostgreSQL
conn = psycopg2.connect(
    dbname="meubanco",
    user="meuusuario",
    password="minhasenha",
    host="db",
    port="5432"
)
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS noticias (
        id SERIAL PRIMARY KEY,
        titulo TEXT NOT NULL,
        link TEXT NOT NULL,
        data_extracao TIMESTAMP DEFAULT NOW()
    )
""")

# Inserir os dados no banco
cursor.executemany("INSERT INTO noticias (titulo, link, data_extracao) VALUES (%s, %s, %s)", dados)

# Salvando e Fechando conexão
conn.commit()
cursor.close()
conn.close()

print("Dados coletados e banco de dados atualizado!")