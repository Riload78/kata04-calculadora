import tkinter as tk
# Creamos la ventana
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__() # Herencia de la clase TK. Se trae todas los metodos
        self.title("Hola Mundo")
        self.geometry("800x600+400+200")
        self.resizable(True, True)
        self.label = tk.Label(self, text="Hola Mundo", bd=2, relief=tk.RAISED)
        self.label.pack()
        self.valor_nombre = tk.StringVar()
        nombre = tk.Entry(self, textvariable=self.valor_nombre)
        nombre.pack()
        boton = tk.Button(self, text="Pulsame", command=self.imprimir_saludo)
        boton.pack()
        
        
    def imprimir_saludo(self):
        self.label.config(text=f"Hola, {self.valor_nombre.get()}")
        
        
        

# Instanciamos la clase venta 
"""interface = Ventana()
interface.mainloop()
Se puede hacer directamente asi: """

Ventana().mainloop()