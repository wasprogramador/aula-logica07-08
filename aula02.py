
## REVISÃo RÁPIDA!
### string = para definir nome, texto etc..
###int = para números inteiros (20)
## float = para número decimais (30,2)
### booleano = para definir TRUE (verdadeiro) ou FALSE (falso)
####################################################################

nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2:"))
nota3 = float(input("digite a nota 3:"))

media = (nota1 + nota2 + nota3) / 3
print("a média do aluno é: "+ str(media))
# quando exibir uma mensagem na tela e tem número, precisamos colocar o str, pois ele vai converter
# a variavel numero em texto. Se não colocarmos, vai dar ERRO!

if (media >=7):
    print(f"Aluno APROVADO! com média de : + {media}")
    if (media > 5):
        print("Aluno está em RECUPERAÇÃO")
else:
    print("Aluno está REPROVADO! com média de: " + str(media))
