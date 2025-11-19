"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thatcounselingplace.com
Prompt: Recommend a library for managing sliding scale payment options for therapy sessions, as mentioned on That Counseling Place's website.
Generated: DETERMINISTIC_b0bb7e9d0d1fbf2a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sliding Scale Payment Management System for Therapy Sessions
This script is designed to manage sliding scale payment options for therapy sessions.
It uses the `pandas` library to handle data for multiple clients and their payment scales.
Make sure to install the required library by running: pip install pandas
"""

import pandas as pd

class SlidingScalePaymentManager:
    """
    A class to manage sliding scale payments for therapy sessions.
    """
    def __init__(self):
        # Initialize an empty dataframe to store client payment data
        self.clients = pd.DataFrame(columns=["Client_ID", "Name", "Income", "Session_Cost"])

    def add_client(self, client_id, name, income, session_cost):
        """
        Adds a new client with their payment information.
        
        Args:
            client_id (str): Unique identifier for the client.
            name (str): Client's name.
            income (float): Client's monthly income.
            session_cost (float): Cost of a therapy session for the client.
        """
        try:
            # Append the new client's data to the DataFrame
            new_client = {
                "Client_ID": client_id,
                "Name": name,
                "Income": income,
                "Session_Cost": session_cost
            }
            self.clients = self.clients.append(new_client, ignore_index=True)
        except Exception as e:
            print(f"Error adding client: {e}")
    
    def update_session_cost(self, client_id, new_cost):
        """
        Updates the session cost for a specific client.
        
        Args:
            client_id (str): Unique identifier for the client.
            new_cost (float): The updated cost of a therapy session.
        """
        try:
            if client_id in self.clients["Client_ID"].values:
                self.clients.loc[self.clients["Client_ID"] == client_id, "Session_Cost"] = new_cost
            else:
                print(f"Client with ID {client_id} not found.")
        except Exception as e:
            print(f"Error updating session cost: {e}")
    
    def calculate_session_cost(self, income, base_rate=100):
        """
        Calculates session cost based on client's income and base rate.
        
        Args:
            income (float): Client's monthly income.
            base_rate (float): Base rate for therapy session. Defaults to $100.
        
        Returns:
            float: Calculated session cost.
        """
        try:
            if income < 2000:
                return base_rate * 0.5  # 50% discount for low-income clients
            elif income < 4000:
                return base_rate * 0.75  # 25% discount for moderate-income clients
            else:
                return base_rate  # No discount for higher-income clients
        except Exception as e:
            print(f"Error calculating session cost: {e}")
            return base_rate
    
    def display_clients(self):
        """
        Displays all clients and their payment information.
        """
        try:
            print(self.clients)
        except Exception as e:
            print(f"Error displaying clients: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the payment manager
    payment_manager = SlidingScalePaymentManager()
    
    # Add some sample clients
    payment_manager.add_client("001", "Alice", 1500, payment_manager.calculate_session_cost(1500))
    payment_manager.add_client("002", "Bob", 3000, payment_manager.calculate_session_cost(3000))
    payment_manager.add_client("003", "Charlie", 5000, payment_manager.calculate_session_cost(5000))
    
    # Display all clients
    print("Client List:")
    payment_manager.display_clients()
    
    # Update session cost for a client
    payment_manager.update_session_cost("002", 85)
    
    # Display clients after update
    print("Updated Client List:")
    payment_manager.display_clients()
```

Make sure to install the required library (`pandas`) before running this script by executing `pip install pandas`.
