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
class StromkontoPlatform:
    def __init__(self):
        # Initialize the users' accounts with their balances (in kWh) and emission factors
        self.accounts = {}

    def add_user(self, user_id, balance=0, emission_factor=0):
        """
        Add a new user to the platform with an initial balance and emission factor.
        
        :param user_id: Unique identifier for the user.
        :param balance: Initial kWh balance for the user (default is 0).
        :param emission_factor: Emission factor (e.g., grams CO2 per kWh) for the user (default is 0).
        """
        if user_id in self.accounts:
            raise ValueError("User ID already exists.")
        self.accounts[user_id] = {
            "balance": balance,
            "emission_factor": emission_factor
        }

    def transfer_kwh(self, sender_id, receiver_id, amount):
        """
        Transfer kWh between two users on the Stromkonto platform while considering emission factors.
        
        :param sender_id: The user ID of the sender.
        :param receiver_id: The user ID of the receiver.
        :param amount: The amount of kWh to transfer.
        :raises ValueError: If any preconditions are violated (e.g., insufficient balance).
        """
        # Validate sender and receiver existence
        if sender_id not in self.accounts:
            raise ValueError(f"Sender {sender_id} does not exist.")
        if receiver_id not in self.accounts:
            raise ValueError(f"Receiver {receiver_id} does not exist.")

        # Validate transfer amount
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        # Check sender's balance
        sender_balance = self.accounts[sender_id]["balance"]
        if sender_balance < amount:
            raise ValueError(f"Sender {sender_id} has insufficient balance.")

        # Perform the transfer
        self.accounts[sender_id]["balance"] -= amount
        self.accounts[receiver_id]["balance"] += amount

        # Calculate weighted emission factor
        sender_emission_factor = self.accounts[sender_id]["emission_factor"]
        receiver_emission_factor = self.accounts[receiver_id]["emission_factor"]
        
        # Update receiver's emission factor based on weighted average
        receiver_total_kwh = self.accounts[receiver_id]["balance"]
        receiver_emission_factor = (
            (receiver_emission_factor * (receiver_total_kwh - amount)) +
            (sender_emission_factor * amount)
        ) / receiver_total_kwh
        self.accounts[receiver_id]["emission_factor"] = receiver_emission_factor

    def get_user(self, user_id):
        """
        Retrieve account information for a specific user.
        
        :param user_id: Unique identifier for the user.
        :return: A dictionary containing the user's balance and emission factor.
        """
        if user_id not in self.accounts:
            raise ValueError(f"User {user_id} does not exist.")
        return self.accounts[user_id]


# Example Usage
if __name__ == "__main__":
    platform = StromkontoPlatform()
    
    # Add users
    platform.add_user("Alice", balance=100, emission_factor=50)
    platform.add_user("Bob", balance=50, emission_factor=20)
    
    # Perform a transfer
    try:
        platform.transfer_kwh("Alice", "Bob", 30)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get user details
    print("Alice:", platform.get_user("Alice"))
    print("Bob:", platform.get_user("Bob"))
```
