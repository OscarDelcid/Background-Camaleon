from cProfile import label
from cgi import test
import tkinter as tk
import random

from click import command



ventana = tk.Tk()
ventana.geometry("300x300")

#Función Cambiar Color
def cambiar_color():
    colors =["black","green","red","blue"]
    random_colors = random.choice(colors)
    ventana.config(bg= random_colors)
    label_color = tk.Label(ventana, text ="Background Color: "  + random_colors , bg=random_colors)
    label_color.place(x=90, y=100)

#Botones
btn_1 = tk.Button(ventana, text = "Haz Clic Aqui", command=cambiar_color)
btn_1.place(x=110, y=200)
ventana.mainloop()