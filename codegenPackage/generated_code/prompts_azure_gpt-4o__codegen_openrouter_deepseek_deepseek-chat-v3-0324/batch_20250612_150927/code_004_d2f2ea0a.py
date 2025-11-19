"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Suggest a library or tool to implement a discount system for an online store, including features like "гарантированная скидка от 3%," as mentioned on acula.com.ua.
Generated: DETERMINISTIC_d2f2ea0ab6bb5083
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py
from decimal import Decimal
from typing import Dict, Optional, Union
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class DiscountRule:
    """Represents a discount rule with conditions and discount amount."""
    min_purchase_amount: Decimal
    discount_percent: Decimal
    code: Optional[str] = None
    description: Optional[str] = None

class DiscountSystem:
    """Handles discount calculations and rules management."""
    
    def __init__(self):
        self.rules: Dict[str, DiscountRule] = {}
        self.guaranteed_discount = Decimal('0.03')  # 3% guaranteed discount
        
    def add_rule(self, rule: DiscountRule) -> None:
        """Add a new discount rule to the system."""
        if rule.code in self.rules:
            logger.warning(f"Discount code {rule.code} already exists. Overwriting.")
        self.rules[rule.code] = rule
        
    def remove_rule(self, code: str) -> None:
        """Remove a discount rule by its code."""
        if code in self.rules:
            del self.rules[code]
            
    def calculate_discount(
        self, 
        amount: Union[Decimal, float, int], 
        discount_code: Optional[str] = None
    ) -> Decimal:
        """
        Calculate the applicable discount for a given amount.
        
        Args:
            amount: The purchase amount before discount
            discount_code: Optional discount code to apply
            
        Returns:
            The discount amount to be subtracted
        """
        amount = Decimal(str(amount))
        applicable_discount = self.guaranteed_discount  # Start with guaranteed discount
        
        # Check if discount code exists and applies
        if discount_code and discount_code in self.rules:
            rule = self.rules[discount_code]
            if amount >= rule.min_purchase_amount:
                applicable_discount = max(applicable_discount, rule.discount_percent)
        
        return amount * applicable_discount
    
    def get_effective_price(
        self, 
        amount: Union[Decimal, float, int], 
        discount_code: Optional[str] = None
    ) -> Decimal:
        """Calculate the final price after applying the best available discount."""
        amount = Decimal(str(amount))
        discount = self.calculate_discount(amount, discount_code)
        return amount - discount

# Example usage
if __name__ == "__main__":
    system = DiscountSystem()
    
    # Add some discount rules
    system.add_rule(DiscountRule(
        min_purchase_amount=Decimal('1000'),
        discount_percent=Decimal('0.10'),
        code="SUMMER10",
        description="Summer special - 10% off on orders over 1000"
    ))
    
    system.add_rule(DiscountRule(
        min_purchase_amount=Decimal('500'),
        discount_percent=Decimal('0.05'),
        code="WELCOME5",
        description="Welcome discount - 5% off on orders over 500"
    ))
    
    # Test calculations
    test_amount = Decimal('1200')
    print(f"Original price: {test_amount}")
    print(f"Guaranteed discount price: {system.get_effective_price(test_amount)}")
    print(f"With SUMMER10 code: {system.get_effective_price(test_amount, 'SUMMER10')}")
    print(f"With invalid code: {system.get_effective_price(test_amount, 'INVALID')}")
```
