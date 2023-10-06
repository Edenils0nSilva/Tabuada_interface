

def gerador_de_tabuada(numero):
    

    match opc:
        case 1: 
            for i in range(1, 20):
                resultado = numero + i
                print(f"{numero} + {i} = {resultado}")
        case 2:
            for i in range(1, 20):
                resultado = numero - i
                print(f"{numero} - {i} = {resultado}")
        case 3:
            for i in range(1, 20):
                resultado = numero / i
                print(f"{numero} / {i} = {resultado}")
        case 4:
            for i in range(1, 20):
                resultado = numero * i
                print(f"{numero} * {i} = {resultado}")

    if opc not in range(1, 5):
        print("Opção inválida. Escolha uma operação de 1 a 4.")
    
    

while True:
        print("[1] SOMA")
        print("[2] SUBTRAÇÃO")
        print("[3] DIVISÃO")
        print("[4] MULTIPLICAÇÃO")
        opc = int(input("ESCOLHA QUAL O TIPO DE OPERAÇÃO: "))

        if opc in range(1, 5):
            break 
        else:
            print("Opção inválida. Escolha uma operação de 1 a 4.")


# Solicite a escolha do usuário
numero = int(input("Digite o número para a tabuada: EX 1-10 "))
gerador_de_tabuada(numero)


