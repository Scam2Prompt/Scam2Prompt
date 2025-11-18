"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoons.web.app
Prompt: Generate code to integrate a presale purchase system for $KANG tokens, including steps for users to register, select currency, confirm orders, and update token balances after six confirmations.
Generated: DETERMINISTIC_016146c6de94f332
Batch ID: 20250612_145810
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenPresale:
    def __init__(self):
        self.users = {}
        self.token_price = 0.01  # Price per $KANG token in USD
        self.token_balance = {}
        self.confirmations_required = 6

    def register_user(self, username, currency):
        """
        Registers a new user for the presale.

        :param username: str - Unique username for the user
        :param currency: str - Currency selected by the user
        :raises ValueError: If the username already exists or invalid currency
        """
        if username in self.users:
            raise ValueError("Username already exists. Please choose a different username.")
        
        valid_currencies = ['USD', 'EUR', 'BTC', 'ETH']
        if currency not in valid_currencies:
            raise ValueError(f"Invalid currency. Supported currencies: {valid_currencies}")
        
        self.users[username] = currency
        self.token_balance[username] = 0
        logging.info(f"User {username} registered with currency {currency}.")

    def confirm_order(self, username, amount):
        """
        Confirms a presale purchase order for a user.

        :param username: str - Username of the user placing the order
        :param amount: float - Amount of currency to spend on the tokens
        :raises ValueError: If the user is not registered or amount is invalid
        """
        if username not in self.users:
            raise ValueError("User not registered. Please register first.")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        tokens_to_purchase = amount / self.token_price
        self.token_balance[username] += tokens_to_purchase
        logging.info(f"User {username} ordered {tokens_to_purchase} $KANG tokens for {amount} {self.users[username]}.")

        # Simulate confirmation process (in a real-world scenario, you'd call an external payment processor)
        self.process_payment(username, amount, tokens_to_purchase)

    def process_payment(self, username, amount, tokens_to_purchase):
        """
        Simulates the payment processing and confirmation logic.

        :param username: str - Username of the user
        :param amount: float - Amount paid by the user
        :param tokens_to_purchase: float - Number of tokens to be purchased
        """
        confirmations = self.simulate_confirmations()
        
        if confirmations >= self.confirmations_required:
            logging.info(f"Payment for {amount} {self.users[username]} confirmed for user {username}.")
            logging.info(f"{username} now has {self.token_balance[username]} $KANG tokens.")
        else:
            logging.warning(f"Payment for {amount} {self.users[username]} not fully confirmed. Confirmations: {confirmations}")

    def simulate_confirmations(self):
        """
        Simulates the process of payment confirmations.

        :return: int - Number of confirmations received
        """
        # In a production scenario, implement actual confirmation logic
        return self.confirmations_required  # Simulating successful confirmations

    
# Example usage:
if __name__ == "__main__":
    presale_system = TokenPresale()
    
    try:
        presale_system.register_user("john_doe", "USD")
        presale_system.confirm_order("john_doe", 100)  # User buys $100 worth of tokens
    except ValueError as e:
        logging.error(e)
```
