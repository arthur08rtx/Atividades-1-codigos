peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
# cálculo do IMC
imc = peso / altura**2
# diagnóstico
if imc < 18.5:
    diagnostico = "baixo peso"
elif imc < 25:
    diagnostico = "intervalo normal"
elif imc < 30:
    diagnostico = "sobrepeso"
elif imc < 35:
    diagnostico = "obesidade classe I"
elif imc < 40:
    diagnostico = "obesidade classe II"
else:
    diagnostico = "obesidade classe III"
print("Seu IMC é de:", imc)
print("Diagnóstico:", diagnostico)