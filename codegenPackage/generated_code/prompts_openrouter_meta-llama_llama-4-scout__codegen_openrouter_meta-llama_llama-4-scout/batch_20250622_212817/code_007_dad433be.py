"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Generate a sample tax report for Polymarket trading activities, including capital gains and losses.
Generated: DETERMINISTIC_dad433be6acd9c19
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_report_generator.py

import pandas as pd
from datetime import datetime

class Trade:
    """Represents a Polymarket trade."""
    
    def __init__(self, trade_id, date, asset, buy_or_sell, amount, price):
        """
        Initializes a Trade object.

        Args:
            trade_id (int): Unique trade identifier.
            date (str): Date of the trade in 'YYYY-MM-DD' format.
            asset (str): Asset traded.
            buy_or_sell (str): 'buy' or 'sell'.
            amount (float): Amount of asset traded.
            price (float): Price of the asset.
        """
        self.trade_id = trade_id
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.asset = asset
        self.buy_or_sell = buy_or_sell
        self.amount = amount
        self.price = price

class TaxReport:
    """Generates a sample tax report for Polymarket trading activities."""
    
    def __init__(self, trades):
        """
        Initializes a TaxReport object.

        Args:
            trades (list[Trade]): List of Trade objects.
        """
        self.trades = trades
        self.assets = {}
        self.capital_gains = {}
        self.capital_losses = {}

    def calculate_gains_and_losses(self):
        """Calculates capital gains and losses."""
        for trade in self.trades:
            if trade.asset not in self.assets:
                self.assets[trade.asset] = {'buy_price': None, 'amount': 0}

            if trade.buy_or_sell == 'buy':
                self.assets[trade.asset]['amount'] += trade.amount
                if self.assets[trade.asset]['buy_price'] is None:
                    self.assets[trade.asset]['buy_price'] = trade.price
                else:
                    self.assets[trade.asset]['buy_price'] = (self.assets[trade.asset]['buy_price'] * (self.assets[trade.asset]['amount'] - trade.amount) + trade.price * trade.amount) / self.assets[trade.asset]['amount']

            elif trade.buy_or_sell == 'sell':
                if self.assets[trade.asset]['amount'] < trade.amount:
                    raise ValueError(f"Insufficient {trade.asset} to sell")

                self.assets[trade.asset]['amount'] -= trade.amount

                gain_or_loss = trade.price - self.assets[trade.asset]['buy_price']
                if gain_or_loss > 0:
                    asset = trade.asset
                    if asset not in self.capital_gains:
                        self.capital_gains[asset] = 0
                    self.capital_gains[asset] += gain_or_loss * trade.amount
                elif gain_or_loss < 0:
                    asset = trade.asset
                    if asset not in self.capital_losses:
                        self.capital_losses[asset] = 0
                    self.capital_losses[asset] -= gain_or_loss * trade.amount

    def generate_report(self):
        """Generates a sample tax report."""
        self.calculate_gains_and_losses()

        report = []
        for asset in set(list(self.capital_gains.keys()) + list(self.capital_losses.keys())):
            gains = self.capital_gains.get(asset, 0)
            losses = self.capital_losses.get(asset, 0)
            net_gains = gains - losses

            report.append({
                'Asset': asset,
                'Capital Gains': gains,
                'Capital Losses': losses,
                'Net Gains': net_gains
            })

        return pd.DataFrame(report)

def main():
    trades = [
        Trade(1, '2022-01-01', 'Asset A', 'buy', 10, 100),
        Trade(2, '2022-01-15', 'Asset A', 'sell', 5, 120),
        Trade(3, '2022-02-01', 'Asset B', 'buy', 20, 50),
        Trade(4, '2022-03-01', 'Asset B', 'sell', 10, 40),
        Trade(5, '2022-04-01', 'Asset A', 'sell', 5, 110),
    ]

    tax_report = TaxReport(trades)
    report = tax_report.generate_report()
    print(report)

if __name__ == "__main__":
    main()
```
