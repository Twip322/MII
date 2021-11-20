def count_cluster(x,clusterLabels):
    if clusterLabels[0] <= x <= clusterLabels[3]:
        if clusterLabels[0] <= x <= clusterLabels[1]:
            return (x - clusterLabels[0]) / (clusterLabels[1] - clusterLabels[0])
        if clusterLabels[1] < x < clusterLabels[2]:
            return 1
        if clusterLabels[2] <= x <= clusterLabels[3]:
            return (clusterLabels[3] - x) / (clusterLabels[3] - clusterLabels[2])
    else:
        return 0


def last_cluster(x, clusterLabels):
    if clusterLabels[0] <= x:
        if clusterLabels[0] <= x <= clusterLabels[1]:
            return (x - clusterLabels[0]) / (clusterLabels[1] - clusterLabels[0])
        if clusterLabels[1] < x:
            return 1

    else:
        return 0



def clustering(x):
    result = []

    # print(x)
    result.append(count_cluster(x, [30, 38, 42, 44]))
    print(f"На {result[0]} узник концлагеря")
    result.append(count_cluster(x, [40, 45,50,55]))
    print(f"На {result[1]} малый вес")

    result.append(count_cluster(x, [52, 60, 68, 70]))
    print(f"На {result[2]} средний вес")

    result.append(count_cluster(x, [69, 72, 80, 95]))
    print(f"На {result[3]} большой вес")

    result.append(last_cluster(x, [92, 98, 100, 112]))
    print(f"На {result[4]} жировое цунами")



    max = result[0]
    for i in result:
        if i > max:
            max = i

    print(f"Max {max}")
    print()
while True:
    clustering(int(input('Введите вес:')))
##TODO
##Таблица
##Графики
##Операции