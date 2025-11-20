from clases.Personaje import Personaje


class Guerrero(Personaje):
    """Hereda de Personaje. Es un tipo específico."""
    def __init__(self, canvas, nombre, x, y):
        # Llamamos al constructor del padre (super)
        super().__init__(canvas, nombre, x, y)
        self.color = "#e74c3c" # Rojo
        self.arma = "Espada"

    # POLIMORFISMO: Sobrescribimos el método realizar_accion
    def realizar_accion(self):
        return f"¡{self.nombre} ataca fuertemente con su {self.arma}!"