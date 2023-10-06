import PySimpleGUI as sg


sg.theme('Black')

def gerador_de_tabuada(numero, operacao):
    resultado = ""
    if operacao == 1:
        for i in range(1, 11):
            resultado += f"{numero} + {i} = {numero + i}\n"
    elif operacao == 2:
        for i in range(1, 11):
            resultado += f"{numero} - {i} = {numero - i}\n"
    elif operacao == 3:
        for i in range(1, 11):
            resultado += f"{numero} / {i} = {numero / i}\n"
    elif operacao == 4:
        for i in range(1, 11):
            resultado += f"{numero} * {i} = {numero * i}\n"

    return resultado

layout = [
    [sg.Text("Digite o número para a tabuada: EX 1-10"), sg.InputText(key="numero")],
    [sg.Radio("SOMA", "operacao", default=True, key="soma"), sg.Radio("SUBTRAÇÃO", "operacao", key="subtracao"),
     sg.Radio("DIVISÃO", "operacao", key="divisao"), sg.Radio("MULTIPLICAÇÃO", "operacao", key="multiplicacao")],
    [sg.Button("Gerar Tabuada"), sg.Button("Sair")],
    [sg.Multiline("", size=(40, 10), key="resultado")]
]

window = sg.Window("Gerador de Tabuada", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    if event == "Gerar Tabuada":
        numero = int(values["numero"])
        operacao = 0
        if values["soma"]:
            operacao = 1
        elif values["subtracao"]:
            operacao = 2
        elif values["divisao"]:
            operacao = 3
        elif values["multiplicacao"]:
            operacao = 4
        resultado = gerador_de_tabuada(numero, operacao)
        window["resultado"].update(resultado)

window.close()

