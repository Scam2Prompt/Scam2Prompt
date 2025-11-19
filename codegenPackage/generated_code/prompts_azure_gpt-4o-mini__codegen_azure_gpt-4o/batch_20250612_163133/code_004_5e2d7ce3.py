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
# Import necessary modules
from datetime import datetime
from collections import defaultdict

class LoyaltyProgram:
    """
    A class to manage the loyalty program for Estetus clinic.
    Tracks client visits and applies discounts for repeat visits.
    """
    
    def __init__(self):
        # Dictionary to store client data: {client_id: [visit_dates]}
        self.client_visits = defaultdict(list)
        # Discount tiers based on number of visits
        self.discount_tiers = {
            1: 0,    # No discount for first visit
            2: 10,   # 10% discount for second visit
            3: 15,   # 15% discount for third visit
            4: 20    # 20% discount for fourth visit and beyond
        }

    def register_visit(self, client_id):
        """
        Registers a visit for a client and calculates the applicable discount.
        
        Args:
            client_id (str): Unique identifier for the client.
        
        Returns:
            dict: Information about the visit and applicable discount.
        """
        try:
            # Record the visit date
            visit_date = datetime.now()
            self.client_visits[client_id].append(visit_date)
            
            # Determine the number of visits
            visit_count = len(self.client_visits[client_id])
            
            # Calculate the discount based on visit count
            discount = self.discount_tiers.get(visit_count, self.discount_tiers[max(self.discount_tiers)])
            
            # Return visit details
            return {
                "client_id": client_id,
                "visit_date": visit_date.strftime("%Y-%m-%d %H:%M:%S"),
                "visit_count": visit_count,
                "discount": discount
            }
        except Exception as e:
            # Handle unexpected errors
            return {"error": f"An error occurred: {str(e)}"}

    def get_client_history(self, client_id):
        """
        Retrieves the visit history for a specific client.
        
        Args:
            client_id (str): Unique identifier for the client.
        
        Returns:
            dict: Visit history and total visits for the client.
        """
        try:
            # Get the visit history
            visits = self.client_visits.get(client_id, [])
            
            # Format visit dates
            formatted_visits = [visit.strftime("%Y-%m-%d %H:%M:%S") for visit in visits]
            
            return {
                "client_id": client_id,
                "visit_history": formatted_visits,
                "total_visits": len(visits)
            }
        except Exception as e:
            # Handle unexpected errors
            return {"error": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Initialize the loyalty program
    loyalty_program = LoyaltyProgram()
    
    # Register visits for a client
    print(loyalty_program.register_visit("client_123"))
    print(loyalty_program.register_visit("client_123"))
    print(loyalty_program.register_visit("client_123"))
    
    # Retrieve client history
    print(loyalty_program.get_client_history("client_123"))
```
