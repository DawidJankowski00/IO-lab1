import pandas
import matplotlib.pyplot as plt

def read():
    miasta = pandas.read_csv("miasta.csv")

    return miasta


def a(miasta):
    print(miasta)
    print(miasta.values)

def b(miasta, new):
    miasta.loc[len(miasta)] = new
    print(miasta)
    return miasta

def c(miasta):
    miasta.plot(x = 'Rok', y = 'Gdansk', marker = '.', color = 'red')
    plt.xlabel("Lata")
    plt.ylabel("Liczba ludnosci [w tys.]")
    plt.show()

def d(miasta):
    miasta.plot(x='Rok', marker='.')
    plt.xlabel("Lata")
    plt.ylabel("Liczba ludnosci [w tys.]")
    plt.show()


if __name__ == '__main__':
    miasta = read()
    a(miasta)
    new = {'Rok': 2010, 'Gdansk': 460, 'Poznan': 555, "Szczecin": 405}
    miasta = b(miasta, new)
    c(miasta)
    d(miasta)


