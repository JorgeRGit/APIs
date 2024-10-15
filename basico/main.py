# Aqui se iniciará la api

from fastapi import FastAPI, HTTPException, status
from boton import Boton
from pydantic import BaseModel, Field

# app
app = FastAPI()

# Guardar botones hasta que se reinicie
lista_variable_botones = []


@app.get("/")
def root():  # No voy a usar async en principio
    return {"message": "Hello World"}


@app.get("/botones/{nombre}")
def getBoton(nombre: str, status_code=200):

    for boton in lista_variable_botones:
        if boton.nombre == nombre:
            return boton

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/botones")
def crearBoton(nombre: str, color: str, status_code=status.HTTP_201_CREATED):

    try:
        nuevoBoton = Boton(nombre, color)

    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Problema al crear Boton, Nombre ya usado o codigo de color incorrecto")

    lista_variable_botones.append(nuevoBoton)
    return nuevoBoton


@app.delete("/botones/{nombre}")
def deleteBoton(nombre: str, status_code=status.HTTP_200_OK):

    for index, boton in enumerate(lista_variable_botones):
        if boton.nombre == nombre:
            lista_variable_botones.pop(index)
            return boton

    raise HTTPException(status_code=404, detail="Item not found")


class BotonUpdate(BaseModel):
    nombreNuevo: str = Field(None, description="Nuevo nombre del Boton")
    color: str = Field(None, description="Nuevo color del Boton (formato hexadecimal)")
    estado: bool = Field(None, description="Nuevo estado del Boton")


@app.put("/botones/{nombre}")
def updateBoton(nombre: str, boton_update: BotonUpdate, status_code=status.HTTP_200_OK):

    for boton in lista_variable_botones:
        if boton.nombre == nombre:

            try:

                if boton_update.nombreNuevo is not None and boton_update.nombreNuevo != "":
                    boton.nombre = boton_update.nombreNuevo

                if boton_update.color is not None and boton_update.color != "":
                    boton.color = boton_update.color

            except:
                raise HTTPException(status_code=500, detail="Nombre o color no validos.")

            if boton_update.estado is not None:
                boton.estado = boton_update.estado

            return boton

    raise HTTPException(status_code=404, detail="Botón no encontrado.")
