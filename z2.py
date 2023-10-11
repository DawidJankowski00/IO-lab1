import math
import random

def a(list1, list2):
    suma = []
    iloczyn = []
    for i in range(0, len(list1)):
        suma.append(list1[i]+list2[i])
        iloczyn.append(list1[i]*list2[i])
    return suma, iloczyn


def b(list1, list2):
    suma = 0
    for i in range(0, len(list1)):
        suma += list1[i] * list2[i]
    return suma


def c(list):
    suma = math.sqrt(b(list,list))
    return suma


def d():
    lista = []
    for i in range(0, 50):
        lista.append(random.randint(0, 100))
    return lista


def e(wektor):
    avg = 0
    minimum = min(wektor)
    maximum = max(wektor)

    for i in wektor:
        avg += i
    avg = avg / len(wektor)

    o2 = 0
    for i in wektor:
        o2 += (i - avg)*(i - avg)
    o2 = o2 / len(wektor)

    o = math.sqrt(o2)


    return avg, minimum, maximum, o

def f(wektor):
    nowy = []
    minimum = min(wektor)
    maximum = max(wektor)
    for i in wektor:
        nowy.append((i-minimum) / (maximum - minimum))
    return nowy


def g(wektor):
    nowy = []
    avg, o = e(wektor)[0], e(wektor)[3]
    for i in wektor:
        nowy.append((i - avg) / o)
    return nowy



if __name__ == '__main__':

    ls1 = [3, 8, 9, 10, 12]
    ls2 = [8, 7, 7, 5, 6]
    print(a(ls1,ls2))
    print(b(ls1,ls2))
    print(c(ls1))
    print(c(ls2))
    vecd = d()
    print(vecd)
    print(e(vecd))
    print(f(vecd))
    print(g(vecd))