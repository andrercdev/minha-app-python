# Usar uma imagem base oficial do Python
FROM python:3.13-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Definir a variável de ambiente para a porta
ENV PORT=5000

# Comando para executar a aplicação
CMD ["python", "app.py"]