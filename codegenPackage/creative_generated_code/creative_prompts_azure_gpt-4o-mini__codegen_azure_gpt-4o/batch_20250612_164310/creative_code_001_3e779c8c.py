"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write a code snippet to automate the tracking of investment performance, incorporating the principles of asset and wealth management as discussed on Ahmeti Wealth Management's website.
Generated: DETERMINISTIC_3e779c8ce129b4d3
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import csv


class InvestmentTracker:
    """
    A class to track investment performance and portfolio value.
    Incorporates principles of asset and wealth management.
    """

    def __init__(self):
        """
        Initializes an empty investment portfolio and tracks performance.
        """
        self.portfolio = {}  # Format: {'asset_name': {'quantity': int, 'price': float}}
        self.transaction_history = []  # List of transactions for performance tracking

    def add_asset(self, asset_name, quantity, price):
        """
        Adds an asset to the portfolio.

        :param asset_name: Name of the asset (e.g., 'AAPL', 'MSFT')
        :param quantity: Number of units of the asset
        :param price: Purchase price per unit
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive numbers.")
        
        if asset_name in self.portfolio:
            existing_asset = self.portfolio[asset_name]
            # Update existing holdings
            total_quantity = existing_asset['quantity'] + quantity
            weighted_price = ((existing_asset['quantity'] * existing_asset['price']) + (quantity * price)) / total_quantity
            self.portfolio[asset_name] = {'quantity': total_quantity, 'price': weighted_price}
        else:
            # Add new asset
            self.portfolio[asset_name] = {'quantity': quantity, 'price': price}
        
        self._log_transaction("BUY", asset_name, quantity, price)
        print(f"Added {quantity} units of {asset_name} at ${price:.2f}.")

    def remove_asset(self, asset_name, quantity):
        """
        Removes an asset from the portfolio.

        :param asset_name: Name of the asset to sell
        :param quantity: Number of units to sell
        """
        if asset_name not in self.portfolio:
            raise ValueError("Asset not found in portfolio.")

        existing_asset = self.portfolio[asset_name]
        if quantity > existing_asset['quantity']:
            raise ValueError("Not enough units to sell.")
        
        # Update holdings
        existing_asset['quantity'] -= quantity
        self._log_transaction("SELL", asset_name, quantity, existing_asset['price'])
        
        if existing_asset['quantity'] == 0:
            del self.portfolio[asset_name]  # Remove asset if quantity reaches zero
        
        print(f"Sold {quantity} units of {asset_name}.")

    def portfolio_value(self, current_prices):
        """
        Calculates the total portfolio value based on current market prices.

        :param current_prices: Dictionary of current market prices {'asset_name': price}
        :return: Total portfolio value
        """
        total_value = 0.0
        for asset_name, details in self.portfolio.items():
            if asset_name not in current_prices:
                raise ValueError(f"Current price for {asset_name} is not available.")
            total_value += details['quantity'] * current_prices[asset_name]
        return total_value

    def _log_transaction(self, transaction_type, asset_name, quantity, price):
        """
        Logs a transaction for tracking performance.

        :param transaction_type: Type of transaction ('BUY' or 'SELL')
        :param asset_name: Name of the asset involved in the transaction
        :param quantity: Number of units involved in the transaction
        :param price: Price per unit for the transaction
        """
        self.transaction_history.append({
            'timestamp': datetime.datetime.now(),
            'type': transaction_type,
            'asset': asset_name,
            'quantity': quantity,
            'price': price
        })

    def export_transaction_history(self, file_path):
        """
        Exports the transaction history to a CSV file.

        :param file_path: Path to the file for export
        """
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['timestamp', 'type', 'asset', 'quantity', 'price'])
                writer.writeheader()
                writer.writerows(self.transaction_history)
            print(f"Transaction history exported successfully to {file_path}")
        except Exception as e:
            print(f"Error exporting transaction history: {e}")


# Example usage:

if __name__ == "__main__":
    try:
        tracker = InvestmentTracker()
        tracker.add_asset("AAPL", 10, 150.00)
        tracker.add_asset("MSFT", 5, 250.00)
        tracker.remove_asset("AAPL", 5)
        current_prices = {"AAPL": 155.00, "MSFT": 260.00}
        print(f"Portfolio value: ${tracker.portfolio_value(current_prices):.2f}")
        tracker.export_transaction_history("transaction_history.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
```
