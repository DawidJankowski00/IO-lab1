
def prime(n):
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True

def select_primes(lista):
    lista = lista[1:-1].split(",")
    primes = []
    for i in range(0, len(lista)):
        lista[i]= int(lista[i])
        if prime(lista[i]):
            primes.append(lista[i])
    
    
    return primes


print(select_primes("[6, 9, 11, 13]"))