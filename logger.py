# ==========================================================
# ARCHIVO: logger.py
# PROYECTO: SOFTWARE FJ
# DESCRIPCIÓN:
# Registro de eventos y errores del sistema.
# ==========================================================

from datetime import datetime


class Logger:

    ARCHIVO_LOG = "logs.txt"

    @staticmethod
    def registrar_evento(mensaje):
        """
        Guarda un evento en el archivo de logs.
        """

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"[{fecha}] EVENTO: {mensaje}\n"
            )

    @staticmethod
    def registrar_error(error):
        """
        Guarda un error en el archivo de logs.
        """

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"[{fecha}] ERROR: {error}\n"
            )