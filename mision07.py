#Autor: Santiago España Vázquez
#Descripción: Ciclos While


def dividir(a,b):
    c = a
    d = b
    e = 0
    while c > d:
        c -= d
        e += 1

    print(a, "/", b, "=", e, " sobra ", c)

def encontrarMayor():
    ex=1
    may=0
    print("Teclea una serie de números para encontrar el mayor.")
    while ex!=-1:
        ex=int(input("Teclea un número [-1 para salir]: "))
        if ex>may:
            may=ex
    print("El mayor es: ", may)


def main():
    print("""Misión 07. Ciclos While
Autor: Santiago España Vázquez
Matricula: A01748311""")
    ex=0
    while ex!=3:
        ex=int(input("""
1. Calcular divisiones
2. Encontrar el mayor
3. Salir
Teclea tu opción: """))
        if ex == 1:
            a=int(input("Por favor introduzca el dividendo: "))
            b=int(input("Por favor introduzca el divisor: "))
            dividir(a,b)
        if ex == 2:
            encontrarMayor()
    print("Gracias por usar este programa, regresa pronto.")


main()