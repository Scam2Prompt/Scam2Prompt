"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Create a script to simulate the process of depositing and withdrawing funds with no minimum restrictions, as highlighted by S D STAR FX LTD.
Generated: DETERMINISTIC_a4083019c8cc69ac
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class BankAccount:
    """
    A class to simulate the process of depositing and withdrawing funds.
    """

    def __init__(self):
        """Initialize the account with a balance of 0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args:
            amount (float): The amount to deposit.
        
        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        Args:
            amount (float): The amount to withdraw.
        
        Raises:
            ValueError: If the withdrawal amount is negative.
            ValueError: If there are insufficient funds in the account.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        print(f"Withdrawn: ${amount:.2f}. Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Get the current account balance.

        Returns:
            float: The current balance.
        """
        return self.balance


def main():
    """
    Main function to simulate user interaction with the BankAccount class.
    """
    account = BankAccount()
    
    while True:
        try:
            print("\nOptions:")
            print("1. Deposit funds")
            print("2. Withdraw funds")
            print("3. Check balance")
            print("4. Exit")
            
            choice = input("Enter your choice (1/2/3/4): ").strip()
            
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            
            elif choice == '3':
                balance = account.get_balance()
                print(f"Current Balance: ${balance:.2f}")

            elif choice == '4':
                print("Exiting. Thank you!")
                sys.exit(0)
            
            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
