import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("É necessário incluir pelo menos um tipo de caractere para gerar uma senha.")

    senha = []
    if incluir_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        senha.append(random.choice(string.digits))
    if incluir_simbolos:
        senha.append(random.choice(string.punctuation))

    senha += [random.choice(caracteres) for _ in range(tamanho - len(senha))]
    random.shuffle(senha)  # Embaralha a senha para torná-la mais imprevisível

    return ''.join(senha)

tamanho = int(input("Digite o tamanho da senha que deseja (ex.: 12): "))
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

senha_forte = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
print("Senha Gerada:", senha_forte)
