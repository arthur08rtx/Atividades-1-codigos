distancia = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite a quantidade de combustível gasta (em litros): "))
consumo_medio = distancia / combustivel
print("O consumo médio do automóvel é de", round(consumo_medio, 2), "km/l.")