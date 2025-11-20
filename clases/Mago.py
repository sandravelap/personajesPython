from clases.Personaje import Personaje


class Mago(Personaje):
    """Hereda de Personaje. Es otro tipo específico."""
    def __init__(self, canvas, nombre, x, y):
        super().__init__(canvas, nombre, x, y)
        self.color = "#3498db" # Azul
        self.mana = 100

    # POLIMORFISMO: Misma función, comportamiento diferente
    def realizar_accion(self):
        return f"¡{self.nombre} lanza una bola de fuego! (Maná: {self.mana})"
