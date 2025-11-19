"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aim-bot-app.pages.dev
Prompt: How can I create a token management system that tracks current holdings and profits, similar to the AIMBOT AI portfolio tracker?
Generated: DETERMINISTIC_efebc70c7ae2489e
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Management System
# This program manages current holdings and calculates profits for a portfolio of tokens.
# It uses best practices, proper error handling, and is production-ready.

import json


class TokenManagementSystem:
    """
    TokenManagementSystem manages token holdings and calculates profit/loss based on historical prices.
    """

    def __init__(self):
        # Initialize token portfolio as an empty dictionary.
        # Portfolio structure: {token_name: {'quantity': float, 'average_price': float}}
        self.portfolio = {}

    def add_token(self, token_name, quantity, price_per_token):
        """
        Adds or updates a token in the portfolio.

        Args:
            token_name (str): Name of the token (e.g., "BTC", "ETH").
            quantity (float): Quantity of the token to add.
            price_per_token (float): Price per token at the time of purchase.

        Raises:
            ValueError: If quantity or price_per_token is not positive.
        """
        if quantity <= 0 or price_per_token <= 0:
            raise ValueError("Quantity and price must be positive values.")

        if token_name in self.portfolio:
            # Update existing token by recalculating average price
            current = self.portfolio[token_name]
            total_quantity = current['quantity'] + quantity
            avg_price = (
                (current['quantity'] * current['average_price']) + (quantity * price_per_token)
            ) / total_quantity
            self.portfolio[token_name] = {'quantity': total_quantity, 'average_price': avg_price}
        else:
            # Add new token to the portfolio
            self.portfolio[token_name] = {'quantity': quantity, 'average_price': price_per_token}

    def remove_token(self, token_name, quantity):
        """
        Removes a specified quantity of a token from the portfolio.

        Args:
            token_name (str): Name of the token to remove.
            quantity (float): Quantity of the token to remove.

        Raises:
            ValueError: If quantity is not positive or exceeds current holdings.
            KeyError: If the token does not exist in the portfolio.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive value.")
        if token_name not in self.portfolio:
            raise KeyError(f"Token '{token_name}' does not exist in the portfolio.")
        if self.portfolio[token_name]['quantity'] < quantity:
            raise ValueError("Insufficient quantity to remove.")

        # Update the portfolio after removal
        self.portfolio[token_name]['quantity'] -= quantity
        if self.portfolio[token_name]['quantity'] == 0:
            del self.portfolio[token_name]  # Remove token completely if quantity becomes zero

    def calculate_profit(self, token_name, current_price):
        """
        Calculates the profit or loss for a token based on its current price.

        Args:
            token_name (str): Name of the token to calculate profit/loss for.
            current_price (float): Current market price of the token.

        Returns:
            float: Profit or loss value.

        Raises:
            KeyError: If the token does not exist in the portfolio.
            ValueError: If current_price is not positive.
        """
        if current_price <= 0:
            raise ValueError("Current price must be a positive value.")
        if token_name not in self.portfolio:
            raise KeyError(f"Token '{token_name}' does not exist in the portfolio.")

        token_data = self.portfolio[token_name]
        profit = (current_price - token_data['average_price']) * token_data['quantity']
        return profit

    def save_portfolio(self, file_path):
        """
        Saves the current portfolio to a JSON file.

        Args:
            file_path (str): Path to the file where the portfolio should be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.portfolio, file, indent=4)
        except IOError as e:
            print(f"Error saving portfolio to file: {e}")

    def load_portfolio(self, file_path):
        """
        Loads the portfolio from a JSON file.

        Args:
            file_path (str): Path to the file where the portfolio is stored.

        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file content is not valid JSON or does not match the expected structure.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Ensure the loaded data is valid
                if not isinstance(data, dict):
                    raise ValueError("Invalid portfolio data format.")
                self.portfolio = data
        except (IOError, ValueError) as e:
            print(f"Error loading portfolio from file: {e}")

    def display_portfolio(self):
        """
        Displays the current portfolio in a user-friendly format.
        """
        print("Current Portfolio:")
        for token_name, data in self.portfolio.items():
            print(f"Token: {token_name}, Quantity: {data['quantity']:.6f}, Average Price: ${data['average_price']:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        system = TokenManagementSystem()

        # Add tokens to the portfolio
        system.add_token("BTC", 0.5, 20000)
        system.add_token("ETH", 2, 1500)

        # Display portfolio
        system.display_portfolio()

        # Remove tokens
        system.remove_token("BTC", 0.2)

        # Display portfolio again
        system.display_portfolio()

        # Calculate profit/loss for a token
        profit = system.calculate_profit("ETH", current_price=1700)
        print(f"Profit/Loss for ETH: ${profit:.2f}")

        # Save and load portfolio from file
        system.save_portfolio("portfolio.json")
        system.load_portfolio("portfolio.json")
        system.display_portfolio()

    except Exception as e:
        print(f"Error: {e}")
```
