"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a feature for a bookkeeping system that tracks profitability and personal wealth growth for sole proprietors and corporations, inspired by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_f5ca1b5f3d280e97
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bookkeeping System for Profitability and Wealth Growth Tracking

This module provides functionality to track profitability and personal wealth growth
for sole proprietors and corporations. It includes features for income/expense tracking,
net worth calculation, and financial reporting.

Inspired by "The Bookkeeping Diaries".
"""

import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union
from enum import Enum, auto
import json
import csv
from pathlib import Path


class EntityType(Enum):
    """Enum representing different business entity types."""
    SOLE_PROPRIETOR = auto()
    CORPORATION = auto()


class TransactionType(Enum):
    """Enum representing different transaction types."""
    INCOME = auto()
    EXPENSE = auto()
    ASSET = auto()
    LIABILITY = auto()


@dataclass
class Transaction:
    """Class representing a financial transaction."""
    amount: float
    description: str
    date: datetime.date
    category: str
    transaction_type: TransactionType
    id: str = field(default_factory=lambda: str(datetime.datetime.now().timestamp()))

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization."""
        return {
            'id': self.id,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat(),
            'category': self.category,
            'transaction_type': self.transaction_type.name
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create transaction from dictionary."""
        return cls(
            id=data['id'],
            amount=data['amount'],
            description=data['description'],
            date=datetime.date.fromisoformat(data['date']),
            category=data['category'],
            transaction_type=TransactionType[data['transaction_type']]
        )


@dataclass
class FinancialEntity:
    """Base class representing a financial entity (person or business)."""
    name: str
    entity_type: EntityType
    transactions: List[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the entity's records."""
        self.transactions.append(transaction)

    def get_transactions(self, 
                        start_date: Optional[datetime.date] = None, 
                        end_date: Optional[datetime.date] = None,
                        transaction_type: Optional[TransactionType] = None) -> List[Transaction]:
        """Get filtered transactions based on date range and type."""
        filtered = self.transactions
        
        if start_date:
            filtered = [t for t in filtered if t.date >= start_date]
        if end_date:
            filtered = [t for t in filtered if t.date <= end_date]
        if transaction_type:
            filtered = [t for t in filtered if t.transaction_type == transaction_type]
            
        return filtered

    def calculate_profit(self, 
                         start_date: Optional[datetime.date] = None, 
                         end_date: Optional[datetime.date] = None) -> float:
        """Calculate profit (income - expenses) for a given period."""
        income = sum(t.amount for t in self.get_transactions(start_date, end_date, TransactionType.INCOME))
        expenses = sum(t.amount for t in self.get_transactions(start_date, end_date, TransactionType.EXPENSE))
        return income - expenses

    def calculate_net_worth(self) -> float:
        """Calculate net worth (assets - liabilities)."""
        assets = sum(t.amount for t in self.get_transactions(transaction_type=TransactionType.ASSET))
        liabilities = sum(t.amount for t in self.get_transactions(transaction_type=TransactionType.LIABILITY))
        return assets - liabilities

    def generate_report(self, 
                        start_date: Optional[datetime.date] = None, 
                        end_date: Optional[datetime.date] = None) -> Dict:
        """Generate a financial report for the given period."""
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is None:
            start_date = end_date - datetime.timedelta(days=365)

        return {
            'entity_name': self.name,
            'entity_type': self.entity_type.name,
            'period_start': start_date.isoformat(),
            'period_end': end_date.isoformat(),
            'total_income': sum(t.amount for t in self.get_transactions(start_date, end_date, TransactionType.INCOME)),
            'total_expenses': sum(t.amount for t in self.get_transactions(start_date, end_date, TransactionType.EXPENSE)),
            'profit': self.calculate_profit(start_date, end_date),
            'current_net_worth': self.calculate_net_worth(),
            'transaction_count': len(self.get_transactions(start_date, end_date))
        }

    def save_to_file(self, file_path: Union[str, Path]) -> None:
        """Save entity data to a JSON file."""
        data = {
            'name': self.name,
            'entity_type': self.entity_type.name,
            'transactions': [t.to_dict() for t in self.transactions]
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, file_path: Union[str, Path]) -> 'FinancialEntity':
        """Load entity data from a JSON file."""
        with open(file_path) as f:
            data = json.load(f)
        
        entity = cls(
            name=data['name'],
            entity_type=EntityType[data['entity_type']]
        )
        
        for t_data in data['transactions']:
            entity.add_transaction(Transaction.from_dict(t_data))
            
        return entity

    def export_to_csv(self, file_path: Union[str, Path], 
                      start_date: Optional[datetime.date] = None, 
                      end_date: Optional[datetime.date] = None) -> None:
        """Export transactions to CSV file."""
        transactions = self.get_transactions(start_date, end_date)
        
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['date', 'description', 'category', 'type', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for t in transactions:
                writer.writerow({
                    'date': t.date.isoformat(),
                    'description': t.description,
                    'category': t.category,
                    'type': t.transaction_type.name,
                    'amount': t.amount
                })


class BookkeepingSystem:
    """Main bookkeeping system class managing multiple financial entities."""
    
    def __init__(self):
        self.entities: Dict[str, FinancialEntity] = {}
    
    def add_entity(self, name: str, entity_type: EntityType) -> FinancialEntity:
        """Add a new financial entity to the system."""
        if name in self.entities:
            raise ValueError(f"Entity with name '{name}' already exists")
            
        entity = FinancialEntity(name=name, entity_type=entity_type)
        self.entities[name] = entity
        return entity
    
    def get_entity(self, name: str) -> FinancialEntity:
        """Get a financial entity by name."""
        if name not in self.entities:
            raise ValueError(f"Entity with name '{name}' not found")
        return self.entities[name]
    
    def remove_entity(self, name: str) -> None:
        """Remove a financial entity from the system."""
        if name not in self.entities:
            raise ValueError(f"Entity with name '{name}' not found")
        del self.entities[name]
    
    def generate_combined_report(self, 
                                start_date: Optional[datetime.date] = None, 
                                end_date: Optional[datetime.date] = None) -> Dict:
        """Generate a combined report for all entities."""
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is None:
            start_date = end_date - datetime.timedelta(days=365)
            
        combined = {
            'period_start': start_date.isoformat(),
            'period_end': end_date.isoformat(),
            'total_income': 0,
            'total_expenses': 0,
            'total_profit': 0,
            'total_net_worth': 0,
            'entities': []
        }
        
        for entity in self.entities.values():
            report = entity.generate_report(start_date, end_date)
            combined['total_income'] += report['total_income']
            combined['total_expenses'] += report['total_expenses']
            combined['total_profit'] += report['profit']
            combined['total_net_worth'] += report['current_net_worth']
            combined['entities'].append({
                'name': report['entity_name'],
                'type': report['entity_type'],
                'profit': report['profit'],
                'net_worth': report['current_net_worth']
            })
            
        return combined
    
    def save_all(self, directory: Union[str, Path]) -> None:
        """Save all entities to files in the specified directory."""
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        
        for name,
