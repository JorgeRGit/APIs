# Aquí irá todas las funciones relacionadas con la db que se usen en botones.py

import datetime


class Boton:
    # Variable de clase para llevar la cuenta de los IDs
    _id_counter = 0
    # Un conjunto para asegurar que los nombres sean únicos
    _nombre_unicos = set()

    def __init__(self, nombre, color):
        # Aumentar el contador para garantizar IDs únicos
        Boton._id_counter += 1
        self.id = Boton._id_counter

        # Verificar que el nombre sea único
        if nombre in Boton._nombre_unicos:
            raise ValueError(f"El nombre '{nombre}' ya está en uso.")
        self.nombre = nombre
        Boton._nombre_unicos.add(nombre)

        # Estado por defecto False
        self.estado = False

        # Verificar que el color sea un código hexadecimal válido
        if not self._es_color_hexadecimal_valido(color):
            raise ValueError(f"El color '{color}' no es un color hexadecimal válido.")
        self.color = color

        # Fecha de creación, generada automáticamente
        self.fecha_creacion = datetime.datetime.now()

    # Método estático para validar que el color sea un código hexadecimal
    @staticmethod
    def _es_color_hexadecimal_valido(color):
        if isinstance(color, str) and len(color) == 7 and color.startswith('#'):
            # Intentar convertir los últimos 6 caracteres a hexadecimal
            try:
                int(color[1:], 16)
                return True
            except ValueError:
                return False
        return False

    def __repr__(self):
        return (f"Boton(id={self.id}, nombre='{self.nombre}', estado={self.estado}, "
                f"color='{self.color}', fecha_creacion={self.fecha_creacion})")
