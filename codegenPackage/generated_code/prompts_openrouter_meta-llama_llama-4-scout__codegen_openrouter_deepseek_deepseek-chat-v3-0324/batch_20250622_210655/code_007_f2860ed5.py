"""
Generated Code Metadata:
========================
Original URL: https://creditu.com.ar
Prompt: "Develop a pricing strategy algorithm for an e-commerce platform like Creditu, considering factors like product category, financing options, and customer location."
Generated: DETERMINISTIC_f2860ed5e24e10be
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import math

class ProductCategory(Enum):
    ELECTRONICS = "electronics"
    FURNITURE = "furniture"
    CLOTHING = "clothing"
    APPLIANCES = "appliances"
    OTHER = "other"

class FinancingOption(Enum):
    CASH = "cash"
    EMI_3_MONTHS = "emi_3_months"
    EMI_6_MONTHS = "emi_6_months"
    EMI_12_MONTHS = "emi_12_months"

@dataclass
class CustomerLocation:
    country: str
    state: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None

@dataclass
class Product:
    base_price: float
    category: ProductCategory
    cost_price: float
    min_margin: float = 0.1

class PricingStrategy:
    def __init__(self):
        self.category_multipliers = {
            ProductCategory.ELECTRONICS: 1.2,
            ProductCategory.FURNITURE: 1.3,
            ProductCategory.CLOTHING: 1.1,
            ProductCategory.APPLIANCES: 1.25,
            ProductCategory.OTHER: 1.0
        }
        
        self.financing_multipliers = {
            FinancingOption.CASH: 0.98,
            FinancingOption.EMI_3_MONTHS: 1.0,
            FinancingOption.EMI_6_MONTHS: 1.05,
            FinancingOption.EMI_12_MONTHS: 1.1
        }
        
        self.location_surcharges = {
            "US": {"base": 0.0, "states": {"CA": 0.02, "NY": 0.03}},
            "UK": {"base": 0.0, "cities": {"London": 0.05}},
            "IN": {"base": 0.0, "states": {"MH": 0.01, "DL": 0.02}}
        }

    def _get_location_surcharge(self, location: CustomerLocation) -> float:
        """Calculate location-based surcharge."""
        surcharge = 0.0
        country_data = self.location_surcharges.get(location.country)
        
        if country_data:
            surcharge = country_data["base"]
            
            if location.state and "states" in country_data:
                surcharge += country_data["states"].get(location.state, 0.0)
            
            if location.city and "cities" in country_data:
                surcharge += country_data["cities"].get(location.city, 0.0)
        
        return surcharge

    def calculate_price(
        self,
        product: Product,
        financing_option: FinancingOption,
        location: CustomerLocation,
        quantity: int = 1
    ) -> float:
        """
        Calculate final price considering all factors.
        
        Args:
            product: Product information
            financing_option: Selected financing option
            location: Customer location details
            quantity: Quantity of items (default 1)
            
        Returns:
            Final calculated price
            
        Raises:
            ValueError: If inputs are invalid
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if product.base_price <= 0:
            raise ValueError("Base price must be positive")
        
        if product.cost_price <= 0:
            raise ValueError("Cost price must be positive")
        
        # Apply category multiplier
        category_multiplier = self.category_multipliers.get(product.category, 1.0)
        price = product.base_price * category_multiplier
        
        # Ensure minimum margin
        min_price = product.cost_price * (1 + product.min_margin)
        price = max(price, min_price)
        
        # Apply financing option multiplier
        financing_multiplier = self.financing_multipliers.get(financing_option, 1.0)
        price *= financing_multiplier
        
        # Apply location surcharge
        location_surcharge = self._get_location_surcharge(location)
        price *= (1 + location_surcharge)
        
        # Apply quantity discount
        if quantity > 1:
            quantity_discount = min(0.1, math.log10(quantity) * 0.05)
            price *= (1 - quantity_discount)
        
        return round(price * quantity, 2)

# Example usage
if __name__ == "__main__":
    try:
        strategy = PricingStrategy()
        
        product = Product(
            base_price=1000.0,
            category=ProductCategory.ELECTRONICS,
            cost_price=800.0,
            min_margin=0.15
        )
        
        location = CustomerLocation(
            country="US",
            state="CA",
            city="San Francisco"
        )
        
        final_price = strategy.calculate_price(
            product=product,
            financing_option=FinancingOption.EMI_6_MONTHS,
            location=location,
            quantity=2
        )
        
        print(f"Final price: ${final_price}")
        
    except ValueError as e:
        print(f"Error calculating price: {e}")
```
