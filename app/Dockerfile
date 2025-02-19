# Usar uma imagem oficial do Python
FROM python:3.9

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos para o container
COPY requirements.txt requirements.txt
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Executar o script ao iniciar o container
CMD ["python", "webscraping.py"]

