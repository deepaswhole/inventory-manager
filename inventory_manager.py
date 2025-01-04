print("welcome to inventory manager")
inventory = []

def add_product(name, quantity, price):
    inventory.append({"name": name, "quantity": quantity, "price":price})
    print(f"Inventory : {name} is added.")


