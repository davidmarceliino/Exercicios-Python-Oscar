try:
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    reseultado = dividendo/divisor

except ValueError:
    print("Numero digitado invalido")
except ZeroDivisionError:
    print("Divisão por zero não permitida")