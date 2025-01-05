import json

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


def delete_product(index):
    try:
        removed_item = inventory.pop(index-1)
        print(f"{removed_item['name']} is removed from inventory")
    except IndexError:
        print(f"{index} is not a valid index input!")


def check_low_stock(threshold=5):
    low_stock_items = [product for product in inventory if product['quantity'] <= threshold]
    if not low_stock_items:
        print("all products are with sufficient storage")
    else:
        print("Products listed below require replenishment:\n")
        for i, product in enumerate(low_stock_items, start=1):
            print(f"{i}. Name : {product['name']}, Quantity : {product['quantity']}")


def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory,file)
    print("inventory saved to file!")

def load_inventory():
    global inventory
    try:
        with open("inventory.json", 'r') as file:
            inventory = json.load(file)
        print("inventory loaded from file!")
        print('branch2')
    except FileNotFoundError:
        print("No saved inventory found!")

def inventory_summary():
    total_product = len(inventory)
    total_quantity = sum(product['quantity'] for product in inventory)
    total_value = sum(product['quantity'] * product['price'] for product in inventory)
    print(f"Total products : {total_product}, total quantity : {total_quantity}, total_value : {total_value}")


while True:
    print("\nOptions:")
    print("1. View inventory  2.Add item  3.Update item  4.Delete item\n5.Check low stock  6.Save inventory  7.Load inventory  8.Inventory summary  9.Quit")
    choice = input("Please input your number")

    if choice == '1':
        view_inventory()
    elif choice == '2':
        name = None
        quantity = None
        price = None
        if input("Is there a product name?").strip().lower() == "yes":
            name = input("Please input product name:\n")
        if input("Is there a product quantity?").strip().lower() == "yes":
            quantity = input("Please input quantity:\n")
        if input("Is there a product price?").strip().lower() == "yes":
            price = input("Please input price:\n")
        add_product(name, quantity, price)
    elif choice == '3':
        index = int(input('Enter product index being updated:'))
        name = input("Enter product name(leave blank if no name)")
        quantity = input("Enter product quantity(leave blank if no quantity")
        price = input("Enter product price(leave blank if no price")
        update_product(index, name, quantity, price)
    elif choice == 4:
        index = int(input("Enter the index of item to delete"))
        delete_product(index)
    elif choice == 5:
        threshold = int(input("Enter low stock threshold:"))
        check_low_stock(threshold)
    elif choice == 6:
        save_inventory()
    elif choice == 7:
        load_inventory()
    elif choice == 8:
        inventory_summary()
    elif choice == 9:
        print("Thank you for using inventory manager")
        break
    else:
        print("Invalid input, try again")