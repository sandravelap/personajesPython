import tkinter as tk
import random
from tkinter import messagebox

# --- 1. DEFINICIÓN DE CLASES (El "Molde") ---

class Personaje:
    """Clase Padre (Superclase). Define lo básico que todo personaje tiene."""
    def __init__(self, canvas, nombre, x, y):
        self.canvas = canvas
        self.nombre = nombre
        # Atributos encapsulados (datos del objeto)
        self.x = x
        self.y = y
        self.color = "gray" # Color por defecto
        self.id_dibujo = None # Referencia al dibujo en el canvas

    def dibujar(self):
        """Método para visualizar el objeto en la pantalla."""
        radio = 20
        x1, y1 = self.x - radio, self.y - radio
        x2, y2 = self.x + radio, self.y + radio
        
        # Dibuja el círculo
        self.id_dibujo = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="black")
        # Dibuja el nombre encima
        self.canvas.create_text(self.x, self.y - 30, text=self.nombre, font=("Arial", 10, "bold"))

    def realizar_accion(self):
        """Método genérico que será sobrescrito (Polimorfismo)."""
        return f"{self.nombre} está esperando..."

# --- 2. HERENCIA (Clases Hijas) ---

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

class Mago(Personaje):
    """Hereda de Personaje. Es otro tipo específico."""
    def __init__(self, canvas, nombre, x, y):
        super().__init__(canvas, nombre, x, y)
        self.color = "#3498db" # Azul
        self.mana = 100

    # POLIMORFISMO: Misma función, comportamiento diferente
    def realizar_accion(self):
        return f"¡{self.nombre} lanza una bola de fuego! (Maná: {self.mana})"

# --- 3. INTERFAZ GRÁFICA (La "Fábrica") ---

class AppPOO:
    def __init__(self, root):
        self.root = root
        self.root.title("Demo Visual de POO - Fábrica de Héroes")
        self.root.geometry("600x500")

        # Lista para guardar nuestros OBJETOS en memoria
        self.lista_objetos = []

        # --- Panel de Control ---
        frame_control = tk.Frame(root, pady=10, bg="#ecf0f1")
        frame_control.pack(fill=tk.X)

        tk.Label(frame_control, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        self.entry_nombre = tk.Entry(frame_control)
        self.entry_nombre.pack(side=tk.LEFT, padx=5)

        # Botones para INSTANCIAR (Crear objetos)
        tk.Button(frame_control, text="Crear Guerrero", bg="#e74c3c", fg="white", 
                  command=self.crear_guerrero).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_control, text="Crear Mago", bg="#3498db", fg="white", 
                  command=self.crear_mago).pack(side=tk.LEFT, padx=5)

        tk.Button(frame_control, text="¡TODOS ACTUAR!", bg="#2c3e50", fg="white", 
                  command=self.todos_actuan).pack(side=tk.RIGHT, padx=10)

        # --- Área Visual (Canvas) este es el lienzo donde vamos a dibujar los personajes
        # es el parámetro que pasamos al constructor del objeto (__init__)---
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Log de Acciones ---
        self.log_label = tk.Label(root, text="Registro de acciones aparecerá aquí...", 
                                  font=("Consolas", 10), fg="green", height=2)
        self.log_label.pack(fill=tk.X, pady=5)

    def obtener_posicion_random(self):
        """Genera coordenadas aleatorias dentro del canvas."""
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        return x, y

    def crear_guerrero(self):
        nombre = self.entry_nombre.get() or "Guerrero Anónimo"
        x, y = self.obtener_posicion_random()
        
        # INSTANCIACIÓN: Aquí nace el objeto
        nuevo_guerrero = Guerrero(self.canvas, nombre, x, y)
        nuevo_guerrero.dibujar()
        
        self.lista_objetos.append(nuevo_guerrero)
        self.log_label.config(text=f"Se ha instanciado un objeto Clase Guerrero: {nombre}")

    def crear_mago(self):
        nombre = self.entry_nombre.get() or "Mago Anónimo"
        x, y = self.obtener_posicion_random()
        
        # INSTANCIACIÓN: Aquí nace el objeto
        nuevo_mago = Mago(self.canvas, nombre, x, y)
        nuevo_mago.dibujar()
        
        self.lista_objetos.append(nuevo_mago)
        self.log_label.config(text=f"Se ha instanciado un objeto Clase Mago: {nombre}")

    def todos_actuan(self):
        """Demostración de Polimorfismo: Iteramos la lista y todos responden distinto."""
        if not self.lista_objetos:
            messagebox.showinfo("Info", "¡Primero crea algunos personajes!")
            return

        logs = []
        for personaje in self.lista_objetos:
            # Llamamos al MISMO método, pero cada uno hace algo distinto
            logs.append(personaje.realizar_accion())
        
        mensaje_final = " | ".join(logs)
        self.log_label.config(text=mensaje_final)

# --- Ejecución ---
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppPOO(ventana)
    ventana.mainloop()