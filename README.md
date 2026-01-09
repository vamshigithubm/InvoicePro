# InvoicePro 🧾

InvoicePro is a console-based billing and inventory management system built using Python and Object-Oriented Programming (OOP) principles.  
It is designed to help small stores manage products, generate invoices, calculate taxes, and maintain billing history with persistent storage.

---

## 🚀 Features

- Add, view, update, and delete products (CRUD operations)
- Persist inventory data using JSON files
- Create customer invoices with multiple items
- Automatic subtotal, tax, and total calculation
- Auto-generated invoice IDs (INV001, INV002, …)
- Invoice history tracking across sessions
- Save printable invoices as text files
- Clean separation of business logic using OOP

---

## 🛠 Tech Stack

- **Python 3**
- Object-Oriented Programming (OOP)
- File I/O
- JSON for persistence
- Console-based user interface

---

## 📁 Project Structure

InvoicePro/
├── main.py # Application entry point
├── product.py # Product model
├── inventory.py # Inventory management logic
├── invoice.py # Invoice and billing logic
├── README.md
│
├── data/
│ ├── inventory.json # Stored product data
│ └── invoices.json # Invoice history
│
└── invoices/ # Generated invoice text files

yaml
Copy code

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/invoicepro.git
cd invoicepro
Run the application:

bash
Copy code
python main.py

🧠 Design Decisions

OOP Approach:
Real-world entities like Product, Inventory, and Invoice are modeled as classes for clarity and scalability.

JSON Persistence:
Chosen for lightweight, human-readable storage without introducing database complexity.

Separation of Concerns:
Business logic, data models, and user interaction are handled in separate modules.

📌 Learning Outcomes

Built a modular Python application using OOP

Implemented full CRUD functionality

Designed file-based persistence with JSON

Applied real-world business logic (billing, tax, stock updates)

Improved code structure and maintainability

📄 Future Improvements
Add unit tests

Export invoices as CSV/PDF

Convert to REST API using Flask

Integrate database (SQLite/PostgreSQL)

👤 Author
Vamshi Krishna
Junior Python / Full Stack Developer
GitHub: https://github.com/vamshigithubm
