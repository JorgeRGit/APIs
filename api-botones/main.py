# Aqui se iniciará la api

from fastapi import FastAPI

app = FastAPI()

lista_variable_botones = []


@app.get("/")
def root():  # No voy a usar async en principio
    return {"message": "Hello World"}
