import math
num = float (input("digite um número qualquer: "))
if num > 0:
    raiz = math. sqrt(num)
    print("A raiz quadrada de %.2f é %.2f" % (num, raiz))
else:
    print("em R, nao há raiz quadrada de número negativo")