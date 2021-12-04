import math
import tkinter
import random
from tkinter import *

import numpy as np
from matplotlib import pyplot as plt

## TODO
##  Области
##  Сильные спад и рост

list_functions = []
list_numbers = []
clear_time_series = [random.randint(0,200) for i in range(25)]
list_time_marks = []
graph_indexes = []
list_tendentions = []

def graph_tend():
    dop_list = []
    for i in range(len(clear_time_series) - 1):
        dop_list.append([clear_time_series[i], clear_time_series[i + 1]])
    for i in range(len(dop_list)):
        color = ''

        if list_tendentions[i] == 0:
            color = 'g'
        if list_tendentions[i] == -1:
            color = 'b'
        if list_tendentions[i] == 1:
            color = 'r'
        if list_tendentions[i] == 2:
            color = "orange"
        if list_tendentions[i] == -2:
            color = "black"
        plt.plot((i, i + 1), dop_list[i], color=color)

        plt.axhspan(list_numbers[0][0], list_numbers[0][3], color='pink', alpha=0.3)
        plt.axhspan(list_numbers[1][0], list_numbers[1][3], color='olive', alpha=0.3)
        plt.axhspan(list_numbers[2][0], list_numbers[2][3], color='grey', alpha=0.3)

    plt.show()

def get_tendentions():
    list_tendentions.clear()
    for i in range(len(graph_indexes) - 1):
        if graph_indexes[i] == graph_indexes[i + 1]:
            list_tendentions.append(0)
        if graph_indexes[i] < graph_indexes[i + 1]:
            list_tendentions.append(1)
        if graph_indexes[i] > graph_indexes[i + 1]:
            list_tendentions.append(-1)
        if math.fabs(graph_indexes[i] - graph_indexes[i + 1]) > 1:
            list_tendentions[len(list_tendentions) - 1] *= 2

    print(list_tendentions)

def graph_NVK():
    plt.plot(list_time_marks)
    plt.show()

def graph_ChVK():
    plt.plot(clear_time_series)
    plt.show()

def print_CTS():
    print(f"---Нечеткий временной ряд---")
    for i in range(len(clear_time_series)):
        print(f"{i}. {list_time_marks[i]} - {clear_time_series[i]}")

def get_max(number):
    list_coinsidens = []
    for i in list_functions:
        list_coinsidens.append(i[number])
    max = list_coinsidens[0]
    index = 0
    for i in range(len(list_coinsidens)):
        if list_coinsidens[i] > max:
            max = list_coinsidens[i]
            index = i
    return index

def get_fuzzy_estimate():
    list_time_marks.clear()
    graph_indexes.clear()
    for i in clear_time_series:
        number = get_max(i)
        graph_indexes.append(number)
        if number <= 2:
            if number == 0:
                list_time_marks.append("Тотальный крах")
            if number == 1:
                list_time_marks.append("Серьёзные убытки")
            if number == 2:
                list_time_marks.append("Обычные убытки")
        else:
            list_time_marks.append("Незначительные убытки")
    print_CTS()

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
    x = np.arange(d)
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
    plt.show()


def change():
    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())

    if (d == 0):
        trap = False
        x = np.arange(c)
    else:
        trap = True
        x = np.arange(d)
    list_functions.append(count_function(x, a, b, c, d, trap))
    list_numbers.append(returnNumbers(x, a, b, c, d, trap))
    listbox_update()


def clone():
    nums = list_numbers[lbox.index(lbox.curselection()[0])]

    list_functions.append(cloned_func(nums[0] + 20, nums[1], nums[2], nums[3], nums[4], nums[5],True))
    list_numbers.append(nums)
    list_functions.append(cloned_func(nums[0] - 20, nums[1], nums[2], nums[3], nums[4], nums[5],False))

    listbox_update()
    imp1 = []
    x = np.arange(nums[4])
    l1=list_functions[0]
    l2=list_functions[1]
    l3=list_functions[2]
    for l in x:
        imp1.append(
            max(l1[l],l2[l],l3[l]))
    plt.plot(x,list_functions[0])
    plt.plot(x,list_functions[1])
    plt.plot(x, list_functions[2])
    plt.plot(x,imp1,color='gray')
    plt.show()


def del_function():
    list_functions.pop(lbox.curselection()[0])
    list_numbers.pop(lbox.curselection()[0])
    listbox_update()


def listbox_update():
    lbox.delete(0, tkinter.END)
    for i in range(len(list_functions)):
        lbox.insert(i, str(i))



def hardcode():
    x=np.arange(0,300,1)
    list_functions.append(count_function(x,0,20,40,60,True))
    list_numbers.append([0, 20, 40, 60])
    list_functions.append(count_function(x, 50, 100, 120, 140,True))
    list_numbers.append([50, 100, 120,140])
    list_functions.append(count_function(x, 130, 140, 160,200 , True))
    list_numbers.append([130,140,160,200])
    listbox_update()



window = Tk()
window.title("Оценка убытков")
lbl = Label(window, text="Введите данные")
lbl.grid(column=0, row=0)
window.geometry('600x400')

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

btn_time = Button(window, text="НВР!", command=get_fuzzy_estimate)
btn_time.grid(column=2, row=10)

btn_tend = Button(window, text="Тенденции!", command=get_tendentions)
btn_tend.grid(column=3, row=10)

btn_graph_ChVK = Button(window, text="График чвр!", command=graph_ChVK)
btn_graph_ChVK.grid(column=2, row=9)

btn_graph_NVK = Button(window, text="График НВР!", command=graph_NVK)
btn_graph_NVK.grid(column=2, row=11)

btn_graph_tend = Button(window, text="График тенденций!", command=graph_tend)
btn_graph_tend.grid(column=3, row=11)


hardcode()

window.mainloop()
