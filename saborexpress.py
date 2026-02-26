nome = input("Informe seu nome: ")

novo_item_do_pedido = input(f"{nome}, deseja registrar um novo item no pedido? (S/N): ").upper()
total_pedido = 0

while novo_item_do_pedido == 'S':
    valor_item = float(input("Informe o valor do item (Digite 0 para cancelar): "))

    if valor_item == 0:
        print(f"Pedido de {nome} cancelado")
        break

    if valor_item < 0:
        print("Valor inválido, tente novamente")
        continue

 
    if valor_item > 50:
        print("Item premium")
    elif valor_item > 20 and valor_item <= 50:
        print("Item normal")
    else:
        print("Item econômico")

    total_pedido += valor_item

    novo_item_do_pedido = input(f"{nome}, deseja registrar um novo item no pedido? (S/N): ").upper()

else:
    print(f'Valor total do pedido de {nome}: R${total_pedido:.2f}')
    print("Finalizando...")





