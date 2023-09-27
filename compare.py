from PySimpleGUI import PySimpleGUI as sg


def compare(file_path, file_path_b, New_file, metodo):
    files_a = open(file_path, 'r').read().split('\n')
    files_b = open(file_path_b, 'r').read().split('\n')
    conjunto_a = set(files_a)
    conjunto_b = set(files_b)

    intersection = conjunto_a.intersection(conjunto_b)
    difference = conjunto_a.difference(conjunto_b)

    if metodo == 'iguais':
        with open(New_file, 'w') as file:
            file.write('\n'.join(intersection))
            janela["status"].update("COMPARAÇÃO EFETUADO COM SUCESSO")
    if metodo == 'diferentes':
        with open(New_file, 'w') as file:
            file.write('\n'.join(difference))
            janela["status"].update("COMPARAÇÃO EFETUADO COM SUCESSO")


def compare2():
    files_1 = open('mp3_arq1.txt', 'r').read().split('\n')
    files_2 = open('mp3_arq2.txt', 'r').read().split('\n') 
    intersection = []

    for file in files_1:
        if file in files_2:
            intersection.append(file)

    print(intersection)


if __name__ == "__main__":
    #compare2()
    sg.theme('Reddit')
    layout = [
         [sg.Text('Arquivo1'), sg.Input(key="arquivo1")],
         [sg.Text('Arquivo2'), sg.Input(key="arquivo2")],
         [sg.Text('Salvar local/arquivo'), sg.Input(key="New_file")],
         [sg.Text('Status:', key="status")],
         [sg.Button('Iguais')],
         [sg.Button('Diferentes')]
    ]

    janela = sg.Window('Tela Principal', layout)    



    while True:
         eventos, valores = janela.read()
         if eventos == sg.WINDOW_CLOSED:
              break
         if eventos == 'Iguais':
              metodo = 'iguais'
              compare(valores['arquivo1'], valores['arquivo2'], valores['New_file'], metodo)
         if eventos == 'Diferentes':
              metodo = 'Diferentes'
              compare(valores['arquivo1'], valores['arquivo2'], valores['New_file'], metodo)