import tkinter as tk
from tkinter import ttk, messagebox
from metodosMate import MetodosMate

class VentanaEuler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Euler Mejorado")
        self.root.geometry("750x450")  # Ajustamos el tamaño inicial
        self.root.resizable(False, False)

        # ============ MARCO DE ENTRADA ============
        self.frame_entrada = tk.LabelFrame(self.root, text="Parámetros de Entrada", padx=10, pady=10)
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        labels = ["x0:", "y0:", "h:", "xf:", "f(x, y):"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=3)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=15)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entries[label] = entry

        # Botón para calcular
        self.boton_calcular = tk.Button(self.frame_entrada, text="Calcular", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.calcular)
        self.boton_calcular.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # ============ MARCO DE RESULTADOS ============
        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10)
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        # Tabla con Scrollbar
        self.tabla_frame = tk.Frame(self.frame_resultados)
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Yn", "(Yn+1)*", "Xn+1", "Yn+1"), show="headings", height=8)

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
            # Obtener y validar los valores
            x0 = float(self.entries["x0:"].get())
            y0 = float(self.entries["y0:"].get())
            h = float(self.entries["h:"].get())
            xf = float(self.entries["xf:"].get())
            fxy = self.entries["f(x, y):"].get()

            if h <= 0:
                messagebox.showerror("Error", "El paso h debe ser mayor que 0.")
                return

            if x0 >= xf:
                messagebox.showerror("Error", "x0 debe ser menor que xf.")
                return

            # Calcular los resultados usando Euler Mejorado
            resultados = MetodosMate.euler_mejorado(x0, y0, h, xf, fxy)

            # Limpiar la tabla
            for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)

            # Insertar datos en la tabla
            for resultado in resultados:
                self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Yn"], resultado["(Yn+1)*"], resultado["Xn+1"], resultado["Yn+1"]))

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")