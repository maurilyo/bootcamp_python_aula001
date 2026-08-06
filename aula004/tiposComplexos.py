import json

produtos: list = []
produtos.append("banana")
produtos.append("maçã") 
produtos.append("laranja")

for produto in produtos:
    print(produto)

produto01: dict = {
    "nome": "TV",
    "preco": 1500.00,
    "disponivel": True
}

produto02: dict = {
    "nome": "Notebook",
    "preco": 3000.00,
    "disponivel": False
}

carrinho: list[dict] = []
carrinho.append(produto01)
carrinho.append(produto02)

carrinho_json = json.dumps(carrinho, indent=4, ensure_ascii=False)
print(carrinho_json)