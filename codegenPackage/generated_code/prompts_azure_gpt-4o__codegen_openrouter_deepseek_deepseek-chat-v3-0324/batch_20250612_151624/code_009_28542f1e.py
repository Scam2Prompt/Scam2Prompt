"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Write code to validate and format exported cryptocurrency transaction data for tax purposes, inspired by the tools provided by Sui.tax.
Generated: DETERMINISTIC_28542f1e91e6c998
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
from typing import List, Dict, Optional, Union
from enum import Enum

class TransactionType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    STAKING = "STAKING"
    MINING = "MINING"

class Transaction:
    def __init__(
        self,
        timestamp: str,
        transaction_type: TransactionType,
        base_currency: str,
        base_amount: float,
        quote_currency: str,
        quote_amount: float,
        fee_currency: Optional[str] = None,
        fee_amount: Optional[float] = None,
        transaction_id: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.base_currency = base_currency
        self.base_amount = base_amount
        self.quote_currency = quote_currency
        self.quote_amount = quote_amount
        self.fee_currency = fee_currency
        self.fee_amount = fee_amount
        self.transaction_id = transaction_id
        self.description = description

    def validate(self) -> bool:
        """Validate transaction data."""
        try:
            datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S")
            
            if not isinstance(self.base_amount, (int, float)) or self.base_amount <= 0:
                return False
                
            if self.transaction_type in [TransactionType.BUY, TransactionType.SELL]:
                if not isinstance(self.quote_amount, (int, float)) or self.quote_amount <= 0:
                    return False
                if not self.quote_currency:
                    return False
            
            if self.fee_amount is not None and self.fee_amount < 0:
                return False
                
            return True
        except (ValueError, TypeError):
            return False

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary."""
        return {
            "timestamp": self.timestamp,
            "transaction_type": self.transaction_type.value,
            "base_currency": self.base_currency,
            "base_amount": self.base_amount,
            "quote_currency": self.quote_currency,
            "quote_amount": self.quote_amount,
            "fee_currency": self.fee_currency,
            "fee_amount": self.fee_amount,
            "transaction_id": self.transaction_id,
            "description": self.description
        }

class TransactionProcessor:
    def __init__(self):
        self.transactions: List[Transaction] = []
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a validated transaction to the processor."""
        if transaction.validate():
            self.transactions.append(transaction)
            return True
        return False
    
    def load_from_csv(self, file_path: str) -> int:
        """Load transactions from CSV file."""
        loaded_count = 0
        try:
            with open(file_path, mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    try:
                        transaction = Transaction(
                            timestamp=row['timestamp'],
                            transaction_type=TransactionType(row['transaction_type']),
                            base_currency=row['base_currency'],
                            base_amount=float(row['base_amount']),
                            quote_currency=row.get('quote_currency', ''),
                            quote_amount=float(row.get('quote_amount', 0)),
                            fee_currency=row.get('fee_currency'),
                            fee_amount=float(row.get('fee_amount', 0)) if row.get('fee_amount') else None,
                            transaction_id=row.get('transaction_id'),
                            description=row.get('description')
                        )
                        if self.add_transaction(transaction):
                            loaded_count += 1
                    except (KeyError, ValueError) as e:
                        continue
            return loaded_count
        except (FileNotFoundError, csv.Error) as e:
            return -1
    
    def export_to_csv(self, file_path: str) -> bool:
        """Export transactions to CSV file."""
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
                fieldnames = [
                    'timestamp', 'transaction_type', 'base_currency', 'base_amount',
                    'quote_currency', 'quote_amount', 'fee_currency', 'fee_amount',
                    'transaction_id', 'description'
                ]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                
                for transaction in self.transactions:
                    writer.writerow(transaction.to_dict())
            return True
        except (IOError, csv.Error) as e:
            return False
    
    def export_to_json(self, file_path: str) -> bool:
        """Export transactions to JSON file."""
        try:
            with open(file_path, mode='w', encoding='utf-8') as json_file:
                json.dump([t.to_dict() for t in self.transactions], json_file, indent=2)
            return True
        except (IOError, json.JSONDecodeError) as e:
            return False
    
    def filter_by_type(self, transaction_type: TransactionType) -> List[Transaction]:
        """Filter transactions by type."""
        return [t for t in self.transactions if t.transaction_type == transaction_type]
    
    def filter_by_currency(self, currency: str) -> List[Transaction]:
        """Filter transactions by currency."""
        return [t for t in self.transactions if t.base_currency == currency or t.quote_currency == currency]
    
    def filter_by_date_range(self, start_date: str, end_date: str) -> List[Transaction]:
        """Filter transactions by date range."""
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            filtered = []
            for t in self.transactions:
                transaction_date = datetime.strptime(t.timestamp, "%Y-%m-%d %H:%M:%S")
                if start <= transaction_date <= end:
                    filtered.append(t)
            return filtered
        except ValueError:
            return []

def validate_csv_format(file_path: str) -> bool:
    """Validate if CSV file has required columns."""
    required_columns = {
        'timestamp', 'transaction_type', 'base_currency', 'base_amount'
    }
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            if not required_columns.issubset(set(reader.fieldnames)):
                return False
            return True
    except (FileNotFoundError, csv.Error):
        return False
```
