import requests
from mailtm import Email

def listener(message):
    print("\nAssunto: " + message['subject'])
    print("Conteúdo:  " + message['text'] if message['text'] else message['html'])

def mainclass():
    name = input("Insira seu nome: ")
    if name == "":
        print("Por Favor, Insira seu nome.\n")
        return mainclass()
    else:
        print(f"Bem vindo, {name}")
        test = Email()
        print("\nDomínio do seu email: " + test.domain)
        test.register()
        print(f"\n{name}, Seu Email Temporário é: " + str(test.address))
        test.start(listener)
        print("\nEsperando novos emails...\n(Seus Emails Aparecerão abaixo)")


mainclass()
