"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a basic understanding of tax-loss harvesting and write a Python function to calculate capital gains and losses for tax purposes.
Generated: DETERMINISTIC_87ff2716b4379523
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TaxLossHarvesting:
    """
    A class to calculate capital gains and losses for tax purposes.
    """

    def __init__(self):
        self.transactions = []

    def add_transaction(self, purchase_price, sale_price, quantity):
        """
        Add a transaction to the list of transactions.

        :param purchase_price: The price at which the asset was purchased.
        :param sale_price: The price at which the asset was sold.
        :param quantity: The number of units of the asset.
        """
        if purchase_price < 0 or sale_price < 0 or quantity <= 0:
            raise ValueError("Prices must be non-negative and quantity must be positive.")
        
        self.transactions.append({
            'purchase_price': purchase_price,
            'sale_price': sale_price,
            'quantity': quantity
        })

    def calculate_gains_losses(self):
        """
        Calculate total capital gains and losses from the transactions.

        :return: A dictionary with total gains and losses.
        """
        total_gain = 0.0
        total_loss = 0.0

        for transaction in self.transactions:
            gain_loss = (transaction['sale_price'] - transaction['purchase_price']) * transaction['quantity']
            if gain_loss > 0:
                total_gain += gain_loss
            else:
                total_loss += abs(gain_loss)

        return {
            'total_gain': total_gain,
            'total_loss': total_loss
        }

    def net_gain_loss(self):
        """
        Calculate the net gain or loss after considering both gains and losses.

        :return: The net gain or loss.
        """
        totals = self.calculate_gains_losses()
        return totals['total_gain'] - totals['total_loss']


# Example usage:
if __name__ == "__main__":
    try:
        tax_harvesting = TaxLossHarvesting()
        tax_harvesting.add_transaction(purchase_price=100, sale_price=150, quantity=10)  # Gain
        tax_harvesting.add_transaction(purchase_price=200, sale_price=150, quantity=5)   # Loss
        tax_harvesting.add_transaction(purchase_price=50, sale_price=75, quantity=20)    # Gain

        gains_losses = tax_harvesting.calculate_gains_losses()
        net_result = tax_harvesting.net_gain_loss()

        print(f"Total Gains: {gains_losses['total_gain']}")
        print(f"Total Losses: {gains_losses['total_loss']}")
        print(f"Net Gain/Loss: {net_result}")

    except ValueError as e:
        print(f"Error: {e}")
```
