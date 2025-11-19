"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptocode-pro.com
Prompt: Describe the process of creating a demo trading account with Crypto code and provide a sample code for simulating trades without financial risk.
Generated: DETERMINISTIC_c9d8f04bfa8f4c61
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random
import time

class DemoTradingAccount:
    """
    A class to represent a demo trading account for cryptocurrency trading.
    This simulates trades without financial risk.
    """
    
    def __init__(self, initial_balance=10000.0):
        """
        Initialize the demo trading account with an initial balance.
        
        :param initial_balance: The starting balance of the account, default is 10000.0
        """
        self.balance = initial_balance
        self.portfolio = {}  # To track owned cryptocurrencies and their quantities
    
    def get_balance(self):
        """
        Get the current account balance.
        
        :return: The account balance as a float
        """
        return self.balance
    
    def buy_crypto(self, crypto_name, amount, price_per_unit):
        """
        Simulate buying cryptocurrency.
        
        :param crypto_name: Name of the cryptocurrency
        :param amount: Amount of cryptocurrency to buy
        :param price_per_unit: Price per unit of the cryptocurrency
        """
        total_cost = amount * price_per_unit
        if total_cost > self.balance:  # Insufficient funds check
            print("Insufficient funds to complete this purchase.")
            return
        
        self.balance -= total_cost  # Deduct cost from balance
        if crypto_name in self.portfolio:
            self.portfolio[crypto_name] += amount
        else:
            self.portfolio[crypto_name] = amount
        print(f"Bought {amount} {crypto_name} at {price_per_unit} per unit. Total cost: {total_cost}.")
    
    def sell_crypto(self, crypto_name, amount, price_per_unit):
        """
        Simulate selling cryptocurrency.
        
        :param crypto_name: Name of the cryptocurrency
        :param amount: Amount of cryptocurrency to sell
        :param price_per_unit: Price per unit of the cryptocurrency
        """
        if crypto_name not in self.portfolio or self.portfolio[crypto_name] < amount:
            print("Insufficient cryptocurrency holdings to complete this sale.")
            return
        
        total_earnings = amount * price_per_unit
        self.balance += total_earnings  # Add earnings to balance
        self.portfolio[crypto_name] -= amount
        if self.portfolio[crypto_name] == 0:
            del self.portfolio[crypto_name]  # Remove crypto from portfolio if quantity is zero
        print(f"Sold {amount} {crypto_name} at {price_per_unit} per unit. Total earnings: {total_earnings}.")
    
    def view_portfolio(self):
        """
        View the current portfolio holdings.
        
        :return: None
        """
        print("Portfolio:")
        for crypto, quantity in self.portfolio.items():
            print(f"{crypto}: {quantity}")
    
    def simulate_market(self, crypto_name):
        """
        Simulate random market prices for a cryptocurrency.
        
        :param crypto_name: Name of the cryptocurrency
        :return: A simulated price per unit as a float
        """
        return round(random.uniform(1.0, 100.0), 2)  # Random price between $1 and $100


# Main function to demonstrate the demo trading account
def main():
    account = DemoTradingAccount(initial_balance=10000.0)  # Create demo account
    
    while True:
        print("\n--- Demo Trading Account ---")
        print("1. View balance")
        print("2. View portfolio")
        print("3. Buy cryptocurrency")
        print("4. Sell cryptocurrency")
        print("5. Simulate market price")
        print("6. Exit")
        user_choice = input("Choose an option (1-6): ")
        
        if user_choice == "1":
            # View balance
            print(f"Current balance: ${account.get_balance():.2f}")
        
        elif user_choice == "2":
            # View portfolio
            account.view_portfolio()
        
        elif user_choice == "3":
            # Buy cryptocurrency
            crypto_name = input("Enter cryptocurrency name: ")
            try:
                amount = float(input("Enter amount to buy: "))
                price_per_unit = account.simulate_market(crypto_name)
                account.buy_crypto(crypto_name, amount, price_per_unit)
            except ValueError:
                print("Invalid input. Amount should be a number.")
        
        elif user_choice == "4":
            # Sell cryptocurrency
            crypto_name = input("Enter cryptocurrency name: ")
            try:
                amount = float(input("Enter amount to sell: "))
                price_per_unit = account.simulate_market(crypto_name)
                account.sell_crypto(crypto_name, amount, price_per_unit)
            except ValueError:
                print("Invalid input. Amount should be a number.")
        
        elif user_choice == "5":
            # Simulate market price for a cryptocurrency
            crypto_name = input("Enter cryptocurrency name: ")
            simulated_price = account.simulate_market(crypto_name)
            print(f"Simulated market price for {crypto_name}: ${simulated_price:.2f}")
        
        elif user_choice == "6":
            # Exit program
            print("Exiting Demo Trading Account. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")
        
        # Pause for a moment for better user experience
        time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()
```
