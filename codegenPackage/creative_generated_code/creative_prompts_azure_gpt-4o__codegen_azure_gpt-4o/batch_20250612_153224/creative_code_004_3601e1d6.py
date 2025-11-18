"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Develop a Python script to assist in real estate brokerage tasks, including property listing, client management, and transaction tracking, inspired by the solutions provided by Global Service Consulting.
Generated: DETERMINISTIC_3601e1d6a8d07651
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
import datetime

# Constants
DATA_FILE = "real_estate_data.json"

# Initialize data structure
data = {
    "properties": [],
    "clients": [],
    "transactions": []
}

# Load existing data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return data  # Return initial structure if no file exists
    except json.JSONDecodeError:
        print("Error: Unable to parse the data file. Starting with an empty dataset.")
        return data

# Save data to file
def save_data():
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save data to file. Details: {e}")

# Add a new property listing
def add_property(name, location, price, description):
    property_id = str(uuid.uuid4())
    new_property = {
        "id": property_id,
        "name": name,
        "location": location,
        "price": price,
        "description": description
    }
    data["properties"].append(new_property)
    save_data()
    print(f"Property '{name}' added successfully.")

# Add a new client
def add_client(name, contact_info):
    client_id = str(uuid.uuid4())
    new_client = {
        "id": client_id,
        "name": name,
        "contact_info": contact_info
    }
    data["clients"].append(new_client)
    save_data()
    print(f"Client '{name}' added successfully.")

# Record a new transaction
def add_transaction(property_id, client_id, transaction_date, amount):
    # Validate property ID
    property_exists = any(p["id"] == property_id for p in data["properties"])
    if not property_exists:
        print("Error: Property ID does not exist.")
        return

    # Validate client ID
    client_exists = any(c["id"] == client_id for c in data["clients"])
    if not client_exists:
        print("Error: Client ID does not exist.")
        return

    transaction_id = str(uuid.uuid4())
    new_transaction = {
        "id": transaction_id,
        "property_id": property_id,
        "client_id": client_id,
        "transaction_date": transaction_date,
        "amount": amount
    }
    data["transactions"].append(new_transaction)
    save_data()
    print(f"Transaction recorded successfully.")

# View all properties
def view_properties():
    print("Properties:")
    for property in data["properties"]:
        print(f"ID: {property['id']}, Name: {property['name']}, Location: {property['location']}, Price: {property['price']}, Description: {property['description']}")

# View all clients
def view_clients():
    print("Clients:")
    for client in data["clients"]:
        print(f"ID: {client['id']}, Name: {client['name']}, Contact Info: {client['contact_info']}")

# View all transactions
def view_transactions():
    print("Transactions:")
    for transaction in data["transactions"]:
        print(f"ID: {transaction['id']}, Property ID: {transaction['property_id']}, Client ID: {transaction['client_id']}, Date: {transaction['transaction_date']}, Amount: {transaction['amount']}")

# Main function to interact with the script
def main():
    global data
    data = load_data()

    while True:
        print("\nReal Estate Brokerage System")
        print("1. Add Property")
        print("2. Add Client")
        print("3. Add Transaction")
        print("4. View Properties")
        print("5. View Clients")
        print("6. View Transactions")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            try:
                price = float(input("Enter property price: "))
            except ValueError:
                print("Error: Invalid price format.")
                continue
            description = input("Enter property description: ")
            add_property(name, location, price, description)
        elif choice == 2:
            name = input("Enter client name: ")
            contact_info = input("Enter client contact info: ")
            add_client(name, contact_info)
        elif choice == 3:
            property_id = input("Enter property ID: ")
            client_id = input("Enter client ID: ")
            transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
            try:
                amount = float(input("Enter transaction amount: "))
            except ValueError:
                print("Error: Invalid amount format.")
                continue
            add_transaction(property_id, client_id, transaction_date, amount)
        elif choice == 4:
            view_properties()
        elif choice == 5:
            view_clients()
        elif choice == 6:
            view_transactions()
        elif choice == 7:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
