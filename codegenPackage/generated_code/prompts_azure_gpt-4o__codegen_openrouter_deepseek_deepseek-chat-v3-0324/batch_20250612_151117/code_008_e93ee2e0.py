"""
Generated Code Metadata:
========================
Original URL: https://winusdt.top
Prompt: Write code to simulate a VIP account feature for a USDT trading platform, including exclusive deposit and withdrawal limits.
Generated: DETERMINISTIC_e93ee2e05b668884
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Optional, Dict, Any

class AccountType(Enum):
    REGULAR = "REGULAR"
    VIP = "VIP"

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"

class TransactionLimit:
    def __init__(self, min_amount: float, max_amount: float):
        self.min_amount = min_amount
        self.max_amount = max_amount

class Account:
    def __init__(self, account_id: str, account_type: AccountType, balance: float = 0.0):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.transaction_limits = self._initialize_limits()

    def _initialize_limits(self) -> Dict[TransactionType, TransactionLimit]:
        if self.account_type == AccountType.VIP:
            return {
                TransactionType.DEPOSIT: TransactionLimit(min_amount=1000.0, max_amount=1000000.0),
                TransactionType.WITHDRAWAL: TransactionLimit(min_amount=500.0, max_amount=500000.0)
            }
        else:
            return {
                TransactionType.DEPOSIT: TransactionLimit(min_amount=100.0, max_amount=100000.0),
                TransactionType.WITHDRAWAL: TransactionLimit(min_amount=50.0, max_amount=50000.0)
            }

    def process_transaction(self, transaction_type: TransactionType, amount: float) -> Dict[str, Any]:
        try:
            limit = self.transaction_limits[transaction_type]
            
            if amount < limit.min_amount:
                return {
                    "success": False,
                    "message": f"Amount below minimum {transaction_type.value} limit of {limit.min_amount} USDT"
                }
            
            if amount > limit.max_amount:
                return {
                    "success": False,
                    "message": f"Amount exceeds maximum {transaction_type.value} limit of {limit.max_amount} USDT"
                }
            
            if transaction_type == TransactionType.DEPOSIT:
                self.balance += amount
            elif transaction_type == TransactionType.WITHDRAWAL:
                if amount > self.balance:
                    return {
                        "success": False,
                        "message": "Insufficient balance for withdrawal"
                    }
                self.balance -= amount
            
            return {
                "success": True,
                "message": f"{transaction_type.value} successful",
                "new_balance": self.balance
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Transaction failed: {str(e)}"
            }

    def get_account_info(self) -> Dict[str, Any]:
        return {
            "account_id": self.account_id,
            "account_type": self.account_type.value,
            "balance": self.balance,
            "limits": {
                ttype.value: {
                    "min": limit.min_amount,
                    "max": limit.max_amount
                } for ttype, limit in self.transaction_limits.items()
            }
        }

class TradingPlatform:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_id: str, account_type: AccountType) -> Dict[str, Any]:
        if account_id in self.accounts:
            return {
                "success": False,
                "message": "Account ID already exists"
            }
        
        self.accounts[account_id] = Account(account_id, account_type)
        return {
            "success": True,
            "message": "Account created successfully",
            "account_info": self.accounts[account_id].get_account_info()
        }

    def get_account(self, account_id: str) -> Optional[Account]:
        return self.accounts.get(account_id)

    def process_transaction(self, account_id: str, transaction_type: TransactionType, amount: float) -> Dict[str, Any]:
        account = self.get_account(account_id)
        if not account:
            return {
                "success": False,
                "message": "Account not found"
            }
        
        return account.process_transaction(transaction_type, amount)

    def get_account_info(self, account_id: str) -> Dict[str, Any]:
        account = self.get_account(account_id)
        if not account:
            return {
                "success": False,
                "message": "Account not found"
            }
        
        return {
            "success": True,
            "account_info": account.get_account_info()
        }

# Example usage
if __name__ == "__main__":
    platform = TradingPlatform()
    
    # Create accounts
    print(json.dumps(platform.create_account("user123", AccountType.REGULAR), indent=2))
    print(json.dumps(platform.create_account("vip456", AccountType.VIP), indent=2))
    
    # Process transactions
    print(json.dumps(platform.process_transaction("user123", TransactionType.DEPOSIT, 500.0), indent=2))
    print(json.dumps(platform.process_transaction("vip456", TransactionType.DEPOSIT, 50000.0), indent=2))
    print(json.dumps(platform.process_transaction("user123", TransactionType.WITHDRAWAL, 100000.0), indent=2))  # Should fail
    
    # Get account info
    print(json.dumps(platform.get_account_info("vip456"), indent=2))
```
