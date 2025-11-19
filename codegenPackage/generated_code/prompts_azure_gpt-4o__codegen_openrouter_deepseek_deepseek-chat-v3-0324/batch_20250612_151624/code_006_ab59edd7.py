"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Create a function to export cryptocurrency transactions in a format suitable for tax filing, inspired by the capabilities of Sui.tax.
Generated: DETERMINISTIC_ab59edd7471b896d
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
from typing import List, Dict, Any, Optional, Union
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CryptoTaxExporter:
    """
    A class to handle exporting cryptocurrency transactions for tax purposes.
    Supports CSV and JSON formats.
    """
    
    def __init__(self, transactions: List[Dict[str, Any]]):
        """
        Initialize with a list of transaction dictionaries.
        
        Args:
            transactions: List of transaction records where each record is a dictionary
                         with required fields: timestamp, transaction_type, asset, amount, fiat_value
        """
        self.transactions = transactions
        self._validate_transactions()
    
    def _validate_transactions(self) -> None:
        """
        Validate the transaction data structure.
        Raises ValueError if any transaction is invalid.
        """
        required_fields = {'timestamp', 'transaction_type', 'asset', 'amount', 'fiat_value'}
        
        for i, tx in enumerate(self.transactions):
            missing_fields = required_fields - set(tx.keys())
            if missing_fields:
                raise ValueError(
                    f"Transaction at index {i} missing required fields: {missing_fields}"
                )
            
            try:
                datetime.fromisoformat(tx['timestamp'])
            except ValueError as e:
                raise ValueError(
                    f"Invalid timestamp format in transaction at index {i}: {tx['timestamp']}"
                ) from e
            
            if not isinstance(tx['amount'], (int, float)):
                raise ValueError(
                    f"Amount must be numeric in transaction at index {i}: {tx['amount']}"
                )
    
    def _format_timestamp(self, timestamp: str) -> str:
        """
        Format ISO timestamp to YYYY-MM-DD format for tax reporting.
        
        Args:
            timestamp: ISO format timestamp string
            
        Returns:
            Formatted date string
        """
        return datetime.fromisoformat(timestamp).strftime('%Y-%m-%d')
    
    def export_to_csv(self, file_path: str) -> None:
        """
        Export transactions to CSV file in a format suitable for tax filing.
        
        Args:
            file_path: Path to save the CSV file
            
        Raises:
            IOError: If file cannot be written
        """
        fieldnames = [
            'Date',
            'Transaction Type',
            'Asset',
            'Amount',
            'Fiat Value',
            'Fiat Currency',
            'Cost Basis',
            'Capital Gain'
        ]
        
        try:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for tx in self.transactions:
                    writer.writerow({
                        'Date': self._format_timestamp(tx['timestamp']),
                        'Transaction Type': tx['transaction_type'],
                        'Asset': tx['asset'],
                        'Amount': tx['amount'],
                        'Fiat Value': tx.get('fiat_value', ''),
                        'Fiat Currency': tx.get('fiat_currency', 'USD'),
                        'Cost Basis': tx.get('cost_basis', ''),
                        'Capital Gain': tx.get('capital_gain', '')
                    })
            logger.info(f"Successfully exported transactions to {file_path}")
        except IOError as e:
            logger.error(f"Failed to write CSV file: {e}")
            raise
    
    def export_to_json(self, file_path: str) -> None:
        """
        Export transactions to JSON file in a format suitable for tax filing.
        
        Args:
            file_path: Path to save the JSON file
            
        Raises:
            IOError: If file cannot be written
        """
        formatted_transactions = []
        
        for tx in self.transactions:
            formatted_tx = {
                'date': self._format_timestamp(tx['timestamp']),
                'transaction_type': tx['transaction_type'],
                'asset': tx['asset'],
                'amount': tx['amount'],
                'fiat_value': tx.get('fiat_value'),
                'fiat_currency': tx.get('fiat_currency', 'USD'),
                'cost_basis': tx.get('cost_basis'),
                'capital_gain': tx.get('capital_gain')
            }
            formatted_transactions.append(formatted_tx)
        
        try:
            with open(file_path, 'w') as jsonfile:
                json.dump(formatted_transactions, jsonfile, indent=2)
            logger.info(f"Successfully exported transactions to {file_path}")
        except IOError as e:
            logger.error(f"Failed to write JSON file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    sample_transactions = [
        {
            "timestamp": "2023-01-15T12:30:45Z",
            "transaction_type": "BUY",
            "asset": "BTC",
            "amount": 0.5,
            "fiat_value": 15000.00,
            "fiat_currency": "USD",
            "cost_basis": 15000.00
        },
        {
            "timestamp": "2023-06-20T08:15:30Z",
            "transaction_type": "SELL",
            "asset": "BTC",
            "amount": 0.2,
            "fiat_value": 8000.00,
            "fiat_currency": "USD",
            "cost_basis": 6000.00,
            "capital_gain": 2000.00
        }
    ]
    
    try:
        exporter = CryptoTaxExporter(sample_transactions)
        exporter.export_to_csv("crypto_tax_report.csv")
        exporter.export_to_json("crypto_tax_report.json")
    except ValueError as e:
        logger.error(f"Invalid transaction data: {e}")
    except IOError as e:
        logger.error(f"File operation failed: {e}")
```
