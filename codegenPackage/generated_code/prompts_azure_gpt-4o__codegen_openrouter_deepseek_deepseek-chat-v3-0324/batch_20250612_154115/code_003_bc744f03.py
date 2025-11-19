"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Create a program that calculates capital gains and losses for Polymarket trades, distinguishing between short-term and long-term gains, and outputs IRS-compliant tax documents, as described on https://polymarket.tax.
Generated: DETERMINISTIC_bc744f039775dbd1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional

class PolymarketTrade:
    """Represents a single Polymarket trade."""
    
    def __init__(self, trade_id: str, market: str, outcome: str, 
                 quantity: float, price: float, fee: float, 
                 timestamp: datetime, trade_type: str):
        self.trade_id = trade_id
        self.market = market
        self.outcome = outcome
        self.quantity = quantity
        self.price = price
        self.fee = fee
        self.timestamp = timestamp
        self.trade_type = trade_type  # 'BUY' or 'SELL'
    
    @property
    def cost_basis(self) -> float:
        """Calculate the total cost basis for this trade."""
        return (self.quantity * self.price) + self.fee

class PolymarketTaxCalculator:
    """Calculates capital gains/losses from Polymarket trades."""
    
    SHORT_TERM_DAYS = 365
    
    def __init__(self):
        self.trades: List[PolymarketTrade] = []
    
    def load_trades_from_csv(self, file_path: str) -> None:
        """Load trades from a CSV file."""
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        trade = PolymarketTrade(
                            trade_id=row['trade_id'],
                            market=row['market'],
                            outcome=row['outcome'],
                            quantity=float(row['quantity']),
                            price=float(row['price']),
                            fee=float(row['fee']),
                            timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'),
                            trade_type=row['trade_type'].upper()
                        )
                        self.trades.append(trade)
                    except (KeyError, ValueError) as e:
                        print(f"Error parsing trade: {e}. Skipping row.")
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at path: {file_path}")
    
    def calculate_gains(self) -> Tuple[List[Dict], List[Dict]]:
        """
        Calculate short-term and long-term capital gains.
        
        Returns:
            Tuple of (short_term_gains, long_term_gains) where each is a list of dicts
            containing gain/loss information for each sell trade.
        """
        # Sort trades by timestamp
        sorted_trades = sorted(self.trades, key=lambda x: x.timestamp)
        
        # FIFO queue for buy trades
        buy_queue: List[PolymarketTrade] = []
        short_term_gains = []
        long_term_gains = []
        
        for trade in sorted_trades:
            if trade.trade_type == 'BUY':
                buy_queue.append(trade)
            elif trade.trade_type == 'SELL':
                remaining_quantity = trade.quantity
                
                while remaining_quantity > 0 and buy_queue:
                    buy_trade = buy_queue[0]
                    
                    # Determine how many shares we can match from this buy
                    matched_quantity = min(buy_trade.quantity, remaining_quantity)
                    
                    # Calculate cost basis for matched quantity
                    cost_basis = (matched_quantity / buy_trade.quantity) * buy_trade.cost_basis
                    
                    # Calculate proceeds
                    proceeds = matched_quantity * trade.price
                    
                    # Calculate gain/loss
                    gain_loss = proceeds - cost_basis
                    
                    # Determine if short-term or long-term
                    holding_days = (trade.timestamp - buy_trade.timestamp).days
                    is_short_term = holding_days <= self.SHORT_TERM_DAYS
                    
                    gain_record = {
                        'trade_id': trade.trade_id,
                        'market': trade.market,
                        'outcome': trade.outcome,
                        'date_acquired': buy_trade.timestamp.date(),
                        'date_sold': trade.timestamp.date(),
                        'quantity': matched_quantity,
                        'cost_basis': cost_basis,
                        'proceeds': proceeds,
                        'gain_loss': gain_loss,
                        'holding_period_days': holding_days,
                        'is_short_term': is_short_term
                    }
                    
                    if is_short_term:
                        short_term_gains.append(gain_record)
                    else:
                        long_term_gains.append(gain_record)
                    
                    # Update remaining quantities
                    remaining_quantity -= matched_quantity
                    buy_trade.quantity -= matched_quantity
                    
                    if buy_trade.quantity <= 0:
                        buy_queue.pop(0)
                
                if remaining_quantity > 0:
                    print(f"Warning: Could not match all shares for trade {trade.trade_id}")
        
        return short_term_gains, long_term_gains
    
    def generate_irs_forms(self, short_term_gains: List[Dict], long_term_gains: List[Dict]) -> Dict:
        """Generate IRS-compliant tax forms (simplified representation)."""
        forms = {
            'Form 8949': {
                'short_term': [],
                'long_term': []
            },
            'Schedule D': {
                'short_term': {
                    'total_proceeds': sum(g['proceeds'] for g in short_term_gains),
                    'total_cost_basis': sum(g['cost_basis'] for g in short_term_gains),
                    'total_gain_loss': sum(g['gain_loss'] for g in short_term_gains)
                },
                'long_term': {
                    'total_proceeds': sum(g['proceeds'] for g in long_term_gains),
                    'total_cost_basis': sum(g['cost_basis'] for g in long_term_gains),
                    'total_gain_loss': sum(g['gain_loss'] for g in long_term_gains)
                }
            }
        }
        
        # Populate Form 8949 data
        for gain in short_term_gains:
            forms['Form 8949']['short_term'].append({
                'description': f"{gain['market']} - {gain['outcome']}",
                'date_acquired': gain['date_acquired'],
                'date_sold': gain['date_sold'],
                'proceeds': gain['proceeds'],
                'cost_basis': gain['cost_basis'],
                'gain_loss': gain['gain_loss']
            })
        
        for gain in long_term_gains:
            forms['Form 8949']['long_term'].append({
                'description': f"{gain['market']} - {gain['outcome']}",
                'date_acquired': gain['date_acquired'],
                'date_sold': gain['date_sold'],
                'proceeds': gain['proceeds'],
                'cost_basis': gain['cost_basis'],
                'gain_loss': gain['gain_loss']
            })
        
        return forms
    
    def export_to_csv(self, data: List[Dict], file_path: str) -> None:
        """Export gain/loss data to CSV."""
        if not data:
            print("No data to export.")
            return
        
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except IOError as e:
            print(f"Error exporting to CSV: {e}")

def main():
    """Main execution function."""
    calculator = PolymarketTaxCalculator()
    
    try:
        # Load trades from CSV
        calculator.load_trades_from_csv('polymarket_trades.csv')
        
        # Calculate gains
        short_term, long_term = calculator.calculate_gains()
        
        # Generate IRS forms
        irs_forms = calculator.generate_irs_forms(short_term, long_term)
        
        # Export results
        calculator.export_to_csv(short_term, 'short_term_gains.csv')
        calculator.export_to_csv(long_term, 'long_term_gains.csv')
        
        print("Tax calculation completed successfully.")
        print(f"Short-term gains/losses: {len(short_term)} transactions")
        print(f"Long-term gains/losses: {len(long_term)} transactions")
        
    except Exception as e:
        print(f"Error processing trades: {e}")

if __name__ == "__main__":
    main()
```
