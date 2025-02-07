import tkinter as tk

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")

        # Botón para ocultar la ventana principal
        self.boton_ocultar = tk.Button(self.root, text="Ocultar ventana principal", command=self.ocultar_ventana)
        self.boton_ocultar.pack(pady=10)

        # Botón para abrir la segunda ventana
        self.boton_abrir_segunda = tk.Button(self.root, text="Abrir segunda ventana", command=self.abrir_segunda_ventana)
        self.boton_abrir_segunda.pack(pady=10)

    def ocultar_ventana(self):
        # Ocultar la ventana principal
        self.root.withdraw()

    def abrir_segunda_ventana(self):
        # Crear nueva ventana
        self.ventana_secundaria = tk.Toplevel(self.root)
        self.ventana_secundaria.title("Segunda ventana")
        
        # Botón para mostrar nuevamente la ventana principal
        boton_mostrar_principal = tk.Button(self.ventana_secundaria, text="Mostrar ventana principal", command=self.mostrar_ventana_principal)
        boton_mostrar_principal.pack(pady=10)

    def mostrar_ventana_principal(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()

# Crear la ventana principal
root = tk.Tk()
app = MiAplicacion(root)
root.mainloop()
