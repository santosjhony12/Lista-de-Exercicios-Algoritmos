valor = float(input("\nDigite o valor da prestação: "))
taxa = float(input("\nDigite a taxa: "))
tempo = int(input("\nDigite o tempo (número em meses): ")) 
prest = valor+(valor*(taxa/100)*tempo)
print("\nO valor da prestação em atraso é = ", prest)
print("\n")