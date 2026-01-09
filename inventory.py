import json
from product import Product


class InventoryManager:
    def __init__(self):
        self.products = {}
        self.load_inventory()

    def add_product(self, product_id, name, price, quantity):
        product = Product(name, price, quantity)
        self.products[product_id] = product
        self.save_inventory()

    def show_inventory(self):
        print("\n--- INVENTORY ---")
        for pid, product in self.products.items():
            print(
                f"ID: {pid}, Name: {product.name}, "
                f"Price: {product.price}, Stock: {product.quantity}"
            )

    def load_inventory(self):
        try:
            with open("data/inventory.json", "r") as file:
                data = json.load(file)
                for pid, details in data.items():
                    product = Product(
                        details["name"],
                        details["price"],
                        details["quantity"]
                    )
                    self.products[pid] = product
        except FileNotFoundError:
            self.products = {}

    def save_inventory(self):
        data = {}
        for pid, product in self.products.items():
            data[pid] = {
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }

        with open("data/inventory.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def update_product(self, product_id, price=None, quantity=None):
        if product_id not in self.products:
            print("Product not found")
            return

        product = self.products[product_id]

        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity

        self.save_inventory()
    
    def delete_product(self, product_id):
        if product_id not in self.products:
            print("Product not found")
            return

        del self.products[product_id]
        self.save_inventory()
