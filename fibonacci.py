Fibonacci = []
while True:
    nfib = int(input("Quanti numeri vuoi stampare ?"))
    try:
        if nfib > 0:
            break
        else:
            print("ATTENZIONE ", nfib, " non è > di 0. Riprova... \n\n")
    except ValueError:
        print("ATTENZIONE ", nfib, "non è un numero intero.Riprova...\n\n")
        continue
for n in range(nfib):
    if n < 2:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[n - 1] + fibonacci[n -2])
print(fibonacci)

## append SIGNIFICA concatenare aumentare di 1, come se fosse il +
## fibonacci è una LIST, (Classe) concatenate dal punto 
##linguaggi orientati agli oggetti OOB

## fibonacci sequenza come riportato dalla home page di Python
## per la sequenza dei numeri fino a 1000
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)

