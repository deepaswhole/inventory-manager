print("welcome to inventory manager")
inventory = []

def add_product(name, quantity, price):
    inventory.append({"name": name, "quantity": quantity, "price":price})
    print(f"Inventory : {name} is added.")

def view_inventory():
    if not inventory:
        print("empty inventory")
    else:
        for i, product in enumerate(inventory,1):
            print(f"{i}, Name :{product['name']}, Quantity: {product['quantity']}, Price : {product['price']}")


def update_product(index, name=None, quantity=None, price=None):
    try:
        if name:
            inventory[index-1]['name'] = name
        if quantity:
            inventory[index-1]['quantity'] = quantity
        if price:
            inventory[index-1][quantity] = price
        print(f"Product at index{index} updated!")
    except IndexError:
        print(f"{index} is not a valid index input")