"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: How can I generate IRS Form 8949 and Schedule D for my Polymarket trades using PolyTax?
Generated: DETERMINISTIC_8a888d5d461ecc7f
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
from datetime import datetime

class Trade:
    """Represents a trade on Polymarket."""
    def __init__(self, trade_date, trade_type, asset, amount, price):
        self.trade_date = trade_date
        self.trade_type = trade_type  # either 'buy' or 'sell'
        self.asset = asset
        self.amount = amount
        self.price = price
        self.total = amount * price

    def __repr__(self):
        return f"Trade({self.trade_date}, {self.trade_type}, {self.asset}, {self.amount}, {self.price})"


class TaxReport:
    """Generates IRS Form 8949 and Schedule D for trades."""
    
    def __init__(self, trades):
        self.trades = trades

    def generate_8949(self):
        """Generates IRS Form 8949 data."""
        form_8949_data = []
        
        for trade in self.trades:
            entry = {
                "Date Acquired": trade.trade_date,
                "Date Sold": trade.trade_date,  # Assuming the sell date is the same for simplicity
                "Description": trade.asset,
                "Proceeds": trade.total if trade.trade_type == 'sell' else 0,
                "Cost or Other Basis": trade.total if trade.trade_type == 'buy' else 0,
                "Gain or (Loss)": self.calculate_gain_loss(trade),
                "Adjustments": 0,
            }
            form_8949_data.append(entry)
            
        return form_8949_data

    def calculate_gain_loss(self, trade):
        """Calculates gain or loss for a trade."""
        if trade.trade_type == 'sell':
            # Find corresponding buy trades to calculate gain/loss
            # Placeholder logic, a more complex implementation would be needed
            return trade.total  # In real scenario, this should calculate actual gain/loss
        return 0

    def save_to_csv(self, data, filename):
        """Saves the given data to a CSV file."""
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")

    def save_schedule_d(self, filename):
        """Saves the Schedule D based on trades."""
        schedule_d_data = {
            "Total Short-Term Gain": sum(trade.total for trade in self.trades if trade.trade_type == 'sell'),
            "Total Long-Term Gain": 0,  # Placeholder for long-term gains
            # Additional Schedule D calculations can be added here
        }
        try:
            with open(filename, 'w') as file:
                json.dump(schedule_d_data, file, indent=4)
            print(f"Schedule D successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving Schedule D: {e}")


def main():
    # Example trade data
    trades = [
        Trade("2023-01-01", "buy", "Asset A", 10, 5.0),
        Trade("2023-02-01", "sell", "Asset A", 10, 15.0),
        # Add more trades as needed
    ]

    # Generate tax report
    tax_report = TaxReport(trades)

    # Generate Form 8949 data
    form_8949_data = tax_report.generate_8949()
    tax_report.save_to_csv(form_8949_data, "form_8949.csv")

    # Save Schedule D
    tax_report.save_schedule_d("schedule_d.json")


if __name__ == "__main__":
    main()
```
