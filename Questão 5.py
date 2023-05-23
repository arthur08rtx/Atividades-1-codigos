codigo = int(input("Digite o código do item pedido: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 100:
    preco = 1.20
    descricao = "Cachorro-quente"
elif codigo == 101:
    preco = 1.30
    descricao = "Bauru"
elif codigo == 102:
    preco = 1.20
    descricao = "Hambúrguer"
elif codigo == 103:
    preco = 1.30
    descricao = "Cheeseburguer"
elif codigo == 104:
    preco = 1.00
    descricao = "Refrigerante"
else:
    print("Código inválido")
    preco = 0
    descricao = ""

total = preco * quantidade

if descricao != "":
    print(f"Você pediu {quantidade} {descricao}(s), que custam {preco:.2f} cada. O total a pagar é {total:.2f}")