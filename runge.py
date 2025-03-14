import tkinter as tk
from tkinter import ttk, messagebox
from metodosMate import MetodosMate

class VentanaRunge:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método de Runge Kulta de 4to orden")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
    
        self.frame_entrada = tk.LabelFrame(self.root, text="Parámetros de Entrada", padx=10, pady=10)
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        labels = ["x0:", "y0:", "h:", "xf:", "f(x, y):"]
        self.entries = {}
        
        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=3)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=15)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entries[label] = entry

        self.add_placeholder(self.entries["f(x, y):"], "Ej: 2*x*y o 2*x**2*y")
        tk.Label(self.frame_entrada, text="Instrucciones: Use '*' para multiplicación y '**' para exponentes.", font=("Arial", 8), fg="gray").grid(row=4, column=2, sticky="w", pady=5)
        
        self.frame_botones = tk.Frame(self.frame_entrada)
        self.frame_botones.grid(row=len(labels), column=0, columnspan=5, pady=10)
        
        self.boton_calcular = tk.Button(self.frame_botones, text="Calcular", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.calcular)
        self.boton_calcular.grid(row=0, column=0, padx=5)

        self.boton_limpiar = tk.Button(self.frame_botones, text="Limpiar", font=("Arial", 10, "bold"), bg="#FF0000", fg="white", command=self.limpiar_entradas)
        self.boton_limpiar.grid(row=0, column=1, padx=5)
        
        self.boton_volver = tk.Button(self.frame_botones, text="Volver al Menú Principal", font=("Arial", 10, "bold"), bg="#FF0000", fg="white", command=self.volver_menu_principal)
        self.boton_volver.grid(row=0, column=2, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.volver_menu_principal)

        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10)
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        self.tabla_frame = tk.Frame(self.frame_resultados)
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Yn", "K1", "K2","K3","K4", "Yn+1"), show="headings", height=8)

        for col in self.tabla_resultados["columns"]:
            self.tabla_resultados.heading(col, text=col)
            self.tabla_resultados.column(col, anchor="w", width=85)

        self.tabla_resultados.pack(side="left", fill="both", expand=True)

        self.scroll_y = ttk.Scrollbar(self.tabla_frame, orient="vertical", command=self.tabla_resultados.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.tabla_resultados.configure(yscrollcommand=self.scroll_y.set)

        self.root.mainloop()    

    def add_placeholder(self, entry, placeholder):
        # Establecer el texto inicial del placeholder
        entry.insert(0, placeholder)
        entry.config(fg="gray")

        # Evento para borrar el placeholder cuando el usuario hace clic en el campo
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        # Evento para restaurar el placeholder si el campo está vacío
        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg="gray")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        

    def calcular(self):
        x0=float(self.entries["x0:"].get())
        y0=float(self.entries["y0:"].get())
        h=float(self.entries["h:"].get())
        xf=float(self.entries["xf:"].get())
        fxy=self.entries["f(x, y):"].get()

        resultados = MetodosMate.runge_kutta(x0,y0,h,xf,fxy)

        for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)
        
        for resultado in resultados:
                self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Yn"], resultado["K1"], resultado["K2"],resultado["K3"],resultado["K4"], resultado["Yn+1"]))
    
    def limpiar_entradas(self):
        # Limpiar todos los campos de entrada
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)

        for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)
        
        self.entries["x0:"].focus()
    
    def volver_menu_principal(self):        
        self.root.withdraw()
        self.root.quit()  
        import menu  
        menu_app = menu.Menu()  
        menu_app.run() 