### Exemplo 1: Verificação de idade e permissão de entrada.
## Faça um programa onde le a idade de um usuário e verifica se ele tem convite e se pode entrar.
# lembrando que só pode entrar, se for MAIOR de 18.

# criar as variaveis: idadde e tem_convite

idade = int(input("Digite sua idade: "))
tem_convite = True # booleano

if idade >= 18:
    if tem_convite:
        print("pode entrar na festa!")
    else:
        print("Precisa de um convite para entrar na festa.")
else:
    print("Não pode entrar. É menor de idade.")

