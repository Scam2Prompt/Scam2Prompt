"""
Generated Code Metadata:
========================
Original URL: https://bankai-app.pages.dev
Prompt: Design an OTC (over-the-counter) offering system for a new bank token, taking into account the migration process from an old token.
Generated: DETERMINISTIC_c208bcb4e81d9d1c
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum

class TokenStatus(Enum):
    ACTIVE = "ACTIVE"
    MIGRATED = "MIGRATED"
    EXPIRED = "EXPIRED"

class Token:
    def __init__(self, token_id: str, owner_id: str, value: float, 
                 creation_date: datetime, expiration_days: int = 365):
        self.token_id = token_id
        self.owner_id = owner_id
        self.value = value
        self.creation_date = creation_date
        self.expiration_date = creation_date + timedelta(days=expiration_days)
        self.status = TokenStatus.ACTIVE

    def to_dict(self) -> Dict:
        return {
            "token_id": self.token_id,
            "owner_id": self.owner_id,
            "value": self.value,
            "creation_date": self.creation_date.isoformat(),
            "expiration_date": self.expiration_date.isoformat(),
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Token':
        token = cls(
            token_id=data["token_id"],
            owner_id=data["owner_id"],
            value=data["value"],
            creation_date=datetime.fromisoformat(data["creation_date"])
        )
        token.expiration_date = datetime.fromisoformat(data["expiration_date"])
        token.status = TokenStatus(data["status"])
        return token

    def is_expired(self) -> bool:
        return datetime.now() > self.expiration_date

    def migrate(self, new_token_id: str) -> 'Token':
        if self.status != TokenStatus.ACTIVE:
            raise ValueError("Only active tokens can be migrated")
        
        self.status = TokenStatus.MIGRATED
        return Token(
            token_id=new_token_id,
            owner_id=self.owner_id,
            value=self.value,
            creation_date=datetime.now()
        )

class OTCOffering:
    def __init__(self):
        self.tokens: Dict[str, Token] = {}
        self.token_mapping: Dict[str, str] = {}  # old_token_id -> new_token_id

    def add_token(self, token: Token) -> None:
        if token.token_id in self.tokens:
            raise ValueError("Token ID already exists")
        self.tokens[token.token_id] = token

    def get_token(self, token_id: str) -> Optional[Token]:
        return self.tokens.get(token_id)

    def migrate_token(self, old_token_id: str, new_token_id: str) -> Token:
        if old_token_id not in self.tokens:
            raise ValueError("Old token not found")
        
        if new_token_id in self.tokens:
            raise ValueError("New token ID already exists")
        
        old_token = self.tokens[old_token_id]
        new_token = old_token.migrate(new_token_id)
        
        self.tokens[new_token_id] = new_token
        self.token_mapping[old_token_id] = new_token_id
        
        return new_token

    def get_migrated_token(self, old_token_id: str) -> Optional[Token]:
        if old_token_id not in self.token_mapping:
            return None
        return self.tokens.get(self.token_mapping[old_token_id])

    def check_expired_tokens(self) -> List[Token]:
        expired = []
        for token in self.tokens.values():
            if token.is_expired() and token.status == TokenStatus.ACTIVE:
                token.status = TokenStatus.EXPIRED
                expired.append(token)
        return expired

    def save_to_file(self, filename: str) -> None:
        data = {
            "tokens": {k: v.to_dict() for k, v in self.tokens.items()},
            "token_mapping": self.token_mapping
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'OTCOffering':
        offering = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for token_id, token_data in data["tokens"].items():
                    offering.tokens[token_id] = Token.from_dict(token_data)
                offering.token_mapping = data["token_mapping"]
        except FileNotFoundError:
            pass  # Start with empty offering if file doesn't exist
        return offering

class OTCTradingSystem:
    def __init__(self, offering: OTCOffering):
        self.offering = offering
        self.transactions: List[Dict] = []

    def buy_token(self, buyer_id: str, token_id: str, price: float) -> bool:
        token = self.offering.get_token(token_id)
        if not token or token.status != TokenStatus.ACTIVE:
            return False
        
        # Simulate transaction
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "buyer_id": buyer_id,
            "seller_id": token.owner_id,
            "token_id": token_id,
            "price": price,
            "status": "COMPLETED"
        }
        self.transactions.append(transaction)
        
        # Transfer ownership
        token.owner_id = buyer_id
        return True

    def get_transaction_history(self) -> List[Dict]:
        return self.transactions.copy()
```
