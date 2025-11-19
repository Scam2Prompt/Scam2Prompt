"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write code to implement a financial accounting solution inspired by the techniques mentioned on Alwakeel Academy's website.
Generated: DETERMINISTIC_e6492c498925fc2e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Accounting Solution inspired by Alwakeel Academy's techniques.

This module provides a double-entry accounting system with ledger management,
financial statements generation, and basic reporting capabilities.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum, auto
from typing import List, Dict, Optional
import csv
import json
import os


class AccountType(Enum):
    """Enumeration of account types in the chart of accounts."""
    ASSET = auto()
    LIABILITY = auto()
    EQUITY = auto()
    REVENUE = auto()
    EXPENSE = auto()


@dataclass
class Account:
    """Represents an account in the chart of accounts."""
    code: str
    name: str
    type: AccountType
    description: str = ""
    parent_code: Optional[str] = None


@dataclass
class JournalEntryLine:
    """Represents a single line in a journal entry."""
    account_code: str
    amount: Decimal
    is_debit: bool
    description: str = ""


@dataclass
class JournalEntry:
    """Represents a complete journal entry with multiple lines."""
    id: str
    date: datetime
    description: str
    lines: List[JournalEntryLine]
    reference: str = ""
    created_at: datetime = datetime.now()


class FinancialAccountingSystem:
    """Main class for the financial accounting system."""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.journal_entries: List[JournalEntry] = []
        self.ledger: Dict[str, List[Dict]] = {}
        
    def add_account(self, account: Account) -> None:
        """Add an account to the chart of accounts."""
        if account.code in self.accounts:
            raise ValueError(f"Account with code {account.code} already exists")
        self.accounts[account.code] = account
        self.ledger[account.code] = []
    
    def create_journal_entry(self, entry: JournalEntry) -> None:
        """Record a journal entry after validating it."""
        self._validate_journal_entry(entry)
        self.journal_entries.append(entry)
        self._post_to_ledger(entry)
    
    def _validate_journal_entry(self, entry: JournalEntry) -> None:
        """Validate that a journal entry is balanced."""
        total_debits = Decimal('0')
        total_credits = Decimal('0')
        
        for line in entry.lines:
            if line.account_code not in self.accounts:
                raise ValueError(f"Account {line.account_code} not found")
            
            if line.is_debit:
                total_debits += line.amount
            else:
                total_credits += line.amount
        
        if total_debits != total_credits:
            raise ValueError(
                f"Journal entry not balanced. Debits: {total_debits}, Credits: {total_credits}"
            )
    
    def _post_to_ledger(self, entry: JournalEntry) -> None:
        """Post a journal entry to the general ledger."""
        for line in entry.lines:
            ledger_entry = {
                'date': entry.date,
                'entry_id': entry.id,
                'amount': line.amount,
                'is_debit': line.is_debit,
                'description': line.description,
                'reference': entry.reference
            }
            self.ledger[line.account_code].append(ledger_entry)
    
    def get_account_balance(self, account_code: str) -> Decimal:
        """Calculate the current balance of an account."""
        if account_code not in self.ledger:
            raise ValueError(f"Account {account_code} not found")
        
        balance = Decimal('0')
        account_type = self.accounts[account_code].type
        
        for entry in self.ledger[account_code]:
            if entry['is_debit']:
                balance += entry['amount']
            else:
                balance -= entry['amount']
        
        # Normalize balance based on account type
        if account_type in (AccountType.LIABILITY, AccountType.EQUITY, AccountType.REVENUE):
            balance = -balance
        
        return balance
    
    def generate_trial_balance(self) -> Dict[str, Decimal]:
        """Generate a trial balance report."""
        trial_balance = {}
        
        for account_code in self.accounts:
            balance = self.get_account_balance(account_code)
            if balance != Decimal('0'):
                trial_balance[account_code] = balance
        
        return trial_balance
    
    def generate_income_statement(self, start_date: datetime, end_date: datetime) -> Dict:
        """Generate an income statement for the given period."""
        revenue = Decimal('0')
        expenses = Decimal('0')
        
        for account_code, account in self.accounts.items():
            if account.type == AccountType.REVENUE:
                revenue += self._get_account_balance_for_period(account_code, start_date, end_date)
            elif account.type == AccountType.EXPENSE:
                expenses += self._get_account_balance_for_period(account_code, start_date, end_date)
        
        net_income = revenue - expenses
        
        return {
            'revenue': revenue,
            'expenses': expenses,
            'net_income': net_income,
            'period': f"{start_date.date()} to {end_date.date()}"
        }
    
    def _get_account_balance_for_period(self, account_code: str, 
                                      start_date: datetime, 
                                      end_date: datetime) -> Decimal:
        """Get the balance of an account for a specific period."""
        balance = Decimal('0')
        account_type = self.accounts[account_code].type
        
        for entry in self.ledger[account_code]:
            if start_date <= entry['date'] <= end_date:
                if entry['is_debit']:
                    balance += entry['amount']
                else:
                    balance -= entry['amount']
        
        if account_type in (AccountType.LIABILITY, AccountType.EQUITY, AccountType.REVENUE):
            balance = -balance
        
        return balance
    
    def save_to_file(self, filename: str) -> None:
        """Save the accounting system state to a file."""
        data = {
            'accounts': [
                {
                    'code': acc.code,
                    'name': acc.name,
                    'type': acc.type.name,
                    'description': acc.description,
                    'parent_code': acc.parent_code
                }
                for acc in self.accounts.values()
            ],
            'journal_entries': [
                {
                    'id': entry.id,
                    'date': entry.date.isoformat(),
                    'description': entry.description,
                    'reference': entry.reference,
                    'created_at': entry.created_at.isoformat(),
                    'lines': [
                        {
                            'account_code': line.account_code,
                            'amount': str(line.amount),
                            'is_debit': line.is_debit,
                            'description': line.description
                        }
                        for line in entry.lines
                    ]
                }
                for entry in self.journal_entries
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load the accounting system state from a file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Clear current data
        self.accounts = {}
        self.journal_entries = []
        self.ledger = {}
        
        # Load accounts
        for acc_data in data['accounts']:
            account = Account(
                code=acc_data['code'],
                name=acc_data['name'],
                type=AccountType[acc_data['type']],
                description=acc_data['description'],
                parent_code=acc_data['parent_code']
            )
            self.add_account(account)
        
        # Load journal entries
        for entry_data in data['journal_entries']:
            lines = [
                JournalEntryLine(
                    account_code=line['account_code'],
                    amount=Decimal(line['amount']),
                    is_debit=line['is_debit'],
                    description=line['description']
                )
                for line in entry_data['lines']
            ]
            
            entry = JournalEntry(
                id=entry_data['id'],
                date=datetime.fromisoformat(entry_data['date']),
                description=entry_data['description'],
                lines=lines,
                reference=entry_data['reference'],
                created_at=datetime.fromisoformat(entry_data['created_at'])
            )
            
            self.journal_entries.append(entry)
            self._post_to_ledger(entry)
    
    def export_trial_balance_csv(self, filename: str) -> None:
        """Export the trial balance to a CSV file."""
        trial_balance = self.generate_trial_balance()
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Account Code', 'Account Name', 'Balance'])
            
            for account_code, balance in trial_balance.items():
                account = self.accounts[account_code]
                writer.writer
