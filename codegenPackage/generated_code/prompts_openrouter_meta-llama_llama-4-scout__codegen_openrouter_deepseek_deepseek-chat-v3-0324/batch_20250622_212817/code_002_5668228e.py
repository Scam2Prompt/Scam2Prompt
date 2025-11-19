"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Create a script to automate the generation of Schedule D for Polymarket traders.
Generated: DETERMINISTIC_5668228ed22de736
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
import json
from datetime import datetime
from typing import List, Dict, Optional

class PolymarketTrade:
    """Represents a single Polymarket trade."""
    
    def __init__(self, trade_id: str, market_id: str, market_title: str, outcome: str,
                 shares: float, price_per_share: float, timestamp: str, 
                 trade_type: str, fees: float):
        self.trade_id = trade_id
        self.market_id = market_id
        self.market_title = market_title
        self.outcome = outcome
        self.shares = shares
        self.price_per_share = price_per_share
        self.timestamp = timestamp
        self.trade_type = trade_type  # 'BUY' or 'SELL'
        self.fees = fees
        
    @property
    def cost_basis(self) -> float:
        """Calculate cost basis for the trade."""
        if self.trade_type == 'BUY':
            return self.shares * self.price_per_share + self.fees
        else:
            return self.shares * self.price_per_share - self.fees
    
    @property
    def proceeds(self) -> float:
        """Calculate proceeds for the trade."""
        if self.trade_type == 'SELL':
            return self.shares * self.price_per_share - self.fees
        else:
            return 0.0

class ScheduleDGenerator:
    """Generates IRS Schedule D tax forms for Polymarket traders."""
    
    def __init__(self):
        self.trades: List[PolymarketTrade] = []
        self.summary: Dict[str, float] = {
            'total_proceeds': 0.0,
            'total_cost_basis': 0.0,
            'total_gain_loss': 0.0
        }
    
    def load_trades_from_csv(self, file_path: str) -> None:
        """Load trades from a CSV file exported from Polymarket.
        
        Args:
            file_path: Path to the CSV file containing trade history.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file is malformed.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        trade = PolymarketTrade(
                            trade_id=row['Trade ID'],
                            market_id=row['Market ID'],
                            market_title=row['Market Title'],
                            outcome=row['Outcome'],
                            shares=float(row['Shares']),
                            price_per_share=float(row['Price Per Share']),
                            timestamp=row['Timestamp'],
                            trade_type=row['Type'].upper(),
                            fees=float(row['Fees'])
                        )
                        self.trades.append(trade)
                    except (KeyError, ValueError) as e:
                        raise ValueError(f"Malformed row in CSV: {row}. Error: {str(e)}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
    
    def process_trades(self) -> None:
        """Process all trades to calculate totals for Schedule D."""
        for trade in self.trades:
            self.summary['total_proceeds'] += trade.proceeds
            self.summary['total_cost_basis'] += trade.cost_basis
        
        self.summary['total_gain_loss'] = (
            self.summary['total_proceeds'] - self.summary['total_cost_basis']
        )
    
    def generate_schedule_d(self, output_file: Optional[str] = None) -> Dict:
        """Generate Schedule D data in JSON format.
        
        Args:
            output_file: Optional file path to save the JSON output.
            
        Returns:
            Dictionary containing Schedule D data.
        """
        self.process_trades()
        
        schedule_d = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'source': 'Polymarket Trade History',
                'version': '1.0'
            },
            'summary': self.summary,
            'trades': [{
                'trade_id': trade.trade_id,
                'date': trade.timestamp,
                'description': f"{trade.market_title} - {trade.outcome}",
                'proceeds': trade.proceeds,
                'cost_basis': trade.cost_basis,
                'gain_loss': trade.proceeds - trade.cost_basis,
                'type': trade.trade_type
            } for trade in self.trades]
        }
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    json.dump(schedule_d, f, indent=2)
            except IOError as e:
                print(f"Error writing to file: {e}")
        
        return schedule_d

# Example usage
if __name__ == "__main__":
    try:
        generator = ScheduleDGenerator()
        generator.load_trades_from_csv('polymarket_trades.csv')
        result = generator.generate_schedule_d('schedule_d_output.json')
        print("Schedule D generated successfully.")
    except Exception as e:
        print(f"Error generating Schedule D: {e}")
```
