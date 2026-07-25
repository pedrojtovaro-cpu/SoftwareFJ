# ==========================================================
# ARCHIVO: reserva.py
# PROYECTO: SOFTWARE FJ
# DESCRIPCIÓN:
# Clase Reserva.
# ==========================================================

from excepciones import (
    ReservaError,
    CostoInvalidoError
)

from logger import Logger


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida al crear una reserva."
            )

            raise ReservaError(
                "La duración debe ser mayor que cero."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        Logger.registrar_evento(
            f"Reserva creada para {cliente.get_nombre()}."
        )

    # --------------------------------------------------
    # GETTERS
    # --------------------------------------------------

    def get_cliente(self):
        return self.__cliente

    def get_servicio(self):
        return self.__servicio

    def get_duracion(self):
        return self.__duracion

    def get_estado(self):
        return self.__estado

    # --------------------------------------------------
    # OPERACIONES
    # --------------------------------------------------

    def confirmar(self):

        self.__estado = "Confirmada"

        Logger.registrar_evento(
            "Reserva confirmada."
        )

    def cancelar(self):

        self.__estado = "Cancelada"

        Logger.registrar_evento(
            "Reserva cancelada."
        )

    def calcular_total(self):

        try:

            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            if costo < 0:

                raise ValueError(
                    "El costo no puede ser negativo."
                )

        except Exception as e:

            Logger.registrar_error(
                f"Error al calcular el costo: {e}"
            )

            raise CostoInvalidoError(
                "No fue posible calcular el costo de la reserva."
            ) from e

        else:

            return costo

        finally:

            Logger.registrar_evento(
                "Proceso de cálculo del costo finalizado."
            )

    # --------------------------------------------------
    # MOSTRAR INFORMACIÓN
    # --------------------------------------------------

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.__cliente.get_nombre()}\n"
            f"Servicio: {self.__servicio.get_nombre()}\n"
            f"Duración: {self.__duracion} hora(s)\n"
            f"Estado: {self.__estado}\n"
            f"Total: ${self.calcular_total():,.0f}"
        )

    def __str__(self):

        return (
            f"{self.__cliente.get_nombre()} - "
            f"{self.__servicio.get_nombre()} - "
            f"{self.__estado}"
        )