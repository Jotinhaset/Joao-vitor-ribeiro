# 1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b}")

# 2. Leia o nome e a idade de uma pessoa e exiba uma mensagem com essas informações.

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
print(f"Nome: {nome}, Idade: {idade}")

# 3. Leia um número e informe se ele é positivo, negativo ou zero.

c = int(input("Digite um número: "))
if c > 0:
    print("O número é positivo.")
elif c < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 4. Leia a nota de um aluno e informe se ele foi aprovado (nota ≥ 7) ou reprovado.

nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
    print("O aluno foi aprovado.")


# 5. Leia um número inteiro e mostre sua tabuada de 1 a 10.

num = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 6. Leia um número N e calcule a soma dos números de 1 até N.

n = int(input("Digite um número N: "))
soma = 0
for i in range(1, n + 1):
    soma += i
print(f"A soma dos números de 1 até {n} é: {soma}")

# 7. Leia 10 números e informe a soma e a média.

soma = 0
for _ in range(10):
    numero = int(input("Digite um número: "))
    soma += numero
media = soma / 10
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")

# 8. Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.

soma = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero
print(f"A soma dos valores digitados é: {soma}")

# 9. Crie uma função que receba dois números e retorne o maior deles.

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

# 10. Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.

numeros = []
for _ in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)