FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .streamlit/config.toml .streamlit/config.toml
COPY .env .env
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8501

CMD [ "streamlit","run", "./app.py" ]