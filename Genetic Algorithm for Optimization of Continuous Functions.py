from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import *
import random
import numpy as np
import threading
import seaborn as sns

sns.set(style="darkgrid")

# Цвета и шрифты
BG_COLOR = '#f0f4f8'
FG_COLOR = '#333333'

BTN_BG = 'white'
BTN_FG = '#008000'
BTN_FONT = ("Segoe UI", 11, "bold")
BTN_RELIEF = RAISED
BTN_BORDER = 3

LBL_FONT = ("Segoe UI", 10)
TXT_FONT = ("Consolas", 10)
TITLE_FONT = ("Segoe UI Semibold", 12)


# Функция для красивого стиля кнопки
def style_button(btn):
    def on_enter(e):
        btn['bg'] = '#ccffcc'
    def on_leave(e):
        btn['bg'] = BTN_BG
    btn.config(bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, relief=BTN_RELIEF, bd=BTN_BORDER, activebackground='#a3dca3',
               activeforeground=BTN_FG, cursor='hand2')
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


# Initialization Window
window = Tk()
window.title("Genetic Optimization of Continuous Functions - Mehdi Mehdiyev")
window.iconbitmap("GAE.ico")
window.resizable(False, False)
window.geometry('950x380')
window.configure(bg=BG_COLOR)


frame_main = Frame(window, bg=BG_COLOR, padx=20, pady=20)
frame_main.pack(expand=True, fill=BOTH)


Label(frame_main, text="Function:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT).grid(column=0, row=0, sticky=W, pady=5, padx=5)

e1_var = StringVar()
e1 = Entry(frame_main, textvariable=e1_var, width=100, font=TXT_FONT, relief=SOLID, bd=1)
e1.insert(END, '-1*x[0]**2-100')
e1.grid(column=1, row=0, columnspan=5, sticky=W, pady=5, padx=5)

Label(frame_main, text="Alpha:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT).grid(column=0, row=1, sticky=W, pady=10, padx=5)

e2_var = StringVar()
e2 = Entry(frame_main, textvariable=e2_var, width=15, font=TXT_FONT, relief=SOLID, bd=1)
e2.insert(END, '0.5')
e2.grid(column=1, row=1, sticky=W, pady=10, padx=5)

Label(frame_main, text="Deviance:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT).grid(column=2, row=1, sticky=W, pady=10, padx=5)

e3_var = StringVar()
e3 = Entry(frame_main, textvariable=e3_var, width=15, font=TXT_FONT, relief=SOLID, bd=1)
e3.insert(END, '2.5')
e3.grid(column=3, row=1, sticky=W, pady=10, padx=5)

Label(frame_main, text="Mutation Rate:", bg=BG_COLOR, fg=FG_COLOR, font=LBL_FONT).grid(column=4, row=1, sticky=W, pady=10, padx=5)

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


btn_run = Button(frame_main, text="RUN GENETIC ALGORITHM", width=30, height=2, command=GetData)
style_button(btn_run)
btn_run.grid(column=0, row=4, columnspan=6, pady=15)

window.mainloop()

# Genetic Algorithm Parameters Initialization
inpp = funksiya
dim111 = 0
for i in inpp:
    if i == '[':
        dim111 += 1

dim = dim111
n_iter = n_it
pop = pop_size
funct = funksiya
alpha = al_CO
mut = mut1
mut_dev = dev

# Genetic Algorithm Functions


def evaluate(func, a):
    x = a
    res1 = eval(func)
    return res1


def LFP(popp):
    res2 = [None] * pop
    for k in range(pop):
        res2[k] = evaluate(funct, popp[k])
    return res2


def selection(popp):
    LFPr = LFP(popp)
    array = np.array(LFPr)
    temp = array.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(array))
    ranks = ranks + 1
    rank = ranks.tolist()
    summa = sum(rank)
    fit = [rank[l] / summa for l in range(pop)]
    popp_c = [*range(pop)]
    sampling = np.random.choice(popp_c, 2 * pop, p=fit)
    sampling_l = sampling.tolist()
    res_f = [[None for j in range(2)] for i in range(pop)]
    for zxc in range(pop):
        rr1 = random.choice(sampling_l)
        ii1 = sampling_l.index(rr1)
        sampling_l.pop(ii1)
        res_f[zxc][0] = rr1

        rr2 = random.choice(sampling_l)
        ii2 = sampling_l.index(rr2)
        sampling_l.pop(ii2)
        res_f[zxc][1] = rr2

    res_ff = [[[None for qqqq in range(dim)] for jjjj in range(2)] for iiii in range(pop)]
    for aa in range(pop):
        for bb in range(2):
            res_ff[aa][bb] = popp[res_f[aa][bb]]
    return res_ff


def crossover(parents):
    parents = np.array(parents)  # shape (pop, 2, dim)
    b1 = parents[:, 0, :] - alpha * (parents[:, 1, :] - parents[:, 0, :])
    b2 = parents[:, 1, :] + alpha * (parents[:, 1, :] - parents[:, 0, :])
    kids_ND = [np.random.uniform(b1[u], b2[u]) for u in range(pop)]
    return kids_ND


def mutation(kids):
    for t in range(pop):
        rand_num = random.random()
        if rand_num > mut:
            GAUSS = random.gauss(0, mut_dev)
            kids[t] = np.array(kids[t]) + GAUSS
    return kids


def maxpo(l1):
	return np.argmax(l1)

def minpo(l2):
	return np.argmin(l2)


def elitism(p_o, p_n):
    LFP_o = LFP(p_o)
    i_o = maxpo(LFP_o)
    elite = p_o[i_o]

    LFP_n = LFP(p_n)
    i_n = minpo(LFP_n)
    p_n[i_n] = elite

    return p_n


track_i = []
track_m = []

stop_flag = False  # Флаг для остановки цикла GA


def GA_loop():
    global stop_flag
    BBB["state"] = "disabled"
    force_stop_btn["state"] = "normal"
    popu = [None] * pop
    for j in range(pop):
        popu[j] = [random.randrange(1, 500, 1) for z in range(dim)]

    global i
    i = 0
    max_old = [None] * dim

    while i < n_iter and not stop_flag:
        popu_old = popu
        parents1 = selection(popu)
        kids1 = crossover(parents1)
        popu_new = mutation(kids1)
        popu = elitism(popu_old, popu_new)

        tops = LFP(popu)
        top_pos = maxpo(tops)
        maximizer = popu[top_pos]
        current_top = evaluate(funct, popu[top_pos])

        maximizer111 = np.array(maximizer)
        max_old111 = np.array(max_old)

        if not all(maximizer111 == max_old111):
            ZZZ = "At the iteration " + str(i) + "\n" + "The current maximizer is: \n" + str(maximizer) + "\n" + "The current maximum is: \n" + str(current_top) + "\n\n"
            textbox.insert(END, ZZZ)
            max_old = maximizer
            if i != 0:
                track_i.append(i)
                track_m.append(current_top)

        maximizer1 = maximizer111.round(decimals=3)
        current_top1 = round(current_top, 3)

        GHG = "i = " + str(i) + " x* = " + str(maximizer1)
        HGH = "f(x) = " + str(current_top1)
        CC2.config(text=GHG)
        CC4.config(text=HGH)

        i += 1

    force_stop_btn["state"] = "disabled"
    BBB.pack(padx=10, pady=10)
    BBB["state"] = "normal"

def GA_fun():
    global stop_flag, track_i, track_m
    stop_flag = False
    track_i.clear()
    track_m.clear()
    BBB.pack_forget()  # скрыть кнопку старт
    GA_thread = threading.Thread(target=GA_loop, daemon=True)
    GA_thread.start()
    start_plot()

def force_stop():
    global stop_flag, track_i, track_m
    stop_flag = True
    force_stop_btn["state"] = "disabled"
    track_i.clear()
    track_m.clear()



def on_closing():
    global stop_flag
    stop_flag = True
    root.destroy()


# Status Window setup
root = Tk()
root.title("Genetic Optimization of Continuous Functions")
root.geometry('1250x700')
root.iconbitmap("GAE.ico")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Основной frame для верхней панели (лог, статусные поля)
main_frame = Frame(root, bg=BG_COLOR)
main_frame.pack(side=TOP, fill=BOTH, expand=True)

upper_frame = Frame(main_frame, bg=BG_COLOR)
upper_frame.pack(side=TOP, fill=X, padx=18, pady=(10, 2), expand=False)

# Лог слева
log_frame = Frame(upper_frame, bg=BG_COLOR)
log_frame.pack(side=LEFT, fill=Y, expand=False, padx=(0, 7))
textbox = Text(log_frame, width=54, height=18, font=TXT_FONT, bg='white', fg=FG_COLOR, relief=SOLID, bd=1)
textbox.pack(side=LEFT, fill=Y)
scrollbar = Scrollbar(log_frame, command=textbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
textbox.config(yscrollcommand=scrollbar.set)

# Статусные виджеты справа
status_frame = Frame(upper_frame, bg=BG_COLOR)
status_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(7, 0), pady=5)

HP1 = Label(status_frame, text="Dim=" + str(dim) + " f(x)=" + str(funct), font=TITLE_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
HP1.pack(anchor='w', pady=(2, 4))

HP2 = Label(status_frame, text="Pop=" + str(pop) + " N_iter=" + str(n_iter) + " Alpha=" + str(alpha) + " Deviance=" + str(mut_dev) + " MutRate=" + str(mut),
            font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
HP2.pack(anchor='w', pady=(0, 10))

CC1 = Label(status_frame, text="The current maximizer", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
CC1.pack(anchor='w')

CC2 = Label(status_frame, text="__________________", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
CC2.pack(anchor='w')

CC3 = Label(status_frame, text="The current maximum", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
CC3.pack(anchor='w')

CC4 = Label(status_frame, text="__________________", font=LBL_FONT, bg=BG_COLOR, fg=FG_COLOR, anchor='w')
CC4.pack(anchor='w', pady=(0, 10))

BBB = Button(status_frame, text="START", width=20, height=2, command=GA_fun)
style_button(BBB)
BBB.pack(pady=10)

force_stop_btn = Button(status_frame, text="FORCE STOP", width=20, height=2, command=force_stop, state=DISABLED, bg='#ffcccc', fg='#cc0000', font=LBL_FONT, relief=RAISED, bd=3, activebackground='#ff9999', activeforeground='#992222', cursor='hand2')
force_stop_btn.pack(pady=5)

# Нижний большой график
plot_frame = Frame(main_frame, bg=BG_COLOR)
plot_frame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=(15, 25))

fig = Figure(figsize=(14, 5.2), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot([], [])

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=BOTH, expand=True)

def update_plot():
    x = track_i.copy()
    y = track_m.copy()
    ax.clear()
    if len(x) > 0 and len(y) > 0:
        ax.plot(x, y, color=sns.color_palette("deep")[2], linewidth=4, alpha=0.9)
        ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.4)
    else:
        # График пустой — можно показать пустой холст или текст
        ax.text(0.5,0.5,"No data", ha='center', va='center', fontsize=14, color='gray', transform=ax.transAxes)
    ax.set_title("GA PROGRESS GRAPH", fontsize=21, fontweight='bold', color="#037e42")
    ax.set_xlabel("Iteration", fontsize=16)
    ax.set_ylabel("Maximum", fontsize=16)
    fig.tight_layout(pad=3)
    canvas.draw()
    root.after(1000, update_plot)


def start_plot():
    update_plot()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
