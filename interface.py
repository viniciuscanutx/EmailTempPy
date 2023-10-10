from mailtm import Email
import PySimpleGUI as sg

class EmailTemp:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Seu Email Temporário: ',size=(17, 1)), sg.Output(size=(40, 1), key='output1'), sg.Button('Copiar!')],
            [sg.Output(size=(69, 10), key='output2')],
            [sg.Text('Para gerar um outro email, reinicie o programa.',size=(35, 1))],
            [sg.Button('Iniciar')]

        ]

        self.janela = sg.Window('Temporary Email', layout, icon=f'./img/ico1.ico')

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Iniciar':
                test = Email()
                test.register()
                emailfield = test.address
                test.start(self.listener)
                self.janela['output1'].update(emailfield)
                self.janela['output2'].update('')
                print("(Seus Emails Aparecerão abaixo)\nEsperando novos emails...")

    def listener(self, message):
        print('\nNovo Email: ')
        print("\nAssunto: " + message['subject'])
        print("Conteúdo:  " + message['text'] if message['text'] else message['html'])

gen = EmailTemp()
gen.Iniciar()
