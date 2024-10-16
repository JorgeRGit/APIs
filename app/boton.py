from datetime import datetime


class Boton:

    # Set de la clase para alamacenar cosas unicas
    _next_id = 1
    _nombres = set()

    def __init__(self, nombre: str, color: str):
        if nombre in Boton._nombres:
            raise ValueError("El nombre debe ser unico.")
        if not self._comprueba_color(color):
            raise ValueError("El color debe estar en formato hexadecimal.")
        
        self.__id = Boton._next_id
        Boton._next_id += 1
        self.__nombre = nombre
        self.__estado = False
        self.__color = color
        self.__fecha_creacion = datetime.now()

        # Para que no puedan repetirse
        Boton._nombres.add(nombre)

    """
    Valida que el color esté en formato hexadecimal tratando 
    el string como lista de caracteres

    Returns:
    _type_: booleano que indica si esta bien (True) o mal (False)
    """
    @staticmethod
    def _comprueba_color(color: str) -> bool:
        return (isinstance(color, str) and
                len(color) == 7 and color[0] == '#'
                and all(c in '0123456789abcdefABCDEF' for c in color[1:]))

    @property
    def id(self) -> int:
        return self.__id

    # nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo: str):
        if nuevo in Boton._nombres:
            raise ValueError("El nombre debe ser unico.")
        Boton._nombres.remove(self.__nombre)
        Boton._nombres.add(nuevo)
        self.__nombre = nuevo

    # estado
    @property
    def estado(self) -> bool:
        return self.__estado
    
    @estado.setter
    def estado(self, valor: bool):
        self.__estado = valor

    # color
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, nuevo: str):
        if not self._comprueba_color(nuevo):
            raise ValueError("El color debe estar en formato hexadecimal.")
        self.__color = nuevo

    @property
    def fecha_creacion(self) -> datetime:
        return self.__fecha_creacion
