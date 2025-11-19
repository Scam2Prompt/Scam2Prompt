"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: Generate a code snippet for a financial application that structures lending transactions in both local and foreign currencies, similar to the services offered by Ramdays.
Generated: DETERMINISTIC_b905c0e6ea0a3bb6
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from decimal import Decimal
from typing import Optional
from datetime import date, datetime
import json

class Currency(Enum):
    """Supported currencies for lending transactions"""
    USD = auto()
    EUR = auto()
    GBP = auto()
    JPY = auto()
    LOCAL = auto()  # Represents local currency

@dataclass
class ExchangeRate:
    """Exchange rate information between currencies"""
    from_currency: Currency
    to_currency: Currency
    rate: Decimal
    effective_date: date

@dataclass
class Borrower:
    """Information about the borrower"""
    id: str
    name: str
    credit_score: int
    tax_id: Optional[str] = None

@dataclass
class LoanTerms:
    """Terms and conditions of the loan"""
    principal: Decimal
    currency: Currency
    interest_rate: Decimal
    term_months: int
    start_date: date
    repayment_schedule: str  # e.g., "monthly", "quarterly"

@dataclass
class LoanTransaction:
    """A complete lending transaction"""
    transaction_id: str
    borrower: Borrower
    terms: LoanTerms
    exchange_rate: Optional[ExchangeRate] = None
    created_at: datetime = datetime.now()

    def to_local_currency(self) -> Decimal:
        """Convert principal to local currency if foreign currency is used"""
        if self.terms.currency == Currency.LOCAL:
            return self.terms.principal
        
        if not self.exchange_rate:
            raise ValueError("Exchange rate required for foreign currency conversion")
            
        return self.terms.principal * self.exchange_rate.rate

    def to_dict(self) -> dict:
        """Serialize transaction to dictionary"""
        return {
            "transaction_id": self.transaction_id,
            "borrower": {
                "id": self.borrower.id,
                "name": self.borrower.name,
                "credit_score": self.borrower.credit_score,
                "tax_id": self.borrower.tax_id
            },
            "terms": {
                "principal": str(self.terms.principal),
                "currency": self.terms.currency.name,
                "interest_rate": str(self.terms.interest_rate),
                "term_months": self.terms.term_months,
                "start_date": self.terms.start_date.isoformat(),
                "repayment_schedule": self.terms.repayment_schedule
            },
            "exchange_rate": {
                "from_currency": self.exchange_rate.from_currency.name if self.exchange_rate else None,
                "to_currency": self.exchange_rate.to_currency.name if self.exchange_rate else None,
                "rate": str(self.exchange_rate.rate) if self.exchange_rate else None,
                "effective_date": self.exchange_rate.effective_date.isoformat() if self.exchange_rate else None
            } if self.exchange_rate else None,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'LoanTransaction':
        """Deserialize dictionary to LoanTransaction"""
        borrower_data = data["borrower"]
        terms_data = data["terms"]
        exchange_data = data.get("exchange_rate")
        
        return cls(
            transaction_id=data["transaction_id"],
            borrower=Borrower(
                id=borrower_data["id"],
                name=borrower_data["name"],
                credit_score=borrower_data["credit_score"],
                tax_id=borrower_data.get("tax_id")
            ),
            terms=LoanTerms(
                principal=Decimal(terms_data["principal"]),
                currency=Currency[terms_data["currency"]],
                interest_rate=Decimal(terms_data["interest_rate"]),
                term_months=terms_data["term_months"],
                start_date=date.fromisoformat(terms_data["start_date"]),
                repayment_schedule=terms_data["repayment_schedule"]
            ),
            exchange_rate=ExchangeRate(
                from_currency=Currency[exchange_data["from_currency"]],
                to_currency=Currency[exchange_data["to_currency"]],
                rate=Decimal(exchange_data["rate"]),
                effective_date=date.fromisoformat(exchange_data["effective_date"])
            ) if exchange_data else None,
            created_at=datetime.fromisoformat(data["created_at"])
        )

    def to_json(self) -> str:
        """Serialize transaction to JSON"""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'LoanTransaction':
        """Deserialize JSON to LoanTransaction"""
        return cls.from_dict(json.loads(json_str))

class LoanTransactionManager:
    """Manages a collection of loan transactions"""
    def __init__(self):
        self.transactions: dict[str, LoanTransaction] = {}

    def add_transaction(self, transaction: LoanTransaction) -> None:
        """Add a new transaction to the manager"""
        if transaction.transaction_id in self.transactions:
            raise ValueError(f"Transaction ID {transaction.transaction_id} already exists")
        self.transactions[transaction.transaction_id] = transaction

    def get_transaction(self, transaction_id: str) -> LoanTransaction:
        """Retrieve a transaction by ID"""
        if transaction_id not in self.transactions:
            raise ValueError(f"Transaction ID {transaction_id} not found")
        return self.transactions[transaction_id]

    def get_total_exposure(self, currency: Currency = Currency.LOCAL) -> Decimal:
        """Calculate total exposure in specified currency"""
        total = Decimal('0')
        for transaction in self.transactions.values():
            if transaction.terms.currency == currency:
                total += transaction.terms.principal
            else:
                total += transaction.to_local_currency()
        return total

    def save_to_file(self, filename: str) -> None:
        """Save all transactions to a JSON file"""
        data = [t.to_dict() for t in self.transactions.values()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'LoanTransactionManager':
        """Load transactions from a JSON file"""
        manager = cls()
        with open(filename) as f:
            data = json.load(f)
            for item in data:
                transaction = LoanTransaction.from_dict(item)
                manager.add_transaction(transaction)
        return manager
```
