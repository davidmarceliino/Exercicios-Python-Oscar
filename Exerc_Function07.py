salario = float(input("Digite seu salario "))
calculo1 = (salario * 10 / 100 )
calculo2 = (salario * 15 / 100 )

def reajuste(salario):
    if salario >= 5000:
        return calculo1 + salario
    else:
        return calculo2 + salario


salReajuste=reajuste(salario)
print(salReajuste)
