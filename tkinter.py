import tkinter as tk
import random

root = tk.Tk()
root.geometry('200x200')

def hover(event):
    x = random.randint(0, 180)
    y = random.randint(0, 180)
    nao.place(x=x, y=y)

def messages():
    message = tk.Label(root, text='toba')
    message.place(x=70, y=115, relx=0, rely=0)

pergunta = tk.Label(root, text='Você é corno?')
pergunta.pack(anchor='n', pady=20)

nao = tk.Button(root, text='Não')
nao.place(x='98', y='80')
nao.bind('<Enter>', hover)

sim = tk.Button(root, text='Sim', command=messages)
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()
