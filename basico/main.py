# Aqui se iniciará la api

from fastapi import FastAPI, HTTPException, status
from levantar import levantar_local
from boton import Boton

# app
app = FastAPI()

# Guardar botones hasta que se reinicie
lista_variable_botones = []

#levantar_local()

@app.get("/")
def root():  # No voy a usar async en principio
    return {"message": "Hello World"}

@app.get("/botones/{nombre}")
def getBoton(nombre: str, staus_code=200):

    for boton in lista_variable_botones:
        if boton.nombre == nombre:
            return boton

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/botones")
def crearBoton(nombre: str, color: str, status_code=status.HTTP_201_CREATED):

    try:
        nuevoBoton = Boton(nombre, color)

    except:
        print(nombre)
        print(color)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Problema al crear Boton, Nombre ya usado o codigo de color incorrecto")

    lista_variable_botones.append(nuevoBoton)


@app.delete("/botones/{nombre}")
def deleteBoton(nombre: str, staus_code=status.HTTP_200_OK):

    for index, boton in enumerate(lista_variable_botones):
        if boton.nombre == nombre:
            lista_variable_botones.pop(index)
            return boton

    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/botones/{nombre}")
def updateBoton(nombre: str, nombreNuevo, staus_code=status.HTTP_200_OK):

    # Falta de comprobar que no se cambie el nombre a uno que no exista.
    # Tengo que educarme sobre como funciona Python con variables privadas
    for index, boton in enumerate(lista_variable_botones):
        if boton.nombre == nombre:
            
            boton.nombre = nombreNuevo
            return boton


    raise HTTPException(status_code=404, detail="Item not found")
