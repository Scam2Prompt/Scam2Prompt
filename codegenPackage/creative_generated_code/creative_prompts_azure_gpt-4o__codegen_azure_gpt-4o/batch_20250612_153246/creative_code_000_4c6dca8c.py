"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Write a Python script to simulate a deposit system for an online slot game platform, including support for Pulsa-based transactions and a minimum deposit of 10,000 IDR.
Generated: DETERMINISTIC_4c6dca8c36724abf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DepositError(Exception):
    """Custom exception class for deposit-related errors."""
    pass

class SlotGameDepositSystem:
    def __init__(self, min_deposit_amount):
        """
        Initialize the deposit system.
        
        :param min_deposit_amount: Minimum allowed deposit amount in IDR.
        """
        self.min_deposit_amount = min_deposit_amount

    def process_pulsa_deposit(self, user_id, deposit_amount):
        """
        Simulate a Pulsa-based deposit transaction.
        
        :param user_id: ID of the user making the deposit.
        :param deposit_amount: Amount to deposit in IDR.
        :return: Confirmation message if the transaction succeeds.
        :raises DepositError: If deposit amount is less than the minimum allowed.
        """
        if deposit_amount < self.min_deposit_amount:
            raise DepositError(
                f"Deposit amount must be at least {self.min_deposit_amount} IDR. "
                f"Received: {deposit_amount} IDR."
            )
        
        # Simulating deposit transaction (this would involve external systems in a real-world scenario)
        logging.info(f"Processing Pulsa deposit for user {user_id}...")
        logging.info(f"Deposit amount: {deposit_amount} IDR.")
        
        # Transaction is successful
        confirmation_message = (
            f"Deposit successful! User {user_id} has deposited {deposit_amount} IDR using Pulsa."
        )
        logging.info(confirmation_message)
        return confirmation_message

def main():
    """
    Entry point for the deposit simulation script.
    """
    # Initialize the deposit system with a minimum deposit requirement of 10,000 IDR
    deposit_system = SlotGameDepositSystem(min_deposit_amount=10000)
    
    # Example user input (this would typically come from a user interface or API)
    user_id = "user123"
    deposit_amount = 15000  # Change this value to test the minimum deposit condition

    try:
        # Process the user's deposit
        confirmation = deposit_system.process_pulsa_deposit(user_id, deposit_amount)
        print(confirmation)
    except DepositError as e:
        # Handle deposit errors
        logging.error(str(e))
        print(f"Error: {e}")
    except Exception as ex:
        # Handle unexpected errors
        logging.error(f"An unexpected error occurred: {ex}")
        print("An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    main()
```
