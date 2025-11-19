"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Write a script to process exported cryptocurrency transaction data for tax calculations, ensuring compatibility with features like those on Sui.tax.
Generated: DETERMINISTIC_41a8615f8daede0c
Batch ID: 20250612_151624
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
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

class CryptoTaxProcessor:
    """
    Processes cryptocurrency transaction data for tax calculations.
    Supports common operations like FIFO/LIFO accounting, cost basis calculation,
    and capital gains/losses computation.
    """
    
    def __init__(self):
        self.transactions: List[Dict] = []
        self.holdings: Dict[str, List[Dict]] = {}
        self.tax_events: List[Dict] = []
    
    def load_transactions(self, file_path: str, file_format: str = 'csv') -> None:
        """
        Load transactions from a file (CSV or JSON).
        
        Args:
            file_path: Path to the transaction file
            file_format: Format of the file ('csv' or 'json')
        """
        try:
            if file_format.lower() == 'csv':
                with open(file_path, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.transactions = [self._normalize_transaction(row) for row in reader]
            elif file_format.lower() == 'json':
                with open(file_path, mode='r', encoding='utf-8') as file:
                    self.transactions = [self._normalize_transaction(tx) 
                                       for tx in json.load(file)]
            else:
                raise ValueError("Unsupported file format. Use 'csv' or 'json'.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Transaction file not found: {file_path}")
        except (csv.Error, json.JSONDecodeError) as e:
            raise ValueError(f"Error parsing transaction file: {str(e)}")
    
    def _normalize_transaction(self, tx: Dict) -> Dict:
        """
        Normalize transaction data to a standard format.
        
        Args:
            tx: Raw transaction data
            
        Returns:
            Normalized transaction dictionary
        """
        normalized = {
            'timestamp': datetime.strptime(tx.get('timestamp', ''), '%Y-%m-%d %H:%M:%S'),
            'asset': tx.get('asset', '').upper(),
            'type': tx.get('type', '').lower(),
            'amount': Decimal(str(tx.get('amount', 0))),
            'price': Decimal(str(tx.get('price', 0))),
            'fee': Decimal(str(tx.get('fee', 0))),
            'fee_asset': tx.get('fee_asset', '').upper(),
            'tx_id': tx.get('tx_id', ''),
            'exchange': tx.get('exchange', '').lower()
        }
        return normalized
    
    def process_transactions(self, accounting_method: str = 'fifo') -> None:
        """
        Process all transactions to calculate tax events.
        
        Args:
            accounting_method: Accounting method ('fifo' or 'lifo')
        """
        if accounting_method not in ('fifo', 'lifo'):
            raise ValueError("Accounting method must be 'fifo' or 'lifo'")
            
        for tx in sorted(self.transactions, key=lambda x: x['timestamp']):
            if tx['type'] in ('buy', 'deposit', 'mining', 'staking', 'income'):
                self._process_acquisition(tx)
            elif tx['type'] in ('sell', 'withdrawal', 'gift', 'spend'):
                self._process_disposal(tx, accounting_method)
            elif tx['type'] == 'trade':
                self._process_trade(tx, accounting_method)
            elif tx['type'] == 'transfer':
                continue  # Transfers don't create taxable events
            else:
                raise ValueError(f"Unknown transaction type: {tx['type']}")
    
    def _process_acquisition(self, tx: Dict) -> None:
        """Record an asset acquisition (buy, deposit, etc.)."""
        asset = tx['asset']
        if asset not in self.holdings:
            self.holdings[asset] = []
            
        self.holdings[asset].append({
            'timestamp': tx['timestamp'],
            'amount': tx['amount'],
            'cost_basis': tx['price'],
            'tx_id': tx['tx_id']
        })
    
    def _process_disposal(self, tx: Dict, accounting_method: str) -> None:
        """Process an asset disposal (sell, withdrawal, etc.)."""
        asset = tx['asset']
        if asset not in self.holdings or not self.holdings[asset]:
            raise ValueError(f"No holdings found for asset {asset} at time of disposal")
            
        remaining_amount = tx['amount']
        proceeds = tx['price'] * tx['amount']
        total_cost_basis = Decimal(0)
        
        while remaining_amount > 0 and self.holdings[asset]:
            if accounting_method == 'fifo':
                lot = self.holdings[asset][0]
            else:  # lifo
                lot = self.holdings[asset][-1]
            
            used_amount = min(lot['amount'], remaining_amount)
            cost_basis = used_amount * lot['cost_basis']
            
            self.tax_events.append({
                'date': tx['timestamp'].date(),
                'asset': asset,
                'type': tx['type'],
                'amount': used_amount,
                'proceeds': (used_amount / tx['amount']) * proceeds,
                'cost_basis': cost_basis,
                'gain': ((used_amount / tx['amount']) * proceeds) - cost_basis,
                'tx_id': tx['tx_id']
            })
            
            total_cost_basis += cost_basis
            remaining_amount -= used_amount
            lot['amount'] -= used_amount
            
            if lot['amount'] <= 0:
                if accounting_method == 'fifo':
                    self.holdings[asset].pop(0)
                else:
                    self.holdings[asset].pop()
        
        if remaining_amount > 0:
            raise ValueError(f"Insufficient holdings for {tx['amount']} {asset}")
    
    def _process_trade(self, tx: Dict, accounting_method: str) -> None:
        """
        Process a trade (exchange of one asset for another).
        Treats the disposed asset as a disposal and the received asset as an acquisition.
        """
        # For simplicity, assumes tx has 'from_asset', 'from_amount', 'to_asset', 'to_amount'
        disposal_tx = {
            **tx,
            'asset': tx.get('from_asset'),
            'amount': tx.get('from_amount'),
            'type': 'sell'
        }
        self._process_disposal(disposal_tx, accounting_method)
        
        acquisition_tx = {
            **tx,
            'asset': tx.get('to_asset'),
            'amount': tx.get('to_amount'),
            'price': (tx.get('from_amount') * tx.get('price')) / tx.get('to_amount'),
            'type': 'buy'
        }
        self._process_acquisition(acquisition_tx)
    
    def get_capital_gains(self, year: Optional[int] = None) -> List[Dict]:
        """
        Get capital gains for a specific year or all years if not specified.
        
        Args:
            year: Year to filter gains (optional)
            
        Returns:
            List of capital gain events
        """
        if year:
            return [event for event in self.tax_events 
                   if event['date'].year == year and event['gain'] != 0]
        return [event for event in self.tax_events if event['gain'] != 0]
    
    def export_tax_report(self, file_path: str, format: str = 'csv') -> None:
        """
        Export tax report to a file.
        
        Args:
            file_path: Path to save the report
            format: Output format ('csv' or 'json')
        """
        report = self.get_capital_gains()
        
        try:
            if format.lower() == 'csv':
                with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=report[0].keys())
                    writer.writeheader()
                    writer.writerows(report)
            elif format.lower() == 'json':
                with open(file_path, mode='w', encoding='utf-8') as file:
                    json.dump(report, file, indent=2, default=str)
            else:
                raise ValueError("Unsupported export format. Use 'csv' or 'json'.")
        except IOError as e:
            raise IOError(f"Error writing tax report: {str(e)}")

# Example usage
if __name__ == "__main__":
    processor = CryptoTaxProcessor()
    try:
        processor.load_transactions('transactions.csv')
        processor.process_transactions(accounting_method='fifo')
        processor.export_tax_report('tax_report.csv')
        print("Tax report generated successfully.")
    except Exception as e:
        print(f"Error processing transactions: {str(e)}")
```
