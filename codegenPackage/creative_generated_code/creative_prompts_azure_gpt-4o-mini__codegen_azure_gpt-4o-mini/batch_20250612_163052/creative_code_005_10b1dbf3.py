"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.org
Prompt: Create a function that simulates the process of connecting a user with an investment education firm through Immediate Peak's platform.
Generated: DETERMINISTIC_10b1dbf356fd660a
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentEducationFirm:
    """Class representing an investment education firm."""
    
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class User:
    """Class representing a user seeking investment education."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

def connect_user_to_firm(user: User, firms: list) -> str:
    """
    Connects a user with a randomly selected investment education firm.
    
    Parameters:
    user (User): The user seeking education.
    firms (list): A list of available investment education firms.
    
    Returns:
    str: A connection message with the firm's details or an error message.
    
    Raises:
    ValueError: If no firms are provided.
    """
    if not firms:
        logging.error("No firms available for connection.")
        raise ValueError("No investment education firms available for connection.")
    
    # Randomly select a firm from the list
    firm = random.choice(firms)
    
    # Log the connection attempt
    logging.info(f"Connecting user {user.name} to firm {firm.name}.")
    
    # Simulate sending a connection email (this is just a log for the purpose of this simulation)
    logging.info(f"Sending connection email to {user.email} with firm details: {firm.name} - {firm.contact_info}.")
    
    return f"Successfully connected {user.name} with {firm.name}.\nContact Info: {firm.contact_info}"

def main():
    # Sample investment education firms
    firms = [
        InvestmentEducationFirm("Wealth Builders", "contact@wealthbuilders.com"),
        InvestmentEducationFirm("Investment Insights", "info@investmentinsights.com"),
        InvestmentEducationFirm("Finance Futures", "support@financefutures.com")
    ]
    
    # Sample user
    user = User("John Doe", "johndoe@example.com")
    
    try:
        # Attempt to connect the user with a firm
        connection_message = connect_user_to_firm(user, firms)
        print(connection_message)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
