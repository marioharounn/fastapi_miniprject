# Bruk en Python-basisbilde
FROM python:3.10-slim

# Sett arbeidskatalog
WORKDIR /app

# Kopier nødvendige filer
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

# Installer avhengigheter
RUN pip install --no-cache-dir -r requirements.txt

# Eksponer porten
EXPOSE 8000

# Start API-et
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]