import tkinter as tk
def imprimir_saludo():
    label.config(text=f'Hola, {valor_nombre.get()}')
    
root = tk.Tk()
root.title("Hola Mundo")
print(root.geometry())
root.geometry("800x600+400+200")

label = tk.Label(root, text="Hola Mundo", bd=2, relief=tk.RAISED)
label1 = tk.Label(root, text="NUeva label")
label.place(x=100, y=100)
label1.pack(side=tk.LEFT)

valor_nombre = tk.StringVar()

nombre = tk.Entry(root, textvariable=valor_nombre)
nombre.pack()

boton = tk.Button(root, text="Pulsame", command=imprimir_saludo)
boton.pack()



root.mainloop()
