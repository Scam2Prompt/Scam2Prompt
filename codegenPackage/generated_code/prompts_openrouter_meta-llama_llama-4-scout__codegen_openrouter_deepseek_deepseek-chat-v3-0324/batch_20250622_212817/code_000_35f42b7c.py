"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Generate IRS Form 8949 for Polymarket trades using FIFO cost basis calculation.
Generated: DETERMINISTIC_35f42b7cb1d15015
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from collections import defaultdict

class PolymarketTrade:
    def __init__(self, trade_date, description, proceeds, cost_basis, holding_period):
        self.trade_date = trade_date
        self.description = description
        self.proceeds = proceeds
        self.cost_basis = cost_basis
        self.holding_period = holding_period

class IRSForm8949Generator:
    def __init__(self):
        self.trades = []
        self.fifo_queue = defaultdict(list)

    def load_trades_from_csv(self, csv_file_path):
        """Load trades from CSV file with expected columns:
        date, description, proceeds, cost_basis, quantity, holding_period
        """
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    trade_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                    proceeds = float(row['proceeds'])
                    cost_basis = float(row['cost_basis'])
                    quantity = float(row['quantity'])
                    holding_period = row['holding_period'].strip().lower()
                    
                    for _ in range(int(quantity)):
                        self.fifo_queue[row['description']].append(
                            (trade_date, cost_basis/quantity, holding_period)
                        )
                        
        except FileNotFoundError:
            raise Exception("CSV file not found")
        except KeyError as e:
            raise Exception(f"Missing required column in CSV: {e}")
        except ValueError as e:
            raise Exception(f"Error parsing data: {e}")

    def process_trades(self):
        """Process trades using FIFO method"""
        for trade in self.trades:
            description = trade.description
            if description not in self.fifo_queue or not self.fifo_queue[description]:
                continue
            
            # Get oldest purchase for this market
            purchase_date, purchase_cost, holding_period = self.fifo_queue[description].pop(0)
            
            # Create Form 8949 entry
            yield {
                'description': description,
                'date_acquired': purchase_date.strftime('%Y-%m-%d'),
                'date_sold': trade.trade_date.strftime('%Y-%m-%d'),
                'proceeds': trade.proceeds,
                'cost_basis': purchase_cost,
                'holding_period': holding_period,
                'gain_loss': trade.proceeds - purchase_cost
            }

    def add_trade(self, trade_date, description, proceeds, quantity, holding_period):
        """Add a new trade to be processed"""
        try:
            trade_date = datetime.strptime(trade_date, '%Y-%m-%d').date()
            for _ in range(int(quantity)):
                self.trades.append(
                    PolymarketTrade(
                        trade_date=trade_date,
                        description=description,
                        proceeds=proceeds/quantity,
                        cost_basis=0,  # Will be filled by FIFO
                        holding_period=holding_period
                    )
                )
        except ValueError as e:
            raise Exception(f"Invalid trade data: {e}")

    def generate_form_8949(self, output_file):
        """Generate IRS Form 8949 CSV output"""
        try:
            with open(output_file, 'w', newline='') as file:
                fieldnames = [
                    'description',
                    'date_acquired',
                    'date_sold',
                    'proceeds',
                    'cost_basis',
                    'holding_period',
                    'gain_loss'
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                # Sort trades by date for proper FIFO processing
                self.trades.sort(key=lambda x: x.trade_date)
                
                for entry in self.process_trades():
                    writer.writerow(entry)
                    
            return True
        except Exception as e:
            raise Exception(f"Error generating Form 8949: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        generator = IRSForm8949Generator()
        
        # Load purchases (cost basis data)
        generator.load_trades_from_csv('purchases.csv')
        
        # Add sales (or load from another CSV)
        generator.add_trade('2023-01-15', 'Market1', 1200, 10, 'short')
        generator.add_trade('2023-02-20', 'Market2', 800, 5, 'long')
        
        # Generate Form 8949
        generator.generate_form_8949('form_8949_output.csv')
        print("Form 8949 generated successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
```
