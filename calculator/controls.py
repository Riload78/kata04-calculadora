import tkinter as tk
from tkinter.font import Font

class Display(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=272, height = 50)
        self.pack_propagate(False)
        self.font = Font(family='Arial',size=30, weight='bold')
        self.label = tk.Label(self, background="#000",text='Prueba',foreground='#FFFFFF',
                              anchor=tk.E, padx=8, font=self.font)
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand= True)
        
    def typing(self, text):
        self.label.config(text=text)
        
        

