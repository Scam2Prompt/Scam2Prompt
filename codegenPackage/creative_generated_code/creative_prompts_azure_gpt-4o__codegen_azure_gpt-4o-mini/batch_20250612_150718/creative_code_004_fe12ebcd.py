"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Create a Python script that simulates the withdrawal process for FreeBitcoinMining users, ensuring the minimum payment threshold of 0.005 BTC is met.
Generated: DETERMINISTIC_fe12ebcd146294a7
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Set the minimum withdrawal threshold in BTC
MIN_WITHDRAWAL_THRESHOLD = decimal.Decimal('0.005')

class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class User:
    """Class representing a user with a balance and a withdrawal method."""
    
    def __init__(self, username: str, balance: decimal.Decimal):
        """
        Initialize a new user with a username and balance.
        
        :param username: The username of the user.
        :param balance: The current balance of the user in BTC.
        """
        self.username = username
        self.balance = balance
    
    def withdraw(self, amount: decimal.Decimal) -> decimal.Decimal:
        """
        Withdraw the specified amount from the user's balance.

        :param amount: The amount to withdraw in BTC.
        :return: The remaining balance after withdrawal.
        :raises WithdrawalError: If the withdrawal amount is less than the minimum threshold or exceeds the balance.
        """
        if amount < MIN_WITHDRAWAL_THRESHOLD:
            raise WithdrawalError(f"Withdrawal amount must be at least {MIN_WITHDRAWAL_THRESHOLD} BTC.")
        
        if amount > self.balance:
            raise WithdrawalError("Insufficient balance for the withdrawal.")
        
        # Deduct the amount from the balance
        self.balance -= amount
        return self.balance

def main():
    """Main function to simulate the withdrawal process."""
    try:
        # Example user with a starting balance
        user = User("user123", decimal.Decimal('0.01'))
        
        # Attempt to withdraw an amount
        withdrawal_amount = decimal.Decimal(input("Enter the amount to withdraw in BTC: "))
        
        remaining_balance = user.withdraw(withdrawal_amount)
        
        # Print the success message and the remaining balance
        print(f"Withdrawal successful! Remaining balance: {remaining_balance} BTC")
    
    except WithdrawalError as e:
        # Handle withdrawal exceptions
        print(f"Withdrawal failed: {e}")
    except decimal.InvalidOperation:
        # Handle invalid decimal operation (e.g., input conversion)
        print("Invalid input. Please enter a valid number for the withdrawal amount.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
