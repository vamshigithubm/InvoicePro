from datetime import datetime


class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity


class Invoice:
    TAX_RATE = 0.18

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.date = datetime.now()

    def add_item(self, product, quantity):
        if quantity > product.quantity:
            print("❌ Not enough stock")
            return

        product.quantity -= quantity
        item = InvoiceItem(product, quantity)
        self.items.append(item)

    def calculate_totals(self):
        self.subtotal = 0
        for item in self.items:
            self.subtotal += item.total_price

        self.tax = self.subtotal * self.TAX_RATE
        self.total = self.subtotal + self.tax

    def print_invoice(self):
        print("\n========== INVOICE ==========")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M')}")
        print("-----------------------------")

        for item in self.items:
            print(
                f"{item.product.name} x {item.quantity} = {item.total_price}"
            )

        print("-----------------------------")
        print(f"Subtotal: {self.subtotal}")
        print(f"Tax: {self.tax}")
        print(f"Total: {self.total}")
        print("=============================")

    def save_invoice(self):
        filename = f"invoices/{self.customer_name}_{self.date.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as file:
            file.write("========== INVOICE ==========\n")
            file.write(f"Customer: {self.customer_name}\n")
            file.write(f"Date: {self.date}\n\n")

            for item in self.items:
                file.write(
                    f"{item.product.name} x {item.quantity} = {item.total_price}\n"
                )

            file.write(f"\nSubtotal: {self.subtotal}\n")
            file.write(f"Tax: {self.tax}\n")
            file.write(f"Total: {self.total}\n")
