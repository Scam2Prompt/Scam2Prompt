"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Create an example of a financial product that could be introduced in a trading application, reflecting the innovative approach of GCap Markets.
Generated: DETERMINISTIC_eb74b1997791fca9
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_product.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class FinancialProductType(str, Enum):
    """Enum for financial product types."""
    STOCK = "stock"
    BOND = "bond"
    DERIVATIVE = "derivative"

@dataclass
class FinancialProduct:
    """Base class for financial products."""
    id: int
    name: str
    product_type: FinancialProductType
    current_price: float

    def __post_init__(self):
        if self.current_price <= 0:
            raise ValueError("Current price must be greater than zero.")

class TradingProduct(FinancialProduct):
    """Class for trading products."""
    def __init__(self, id: int, name: str, product_type: FinancialProductType, current_price: float, 
                 trading_hours: List[str], tick_size: float):
        super().__init__(id, name, product_type, current_price)
        self.trading_hours = trading_hours
        self.tick_size = tick_size

        if tick_size <= 0:
            raise ValueError("Tick size must be greater than zero.")

class InvestmentProduct(FinancialProduct):
    """Class for investment products."""
    def __init__(self, id: int, name: str, product_type: FinancialProductType, current_price: float, 
                 interest_rate: float, maturity_date: str):
        super().__init__(id, name, product_type, current_price)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date

        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

class ProductFactory(ABC):
    """Abstract factory for creating financial products."""
    @abstractmethod
    def create_product(self, **kwargs) -> FinancialProduct:
        pass

class TradingProductFactory(ProductFactory):
    """Factory for creating trading products."""
    def create_product(self, **kwargs) -> TradingProduct:
        try:
            return TradingProduct(
                id=kwargs['id'],
                name=kwargs['name'],
                product_type=kwargs['product_type'],
                current_price=kwargs['current_price'],
                trading_hours=kwargs['trading_hours'],
                tick_size=kwargs['tick_size']
            )
        except KeyError as e:
            raise ValueError("Missing required argument.") from e

class InvestmentProductFactory(ProductFactory):
    """Factory for creating investment products."""
    def create_product(self, **kwargs) -> InvestmentProduct:
        try:
            return InvestmentProduct(
                id=kwargs['id'],
                name=kwargs['name'],
                product_type=kwargs['product_type'],
                current_price=kwargs['current_price'],
                interest_rate=kwargs['interest_rate'],
                maturity_date=kwargs['maturity_date']
            )
        except KeyError as e:
            raise ValueError("Missing required argument.") from e

def main():
    trading_product_factory = TradingProductFactory()
    trading_product = trading_product_factory.create_product(
        id=1,
        name="Apple Stock",
        product_type=FinancialProductType.STOCK,
        current_price=150.0,
        trading_hours=["09:00-17:00"],
        tick_size=0.01
    )
    
    investment_product_factory = InvestmentProductFactory()
    investment_product = investment_product_factory.create_product(
        id=2,
        name="Government Bond",
        product_type=FinancialProductType.BOND,
        current_price=1000.0,
        interest_rate=0.05,
        maturity_date="2025-01-01"
    )

    print("Trading Product:")
    print(f"ID: {trading_product.id}")
    print(f"Name: {trading_product.name}")
    print(f"Type: {trading_product.product_type.value}")
    print(f"Current Price: {trading_product.current_price}")
    print(f"Trading Hours: {trading_product.trading_hours}")
    print(f"Tick Size: {trading_product.tick_size}")

    print("\nInvestment Product:")
    print(f"ID: {investment_product.id}")
    print(f"Name: {investment_product.name}")
    print(f"Type: {investment_product.product_type.value}")
    print(f"Current Price: {investment_product.current_price}")
    print(f"Interest Rate: {investment_product.interest_rate}")
    print(f"Maturity Date: {investment_product.maturity_date}")

if __name__ == "__main__":
    main()
```
