nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:")) 

def acesso(idade):
    if idade >= 18: 
        print("Usuario maior de idade")
    else:
        print("Usuario menor de idade")    

print(acesso(idade))
    

