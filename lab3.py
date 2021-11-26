import tkinter
from tkinter import *

import numpy as np
from matplotlib import pyplot as plt

list_functions = []


def count_function(x, a, b, c, d, isTrapezoid):
    result = []
    if isTrapezoid:
        for i in x:
            if a <= i <= d:
                if a <= i <= b:
                    result.append(1 - (b - i) / (b - a))
                    continue
                if b <= i <= c:
                    result.append(1)
                    continue
                if c <= i <= d:
                    result.append(1 - (i - c) / (d - c))
                    continue
            else:
                result.append(0)
    else:
        for i in x:
            if a <= i <= c:
                if a <= i <= b:
                    result.append(1 - (b - i) / (b - a))
                    continue
                if b <= i <= c:
                    result.append(1 - (i - b) / (c - b))
            else:
                result.append(0)

    return result


def clicked():
    x = np.arange(300)

    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())

    list_functions.append(count_function(x, a, b, c, d, CheckVar1.get()))
    listbox_update()


def show():
    for i in list_functions:
        plt.plot(i)
    plt.show()


def change():
    list_functions.pop(lbox.curselection()[0])

    x = np.arange(300)

    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())

    list_functions.append(count_function(x, a, b, c, d, CheckVar1.get()))
    listbox_update()


def del_function():
    list_functions.pop(lbox.curselection()[0])
    listbox_update()


def dop():
    result = []
    for i in range(len(list_functions[lbox.curselection()[0]])):
        result.append(1 - list_functions[lbox.curselection()[0]][i])
    list_functions.append(result)
    listbox_update()


def listbox_update():
    lbox.delete(0, tkinter.END)
    for i in range(len(list_functions)):
        lbox.insert(i, str(i))


window = Tk()
window.title("Оценка эффективностиопераций с валютой")
lbl = Label(window, text="Введите данные")
lbl.grid(column=0, row=0)
window.geometry('400x250')

# function 1
lbl_fn1 = Label(window, text="Функция 1:")
lbl_fn1.grid(column=0, row=1)

fn_1_1 = Entry(window, width=5)
fn_1_1.grid(column=1, row=1)

fn_1_2 = Entry(window, width=5)
fn_1_2.grid(column=2, row=1)

fn_1_3 = Entry(window, width=5)
fn_1_3.grid(column=3, row=1)

fn_1_4 = Entry(window, width=5)
fn_1_4.grid(column=4, row=1)

CheckVar1 = BooleanVar()
chk_fn1 = Checkbutton(window, text='Трапецевидная?', variable=CheckVar1)
chk_fn1.grid(column=5, row=1)

btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=5)

btn_del = Button(window, text="Показать!", command=show)
btn_del.grid(column=5, row=5)


btn_change = Button(window, text="Изменить!", command=change)
btn_change.grid(column=2, row=6)

btn_del = Button(window, text="Удалить!", command=del_function)
btn_del.grid(column=3, row=6)


#btn_del = Button(window, text="Дополнить!", command=dop)
#btn_del.grid(column=3, row=7)

lbox = Listbox(width=15, height=8)
lbox.grid(column=1, row=8)

window.mainloop()