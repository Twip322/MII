import matplotlib.pyplot as plt
import random as rand

import numpy as np


def count_cluster(x, clusterLabels):
    if clusterLabels[0] <= x <= clusterLabels[3]:
        if clusterLabels[0] <= x <= clusterLabels[1]:
            return (x - clusterLabels[0]) / (clusterLabels[1] - clusterLabels[0])
        if clusterLabels[1] < x < clusterLabels[2]:
            return 1
        if clusterLabels[2] <= x <= clusterLabels[3]:
            return (clusterLabels[3] - x) / (clusterLabels[3] - clusterLabels[2])
    else:
        return 0


weights = {
    'Узник концлагеря': [30, 38, 42, 44],
    'Малый вес': [40, 45, 50, 55],
    'Средний вес': [52, 60, 68, 70],
    'Большой вес': [69, 72, 80, 95],
    'Жировое цунами': [92, 98, 100, 112]
}

list_of_weight = [rand.randrange(30, 112) for i in range(10)]


def clustering(x):
    result = []
    resultW = []
    result.append(count_cluster(x, weights['Узник концлагеря']))
    resultW.append('Узник концлагеря')
    result.append(count_cluster(x, weights['Малый вес']))
    resultW.append('Малый вес')
    result.append(count_cluster(x, weights['Средний вес']))
    resultW.append('Средний вес')
    result.append(count_cluster(x, weights['Большой вес']))
    resultW.append('Большой вес')
    result.append(count_cluster(x, weights['Жировое цунами']))
    resultW.append('Жировое цунами')
    iterator=0
    iterStop=0
    max = result[0]
    for i in result:
        if i > max:
            max = i
            iterStop+=iterator
        else:
            iterator+=1
    print(
        "Чёткое значение: {0}, Узник концлагеря: {1}, Малый вес {2}, Средний вес {3}, Большой вес {4}, Жировое цунами {5}, Результат : {6}".format(
            max, result[0], result[1], result[2], result[3], result[4], resultW[iterStop]))


for i in list_of_weight:
    clustering(i)

U = np.arange(30, 120, 0.1)
values = []

for plt_set in weights.keys():
    memberships = [count_cluster(x, weights[plt_set]) for x in U]
    tmp, = plt.plot(U, memberships, label=plt_set)
    values.append(tmp)
plt.legend(handles=values)


def crossing():
    imp1 = []
    for x in U:
        imp1.append(min(count_cluster(x, weights['Узник концлагеря']), count_cluster(x, weights['Средний вес']),
                        count_cluster(x, weights['Жировое цунами'])))
    return imp1


plt.plot(U, crossing(), color='black')


def union():
    imp2 = []
    for x in U:
        imp2.append(max(count_cluster(x, weights['Узник концлагеря']), count_cluster(x, weights['Малый вес']),
                        count_cluster(x, weights['Средний вес']), count_cluster(x, weights['Большой вес']),
                        count_cluster(x, weights['Жировое цунами'])))
    return imp2


plt.plot(U, union(), color='gray')
plt.show()

## TODO
## Захардкодить список
## Графики
## Пересечение 1 и 3 и 5, объединение всех
## Таблицу {Четкое значение, Все степени, результат}
