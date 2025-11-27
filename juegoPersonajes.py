import tkinter as tk
import random

from clases.Guerrero import Guerrero
from clases.Personaje import Personaje

# --- 1. DEFINICIÓN DE CLASES (El "Molde") ---



personajePrueba = Personaje("canvas", "Pepe", 3, 4)
print(personajePrueba.realizar_accion())
guerreroPrueba = Guerrero("canvas", "Conan", 2, 4)
print(guerreroPrueba.realizar_accion())

ventana = tk.Tk()
ventana.title("Demo Visual de POO - Fábrica de Héroes")
ventana.geometry("600x500")

# --- Panel de Control ---
frameControl = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frameControl.pack(fill=tk.X)

tk.Label(frameControl, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
inputNombre = tk.Entry(frameControl)
inputNombre.pack(side=tk.LEFT, padx=5)

#escenario canvas donde se van a dibujar los personajes
escenario_canvas = tk.Canvas(ventana, width=800, height=500, bg="#2c3e50")
#lo colocamos debajo del frameControl en la ventana
escenario_canvas.pack(fill=tk.BOTH, expand=True) # expand=True permite que crezca si la ventana cambia de tamaño

# Funciones para crear los personajes en el escenario
def obtener_posicion_random():
        """Genera coordenadas aleatorias dentro del canvas."""
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        return x, y

def crear_guerrero():
    nombre = inputNombre.get() or "Guerrero Anónimo"
    x, y = obtener_posicion_random()
    
    # INSTANCIACIÓN: Aquí nace el objeto
    nuevo_guerrero = Guerrero(escenario_canvas, nombre, x, y)
    nuevo_guerrero.dibujar()

def crear_mago():
    nombre = inputNombre.get() or "Mago Anónimo"
    x, y = obtener_posicion_random()

# Botones para INSTANCIAR (Crear objetos)
tk.Button(frameControl, text="Crear Guerrero", bg="#e74c3c", fg="white", 
            command=crear_guerrero).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="Crear Mago", bg="#3498db", fg="white", 
            command=crear_mago).pack(side=tk.LEFT, padx=5)

#tk.Button(frameControl, text="¡TODOS ACTUAR!", bg="#2c3e50", fg="white", 
#            command=todos_actuan).pack(side=tk.RIGHT, padx=10)

ventana.mainloop()