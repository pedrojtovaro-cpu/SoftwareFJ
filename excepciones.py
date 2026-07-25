# ==========================================================
# ARCHIVO: excepciones.py
# PROYECTO: SOFTWARE FJ
# DESCRIPCIÓN:
# Excepciones personalizadas del sistema.
# ==========================================================


class ErrorSistema(Exception):
    """Clase base para las excepciones del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Se genera cuando los datos del cliente no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando el servicio solicitado no existe."""
    pass


class ReservaError(ErrorSistema):
    """Se genera cuando ocurre un problema con la reserva."""
    pass


class DuracionInvalidaError(ErrorSistema):
    """Se genera cuando la duración ingresada es incorrecta."""
    pass


class CostoInvalidoError(ErrorSistema):
    """Se genera cuando el costo calculado es inválido."""
    pass