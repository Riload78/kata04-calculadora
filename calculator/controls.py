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
        
        
class CalcButton(tk.Frame):
    def __init__(self, parent, command, text):
        super().__init__(parent, width=68, height=50)
        self.pack_propagate(False)
        self.command = command
        self.text = text
        self.boton = tk.Button(self,text=text, command=self.press)
        self.boton.pack(side=tk.TOP, fill=tk.BOTH, expand= True)
        
    def press(self):
        self.command(self.text)
     

        
class KeyBoard(tk.Frame):
    def __init__(self,parent, command):
        super().__init__(parent,width=272, height=250)
        CalcButton(self, command, "AC").grid(column=0, row=0, columnspan=3,sticky='WENS')
        CalcButton(self, command, "÷").grid(column=3, row=0)
        CalcButton(self, command, "C").grid(column=0, row=1)
        CalcButton(self, command, "D").grid(column=1, row=1)
        CalcButton(self, command, "M").grid(column=2, row=1, rowspan=3, sticky='WENS')
        CalcButton(self, command, "x").grid(column=3, row=1)
        CalcButton(self, command, "X").grid(column=0, row=2)
        CalcButton(self, command, "L").grid(column=1, row=2)
        CalcButton(self, command, "-").grid(column=3, row=2)
        CalcButton(self, command, "I").grid(column=0, row=3)
        CalcButton(self, command, "V").grid(column=1, row=3)
        CalcButton(self, command, "+").grid(column=3, row=3)
        CalcButton(self, command, "=").grid(column=0, row=4, columnspan=4, sticky='WENS')
        