nota = float(input("Digite a nota do aluno: "))
if nota == 10:
    conceito = "Excelente"
elif nota >= 8:
    conceito = "Ótimo"
elif nota >= 7:
    conceito = "Bom"
elif nota >= 5:
    conceito = "Regular"
else:
    conceito = "Insuficiente"
print("O conceito do aluno é:", conceito)