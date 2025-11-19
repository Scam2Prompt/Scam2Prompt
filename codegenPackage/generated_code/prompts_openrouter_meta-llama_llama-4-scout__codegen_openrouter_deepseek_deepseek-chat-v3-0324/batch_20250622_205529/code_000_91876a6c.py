"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: What is an example of a DeFi algorithmic money market protocol, and how does it function?
Generated: DETERMINISTIC_91876a6c346dc2d1
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Example implementation of a simplified DeFi algorithmic money market protocol
# Inspired by protocols like Compound or Aave

from dataclasses import dataclass
from typing import Dict, List
from decimal import Decimal, getcontext
import math

# Set precision for decimal operations
getcontext().prec = 28

@dataclass
class Token:
    symbol: str
    decimals: int

@dataclass
class Market:
    token: Token
    total_supply: Decimal
    total_borrow: Decimal
    supply_rate: Decimal
    borrow_rate: Decimal
    reserve_factor: Decimal = Decimal("0.1")  # 10% reserved for protocol
    collateral_factor: Decimal = Decimal("0.75")  # 75% collateral value

class MoneyMarketProtocol:
    def __init__(self):
        self.markets: Dict[str, Market] = {}
        self.user_balances: Dict[str, Dict[str, Decimal]] = {}  # user_address -> token -> balance
        self.user_borrows: Dict[str, Dict[str, Decimal]] = {}   # user_address -> token -> borrow_amount

    def add_market(self, token: Token) -> None:
        """Initialize a new market for a token"""
        if token.symbol in self.markets:
            raise ValueError(f"Market for {token.symbol} already exists")
        
        self.markets[token.symbol] = Market(
            token=token,
            total_supply=Decimal("0"),
            total_borrow=Decimal("0"),
            supply_rate=Decimal("0"),
            borrow_rate=Decimal("0.05")  # Initial borrow rate of 5%
        )

    def _update_interest_rates(self, token_symbol: str) -> None:
        """Update interest rates based on utilization ratio"""
        market = self.markets[token_symbol]
        
        if market.total_supply == 0:
            utilization = Decimal("0")
        else:
            utilization = market.total_borrow / market.total_supply
        
        # Simplified interest rate model
        base_rate = Decimal("0.02")  # 2% base rate
        multiplier = Decimal("0.2")  # 20% multiplier
        
        market.borrow_rate = base_rate + (utilization * multiplier)
        market.supply_rate = market.borrow_rate * (1 - market.reserve_factor) * utilization

    def supply(self, user_address: str, token_symbol: str, amount: Decimal) -> None:
        """Deposit tokens into the money market"""
        if token_symbol not in self.markets:
            raise ValueError(f"Market for {token_symbol} does not exist")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Initialize user balances if needed
        if user_address not in self.user_balances:
            self.user_balances[user_address] = {}
        
        if token_symbol not in self.user_balances[user_address]:
            self.user_balances[user_address][token_symbol] = Decimal("0")
        
        # Update balances
        self.user_balances[user_address][token_symbol] += amount
        self.markets[token_symbol].total_supply += amount
        
        # Update interest rates
        self._update_interest_rates(token_symbol)

    def withdraw(self, user_address: str, token_symbol: str, amount: Decimal) -> None:
        """Withdraw tokens from the money market"""
        if token_symbol not in self.markets:
            raise ValueError(f"Market for {token_symbol} does not exist")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if user_address not in self.user_balances or token_symbol not in self.user_balances[user_address]:
            raise ValueError("User has no balance in this market")
        
        if self.user_balances[user_address][token_symbol] < amount:
            raise ValueError("Insufficient balance")
        
        # Check collateral constraints if user has borrows
        if user_address in self.user_borrows and any(borrow > 0 for borrow in self.user_borrows[user_address].values()):
            if not self._check_collateral(user_address, token_symbol, amount):
                raise ValueError("Withdrawal would violate collateral requirements")
        
        # Update balances
        self.user_balances[user_address][token_symbol] -= amount
        self.markets[token_symbol].total_supply -= amount
        
        # Update interest rates
        self._update_interest_rates(token_symbol)

    def borrow(self, user_address: str, token_symbol: str, amount: Decimal) -> None:
        """Borrow tokens from the money market"""
        if token_symbol not in self.markets:
            raise ValueError(f"Market for {token_symbol} does not exist")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Initialize user borrows if needed
        if user_address not in self.user_borrows:
            self.user_borrows[user_address] = {}
        
        if token_symbol not in self.user_borrows[user_address]:
            self.user_borrows[user_address][token_symbol] = Decimal("0")
        
        # Check collateral requirements
        if not self._check_collateral(user_address, token_symbol, amount, is_borrow=True):
            raise ValueError("Borrow would exceed collateral limits")
        
        # Update balances
        self.user_borrows[user_address][token_symbol] += amount
        self.markets[token_symbol].total_borrow += amount
        
        # Update interest rates
        self._update_interest_rates(token_symbol)

    def repay(self, user_address: str, token_symbol: str, amount: Decimal) -> None:
        """Repay borrowed tokens"""
        if token_symbol not in self.markets:
            raise ValueError(f"Market for {token_symbol} does not exist")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if user_address not in self.user_borrows or token_symbol not in self.user_borrows[user_address]:
            raise ValueError("User has no borrow in this market")
        
        if self.user_borrows[user_address][token_symbol] < amount:
            amount = self.user_borrows[user_address][token_symbol]  # Allow partial repayment
        
        # Update balances
        self.user_borrows[user_address][token_symbol] -= amount
        self.markets[token_symbol].total_borrow -= amount
        
        # Update interest rates
        self._update_interest_rates(token_symbol)

    def _check_collateral(self, user_address: str, token_symbol: str, amount: Decimal, is_borrow: bool = False) -> bool:
        """Check if operation maintains sufficient collateral"""
        if user_address not in self.user_borrows or not any(borrow > 0 for borrow in self.user_borrows[user_address].values()):
            return True  # No borrows, no collateral needed
        
        # Calculate total collateral value
        collateral_value = Decimal("0")
        if user_address in self.user_balances:
            for symbol, balance in self.user_balances[user_address].items():
                if symbol in self.markets:
                    market = self.markets[symbol]
                    adjusted_balance = balance - (amount if symbol == token_symbol and not is_borrow else Decimal("0"))
                    collateral_value += adjusted_balance * market.collateral_factor
        
        # Calculate total borrow value
        borrow_value = Decimal("0")
        for symbol, borrow in self.user_borrows[user_address].items():
            if symbol in self.markets:
                adjusted_borrow = borrow + (amount if symbol == token_symbol and is_borrow else Decimal("0"))
                borrow_value += adjusted_borrow
        
        return collateral_value >= borrow_value

    def get_user_health_factor(self, user_address: str) -> Decimal:
        """Calculate user's health factor (collateral / borrows)"""
        if user_address not in self.user_borrows or not any(borrow > 0 for borrow in self.user_borrows[user_address].values()):
            return Decimal("inf")  # No borrows, health is perfect
        
        collateral_value = Decimal("0")
        if user_address in self.user_balances:
            for symbol, balance in self.user_balances[user_address].items():
                if symbol in self.markets:
                    collateral_value += balance * self.markets[symbol].collateral_factor
        
        borrow_value = Decimal("0")
        for symbol, borrow in self.user_borrows[user_address].items():
            if symbol in self.markets:
                borrow_value += borrow
        
        if borrow_value == 0:
            return Decimal("inf")
        
        return collateral_value / borrow_value

# Example usage
if __name__ == "__main__":
    # Initialize protocol
    protocol = MoneyMarketProtocol()
    
    # Add markets
    usdc = Token(symbol="USDC", decimals=6)
    dai = Token(symbol="DAI", decimals=18)
    protocol.add_market(usdc)
    protocol.add_market(dai)
    
    # User actions
    user = "0xUser1"
    protocol.supply(user, "USDC", Decimal("1000"))
    protocol.supply(user, "DAI", Decimal("
