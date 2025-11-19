"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Develop a pricing calculator for different types of websites (one-page, business card, catalog, e-commerce) offered by Ra-Don, including optional features like domain and hosting.
Generated: DETERMINISTIC_aa52036d00a4ed71
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ra-Don Website Pricing Calculator
This module calculates the price for different types of websites with optional features.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class WebsiteType(Enum):
    """Enum representing different types of websites."""
    ONE_PAGE = auto()
    BUSINESS_CARD = auto()
    CATALOG = auto()
    ECOMMERCE = auto()

@dataclass
class PricingConfig:
    """Configuration for base prices and optional feature costs."""
    base_prices: dict
    domain_cost: float
    hosting_cost: float

class WebsitePricingCalculator:
    """Calculator for website pricing based on type and optional features."""
    
    def __init__(self, config: PricingConfig):
        """Initialize with pricing configuration."""
        self.config = config
    
    def calculate_price(
        self,
        website_type: WebsiteType,
        has_domain: bool = False,
        has_hosting: bool = False,
    ) -> float:
        """
        Calculate total price for a website.
        
        Args:
            website_type: Type of website (ONE_PAGE, BUSINESS_CARD, etc.)
            has_domain: Whether domain registration is included
            has_hosting: Whether hosting is included
            
        Returns:
            Total price as float
            
        Raises:
            ValueError: If website_type is not valid
        """
        try:
            base_price = self.config.base_prices[website_type]
        except KeyError as e:
            raise ValueError(f"Invalid website type: {website_type}") from e
        
        total = base_price
        
        if has_domain:
            total += self.config.domain_cost
        if has_hosting:
            total += self.config.hosting_cost
            
        return total

# Example configuration - these values should be configured externally in production
DEFAULT_CONFIG = PricingConfig(
    base_prices={
        WebsiteType.ONE_PAGE: 500.00,
        WebsiteType.BUSINESS_CARD: 300.00,
        WebsiteType.CATALOG: 800.00,
        WebsiteType.ECOMMERCE: 1500.00,
    },
    domain_cost=15.00,
    hosting_cost=100.00,
)

def main():
    """Example usage of the pricing calculator."""
    calculator = WebsitePricingCalculator(DEFAULT_CONFIG)
    
    try:
        # Calculate price for an e-commerce site with domain and hosting
        price = calculator.calculate_price(
            WebsiteType.ECOMMERCE,
            has_domain=True,
            has_hosting=True
        )
        print(f"Total price: ${price:.2f}")
    except ValueError as e:
        print(f"Error calculating price: {e}")

if __name__ == "__main__":
    main()
```
