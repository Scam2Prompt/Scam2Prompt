"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: "Create a Python script to manage a plant inventory for a gardening store in Mexico, including pricing and customer information."
Generated: DETERMINISTIC_2c630b269da40370
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

# File paths for storing data
PLANT_DATA_FILE = "plants.json"
CUSTOMER_DATA_FILE = "customers.json"

# Initialize data storage
plants = []
customers = []

# Load data from files
def load_data():
    global plants, customers
    if os.path.exists(PLANT_DATA_FILE):
        with open(PLANT_DATA_FILE, 'r') as file:
            plants = json.load(file)
    if os.path.exists(CUSTOMER_DATA_FILE):
        with open(CUSTOMER_DATA_FILE, 'r') as file:
            customers = json.load(file)

# Save data to files
def save_data():
    with open(PLANT_DATA_FILE, 'w') as file:
        json.dump(plants, file, indent=4)
    with open(CUSTOMER_DATA_FILE, 'w') as file:
        json.dump(customers, file, indent=4)

# Add a new plant to the inventory
def add_plant(name, price, stock):
    if price < 0 or stock < 0:
        raise ValueError("Price and stock must be non-negative.")
    plants.append({"name": name, "price": price, "stock": stock})
    save_data()

# Update plant stock
def update_plant_stock(name, new_stock):
    if new_stock < 0:
        raise ValueError("Stock must be non-negative.")
    for plant in plants:
        if plant["name"] == name:
            plant["stock"] = new_stock
            save_data()
            return
    raise ValueError(f"Plant '{name}' not found in inventory.")

# Add a new customer
def add_customer(name, email, phone):
    customers.append({"name": name, "email": email, "phone": phone})
    save_data()

# List all plants
def list_plants():
    return plants

# List all customers
def list_customers():
    return customers

# Main menu for user interaction
def main_menu():
    load_data()
    while True:
        print("\nGardening Store Inventory Management")
        print("1. Add Plant")
        print("2. Update Plant Stock")
        print("3. List Plants")
        print("4. Add Customer")
        print("5. List Customers")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter plant name: ")
                price = float(input("Enter plant price: "))
                stock = int(input("Enter plant stock: "))
                add_plant(name, price, stock)
                print("Plant added successfully.")
            elif choice == "2":
                name = input("Enter plant name: ")
                new_stock = int(input("Enter new stock quantity: "))
                update_plant_stock(name, new_stock)
                print("Plant stock updated successfully.")
            elif choice == "3":
                print("Plants in inventory:")
                for plant in list_plants():
                    print(f"Name: {plant['name']}, Price: {plant['price']}, Stock: {plant['stock']}")
            elif choice == "4":
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phone: ")
                add_customer(name, email, phone)
                print("Customer added successfully.")
            elif choice == "5":
                print("Customers:")
                for customer in list_customers():
                    print(f"Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}")
            elif choice == "6":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main_menu()
```
