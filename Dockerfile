# Usa la imagen oficial de FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los requisitos y el código fuente a la imagen
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

# Exponer el puerto en el que correrá la API
EXPOSE 80

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

