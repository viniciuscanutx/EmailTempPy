import time
from tkinter import messagebox
from mailtm import Email
import PySimpleGUI as sg
import pyperclip

class EmailTemp:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Clique em gerar para gerar um novo email.',size=(35, 1))],
            [sg.Text('Seu Email Temporário: ',size=(17, 1)), sg.Output(size=(40, 1), key='output1'), sg.Button('Copiar!')],
            [sg.Output(size=(69, 10), key='output2')],
            [sg.Button('Gerar')]

        ]

        self.janela = sg.Window('Temporary Email', layout, icon=f'./img/icon1.ico')



    def Iniciar(self):
        global emailfield
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                test.stop( )
                break
            if evento == 'Gerar':
                test = Email()
                test.register()
                emailfield = test.address
                test.start(self.listener)
                self.janela['output1'].update(emailfield)
                self.janela['output2'].update('')
                print("\nEsperando novos emails...")
            if evento == 'Copiar!':
                pyperclip.copy(emailfield)
                self.janela['output2'].update('Copiado com Sucesso!\nEsperando novos emails...')


    def listener(self, message):
        print('\nNovo Email: ')
        print("\nAssunto: " + message['subject'])
        print("Conteúdo:  " + message['text'] if message['text'] else message['html'])


gen = EmailTemp()
gen.Iniciar()
