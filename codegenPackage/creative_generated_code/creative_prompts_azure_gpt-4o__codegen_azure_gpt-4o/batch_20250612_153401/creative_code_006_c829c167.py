"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Write a program to manage client accounting data, ensuring fast and accurate responses as outlined by Lund & Kieck’s specialized business units.
Generated: DETERMINISTIC_c829c16738c3a175
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python program for managing client accounting data. It ensures fast and accurate responses using efficient data structures and functionalities.

```python
import os
import json
from datetime import datetime

# Constants
DATA_FILE = "client_data.json"

# Utility function for loading client data from a file
def load_client_data():
    """
    Load client accounting data from a JSON file.
    Returns:
        dict: A dictionary containing client accounting data.
    """
    if not os.path.isfile(DATA_FILE):
        # If the file doesn't exist, return an empty dictionary
        return {}
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading client data: {e}")
        return {}

# Utility function for saving client data to a file
def save_client_data(data):
    """
    Save client accounting data to a JSON file.
    Args:
        data (dict): The client data dictionary to save.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving client data: {e}")

# Function to add a new client
def add_client(client_id, name, balance):
    """
    Add a new client to the accounting system.
    Args:
        client_id (str): Unique identifier for the client.
        name (str): Name of the client.
        balance (float): Initial balance for the client.
    Returns:
        str: Success or error message.
    """
    data = load_client_data()
    if client_id in data:
        return f"Client with ID {client_id} already exists."
    data[client_id] = {
        "name": name,
        "balance": balance,
        "last_updated": datetime.now().isoformat()
    }
    save_client_data(data)
    return f"Client {name} added successfully."

# Function to update a client's balance
def update_balance(client_id, amount):
    """
    Update the balance of an existing client.
    Args:
        client_id (str): Unique identifier for the client.
        amount (float): Amount to add (positive) or subtract (negative) from the balance.
    Returns:
        str: Success or error message.
    """
    data = load_client_data()
    if client_id not in data:
        return f"Client with ID {client_id} not found."
    data[client_id]["balance"] += amount
    data[client_id]["last_updated"] = datetime.now().isoformat()
    save_client_data(data)
    return f"Balance updated successfully for client ID {client_id}."

# Function to retrieve client information
def get_client_info(client_id):
    """
    Retrieve information for a specific client.
    Args:
        client_id (str): Unique identifier for the client.
    Returns:
        dict or str: Client information or error message.
    """
    data = load_client_data()
    if client_id not in data:
        return f"Client with ID {client_id} not found."
    return data[client_id]

# Function to delete a client
def delete_client(client_id):
    """
    Delete a client from the accounting system.
    Args:
        client_id (str): Unique identifier for the client.
    Returns:
        str: Success or error message.
    """
    data = load_client_data()
    if client_id not in data:
        return f"Client with ID {client_id} not found."
    del data[client_id]
    save_client_data(data)
    return f"Client ID {client_id} deleted successfully."

# Main function (CLI for testing purposes)
def main():
    """
    Main function to interact with the client accounting system.
    Provides a simple CLI for managing client data.
    """
    print("Welcome to Lund & Kieck's Client Accounting System")
    while True:
        print("\nOptions:")
        print("1. Add Client")
        print("2. Update Balance")
        print("3. Get Client Info")
        print("4. Delete Client")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            client_id = input("Enter client ID: ")
            name = input("Enter client name: ")
            try:
                balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid balance. Please enter a number.")
                continue
            print(add_client(client_id, name, balance))
        elif choice == "2":
            client_id = input("Enter client ID: ")
            try:
                amount = float(input("Enter amount to update (positive or negative): "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            print(update_balance(client_id, amount))
        elif choice == "3":
            client_id = input("Enter client ID: ")
            info = get_client_info(client_id)
            if isinstance(info, dict):
                print(json.dumps(info, indent=4))
            else:
                print(info)
        elif choice == "4":
            client_id = input("Enter client ID: ")
            print(delete_client(client_id))
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    main()
```
