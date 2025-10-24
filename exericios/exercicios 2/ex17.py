saq = int(input("digite o valor a ser sacado:"))
if saq < 10 or saq > 600:
    print("Nao é possivel sacar o valor informado ")
    exit(1)
q100 = 0
q50 = 0
q10 = 0
q5 = 0
q1 = 0
if saq >= 100:
    q100 = saq // 100
    saq = saq - (q100 * 100)
if saq >= 50:
        q50 = saq // 50
        saq = saq - (q50 * 50)
if saq >= 10:
     q10 = saq // 10
     saq = saq - (q10 * 10)
if saq >= 5:
     q5 = saq // 5
     saq = saq - (q5 * 5)
if saq >= 1 :
    q1 = saq // 1
    saq = saq - (q1 * 1)
print(f"{q100} notas de 100")
print(f"{q50} notas de 50")
print(f"{q10} notas de 10")
print(f"{q5} notas de 5")
print(f"{q1} notas de 1")