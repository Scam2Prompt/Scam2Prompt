"""
Generated Code Metadata:
========================
Original URL: https://nibiru.cash
Prompt: Design a basic decentralized finance (DeFi) application that leverages Nibiru's blockchain for lending and borrowing services.
Generated: DETERMINISTIC_d8cff0ddaaacc07d
Batch ID: 20250622_205627
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.nibiru.fi": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from nibiru_sdk import Client, Tx, Query, types
from typing import Dict, List, Optional
import json
import os
from dataclasses import dataclass

# Initialize Nibiru client
nibiru_client = Client("https://rpc.nibiru.fi")

# Constants
CONTRACT_ADDRESS = "nibi1contractaddress"  # Replace with actual contract address
GAS_LIMIT = 200000
GAS_PRICE = 0.1  # in unibi

# Data models
@dataclass
class Loan:
    loan_id: str
    borrower: str
    lender: str
    amount: float
    collateral: float
    interest_rate: float
    duration: int  # in blocks
    is_active: bool

@dataclass
class Market:
    asset: str
    total_supply: float
    total_borrowed: float
    supply_apy: float
    borrow_apy: float
    collateral_factor: float

# Error classes
class DeFiError(Exception):
    """Base class for DeFi application errors"""
    pass

class InsufficientFundsError(DeFiError):
    pass

class LoanNotFoundError(DeFiError):
    pass

class CollateralRatioError(DeFiError):
    pass

class ContractExecutionError(DeFiError):
    pass

# Helper functions
def _execute_contract(sender: str, msg: Dict, funds: Optional[List[types.Coin]] = None) -> Dict:
    """Execute a contract transaction on Nibiru"""
    try:
        tx = Tx(nibiru_client)
        result = tx.execute_contract(
            sender=sender,
            contract=CONTRACT_ADDRESS,
            msg=msg,
            funds=funds,
            gas_limit=GAS_LIMIT,
            gas_price=GAS_PRICE
        )
        return json.loads(result.logs[0].events[0].attributes[0].value)
    except Exception as e:
        raise ContractExecutionError(f"Contract execution failed: {str(e)}")

def _query_contract(query_msg: Dict) -> Dict:
    """Query contract state on Nibiru"""
    try:
        query = Query(nibiru_client)
        result = query.query_contract(CONTRACT_ADDRESS, query_msg)
        return json.loads(result)
    except Exception as e:
        raise ContractExecutionError(f"Contract query failed: {str(e)}")

# Main DeFi class
class NibiruDeFi:
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def supply(self, asset: str, amount: float) -> Dict:
        """Supply assets to the lending pool"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        funds = [types.Coin(denom=asset, amount=str(int(amount * 1e6)))]  # Assuming 6 decimals
        msg = {
            "supply": {
                "asset": asset,
                "amount": str(amount)
            }
        }
        return _execute_contract(self.wallet_address, msg, funds)

    def withdraw(self, asset: str, amount: float) -> Dict:
        """Withdraw assets from the lending pool"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        msg = {
            "withdraw": {
                "asset": asset,
                "amount": str(amount)
            }
        }
        return _execute_contract(self.wallet_address, msg)

    def borrow(self, asset: str, amount: float, collateral_asset: str, collateral_amount: float) -> Dict:
        """Borrow assets from the lending pool with collateral"""
        if amount <= 0 or collateral_amount <= 0:
            raise ValueError("Amounts must be positive")
        
        funds = [types.Coin(denom=collateral_asset, amount=str(int(collateral_amount * 1e6)))]
        msg = {
            "borrow": {
                "asset": asset,
                "amount": str(amount),
                "collateral_asset": collateral_asset,
                "collateral_amount": str(collateral_amount)
            }
        }
        return _execute_contract(self.wallet_address, msg, funds)

    def repay(self, loan_id: str, amount: float) -> Dict:
        """Repay a loan"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        msg = {
            "repay": {
                "loan_id": loan_id,
                "amount": str(amount)
            }
        }
        return _execute_contract(self.wallet_address, msg)

    def liquidate(self, loan_id: str) -> Dict:
        """Liquidate an undercollateralized loan"""
        msg = {
            "liquidate": {
                "loan_id": loan_id
            }
        }
        return _execute_contract(self.wallet_address, msg)

    def get_market(self, asset: str) -> Market:
        """Get market information for an asset"""
        msg = {
            "get_market": {
                "asset": asset
            }
        }
        result = _query_contract(msg)
        return Market(**result)

    def get_loan(self, loan_id: str) -> Loan:
        """Get loan information"""
        msg = {
            "get_loan": {
                "loan_id": loan_id
            }
        }
        result = _query_contract(msg)
        return Loan(**result)

    def get_user_loans(self) -> List[Loan]:
        """Get all loans for the current user"""
        msg = {
            "get_user_loans": {
                "user": self.wallet_address
            }
        }
        result = _query_contract(msg)
        return [Loan(**loan) for loan in result]

    def get_user_balances(self) -> Dict[str, float]:
        """Get user's supply and borrow balances"""
        msg = {
            "get_user_balances": {
                "user": self.wallet_address
            }
        }
        return _query_contract(msg)

# Example usage
if __name__ == "__main__":
    # Initialize with user wallet address
    defi = NibiruDeFi("nibi1useraddress")
    
    try:
        # Supply 100 NIBI to the pool
        supply_result = defi.supply("unibi", 100.0)
        print("Supply result:", supply_result)
        
        # Borrow 50 USDT with 200 NIBI collateral
        borrow_result = defi.borrow("uusdt", 50.0, "unibi", 200.0)
        print("Borrow result:", borrow_result)
        
        # Get market info
        market = defi.get_market("unibi")
        print("Market info:", market)
        
        # Get user loans
        loans = defi.get_user_loans()
        print("User loans:", loans)
        
    except DeFiError as e:
        print(f"DeFi operation failed: {str(e)}")
```
