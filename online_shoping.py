class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, item, quantity):
        if item.stock >= quantity:
            self.cart_items.append((item, quantity))
            item.stock -= quantity

            print(f"{quantity} of {item.name} added in the cart")
        else:
            print("stock not enough")

    def remove_from_cart(self, item):
        for cart_item in self.cart_items:
            if cart_item[0] == item:
                self.cart_items.remove(cart_item)
                item.stock += cart_item[1]
                print(f"{item.name} remove from cart")
                return
        else:
            print(f"{item} not in cart")

    def view_cart(self):
        if not self.cart_items:
            print("cart is empty")
        else:
            print("Items in your cart :")
            for item, quantity in self.cart_items:
                print(f"{item.name} Quantity: {quantity} Price {item.price}")

    def check_out(self):
        total = 0
        if not self.cart_items:
            print("cart is empty")
        else:
            for item, quantity in self.cart_items:
                total += item.price * quantity
                print(f"{item.name} - {quantity} price ${item.price}")
            print(f" Total amount ${total}")


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, stock):
        item = Item(name, price, stock)
        self.items[name] = item

    def display_items(self):
        print("Available items in inventory")
        for name, item in self.items.items():
            print(f"{item.name} Price {item.price} Stock: {item.stock}")

    def get_item(self, name):
        return self.items.get(name)


def main():
    inventory = Inventory()
    cart = Cart()

    inventory.add_item("Laptop", 10000, 2)
    inventory.add_item("Smart Phone", 1000, 10)
    inventory.add_item("Washing Machine", 20000, 5)

    while True:
        print("view inventory, add to cart, remove and so on")
        choice = input("Enter what you want to do: ",).lower()

        if choice == "view inventory":
            inventory.display_items()
        elif choice == "add to cart":
            item_name = input("Enter item name: ")
            item = inventory.get_item(item_name)
            if item:
                quantity = int(input("Enter quantity: "))
                cart.add_to_cart(item, quantity)
            print("Item is not available")
        elif choice == "remove from cart":
            item_name = input("Enter item name: ")
            item = inventory.get_item(item_name)
            if item:
                cart.remove_from_cart(item)
            else:
                print("item not present")
        elif choice == "view cart":
            cart.view_cart()
        elif choice == "checkout":
            cart.check_out()
        elif choice == "exit":
            print("Exit the program")
            break
        else:
            print("Invalid Option, please give valid choice: ")


main()