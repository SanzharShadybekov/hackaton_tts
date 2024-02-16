FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 1

# Установка зависимостей и Google Chrome
RUN apt-get update && apt-get install -y wget gnupg2 apt-transport-https ca-certificates \
    && apt-get update \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && apt-get install -y tesseract-ocr libtesseract-dev tesseract-ocr-rus tesseract-ocr-eng unzip xvfb libxi6 libgconf-2-4 libnss3 curl \
    && rm -rf /var/lib/apt/lists/*

# Загрузка и установка ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
