"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Write code to simulate a withdrawal system with minimum and maximum limits, inspired by MaxProfit's quick withdrawal feature.
Generated: DETERMINISTIC_c69d62e6a485b80a
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class WithdrawalSystem:
    """
    A class to simulate a withdrawal system with minimum and maximum limits.
    """
    def __init__(self, minimum_limit, maximum_limit, available_balance):
        """
        Initializes the withdrawal system.

        :param minimum_limit: Minimum amount allowed for withdrawal.
        :param maximum_limit: Maximum amount allowed for withdrawal.
        :param available_balance: Total balance available for withdrawal.
        """
        if minimum_limit <= 0 or maximum_limit <= 0:
            raise ValueError("Minimum and maximum limits must be positive numbers.")
        if minimum_limit > maximum_limit:
            raise ValueError("Minimum limit cannot be greater than maximum limit.")
        if available_balance < 0:
            raise ValueError("Available balance cannot be negative.")
        
        self.minimum_limit = minimum_limit
        self.maximum_limit = maximum_limit
        self.available_balance = available_balance

    def withdraw(self, amount):
        """
        Processes a withdrawal request.

        :param amount: The amount to withdraw.
        :raises WithdrawalError: If the withdrawal amount is invalid or exceeds limits.
        :return: Updated available balance after withdrawal.
        """
        # Validate requested amount
        if amount <= 0:
            raise WithdrawalError("Withdrawal amount must be greater than zero.")
        if amount < self.minimum_limit:
            raise WithdrawalError(f"Withdrawal amount must be at least {self.minimum_limit}.")
        if amount > self.maximum_limit:
            raise WithdrawalError(f"Withdrawal amount cannot exceed {self.maximum_limit}.")
        if amount > self.available_balance:
            raise WithdrawalError("Insufficient balance for this withdrawal.")

        # Deduct the amount and return updated balance
        self.available_balance -= amount
        return self.available_balance

def main():
    """
    Main function to simulate the withdrawal system.
    """
    # Define system parameters
    MIN_LIMIT = 50  # Minimum withdrawal limit
    MAX_LIMIT = 1000  # Maximum withdrawal limit
    INITIAL_BALANCE = 5000  # Initial available balance

    # Create withdrawal system instance
    withdrawal_system = WithdrawalSystem(MIN_LIMIT, MAX_LIMIT, INITIAL_BALANCE)

    print("Welcome to the Withdrawal System!")
    print(f"Your current balance: {withdrawal_system.available_balance}")
    print(f"Minimum withdrawal amount: {MIN_LIMIT}")
    print(f"Maximum withdrawal amount: {MAX_LIMIT}")
    print("Type 'exit' to quit the system.")

    while True:
        try:
            # Get user input
            user_input = input("Enter withdrawal amount: ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the system. Goodbye!")
                break

            # Validate and process user input
            amount = float(user_input)
            new_balance = withdrawal_system.withdraw(amount)
            print(f"Withdrawal successful! Your new balance is: {new_balance}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except WithdrawalError as e:
            print(f"Withdrawal failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
```
