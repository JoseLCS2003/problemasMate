import tkinter as tk
from euler import VentanaEuler
from newton import VentanaNewton
from runge import VentanaRunge
class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menú Principal")

    def mostrar_opciones(self):
        # Título del menú
        label = tk.Label(self.root, text="Menú Principal", font=("Arial", 20))
        label.pack(pady=20)

        # Euler Mejorado
        btn_opcion1 = tk.Button(self.root, text="Euler Mejorado", width=20, command=self.abrir_euler_mejorado)
        btn_opcion1.pack(pady=10)

        # Runge Kulta
        btn_opcion2 = tk.Button(self.root,text="Runge Kulta", width=20,command=self.abrir_runge_kulta)
        btn_opcion2.pack(pady=10)

        # Runge Newton Raphson
        btn_opcion3 = tk.Button(self.root,text="Newton Raphson", width=20,command=self.abrir_newton_raphson)
        btn_opcion3.pack(pady=10)

    def abrir_euler_mejorado(self):      
        self.root.destroy()                  
        ventana1 = VentanaEuler()

    def abrir_runge_kulta(self):
        self.root.destroy()
        ventana2 =VentanaRunge()

    def abrir_newton_raphson(self):
        self.root.destroy()
        ventana3 =VentanaNewton()

    def run(self):
        self.mostrar_opciones()
        self.root.mainloop()
