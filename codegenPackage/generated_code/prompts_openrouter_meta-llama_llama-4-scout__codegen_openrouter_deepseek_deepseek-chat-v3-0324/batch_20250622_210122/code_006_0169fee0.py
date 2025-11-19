"""
Generated Code Metadata:
========================
Original URL: https://protocalrpc-stakestone.pages.dev
Prompt: Create a basic example of using StakeStone's STONE token in a derivatives market, specifically for creating a crypto T-Bill portfolio for capital principal protected structured products.
Generated: DETERMINISTIC_0169fee00545727d
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from typing import Dict, List, Tuple
from dataclasses import dataclass
from decimal import Decimal, getcontext
from enum import Enum, auto
import math

# Set precision for Decimal calculations
getcontext().prec = 18

class TokenType(Enum):
    STONE = auto()
    STABLE = auto()
    UNDERLYING = auto()

@dataclass
class Token:
    token_type: TokenType
    symbol: str
    decimals: int
    price: Decimal  # Price in USD

@dataclass
class Position:
    token: Token
    amount: Decimal

class Portfolio:
    def __init__(self):
        self.positions: Dict[str, Position] = {}
        self.total_value: Decimal = Decimal('0')
    
    def add_position(self, token: Token, amount: Decimal) -> None:
        if token.symbol in self.positions:
            self.positions[token.symbol].amount += amount
        else:
            self.positions[token.symbol] = Position(token, amount)
        
        self._update_total_value()
    
    def _update_total_value(self) -> None:
        self.total_value = Decimal('0')
        for position in self.positions.values():
            self.total_value += position.amount * position.token.price
    
    def get_composition(self) -> Dict[str, Decimal]:
        composition = {}
        for symbol, position in self.positions.items():
            composition[symbol] = (position.amount * position.token.price) / self.total_value
        return composition

class StructuredProduct:
    def __init__(self, principal: Decimal, duration_days: int):
        self.principal = principal
        self.duration_days = duration_days
        self.portfolio = Portfolio()
        self.min_principal_protection = Decimal('0.95')  # 95% principal protection
    
    def add_asset(self, token: Token, allocation: Decimal) -> None:
        """Add asset to the structured product portfolio"""
        if allocation < 0 or allocation > 1:
            raise ValueError("Allocation must be between 0 and 1")
        
        amount = (self.principal * allocation) / token.price
        self.portfolio.add_position(token, amount)
    
    def calculate_risk(self) -> Decimal:
        """Calculate portfolio risk based on asset volatility"""
        # Simplified risk calculation - in practice would use historical volatility
        risk_score = Decimal('0')
        composition = self.portfolio.get_composition()
        
        for symbol, weight in composition.items():
            if symbol == "STONE":
                risk_score += weight * Decimal('0.1')  # Low risk
            elif symbol == "USDC":
                risk_score += weight * Decimal('0.01')  # Very low risk
            else:
                risk_score += weight * Decimal('0.3')  # Higher risk
        
        return risk_score
    
    def is_principal_protected(self) -> bool:
        """Check if principal protection criteria are met"""
        risk = self.calculate_risk()
        protection_factor = Decimal('1') - risk
        
        return protection_factor >= self.min_principal_protection
    
    def simulate_performance(self, price_changes: Dict[str, Decimal]) -> Decimal:
        """Simulate portfolio performance based on price changes"""
        final_value = Decimal('0')
        
        for symbol, position in self.portfolio.positions.items():
            price_change = price_changes.get(symbol, Decimal('0'))
            new_price = position.token.price * (Decimal('1') + price_change)
            final_value += position.amount * new_price
        
        return final_value

# Example usage
if __name__ == "__main__":
    # Define tokens
    stone_token = Token(
        token_type=TokenType.STONE,
        symbol="STONE",
        decimals=18,
        price=Decimal('1.05')  # $1.05 per STONE
    )
    
    stable_token = Token(
        token_type=TokenType.STABLE,
        symbol="USDC",
        decimals=6,
        price=Decimal('1.00')  # $1.00 per USDC
    )
    
    underlying_token = Token(
        token_type=TokenType.UNDERLYING,
        symbol="ETH",
        decimals=18,
        price=Decimal('2500.00')  # $2500 per ETH
    )
    
    # Create structured product
    product = StructuredProduct(
        principal=Decimal('100000'),  # $100,000 principal
        duration_days=90  # 90-day duration
    )
    
    # Allocate assets
    try:
        product.add_asset(stone_token, Decimal('0.6'))  # 60% STONE
        product.add_asset(stable_token, Decimal('0.3'))  # 30% USDC
        product.add_asset(underlying_token, Decimal('0.1'))  # 10% ETH
        
        # Check principal protection
        if product.is_principal_protected():
            print("✅ Product meets principal protection requirements")
        else:
            print("⚠️ Product does not meet principal protection requirements")
        
        # Simulate performance
        price_changes = {
            "STONE": Decimal('0.05'),  # +5%
            "USDC": Decimal('0.00'),   # 0%
            "ETH": Decimal('0.10')    # +10%
        }
        
        final_value = product.simulate_performance(price_changes)
        roi = (final_value - product.principal) / product.principal
        print(f"Projected final value: ${final_value:.2f}")
        print(f"Projected ROI: {roi*100:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
