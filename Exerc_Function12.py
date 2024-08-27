nt1 = float(input("Digite a primeira nota: "))
nt2 = float(input("Digite a segunda nota: "))
nt3 = float(input("Digite a terceira nota: "))
soma = 0

try:
    def calc (nt1, nt2, nt3):
       if(nt1 > 0 and nt2 > 0 and nt3 > 0):
         soma = (nt1 + nt2 + nt3 / 3)
         return soma
       else:
        print("Apenas numeros positivos")
except:
 print("Digite um numero inteiro!!!!!!!!")
else:
 print('Nenhuma ocorrencia encontrada!') 

mediaAluno=calc(nt1,nt2,nt3)
print(mediaAluno)



























# nt1 = float(input("Digite a primeira nota: "))
# nt2 = float(input("Digite a segunda nota: "))
# nt3 = float(input("Digite a terceira nota: "))

# try:
#     if(nt1 > 0 and nt2 > 0 and nt3 > 0):
#      calc = float(nt1+nt2+nt3/3)
#      print(calc)
#     else:
#       print("Apenas numeros")
# except:
#  print("Digite um numero inteiro!!!!!!!!")
# else:
#  print('Nenhuma ocorrencia encontrada!') 
