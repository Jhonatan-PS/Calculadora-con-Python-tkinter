from tkinter import *

def click(valor):
    if valor == 'C':
        borrar()
    else:
        entrada_texto.insert(END, valor)

def borrar():
    entrada_texto.delete(len(entrada_texto.get()) - 1, END)

def borrar_todo():
    entrada_texto.delete(0, END)

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.delete(0, END)
        entrada_texto.insert(END, str(resultado))
    except Exception as e:
        entrada_texto.delete(0, END)
        entrada_texto.insert(END, "Error")

# Crear la ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.config(background="gray",padx=3,pady=3)

# Crear el campo de entrada de texto
entrada_texto = Entry(ventana, font=("Rockwell", 20))
entrada_texto.config(background="black",fg="#03f943",borderwidth="10px")
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Crear los botones y asignarles las funciones correspondientes
for boton in botones:
    texto, fila, columna = boton
    Button(ventana, text=texto, font=("Rockwell", 25),width=3,height=1,background=("Orange"),command=lambda t=texto: click(t) if t.isdigit() or t in ['+', '-', '*', '/'] else calcular() if t == '=' else borrar_todo()).grid(row=fila, column=columna, pady=1)

# Ejecutar la aplicación
ventana.mainloop()
