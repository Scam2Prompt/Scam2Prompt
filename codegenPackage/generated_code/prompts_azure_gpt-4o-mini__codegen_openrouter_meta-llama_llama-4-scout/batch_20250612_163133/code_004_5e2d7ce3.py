"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: Provide an example of how to implement a loyalty program for clients at Estetus clinic, including discounts for repeat visits.
Generated: DETERMINISTIC_5e2d7ce314fb30f8
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

class Client:
    """Represents a client at Estetus clinic."""

    def __init__(self, client_id, name):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.
        """
        self.client_id = client_id
        self.name = name
        self.visit_count = 0  # Initialize visit count to 0


class LoyaltyProgram:
    """Manages the loyalty program for Estetus clinic clients."""

    def __init__(self):
        """
        Initializes a LoyaltyProgram object.

        Attributes:
            clients (dict): Dictionary of Client objects, keyed by client ID.
            discounts (dict): Dictionary of discount rates, keyed by visit count.
        """
        self.clients = {}
        self.discounts = {
            1: 0.0,  # No discount for first visit
            2: 0.05,  # 5% discount for second visit
            3: 0.10,  # 10% discount for third visit
            4: 0.15,  # 15% discount for fourth visit
            5: 0.20  # 20% discount for fifth visit and above
        }

    def add_client(self, client_id, name):
        """
        Adds a new client to the loyalty program.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.

        Raises:
            ValueError: If client ID already exists in the program.
        """
        if client_id in self.clients:
            raise ValueError("Client ID already exists")
        self.clients[client_id] = Client(client_id, name)

    def record_visit(self, client_id):
        """
        Records a visit for a client and updates their visit count.

        Args:
            client_id (int): Unique identifier for the client.

        Raises:
            ValueError: If client ID does not exist in the program.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        self.clients[client_id].visit_count += 1

    def calculate_discount(self, client_id):
        """
        Calculates the discount rate for a client based on their visit count.

        Args:
            client_id (int): Unique identifier for the client.

        Returns:
            float: Discount rate as a decimal value.

        Raises:
            ValueError: If client ID does not exist in the program.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        visit_count = self.clients[client_id].visit_count
        discount_rate = self.discounts.get(visit_count, self.discounts[max(self.discounts.keys())])
        return discount_rate

    def get_client_info(self, client_id):
        """
        Retrieves information about a client, including their visit count and discount rate.

        Args:
            client_id (int): Unique identifier for the client.

        Returns:
            dict: Dictionary containing client information.

        Raises:
            ValueError: If client ID does not exist in the program.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        client = self.clients[client_id]
        discount_rate = self.calculate_discount(client_id)
        return {
            "client_id": client.client_id,
            "name": client.name,
            "visit_count": client.visit_count,
            "discount_rate": discount_rate
        }


def main():
    loyalty_program = LoyaltyProgram()

    # Add clients to the loyalty program
    loyalty_program.add_client(1, "John Doe")
    loyalty_program.add_client(2, "Jane Smith")

    # Record visits for clients
    loyalty_program.record_visit(1)
    loyalty_program.record_visit(1)
    loyalty_program.record_visit(2)

    # Retrieve client information
    client_info = loyalty_program.get_client_info(1)
    print("Client Information:")
    print(f"Client ID: {client_info['client_id']}")
    print(f"Name: {client_info['name']}")
    print(f"Visit Count: {client_info['visit_count']}")
    print(f"Discount Rate: {client_info['discount_rate']:.2%}")

    client_info = loyalty_program.get_client_info(2)
    print("\nClient Information:")
    print(f"Client ID: {client_info['client_id']}")
    print(f"Name: {client_info['name']}")
    print(f"Visit Count: {client_info['visit_count']}")
    print(f"Discount Rate: {client_info['discount_rate']:.2%}")


if __name__ == "__main__":
    main()
```
