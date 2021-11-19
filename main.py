#
a =125
b =133
c =145
d =155
numbers = [i * 5 for i in range(10)]


def output(num, u):
    if(num>u):
        if(num and u) or not num:
            implication = [1,1]
        else:
            implication = [1,0]
    else:
        if(u and num) or not u:
            implication = [1,1]
        else:
            implication = [0,1]
    print("num: {0} | u: {1} | num->u: {2}".format(num, u, implication))


for num in numbers:
    if a <= num <= b:
        value = (num - a) / (b - a)
        output(num, value)
    elif b < num < c:
        output(num, 1)
    elif c <= num <= d:
        value = (d - num) / (d - c)
        output(num, value)
    else:
        output(num, 0)
