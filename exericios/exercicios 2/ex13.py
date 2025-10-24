teste = input("Digite 1- domingo 2- segunda 3- terça 4- quarta 5-quinta 6- sexta 7- sabado")
match teste:
    case "1":
        print("Domingo")
    case "2":
        print("Segunda")
    case "3":
        print("Terça")
    case "4":
        print("Quarta")
    case "5":
        print("Quinta")
    case "6":
        print("Sexta")
    case "7":
        print("Sabado")
    case _:
        print("Nenhuma das outras opções")