def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Procedimento encerrado.")
            break
        elif opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe")
            continue

        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))

        if opcao == "1":
            result = soma(primeiro_numero, segundo_numero)
        elif opcao == "2":
            result = subtracao(primeiro_numero, segundo_numero)
        elif opcao == "3":
            result = multiplicacao(primeiro_numero, segundo_numero)
        elif opcao == "4":
            result = divisao(primeiro_numero, segundo_numero)

        print(f"Resultado: {result}")

calculadora()