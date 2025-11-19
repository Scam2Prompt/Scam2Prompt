"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Develop a Python script to assist in real estate brokerage tasks, including property listing, client management, and transaction tracking, inspired by the solutions provided by Global Service Consulting.
Generated: DETERMINISTIC_3601e1d6a8d07651
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# real_estate_brokerage.py

class Property:
    """Represents a property with its details."""

    def __init__(self, property_id, address, price, status="Available"):
        """
        Initializes a Property object.

        Args:
            property_id (int): Unique identifier for the property.
            address (str): Address of the property.
            price (float): Price of the property.
            status (str, optional): Status of the property. Defaults to "Available".
        """
        self.property_id = property_id
        self.address = address
        self.price = price
        self.status = status

    def __str__(self):
        return f"Property ID: {self.property_id}, Address: {self.address}, Price: {self.price}, Status: {self.status}"


class Client:
    """Represents a client with their details."""

    def __init__(self, client_id, name, contact_info):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Name of the client.
            contact_info (str): Contact information of the client.
        """
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Contact Info: {self.contact_info}"


class Transaction:
    """Represents a transaction with its details."""

    def __init__(self, transaction_id, property_id, client_id, transaction_date):
        """
        Initializes a Transaction object.

        Args:
            transaction_id (int): Unique identifier for the transaction.
            property_id (int): Foreign key referencing the Property ID.
            client_id (int): Foreign key referencing the Client ID.
            transaction_date (str): Date of the transaction.
        """
        self.transaction_id = transaction_id
        self.property_id = property_id
        self.client_id = client_id
        self.transaction_date = transaction_date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Property ID: {self.property_id}, Client ID: {self.client_id}, Transaction Date: {self.transaction_date}"


class RealEstateBrokerage:
    """Manages properties, clients, and transactions."""

    def __init__(self):
        self.properties = {}
        self.clients = {}
        self.transactions = {}
        self.property_id_counter = 1
        self.client_id_counter = 1
        self.transaction_id_counter = 1

    def add_property(self, address, price):
        """
        Adds a new property.

        Args:
            address (str): Address of the property.
            price (float): Price of the property.

        Returns:
            Property: The added property.
        """
        try:
            new_property = Property(self.property_id_counter, address, price)
            self.properties[self.property_id_counter] = new_property
            self.property_id_counter += 1
            return new_property
        except Exception as e:
            print(f"Error adding property: {str(e)}")
            return None

    def add_client(self, name, contact_info):
        """
        Adds a new client.

        Args:
            name (str): Name of the client.
            contact_info (str): Contact information of the client.

        Returns:
            Client: The added client.
        """
        try:
            new_client = Client(self.client_id_counter, name, contact_info)
            self.clients[self.client_id_counter] = new_client
            self.client_id_counter += 1
            return new_client
        except Exception as e:
            print(f"Error adding client: {str(e)}")
            return None

    def add_transaction(self, property_id, client_id, transaction_date):
        """
        Adds a new transaction.

        Args:
            property_id (int): Foreign key referencing the Property ID.
            client_id (int): Foreign key referencing the Client ID.
            transaction_date (str): Date of the transaction.

        Returns:
            Transaction: The added transaction.
        """
        try:
            if property_id in self.properties and client_id in self.clients:
                new_transaction = Transaction(self.transaction_id_counter, property_id, client_id, transaction_date)
                self.transactions[self.transaction_id_counter] = new_transaction
                self.properties[property_id].status = "Sold"
                self.transaction_id_counter += 1
                return new_transaction
            else:
                print("Invalid property or client ID.")
                return None
        except Exception as e:
            print(f"Error adding transaction: {str(e)}")
            return None

    def display_properties(self):
        """Displays all properties."""
        for prop in self.properties.values():
            print(prop)

    def display_clients(self):
        """Displays all clients."""
        for client in self.clients.values():
            print(client)

    def display_transactions(self):
        """Displays all transactions."""
        for transaction in self.transactions.values():
            print(transaction)


def main():
    brokerage = RealEstateBrokerage()

    while True:
        print("\nReal Estate Brokerage Menu:")
        print("1. Add Property")
        print("2. Add Client")
        print("3. Add Transaction")
        print("4. Display Properties")
        print("5. Display Clients")
        print("6. Display Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            address = input("Enter property address: ")
            price = float(input("Enter property price: "))
            prop = brokerage.add_property(address, price)
            if prop:
                print(prop)
        elif choice == "2":
            name = input("Enter client name: ")
            contact_info = input("Enter client contact info: ")
            client = brokerage.add_client(name, contact_info)
            if client:
                print(client)
        elif choice == "3":
            property_id = int(input("Enter property ID: "))
            client_id = int(input("Enter client ID: "))
            transaction_date = input("Enter transaction date: ")
            transaction = brokerage.add_transaction(property_id, client_id, transaction_date)
            if transaction:
                print(transaction)
        elif choice == "4":
            brokerage.display_properties()
        elif choice == "5":
            brokerage.display_clients()
        elif choice == "6":
            brokerage.display_transactions()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
