"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperhands-checker.pages.dev
Prompt: Write code to calculate the total "paperhanded amount" for a wallet and provide actionable insights to optimize future trading strategies, inspired by the HALO Paperhands feature.
Generated: DETERMINISTIC_d4b58d39bb8c3563
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TradingAnalysis:
    """
    Class to analyze trading data and calculate the paperhanded amount for a wallet.
    """
    def __init__(self, wallet_address, transaction_data):
        """
        Initialize the TradingAnalysis class.
        
        :param wallet_address: The wallet address to analyze.
        :param transaction_data: List of transaction data containing buy/sell events.
        """
        self.wallet_address = wallet_address
        self.transaction_data = transaction_data

    def calculate_paperhanded_amount(self):
        """
        Calculate the total paperhanded amount for the wallet.

        :return: Dictionary containing paperhanded amount and actionable insights.
        """
        paperhanded_amount = 0
        buy_transactions = []

        for transaction in self.transaction_data:
            try:
                # Only process transactions for the specified wallet address
                if transaction['wallet'] == self.wallet_address:
                    if transaction['type'] == 'buy':
                        # Track buy transactions with price and quantity
                        buy_transactions.append(transaction)
                    elif transaction['type'] == 'sell':
                        # Handle sell transactions to calculate paperhanded amount
                        sell_quantity = transaction['quantity']
                        sell_price = transaction['price']

                        # Match sell transactions with earlier buys
                        while sell_quantity > 0 and buy_transactions:
                            buy_transaction = buy_transactions.pop(0)
                            buy_quantity = buy_transaction['quantity']
                            buy_price = buy_transaction['price']
                            
                            # Calculate the paperhanded amount for the current transaction
                            if sell_quantity >= buy_quantity:
                                paperhanded_amount += buy_quantity * max(0, buy_price - sell_price)
                                sell_quantity -= buy_quantity
                            else:
                                paperhanded_amount += sell_quantity * max(0, buy_price - sell_price)
                                buy_transactions.insert(0, {
                                    'quantity': buy_quantity - sell_quantity,
                                    'price': buy_price
                                })
                                sell_quantity = 0
            except KeyError:
                print("Error: Transaction data missing required fields. Skipping transaction.")
            except Exception as e:
                print(f"Unexpected error occurred: {e}. Skipping transaction.")

        # Generate actionable insights based on the paperhanded analysis
        insights = self.generate_actionable_insights(paperhanded_amount)

        return {
            'paperhanded_amount': paperhanded_amount,
            'insights': insights
        }

    def generate_actionable_insights(self, paperhanded_amount):
        """
        Generate actionable insights based on the paperhanded amount.

        :param paperhanded_amount: Total paperhanded amount calculated.
        :return: String containing actionable insights.
        """
        if paperhanded_amount == 0:
            return "Great job! You avoided paperhanding. Keep executing trades strategically."
        elif paperhanded_amount <= 100:
            return "You paperhanded a small amount. Consider holding onto assets longer before selling."
        else:
            return "Significant paperhanding detected. Review your trading strategy to minimize losses."

# Sample transaction data (normally this would come from an external source such as a database or API)
sample_transaction_data = [
    {'wallet': 'abc123', 'type': 'buy', 'quantity': 10, 'price': 50},
    {'wallet': 'abc123', 'type': 'sell', 'quantity': 5, 'price': 45},
    {'wallet': 'abc123', 'type': 'sell', 'quantity': 5, 'price': 40},
    {'wallet': 'xyz789', 'type': 'buy', 'quantity': 15, 'price': 60},
]

# Initialize the analysis for a specific wallet
wallet_address = 'abc123'
analysis = TradingAnalysis(wallet_address, sample_transaction_data)

# Calculate paperhanded amount and actionable insights
result = analysis.calculate_paperhanded_amount()

# Print results
print(json.dumps(result, indent=4))
```
