import tkinter
from tkinter import *

import numpy as np
from matplotlib import pyplot as plt

## TODO
## Трапецивидность в условие || +
## Выбор графиков || +
## На выбранные клонирование, два один на +, другой на -
## Объединение полученных клонированных


list_functions = []
list_numbers = []


def cloned_func(x, a, b, c, d, isTrapezoid,left):
    result = []
    if left == True:
        if isTrapezoid:
            for i in x:
                if a <= i <= d:
                    if a <= i <= b:
                        result.append(1)
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
    else:
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
                        result.append(1)
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


    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())
    x = np.arange(d + 10)
    if d == 0:
        trap = False
    else:
        trap = True
    list_functions.append(count_function(x, a, b, c, d, trap))
    list_numbers.append(returnNumbers(x, a, b, c, d, trap))
    listbox_update()


def returnNumbers(x, a, b, c, d, trap):
    nums = [x, a, b, c, d, trap]
    return nums


def show():
    z = 0
    for i in range(list_functions.__len__()):
        if lbox.curselection().__len__() > z:
            if i == lbox.index(lbox.curselection()[z]):
                plt.plot(list_functions[i])
                z += 1
    union()
    plt.show()


def change():
    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())
    x = np.arange(d + 10)

    if (d == 0):
        trap = False
    else:
        trap = True
    list_functions.append(count_function(x, a, b, c, d, trap))
    list_numbers.append(returnNumbers(x, a, b, c, d, trap))
    listbox_update()


def clone():
    nums = list_numbers[lbox.index(lbox.curselection()[0])]
    imp1=[]
    x=np.arange(600)
    for l in x:
        imp1.append(
            max(list_functions[lbox.index(lbox.curselection()[0])], list_functions[lbox.index(lbox.curselection()[1])],
                list_functions[lbox.index(lbox.curselection()[2])]))
    list_functions.append(cloned_func(nums[0]+100, nums[1], nums[2], nums[3], nums[4], nums[5],True))
    list_numbers.append(nums)
    list_functions.append(cloned_func(nums[0] - 100, nums[1], nums[2], nums[3], nums[4], nums[5],False))

    listbox_update()




def del_function():
    list_functions.pop(lbox.curselection()[0])
    list_numbers.pop(lbox.curselection()[0])
    listbox_update()


def listbox_update():
    lbox.delete(0, tkinter.END)
    for i in range(len(list_functions)):
        lbox.insert(i, str(i))


window = Tk()
window.title("Оценка убытков")
lbl = Label(window, text="Введите данные")
lbl.grid(column=0, row=0)
window.geometry('600x250')

lbl_fn1 = Label(window, text="Функция :")
lbl_fn1.grid(column=0, row=1)

fn_1_1 = Entry(window, width=5)
fn_1_1.grid(column=1, row=1)

fn_1_2 = Entry(window, width=5)
fn_1_2.grid(column=2, row=1)

fn_1_3 = Entry(window, width=5)
fn_1_3.grid(column=3, row=1)

fn_1_4 = Entry(window, width=5)
fn_1_4.grid(column=4, row=1)

btn = Button(window, text="Задать функцию", command=clicked)
btn.grid(column=2, row=5)

btn_del = Button(window, text="Построить график", command=show)
btn_del.grid(column=3, row=5)

btn_change = Button(window, text="Изменить график", command=change)
btn_change.grid(column=2, row=6)

btn_del = Button(window, text="Удалить график", command=del_function)
btn_del.grid(column=3, row=6)

btn_clone = Button(window, text="Клонировать", command=clone)
btn_clone.grid(column=4, row=6)

lbox = Listbox(width=15, height=8, selectmode=MULTIPLE)
lbox.grid(column=1, row=8)

window.mainloop()
