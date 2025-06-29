import os

import validacoes.email_gmail
import validacoes.email_e
import validacoes.senha_v

def cadastrar_usuario(usuarios):

    nome = input("\nDigite seu nome: ")
    email = input("Digite seu email: ")

    validacoes.email_gmail.validar_email(email)

    validacoes.email_e.email_existente(email, usuarios)

    senha = input("Digite sua senha: ")

    validacoes.senha_v.verificar_senha(senha)
        
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha
    }
    usuarios.append(usuario)

    with open('usuarios_salvos.txt', 'a', encoding = 'utf-8') as salvar_usuario:
            salvar_usuario.write(f'{nome};{email};{senha}\n')

    os.system('cls' if os.name == 'nt' else 'clear')
    return usuarios