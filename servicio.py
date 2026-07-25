# ==========================================================
# ARCHIVO: servicio.py
# PROYECTO: SOFTWARE FJ
# DESCRIPCIÓN:
# Clase abstracta Servicio y sus clases derivadas.
# ==========================================================

from abc import ABC, abstractmethod

from excepciones import (
    ServicioNoDisponibleError,
    DuracionInvalidaError
)

from logger import Logger


# ==========================================================
# CLASE ABSTRACTA
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self._nombre = nombre
        self._costo_base = costo_base

    def get_nombre(self):
        return self._nombre

    def get_costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass


# ==========================================================
# RESERVA DE SALA
# ==========================================================

class ReservaSala(Servicio):

    def __init__(self):

        super().__init__(
            "Reserva de Sala",
            50000
        )

    def calcular_costo(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para Reserva de Sala."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        return self._costo_base * duracion


# ==========================================================
# ALQUILER DE EQUIPOS
# ==========================================================

class AlquilerEquipo(Servicio):

    def __init__(self):

        super().__init__(
            "Alquiler de Equipos",
            30000
        )

    def calcular_costo(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para Alquiler."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        return self._costo_base * duracion


# ==========================================================
# ASESORÍA ESPECIALIZADA
# ==========================================================

class AsesoriaEspecializada(Servicio):

    def __init__(self):

        super().__init__(
            "Asesoría Especializada",
            80000
        )

    def calcular_costo(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para Asesoría."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        return self._costo_base * duracion


# ==========================================================
# FÁBRICA DE SERVICIOS
# ==========================================================

def crear_servicio(tipo):

    tipo = tipo.lower()

    if tipo == "sala":
        return ReservaSala()

    elif tipo == "equipo":
        return AlquilerEquipo()

    elif tipo == "asesoria":
        return AsesoriaEspecializada()

    Logger.registrar_error(
        f"Servicio inexistente: {tipo}"
    )

    raise ServicioNoDisponibleError(
        "El servicio solicitado no existe."
    )