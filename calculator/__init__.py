import tkinter as tk
from calculator.controls import Display

WIDTH = 272
HEIGHT = 300


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__() # Hereda 
        self.title("Calculadora")
        self.geometry(f'{WIDTH}x{HEIGHT}')
        
        display = Display(self)
        display.pack()
        display.typing("Probando")