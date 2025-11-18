"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a Python script to simulate a deposit and withdrawal system for an online casino, integrating instant bank transfer functionality as described on Jackpot Cow Casino's website.
Generated: DETERMINISTIC_4eac063b0cf91a7b
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


class CasinoAccount:
    """
    A class to represent a Casino account for deposit and withdrawal functionality.
    """

    def __init__(self, user_name):
        """
        Initializes the casino account.
        
        :param user_name: Name of the user
        """
        self.user_name = user_name
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the casino account.

        :param amount: Amount to deposit (must be positive)
        :raises ValueError: If the deposit amount is invalid
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposit successful! Your new balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw money from the casino account.

        :param amount: Amount to withdraw (must be positive and <= balance)
        :raises ValueError: If the withdrawal amount is invalid or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrawal successful! Your new balance is ${self.balance:.2f}")

    def show_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Your current balance is ${self.balance:.2f}")


def simulate_casino_account():
    """
    Simulate the deposit and withdrawal system for an online casino.
    """
    print("Welcome to Jackpot Cow Casino!")
    user_name = input("Enter your name to create an account: ").strip()
    user_account = CasinoAccount(user_name)

    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        try:
            if choice == 1:
                amount = float(input("Enter the deposit amount: ").strip())
                user_account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the withdrawal amount: ").strip())
                user_account.withdraw(amount)
            elif choice == 3:
                user_account.show_balance()
            elif choice == 4:
                print("Thank you for using Jackpot Cow Casino. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except ValueError as e:
            print(f"Error: {e}")


# Entry point for the script
if __name__ == "__main__":
    simulate_casino_account()
```
