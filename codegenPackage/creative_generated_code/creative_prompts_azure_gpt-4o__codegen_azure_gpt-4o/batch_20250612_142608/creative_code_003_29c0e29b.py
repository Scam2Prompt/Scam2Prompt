"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointaap.com
Prompt: Create a script to simulate a user’s first crypto trade on a platform like Cointaap, ensuring secure transactions and user guidance.
Generated: DETERMINISTIC_29c0e29b0a7d8b3d
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import secrets
import time

class CryptoTradingPlatform:
    def __init__(self):
        # Simulated database for user accounts and balances
        self.users = {}
        self.crypto_prices = {"BTC": 30000, "ETH": 2000}

    def create_user(self, username, password):
        """
        Create a new user with a username and hashed password.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        # Hash the password for secure storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = {
            "password": hashed_password,
            "balance_usd": 1000,  # Default USD balance
            "crypto_holdings": {"BTC": 0, "ETH": 0}
        }
        print(f"User '{username}' created successfully.")

    def authenticate_user(self, username, password):
        """
        Authenticate a user by verifying their password.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.users[username]["password"] != hashed_password:
            raise ValueError("Invalid password.")
        
        print(f"User '{username}' authenticated successfully.")
        return True

    def simulate_trade(self, username, crypto_symbol, usd_amount):
        """
        Simulate a trade where a user exchanges USD for cryptocurrency.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        
        if crypto_symbol not in self.crypto_prices:
            raise ValueError(f"Invalid cryptocurrency symbol: {crypto_symbol}.")
        
        user = self.users[username]
        if usd_amount > user["balance_usd"]:
            raise ValueError("Insufficient balance.")

        # Calculate the amount of cryptocurrency the user will receive
        crypto_price = self.crypto_prices[crypto_symbol]  # Price per unit
        crypto_amount = usd_amount / crypto_price

        # Deduct USD and add cryptocurrency to user's holdings
        user["balance_usd"] -= usd_amount
        user["crypto_holdings"][crypto_symbol] += crypto_amount

        print(f"Trade successful! You purchased {crypto_amount:.8f} {crypto_symbol} for ${usd_amount:.2f}.")
        return {
            "crypto_symbol": crypto_symbol,
            "crypto_amount": crypto_amount,
            "remaining_balance_usd": user["balance_usd"]
        }

def main():
    """
    Main function to simulate user interaction with the trading platform.
    """
    platform = CryptoTradingPlatform()
    
    # Step 1: Create a user
    try:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        platform.create_user(username, password)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Step 2: Authenticate the user
    try:
        password = input("Re-enter your password to authenticate: ")
        if not platform.authenticate_user(username, password):
            return
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Step 3: Simulate the first trade
    try:
        crypto_symbol = input("Enter the cryptocurrency symbol (e.g., BTC, ETH): ")
        usd_amount = float(input("Enter the amount in USD you want to spend: "))
        trade_result = platform.simulate_trade(username, crypto_symbol, usd_amount)
        print(f"Trade details: {trade_result}")
    except ValueError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
```
