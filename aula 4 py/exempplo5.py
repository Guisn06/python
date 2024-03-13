nome = input("digite seu nome: ")
n1 = float(input("digite a sua primeira nota:"))
n2 = float(input("digite a sua segunda nota:"))
média =(n1 + n2) /2
if média >=6.0:
    print(f"{nome} parabéns  você foi aprovado")
else:
    print(f"{nome} você infelizmente foi reprovado" )