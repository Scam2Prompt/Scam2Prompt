"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a Python script to manage moving services for a company like Antalya Şehir İçi Nakliye, including customer information and moving details.
Generated: DETERMINISTIC_7d1e5f2f5352083c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# moving_services.py

class Customer:
    """Represents a customer with their information."""

    def __init__(self, customer_id, name, phone_number, address):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            address (str): Customer's address.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.address = address


class Move:
    """Represents a move with its details."""

    def __init__(self, move_id, customer, move_date, from_address, to_address, services):
        """
        Initializes a Move object.

        Args:
            move_id (int): Unique identifier for the move.
            customer (Customer): Customer associated with the move.
            move_date (str): Date of the move.
            from_address (str): Address to move from.
            to_address (str): Address to move to.
            services (list): List of services required for the move.
        """
        self.move_id = move_id
        self.customer = customer
        self.move_date = move_date
        self.from_address = from_address
        self.to_address = to_address
        self.services = services


class MovingService:
    """Manages customer information and moving details."""

    def __init__(self):
        """Initializes the MovingService with empty data."""
        self.customers = {}
        self.moves = {}

    def add_customer(self, customer_id, name, phone_number, address):
        """
        Adds a new customer.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            address (str): Customer's address.

        Raises:
            ValueError: If customer_id already exists.
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer_id] = Customer(customer_id, name, phone_number, address)

    def add_move(self, move_id, customer_id, move_date, from_address, to_address, services):
        """
        Adds a new move.

        Args:
            move_id (int): Unique identifier for the move.
            customer_id (int): ID of the customer associated with the move.
            move_date (str): Date of the move.
            from_address (str): Address to move from.
            to_address (str): Address to move to.
            services (list): List of services required for the move.

        Raises:
            ValueError: If customer_id or move_id already exists.
            KeyError: If customer_id does not exist in customers.
        """
        if move_id in self.moves:
            raise ValueError("Move ID already exists")
        if customer_id not in self.customers:
            raise KeyError("Customer ID does not exist")
        self.moves[move_id] = Move(move_id, self.customers[customer_id], move_date, from_address, to_address, services)

    def get_customer(self, customer_id):
        """
        Retrieves a customer by their ID.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: The customer object if found, otherwise None.
        """
        return self.customers.get(customer_id)

    def get_move(self, move_id):
        """
        Retrieves a move by its ID.

        Args:
            move_id (int): ID of the move to retrieve.

        Returns:
            Move: The move object if found, otherwise None.
        """
        return self.moves.get(move_id)

    def __str__(self):
        """Returns a string representation of the MovingService."""
        customers_str = "\n".join([f"ID: {customer.customer_id}, Name: {customer.name}" for customer in self.customers.values()])
        moves_str = "\n".join([f"ID: {move.move_id}, Customer ID: {move.customer.customer_id}, Date: {move.move_date}" for move in self.moves.values()])
        return f"Customers:\n{customers_str}\n\nMoves:\n{moves_str}"


def main():
    try:
        service = MovingService()

        # Add customers
        service.add_customer(1, "John Doe", "1234567890", "Antalya")
        service.add_customer(2, "Jane Doe", "9876543210", "Istanbul")

        # Add moves
        service.add_move(1, 1, "2024-09-20", "Antalya", "Istanbul", ["Packing", "Transportation"])
        service.add_move(2, 2, "2024-09-25", "Istanbul", "Ankara", ["Packing", "Loading", "Transportation"])

        # Print customers and moves
        print(service)

        # Retrieve customer and move
        customer = service.get_customer(1)
        move = service.get_move(1)

        if customer:
            print(f"\nCustomer {customer.customer_id}: {customer.name}")
        else:
            print("\nCustomer not found")

        if move:
            print(f"\nMove {move.move_id}:")
            print(f"Customer ID: {move.customer.customer_id}")
            print(f"Date: {move.move_date}")
            print(f"From: {move.from_address}")
            print(f"To: {move.to_address}")
            print(f"Services: {', '.join(move.services)}")
        else:
            print("\nMove not found")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
