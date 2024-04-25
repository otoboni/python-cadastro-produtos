# Use a imagem oficial do Python como base
FROM python:3.9-slim AS base

# Define o ambiente como produção
ENV FLASK_ENV=production

# Configuração para evitar mensagens interativas durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY flask_app.conf /etc/nginx/conf.d/

# Define o diretório de trabalho
WORKDIR /app

# Copia o código da aplicação
COPY . /app

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 80 para o Nginx
EXPOSE 80

# Define o comando de inicialização
CMD ["sh", "-c", "nginx -g 'daemon off;' & gunicorn -b 0.0.0.0:5000 app:app"]
