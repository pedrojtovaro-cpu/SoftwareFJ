# ==========================================================
# ARCHIVO: sistema.py
# PROYECTO: SOFTWARE FJ
# ==========================================================

from logger import Logger


class SistemaReservas:

    def __init__(self):

        self.__clientes = []
        self.__reservas = []

    # -------------------------
    # CLIENTES
    # -------------------------

    def agregar_cliente(self, cliente):

        self.__clientes.append(cliente)

        Logger.registrar_evento(
            f"Cliente agregado: {cliente.get_nombre()}"
        )

    def obtener_clientes(self):

        return self.__clientes

    # -------------------------
    # RESERVAS
    # -------------------------

    def agregar_reserva(self, reserva):

        self.__reservas.append(reserva)

        Logger.registrar_evento(
            f"Reserva agregada para {reserva.get_cliente().get_nombre()}"
        )

    def obtener_reservas(self):

        return self.__reservas

    def eliminar_reserva(self, indice):

        if 0 <= indice < len(self.__reservas):

            reserva = self.__reservas[indice]

            Logger.registrar_evento(
                f"Reserva eliminada de {reserva.get_cliente().get_nombre()}"
            )

            self.__reservas.pop(indice)

    # -------------------------

    def mostrar_clientes(self):

        print("\n========== CLIENTES ==========")

        for cliente in self.__clientes:

            print(cliente)

    # -------------------------

    def mostrar_reservas(self):

        print("\n========== RESERVAS ==========")

        for reserva in self.__reservas:

            print(reserva)