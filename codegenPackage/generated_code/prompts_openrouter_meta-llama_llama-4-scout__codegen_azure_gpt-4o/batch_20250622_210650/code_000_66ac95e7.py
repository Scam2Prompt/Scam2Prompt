"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Write a Python script to manage accounts payable and receivable for a small business, including tasks like payment tracking and invoice generation, similar to services offered by CG Bókhald.
Generated: DETERMINISTIC_66ac95e7670b4511
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

# Constants for file storage
DATA_FILE = "accounts_data.json"

# Initialize data structure
accounts_data = {
    "payable": [],
    "receivable": []
}

# Load data from file if it exists
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Could not decode JSON data. Starting with empty data.")
    return accounts_data

# Save data to file
def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Could not save data to file. {e}")

# Add a payable entry
def add_payable(description, amount, due_date):
    try:
        accounts_data["payable"].append({
            "description": description,
            "amount": amount,
            "due_date": due_date,
            "status": "Pending"
        })
        save_data(accounts_data)
        print("Payable entry added successfully.")
    except Exception as e:
        print(f"Error: Could not add payable entry. {e}")

# Add a receivable entry
def add_receivable(description, amount, due_date):
    try:
        accounts_data["receivable"].append({
            "description": description,
            "amount": amount,
            "due_date": due_date,
            "status": "Pending"
        })
        save_data(accounts_data)
        print("Receivable entry added successfully.")
    except Exception as e:
        print(f"Error: Could not add receivable entry. {e}")

# Mark an entry as paid
def mark_as_paid(entry_type, index):
    try:
        if entry_type not in ["payable", "receivable"]:
            print("Error: Invalid entry type. Use 'payable' or 'receivable'.")
            return
        if index < 0 or index >= len(accounts_data[entry_type]):
            print("Error: Invalid index.")
            return
        accounts_data[entry_type][index]["status"] = "Paid"
        save_data(accounts_data)
        print(f"{entry_type.capitalize()} entry marked as paid.")
    except Exception as e:
        print(f"Error: Could not mark entry as paid. {e}")

# Generate an invoice for a receivable entry
def generate_invoice(index):
    try:
        if index < 0 or index >= len(accounts_data["receivable"]):
            print("Error: Invalid index.")
            return
        receivable = accounts_data["receivable"][index]
        if receivable["status"] == "Paid":
            print("Error: Cannot generate invoice for a paid receivable.")
            return
        invoice = f"""
        Invoice
        --------
        Description: {receivable['description']}
        Amount: ${receivable['amount']}
        Due Date: {receivable['due_date']}
        Status: {receivable['status']}
        """
        print(invoice)
    except Exception as e:
        print(f"Error: Could not generate invoice. {e}")

# Display all entries
def display_entries():
    try:
        print("\nAccounts Payable:")
        for i, payable in enumerate(accounts_data["payable"]):
            print(f"{i}. {payable['description']} - ${payable['amount']} - Due: {payable['due_date']} - Status: {payable['status']}")
        
        print("\nAccounts Receivable:")
        for i, receivable in enumerate(accounts_data["receivable"]):
            print(f"{i}. {receivable['description']} - ${receivable['amount']} - Due: {receivable['due_date']} - Status: {receivable['status']}")
    except Exception as e:
        print(f"Error: Could not display entries. {e}")

# Main menu
def main():
    global accounts_data
    accounts_data = load_data()
    
    while True:
        print("\nAccounts Management System")
        print("1. Add Payable")
        print("2. Add Receivable")
        print("3. Mark as Paid")
        print("4. Generate Invoice")
        print("5. Display Entries")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_payable(description, amount, due_date)
        elif choice == "2":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_receivable(description, amount, due_date)
        elif choice == "3":
            entry_type = input("Enter entry type (payable/receivable): ")
            index = int(input("Enter index: "))
            mark_as_paid(entry_type, index)
        elif choice == "4":
            index = int(input("Enter receivable index: "))
            generate_invoice(index)
        elif choice == "5":
            display_entries()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
