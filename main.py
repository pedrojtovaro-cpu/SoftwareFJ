# ==========================================================
# ARCHIVO: main.py
# PROYECTO: SOFTWARE FJ
# ==========================================================

from cliente import Cliente
from servicio import crear_servicio
from reserva import Reserva
from sistema import SistemaReservas

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError,
    DuracionInvalidaError,
    CostoInvalidoError
)

from logger import Logger


class Aplicacion:

    def __init__(self):

        self.sistema = SistemaReservas()

    # -----------------------------------------------------
    # REGISTRAR CLIENTE
    # -----------------------------------------------------

    def registrar_cliente(
        self,
        nombre,
        documento,
        telefono,
        correo
    ):

        try:

            cliente = Cliente(
                nombre,
                documento,
                telefono,
                correo
            )

        except ClienteInvalidoError as error:

            Logger.registrar_error(error)

            print("\nERROR:", error)

            return None

        else:

            self.sistema.agregar_cliente(cliente)

            print("\nCliente registrado correctamente.")

            return cliente

        finally:

            Logger.registrar_evento(
                "Proceso de registro de cliente finalizado."
            )

    # -----------------------------------------------------
    # CREAR SERVICIO
    # -----------------------------------------------------

    def crear_servicio(
        self,
        tipo
    ):

        try:

            servicio = crear_servicio(tipo)

        except ServicioNoDisponibleError as error:

            Logger.registrar_error(error)

            print("\nERROR:", error)

            return None

        else:

            print(
                f"\nServicio seleccionado: {servicio.get_nombre()}"
            )

            return servicio

        finally:

            Logger.registrar_evento(
                "Proceso de creación del servicio finalizado."
            )

    # -----------------------------------------------------
    # CREAR RESERVA
    # -----------------------------------------------------

    def crear_reserva(
        self,
        cliente,
        servicio,
        duracion
    ):

        try:

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

        except (
            ReservaError,
            DuracionInvalidaError,
            CostoInvalidoError
        ) as error:

            Logger.registrar_error(error)

            print("\nERROR:", error)

            return None

        else:

            self.sistema.agregar_reserva(
                reserva
            )

            print("\nReserva creada correctamente.")

            return reserva

        finally:

            Logger.registrar_evento(
                "Proceso de creación de reserva finalizado."
            )    
    # -----------------------------------------------------
    # CONFIRMAR RESERVA
    # -----------------------------------------------------

    def confirmar_reserva(self, reserva):

        try:

            reserva.confirmar()

        except Exception as error:

            Logger.registrar_error(error)

            print("\nERROR:", error)

        else:

            print("\nReserva confirmada correctamente.")

        finally:

            Logger.registrar_evento(
                "Proceso de confirmación finalizado."
            )

    # -----------------------------------------------------
    # CANCELAR RESERVA
    # -----------------------------------------------------

    def cancelar_reserva(self, reserva):

        try:

            reserva.cancelar()

        except Exception as error:

            Logger.registrar_error(error)

            print("\nERROR:", error)

        else:

            print("\nReserva cancelada correctamente.")

        finally:

            Logger.registrar_evento(
                "Proceso de cancelación finalizado."
            )

    # -----------------------------------------------------
    # MOSTRAR CLIENTES
    # -----------------------------------------------------

    def mostrar_clientes(self):

        print("\n==============================")
        print("LISTA DE CLIENTES")
        print("==============================")

        clientes = self.sistema.obtener_clientes()

        if len(clientes) == 0:

            print("No hay clientes registrados.")

            return

        for cliente in clientes:

            print(cliente.mostrar_informacion())
            print("------------------------------")

    # -----------------------------------------------------
    # MOSTRAR RESERVAS
    # -----------------------------------------------------

    def mostrar_reservas(self):

        print("\n==============================")
        print("LISTA DE RESERVAS")
        print("==============================")

        reservas = self.sistema.obtener_reservas()

        if len(reservas) == 0:

            print("No existen reservas.")

            return

        for reserva in reservas:

            print(reserva.mostrar_reserva())
            print("------------------------------")

    # -----------------------------------------------------
    # MOSTRAR TOTAL RECAUDADO
    # -----------------------------------------------------

    def mostrar_total(self):

        total = 0

        for reserva in self.sistema.obtener_reservas():

            try:

                total += reserva.calcular_total()

            except Exception as error:

                Logger.registrar_error(error)

        print("\n==============================")
        print("TOTAL RECAUDADO")
        print("==============================")
        print(f"${total:,.0f}")

    # -----------------------------------------------------
    # BUSCAR CLIENTE
    # -----------------------------------------------------

    def buscar_cliente(self, documento):

        for cliente in self.sistema.obtener_clientes():

            if cliente.get_documento() == documento:

                return cliente

        return None

    # -----------------------------------------------------
    # BUSCAR RESERVA
    # -----------------------------------------------------

    def buscar_reserva(self, documento):

        for reserva in self.sistema.obtener_reservas():

            if reserva.get_cliente().get_documento() == documento:

                return reserva

        return None
    # ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

if __name__ == "__main__":

    app = Aplicacion()

    print("=" * 60)
    print("SOFTWARE FJ")
    print("SISTEMA DE RESERVAS")
    print("=" * 60)

    # -----------------------------------------------------
    # CLIENTES
    # -----------------------------------------------------

    cliente1 = app.registrar_cliente(
        "Pedro Tovar",
        "12345678",
        "3001234567",
        "pedro@gmail.com"
    )

    cliente2 = app.registrar_cliente(
        "Maria Perez",
        "87654321",
        "3019876543",
        "maria@gmail.com"
    )

    # -----------------------------------------------------
    # SERVICIOS
    # -----------------------------------------------------

    servicio1 = app.crear_servicio("sala")
    servicio2 = app.crear_servicio("equipo")
    servicio3 = app.crear_servicio("asesoria")

    # -----------------------------------------------------
    # RESERVAS
    # -----------------------------------------------------

    if cliente1 and servicio1:

        reserva1 = app.crear_reserva(
            cliente1,
            servicio1,
            2
        )

    if cliente2 and servicio2:

        reserva2 = app.crear_reserva(
            cliente2,
            servicio2,
            3
        )

    # -----------------------------------------------------
    # CONFIRMAR
    # -----------------------------------------------------

    if cliente1:

        reserva = app.buscar_reserva(
            cliente1.get_documento()
        )

        if reserva:

            app.confirmar_reserva(
                reserva
            )

    # -----------------------------------------------------
    # CANCELAR
    # -----------------------------------------------------

    if cliente2:

        reserva = app.buscar_reserva(
            cliente2.get_documento()
        )

        if reserva:

            app.cancelar_reserva(
                reserva
            )

    # -----------------------------------------------------
    # MOSTRAR INFORMACIÓN
    # -----------------------------------------------------

    app.mostrar_clientes()

    app.mostrar_reservas()

    app.mostrar_total()

    # -----------------------------------------------------
    # PRUEBAS DE EXCEPCIONES
    # -----------------------------------------------------

    print("\n========== PRUEBAS ==========\n")

    app.registrar_cliente(
        "",
        "ABC",
        "telefono",
        "correo"
    )

    app.crear_servicio(
        "fotocopia"
    )

    if cliente1 and servicio3:

        app.crear_reserva(
            cliente1,
            servicio3,
            -5
        )

    print("\nFin del programa.")