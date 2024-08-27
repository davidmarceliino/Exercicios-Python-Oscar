# Função com parametro e retorno(return)
def numero(num):
    if num % 2== 0:
        return "PAR"
    else:
        return "IMPAR"
    
resultado = numero(int(input("Digite o numero")))
print(resultado)