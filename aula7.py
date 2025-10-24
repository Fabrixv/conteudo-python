import time
time.sleep(1)
valor = 10
while valor <0:
    print(valor)
    valor = valor - 1
    print("vai tomar no cu")
print()
print()
print()
print()
saque = -1
print('DIGITE UM NUMERO ENTRE 0 E 600')
while saque <= 0 or saque > 600:
    saque = int(input("Digite o valor a ser sacado "))
print()
print()
print()
print()
aluno = ["Anna vest pal", "kauny", "chaine"]
for indice in range (0,3):
    print(f"ola {aluno[indice]}")