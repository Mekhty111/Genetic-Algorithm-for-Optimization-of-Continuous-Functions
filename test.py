from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import *
import random
import numpy as np
import threading

# Цветовая схема
BG_COLOR = '#f0f4f8'
FG_COLOR = '#333333'
BTN_COLOR = '#008cba'
BTN_FG_COLOR = 'white'
LBL_FONT = ("Segoe UI", 10)
TXT_FONT = ("Consolas", 10)
TITLE_FONT = ("Segoe UI Semibold", 12)

# Initialization Window
window = Tk()
window.title("Genetic Optimization of Continuous Functions")
window.iconbitmap("GAE.ico")
window.resizable(False, False)
window.geometry('950x380')
window.configure(bg=BG_COLOR)

# Основной Frame
frame_main = Frame(window, bg=BG_COLOR, padx=20, pady=20)
frame_main.pack(expand=True, fill=BOTH)

lbl1 = Label(frame_main, text="Function:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT)
lbl1.grid(column=0, row=0, sticky=W, pady=5, padx=5)

e1_var = StringVar()
e1 = Entry(frame_main, textvariable=e1_var, width=100, font=TXT_FONT, relief=SOLID, bd=1)
e1.insert(END, '-1*x[0]**2-100')
e1.grid(column=1, row=0, columnspan=5, sticky=W, pady=5, padx=5)

lbl2 = Label(frame_main, text="Alpha:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT)
lbl2.grid(column=0, row=1, sticky=W, pady=10, padx=5)

e2_var = StringVar()
e2 = Entry(frame_main, textvariable=e2_var, width=15, font=TXT_FONT, relief=SOLID, bd=1)
e2.insert(END, '0.5')
e2.grid(column=1, row=1, sticky=W, pady=10, padx=5)

lbl3 = Label(frame_main, text="Deviance:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT)
lbl3.grid(column=2, row=1, sticky=W, pady=10, padx=5)

e3_var = StringVar()
e3 = Entry(frame_main, textvariable=e3_var, width=15, font=TXT_FONT, relief=SOLID, bd=1)
e3.insert(END, '2.5')
e3.grid(column=3, row=1, sticky=W, pady=10, padx=5)

lbl4 = Label(frame_main, text="Mutation Rate:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT)
lbl4.grid(column=4, row=1, sticky=W, pady=10, padx=5)

e4_var = StringVar()
e4 = Entry(frame_main, textvariable=e4_var, width=15, font=TXT_FONT, relief=SOLID, bd=1)
e4.insert(END, '0.0001')
e4.grid(column=5, row=1, sticky=W, pady=10, padx=5)

v2 = IntVar()
s2 = Scale(frame_main, variable=v2, from_=50, to=200, tickinterval=10, orient=HORIZONTAL, length=890,
           label="Population Size :", bg=BG_COLOR, fg=FG_COLOR)
s2.grid(column=0, row=2, columnspan=6, pady=20)

v3 = IntVar()
s3 = Scale(frame_main, variable=v3, from_=100000, to=1000000, tickinterval=100000, orient=HORIZONTAL, length=890,
           label="Number of Iterations :", bg=BG_COLOR, fg=FG_COLOR)
s3.grid(column=0, row=3, columnspan=6, pady=10)

def GetData():
    global funksiya, pop_size, al_CO, dev, mut1, n_it
    funksiya = str(e1_var.get())
    pop_size = int(v2.get())
    al_CO = float(e2_var.get())
    dev = float(e3_var.get())
    mut1 = float(e4_var.get())
    n_it = int(v3.get())
    window.destroy()

btn_run = Button(frame_main, text="RUN GENETIC ALGORITHM", command=GetData, width=30, height=2,
                 bg=BTN_COLOR, fg=BTN_FG_COLOR, font=LBL_FONT, relief=RAISED)
btn_run.grid(column=0, row=4, columnspan=6, pady=15)

window.mainloop()

# --- Ниже основной код Genetic Algorithm и окно статуса, оформленные в новом стиле ---

# (Далее оставляем остальной код с адаптацией цветов, шрифтов, отступов в виджетах главного окна)
# Например:

root = Tk()
root.title("Genetic Optimization of Continuous Functions")
root.geometry('800x600')
root.iconbitmap("GAE.ico")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

frame_top = Frame(root, bg=BG_COLOR)
frame_top.pack(pady=10)

scrollbar = Scrollbar(frame_top)
scrollbar.pack(side=RIGHT, fill=Y)

textbox = Text(frame_top, width=100, height=20, font=TXT_FONT, yscrollcommand=scrollbar.set, bg='white', fg=FG_COLOR,
               relief=SOLID, bd=1)
textbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=textbox.yview)

HP1 = "Dim=" + str(dim) + " f(x)=" + str(funct)
H1 = Label(root, text=HP1, font=TITLE_FONT, bg=BG_COLOR, fg=FG_COLOR)
H1.pack()

HP2 = "Pop=" + str(pop) + " N_iter=" + str(n_iter) + " Alpha=" + str(alpha) + " Deviance=" + str(mut_dev) + " MutRate=" + str(mut)
H2 = Label(root, text=HP2, font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR)
H2.pack()

CC1 = Label(root, text="The current maximizer", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR)
CC1.pack()

CC2 = Label(root, text="__________________", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR)
CC2.pack()

CC3 = Label(root, text="The current maximum", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR)
CC3.pack()

CC4 = Label(root, text="__________________", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR)
CC4.pack()

BBB = Button(root, text="START", command=GA_fun, width=20, height=2,
             bg=BTN_COLOR, fg=BTN_FG_COLOR, font=LBL_FONT, relief=RAISED)
BBB.pack(pady=10)

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot([], [])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# update_plot() and other logic remain as before

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
