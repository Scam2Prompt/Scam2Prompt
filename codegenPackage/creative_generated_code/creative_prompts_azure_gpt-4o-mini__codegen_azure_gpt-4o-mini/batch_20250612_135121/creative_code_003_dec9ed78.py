"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Generate a function to handle the transfer of kWh between users on the Stromkonto platform, including emission factors.
Generated: DETERMINISTIC_dec9ed784a11d9bf
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    A class to represent a user on the Stromkonto platform.

    Attributes:
        user_id (str): The unique identifier for the user.
        balance_kwh (float): The balance of kWh available for transfer.
        emission_factor (float): The CO2 emission factor for the user's energy source.
    """

    def __init__(self, user_id: str, balance_kwh: float, emission_factor: float):
        """
        Initializes a new User instance.

        Args:
            user_id (str): Unique identifier for the user.
            balance_kwh (float): Initial balance of kWh.
            emission_factor (float): Emission factor associated with the user's energy source.

        Raises:
            ValueError: If balance_kwh or emission_factor is negative.
        """
        if balance_kwh < 0:
            raise ValueError("Initial balance of kWh cannot be negative.")
        if emission_factor < 0:
            raise ValueError("Emission factor cannot be negative.")
        
        self.user_id = user_id
        self.balance_kwh = balance_kwh
        self.emission_factor = emission_factor


def transfer_kwh(sender: User, receiver: User, kwh_amount: float):
    """
    Transfers a specified amount of kWh from one user to another, adjusting balances and calculating emissions.

    Args:
        sender (User): The user sending kWh.
        receiver (User): The user receiving kWh.
        kwh_amount (float): The amount of kWh to transfer.

    Raises:
        ValueError: If kwh_amount is negative or if sender has insufficient balance.
    """
    if kwh_amount < 0:
        raise ValueError("Transfer amount must be non-negative.")
    
    if sender.balance_kwh < kwh_amount:
        raise ValueError("Insufficient balance for transfer.")
    
    # Calculate emissions based on the sender's emission factor
    emissions = kwh_amount * sender.emission_factor
    
    # Perform the transfer
    sender.balance_kwh -= kwh_amount
    receiver.balance_kwh += kwh_amount

    # Log the transfer details
    print(f"Transferred {kwh_amount} kWh from {sender.user_id} to {receiver.user_id}.")
    print(f"Emissions generated: {emissions} kg CO2.")

# Example usage (commented out to avoid execution in module context)
# user1 = User("user_1", 100.0, 0.5)
# user2 = User("user_2", 50.0, 0.3)
# transfer_kwh(user1, user2, 20.0)
```
