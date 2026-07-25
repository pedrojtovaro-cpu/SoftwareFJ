# ==========================================================
# ARCHIVO: cliente.py
# PROYECTO: SOFTWARE FJ
# DESCRIPCIÓN:
# Clase Cliente.
# ==========================================================

from excepciones import ClienteInvalidoError
from logger import Logger


class Cliente:

    def __init__(self, nombre, documento, telefono, correo):

        self.__nombre = ""
        self.__documento = ""
        self.__telefono = ""
        self.__correo = ""

        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_telefono(telefono)
        self.set_correo(correo)

        Logger.registrar_evento(
            f"Cliente registrado: {self.__nombre}"
        )

    # --------------------------------------------------
    # GETTERS
    # --------------------------------------------------

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_telefono(self):
        return self.__telefono

    def get_correo(self):
        return self.__correo

    # --------------------------------------------------
    # SETTERS
    # --------------------------------------------------

    def set_nombre(self, nombre):

        if len(nombre.strip()) < 3:

            Logger.registrar_error(
                "Nombre de cliente inválido."
            )

            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        self.__nombre = nombre.strip().title()

    def set_documento(self, documento):

        if not documento.isdigit():

            Logger.registrar_error(
                "Documento inválido."
            )

            raise ClienteInvalidoError(
                "El documento solo puede contener números."
            )

        self.__documento = documento

    def set_telefono(self, telefono):

        if not telefono.isdigit():

            Logger.registrar_error(
                "Teléfono inválido."
            )

            raise ClienteInvalidoError(
                "El teléfono solo puede contener números."
            )

        self.__telefono = telefono

    def set_correo(self, correo):

        if "@" not in correo or "." not in correo:

            Logger.registrar_error(
                "Correo inválido."
            )

            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )

        self.__correo = correo

    # --------------------------------------------------
    # MOSTRAR INFORMACIÓN
    # --------------------------------------------------

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Correo: {self.__correo}"
        )

    def __str__(self):

        return (
            f"{self.__nombre} - {self.__documento}"
        )