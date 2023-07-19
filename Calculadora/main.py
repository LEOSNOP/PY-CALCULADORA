print("bem vindo a calculadora, se quiser desligar a calculadora digite (E), caso nao queira, aperte enter")

comando = str

while comando != "E":

    numero1 = float(input("digite um numero: "))
    numero2 = float(input("digite um numero: "))
    operador = str (input("digite um sinal que seja: +,-, / ou * : "))

    if (operador == "+"):
        resultado = numero1+numero2
        print("resultado da soma: ", resultado)

    elif (operador == "-"):
        resultado = numero1-numero2
        print("resultado da subtracao: ", resultado)

    elif (operador == "*"):
        resultado = numero1*numero2
        print("resultado da multiplicação: ", resultado)

    elif (operador == "/"):
        resultado = numero1/numero2
        print("resultado da divisao: ", resultado)

    else:
        print("Digite um operador valido!!!")

    comando = str(input())

print ("desligando!!!")

