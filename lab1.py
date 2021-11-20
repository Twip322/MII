#Норма уровня освещённости в Люксах для чтения
import matplotlib.pyplot as plt
import numpy as np

a =[0,50]
b =[50,110]
c =[80,150]
d =[200,250]
numbers = [i * 1 for i in range(251)]
imp1=[]
imp2=[]
imp3=[]

def output(num,func1,func2):
    print("num:{0},implication:{1}".format(num,min(func1,func2)))

def trap(a,b,c,d):
    def f(x):
        if(a<x<=b):
            return 1-((b-x)/(b-a))
        elif(b<=x<=c):
            return 1
        elif(c<=x<=d):
            return 1-((x-c)/(d-c))
        else:
            return 0
    return f
func1=trap(a[0],b[0],c[0],d[0])
func2=trap(a[1],b[1],c[1],d[1])


for num in numbers:
    output(num,func1(num),func2(num))
    imp1.append(func1(num))
    imp2.append(func2(num))
plt.plot((a[0],b[0],c[0],d[0])(0,1,0))
plt.plot((a[1],b[1],c[1],d[1])(0,1,0))

for num in numbers:
    print("Пересечение: {0}".format(min(func1(num),func2(num))))
    imp3.append((min(func1(num),func2(num))))
plt.plot(numbers,imp3)
plt.show()


##TODO
##Операция для двух степеней.|| пересечение
##Вывести график
##Применить для множеств пересечение(график)
##График должен быть трапецией (через функцию сделай)