import subprocess

def levantar_api():
    comando = ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    subprocess.run(comando)
    