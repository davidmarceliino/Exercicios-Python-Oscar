def contador(inicio, fim, passo):
    if passo == 0:
        print("O passo não pode ser zero.")
        return

    if passo > 0:
        if inicio > fim:
            print("O início deve ser menor ou igual ao fim para passos positivos.")
            return
        for nuns in range(inicio, fim + 1, passo):
            print(nuns)
        print() 


    elif passo < 0:
        if inicio < fim:
            print("O início deve ser maior ou igual ao fim para passos negativos.")
            return
        for nuns in range(inicio, fim - 1, passo):
            print(nuns)
        print() 


try:
    inicio = int(input("Digite o valor de início: "))
    fim = int(input("Digite o valor de fim: "))
    passo = int(input("Digite o valor do passo: "))

    contador(inicio, fim, passo)
except ValueError:
    print("Por favor, digite apenas números inteiros.")
