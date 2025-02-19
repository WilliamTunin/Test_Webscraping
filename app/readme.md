Web Scraping com Selenium, PostgreSQL e Docker

📌 Descrição do Projeto

Este projeto faz web scraping de notícias do site Globo.com, coletando títulos e links das matérias e armazenando em um banco de dados PostgreSQL. O projeto é totalmente containerizado com Docker, permitindo rodar tudo com um único comando.

📂 Estrutura do Projeto

📁 projeto-webscraping
│-- 📄 webscraping.py                # Script Python para scraping e armazenamento no PostgreSQL
│-- 📄 Dockerfile            # Configuração do container para rodar o Python
│-- 📄 requirements.txt      # Dependências do projeto
│-- 📄 docker-compose.yml    # Arquivo para subir os containers (Python + PostgreSQL)

🛠️ Como Rodar o Projeto

1️⃣ Instalar o Docker e o Docker Compose

Se ainda não tem o Docker instalado, siga as instruções para instalar:

Windows: Instalar Docker Desktop

Linux (Ubuntu):

sudo apt update
sudo apt install docker.io docker-compose -y

Verifique se a instalação foi bem-sucedida:

docker --version
docker-compose --version

2️⃣ Clonar o Repositório

Baixe o código para sua máquina:

git clone https://github.com/seu-usuario/projeto-webscraping.git
cd projeto-webscraping

3️⃣ Subir os Containers

Execute o comando abaixo para construir e rodar os containers do PostgreSQL e do Python:

docker-compose up --build

Isso irá:
✅ Baixar e configurar o PostgreSQL
✅ Instalar as dependências do Python
✅ Rodar o scraper automaticamente

🔍 Verificando os Dados no PostgreSQL

4️⃣ Acessar o Banco de Dados

Depois que o scraper rodar, você pode acessar o banco de dados para conferir os dados salvos:

docker exec -it postgres_container psql -U meuusuario -d meubanco

No terminal do PostgreSQL, execute:

SELECT * FROM noticias;

Isso mostrará as notícias coletadas com título, link e data da extração.

🚀 Parar os Containers

Para parar a execução dos containers, pressione CTRL + C e depois execute:

docker-compose down

🤔 Problemas Comuns e Soluções

1. O scraping não encontrou dados?

Verifique se o site da Globo.com mudou o layout.

Tente aumentar o tempo de espera no app.py: time.sleep(5).

2. PostgreSQL não está rodando?

Certifique-se de que o Docker está ativo: docker ps.

Se precisar reiniciar, use:

docker-compose down
docker-compose up --build

📜 Licença

Este projeto é de livre uso e modificação.