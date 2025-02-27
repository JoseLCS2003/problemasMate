import tkinter as tk
from tkinter import ttk, messagebox
from metodosMate import MetodosMate

class VentanaNewton :
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Newton Raphson")
        self.root.geometry("650x450")  # Ajustamos el tamaño inicial
        self.root.resizable(False, False)

        # ============ MARCO DE ENTRADA ============
        self.frame_entrada = tk.LabelFrame(self.root, text="Parámetros de Entrada", padx=10, pady=10)
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        labels = ["x1:","Precisión (decimales):","fx:"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=3)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=15)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entries[label] = entry

                # Frame para los botones
        self.frame_botones = tk.Frame(self.frame_entrada)
        self.frame_botones.grid(row=len(labels), column=0, columnspan=5, pady=10)

        # Botón Calcular (Verde)
        self.boton_calcular = tk.Button(self.frame_botones, text="Calcular", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.calcular)
        self.boton_calcular.grid(row=0, column=0, padx=5)

        # Botón Limpiar (Rojo)
        self.boton_limpiar = tk.Button(self.frame_botones, text="Limpiar", font=("Arial", 10, "bold"), bg="#FF0000", fg="white", command=self.limpiar_entradas)
        self.boton_limpiar.grid(row=0, column=1, padx=5)

        # Botón Volver al Menú Principal (Rojo)
        self.boton_volver = tk.Button(self.frame_botones, text="Volver al Menú Principal", font=("Arial", 10, "bold"), bg="#FF0000", fg="white", command=self.volver_menu_principal)
        self.boton_volver.grid(row=0, column=2, padx=5)


        # Capturar evento de cierre de la ventana (cuando el usuario hace clic en "X")
        self.root.protocol("WM_DELETE_WINDOW", self.volver_menu_principal)

        # ============ MARCO DE RESULTADOS ============
        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10)
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        # Tabla con Scrollbar
        self.tabla_frame = tk.Frame(self.frame_resultados)
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Xn+1"), show="headings", height=8)

        # Encabezados con mejor alineación y tamaño
        for col in self.tabla_resultados["columns"]:
            self.tabla_resultados.heading(col, text=col)
            self.tabla_resultados.column(col, anchor="w", width=85)

        self.tabla_resultados.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scroll_y = ttk.Scrollbar(self.tabla_frame, orient="vertical", command=self.tabla_resultados.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.tabla_resultados.configure(yscrollcommand=self.scroll_y.set)

        self.root.mainloop()  # Ejecutar la ventana aquí

    def calcular(self):
        try:
            x1=float(self.entries["x1:"].get())             
            Precision= int(self.entries["Precisión (decimales):"].get())
            fx = self.entries["fx:"].get()

            resultados = MetodosMate.newthon_raphson(x1,fx,Precision)

            for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)

            for resultado in resultados:
                self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Xn+1"]))
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def limpiar_entradas(self):
        # Limpiar todos los campos de entrada
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)

        for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)
        
        self.entries["x1:"].focus()
    
    def volver_menu_principal(self):        
        self.root.withdraw()
        self.root.quit()  
        import menu  
        menu_app = menu.Menu()  
        menu_app.run()  