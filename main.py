import json
from inventory import InventoryManager
from invoice import Invoice


# ---------- Invoice Helpers ----------

def generate_invoice_id():
    try:
        with open("data/invoices.json", "r") as file:
            data = json.load(file)
            count = len(data)
    except FileNotFoundError:
        count = 0

    return f"INV{count + 1:03d}"


def save_invoice_history(invoice_id, customer, total, date):
    try:
        with open("data/invoices.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[invoice_id] = {
        "customer": customer,
        "total": total,
        "date": date
    }

    with open("data/invoices.json", "w") as file:
        json.dump(data, file, indent=4)


def view_invoice_history():
    try:
        with open("data/invoices.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No invoices found.")
        return

    print("\n--- INVOICE HISTORY ---")
    for inv_id, details in data.items():
        print(
            f"{inv_id} | {details['customer']} | "
            f"{details['date']} | Total: {details['total']}"
        )


# ---------- App Starts Here ----------

inventory = InventoryManager()

while True:
    print("\n===== INVOICE PRO =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Create Invoice")
    print("6. View Invoice History")
    print("7. Exit")

    choice = input("Choose an option: ")

    # -------- Add Product --------
    if choice == "1":
        pid = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        inventory.add_product(pid, name, price, quantity)
        print("✅ Product added successfully")

    # -------- View Inventory --------
    elif choice == "2":
        inventory.show_inventory()

    # -------- Update Product --------
    elif choice == "3":
        pid = input("Product ID to update: ")

        price_input = input("New Price (press Enter to skip): ")
        qty_input = input("New Quantity (press Enter to skip): ")

        price = float(price_input) if price_input else None
        quantity = int(qty_input) if qty_input else None

        inventory.update_product(pid, price=price, quantity=quantity)
        print("✅ Product updated")

    # -------- Delete Product --------
    elif choice == "4":
        pid = input("Product ID to delete: ")
        inventory.delete_product(pid)
        print("✅ Product deleted")

    # -------- Create Invoice --------
    elif choice == "5":
        customer = input("Customer Name: ")
        invoice_id = generate_invoice_id()
        invoice = Invoice(customer)

        while True:
            pid = input("Enter Product ID (or 'done'): ")
            if pid == "done":
                break

            if pid not in inventory.products:
                print("❌ Invalid Product ID")
                continue

            qty = int(input("Quantity: "))
            product = inventory.products[pid]
            invoice.add_item(product, qty)

        invoice.calculate_totals()
        invoice.print_invoice()
        invoice.save_invoice()
        inventory.save_inventory()

        save_invoice_history(
            invoice_id,
            customer,
            invoice.total,
            invoice.date.strftime("%Y-%m-%d %H:%M")
        )

        print(f"🧾 Invoice ID: {invoice_id}")
        print("✅ Invoice saved successfully")

    # -------- Invoice History --------
    elif choice == "6":
        view_invoice_history()

    # -------- Exit --------
    elif choice == "7":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")
