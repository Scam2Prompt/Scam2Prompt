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
from datetime import datetime

class LoyaltyProgram:
    """
    A class to manage the loyalty program for Estetus clinic clients.
    Includes functionality for tracking visits and applying discounts for repeat visits.
    """
    
    def __init__(self):
        # Initialize a dictionary to store client data
        # Each key is a client ID, and the value is a dictionary with visit count and other details
        self.clients = {}

    def register_visit(self, client_id):
        """
        Register a client's visit and apply discounts based on their loyalty tier.
        
        Args:
            client_id (str): Unique identifier for the client.
        
        Returns:
            dict: Information about the visit, including applied discount and total visits.
        """
        # If the client is new, initialize their record
        if client_id not in self.clients:
            self.clients[client_id] = {
                "visit_count": 0,
                "last_visit_date": None
            }
        
        client_data = self.clients[client_id]
        
        # Update visit count and store the current visit date
        client_data["visit_count"] += 1
        client_data["last_visit_date"] = datetime.now()

        # Determine discount based on number of visits
        discount = self.calculate_discount(client_data["visit_count"])

        return {
            "message": f"Visit registered successfully for client {client_id}.",
            "visit_count": client_data["visit_count"],
            "discount": discount,
            "last_visit_date": client_data["last_visit_date"]
        }

    def calculate_discount(self, visit_count):
        """
        Calculate the discount based on the number of visits.
        
        Args:
            visit_count (int): Count of past visits for the client.
        
        Returns:
            float: Discount percentage applicable for the visit.
        """
        # Define discount tiers
        if visit_count >= 10:
            return 20.0  # 20% discount for 10 or more visits
        elif visit_count >= 5:
            return 10.0  # 10% discount for 5-9 visits
        elif visit_count >= 3:
            return 5.0   # 5% discount for 3-4 visits
        else:
            return 0.0   # No discount for fewer than 3 visits

    def get_client_info(self, client_id):
        """
        Retrieve information about a specific client.
        
        Args:
            client_id (str): Unique identifier for the client.
        
        Returns:
            dict: Information about the client's visits.
        """
        if client_id not in self.clients:
            return {"error": f"Client {client_id} not found in the loyalty program."}
        
        return self.clients[client_id]

# Example usage
if __name__ == "__main__":
    # Create an instance of the loyalty program
    loyalty_program = LoyaltyProgram()
    
    # Register visits for a client
    print(loyalty_program.register_visit("client123"))
    print(loyalty_program.register_visit("client123"))
    print(loyalty_program.register_visit("client123"))
    print(loyalty_program.register_visit("client123"))
    
    # Fetch client information
    print(loyalty_program.get_client_info("client123"))
```
