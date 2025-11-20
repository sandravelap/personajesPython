import tkinter as tk

from clases.Guerrero import Guerrero
from clases.Personaje import Personaje

# --- 1. DEFINICIÓN DE CLASES (El "Molde") ---



personajePrueba = Personaje("canvas", "Pepe", 3, 4)
print(personajePrueba.realizar_accion())
guerreroPrueba = Guerrero("canvas", "Conan", 2, 4)
print(guerreroPrueba.realizar_accion())