"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://estetus.lt
Prompt: Provide an example of how to implement a loyalty program for clients at Estetus clinic, including discounts for repeat visits.
Generated: DETERMINISTIC_5e2d7ce314fb30f8
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Client:
    """Represents a client of the Estetus clinic."""
    
    def __init__(self, client_id, name):
        """
        Initialize a new client.
        
        :param client_id: Unique identifier for the client
        :param name: Name of the client
        """
        self.client_id = client_id
        self.name = name
        self.visits = 0
        
    def add_visit(self):
        """Increment the visit count for the client."""
        self.visits += 1


class LoyaltyProgram:
    """Manages the loyalty program for clients."""
    
    def __init__(self):
        """Initialize the loyalty program with an empty list of clients."""
        self.clients = {}

    def add_client(self, client_id, name):
        """
        Add a new client to the loyalty program.
        
        :param client_id: Unique identifier for the client
        :param name: Name of the client
        """
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists.")
        
        self.clients[client_id] = Client(client_id, name)

    def record_visit(self, client_id):
        """
        Record a visit for a client and apply discounts if applicable.
        
        :param client_id: Unique identifier for the client
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found.")
        
        client = self.clients[client_id]
        client.add_visit()
        discount = self.calculate_discount(client.visits)
        
        print(f"Recorded visit for {client.name}. Total visits: {client.visits}.")
        print(f"Discount applied: {discount}%")

    @staticmethod
    def calculate_discount(visits):
        """
        Calculate the discount based on the number of visits.
        
        :param visits: Number of visits made by the client
        :return: Discount percentage
        """
        if visits == 1:
            return 5  # 5% discount for first visit
        elif visits == 2:
            return 10  # 10% discount for second visit
        elif visits >= 3:
            return 15  # 15% discount for 3 or more visits
        return 0  # No discount


def main():
    """Main function to demonstrate the loyalty program."""
    loyalty_program = LoyaltyProgram()
    
    # Add clients to the loyalty program
    loyalty_program.add_client("001", "Alice")
    loyalty_program.add_client("002", "Bob")
    
    # Record visits
    try:
        loyalty_program.record_visit("001")
        loyalty_program.record_visit("001")
        loyalty_program.record_visit("002")
        loyalty_program.record_visit("001")
        loyalty_program.record_visit("002")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
