import string
import random


def gerar_senha(tamanho = 12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha que deseja (ex.: 12): "))
senha_forte = gerar_senha(tamanho)
print("Senha Gerada:", senha_forte)