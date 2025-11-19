"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: "Compare the costs and benefits of purchasing a car from a US auction site versus buying from a local dealership in Poland."
Generated: DETERMINISTIC_9bf73b90f1ab728d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares the costs and benefits of purchasing a car from a US auction site versus buying from a local dealership in Poland.
It calculates total costs including taxes, shipping, and other fees for both options.
"""

import math
from dataclasses import dataclass
from typing import Optional

@dataclass
class CarPurchaseOption:
    """Represents a car purchase option with associated costs and benefits."""
    name: str
    base_price: float  # in USD
    shipping_cost: float = 0.0  # in USD
    import_tax_percent: float = 0.0  # percentage
    customs_duty_percent: float = 0.0  # percentage
    registration_fee: float = 0.0  # in USD
    warranty_years: int = 0
    delivery_time_days: int = 0
    has_warranty: bool = False

    def total_cost(self) -> float:
        """Calculate total cost including all fees and taxes."""
        tax_and_duty = (self.import_tax_percent + self.customs_duty_percent) / 100
        taxed_amount = self.base_price * (1 + tax_and_duty)
        return taxed_amount + self.shipping_cost + self.registration_fee

    def cost_benefit_score(self) -> float:
        """Calculate a simple cost-benefit score (lower is better)."""
        cost_factor = self.total_cost() / 1000  # normalize cost
        warranty_factor = 1 / (self.warranty_years + 1)  # more warranty is better
        time_factor = math.log(self.delivery_time_days + 1)  # logarithmic scale for time
        
        return cost_factor * warranty_factor * time_factor

def compare_purchase_options(us_auction: CarPurchaseOption, local_dealership: CarPurchaseOption) -> dict:
    """
    Compare two car purchase options and return a comparison dictionary.
    
    Args:
        us_auction: CarPurchaseOption for US auction purchase
        local_dealership: CarPurchaseOption for local dealership purchase
    
    Returns:
        Dictionary with comparison results
    """
    comparison = {
        'us_auction_total': us_auction.total_cost(),
        'local_dealership_total': local_dealership.total_cost(),
        'price_difference': local_dealership.total_cost() - us_auction.total_cost(),
        'us_auction_score': us_auction.cost_benefit_score(),
        'local_dealership_score': local_dealership.cost_benefit_score(),
        'recommendation': 'US Auction' if us_auction.cost_benefit_score() < local_dealership.cost_benefit_score() else 'Local Dealership',
        'cost_savings_percent': ((local_dealership.total_cost() - us_auction.total_cost()) / local_dealership.total_cost()) * 100
    }
    return comparison

def get_user_input() -> tuple[CarPurchaseOption, CarPurchaseOption]:
    """Get user input for both purchase options."""
    print("Enter details for US Auction purchase:")
    us_base = float(input("Base price (USD): "))
    us_shipping = float(input("Shipping cost (USD): "))
    us_tax = float(input("Import tax percentage: "))
    us_duty = float(input("Customs duty percentage: "))
    us_reg = float(input("Registration fee (USD): "))
    us_warranty = int(input("Warranty years (0 if none): "))
    us_delivery = int(input("Delivery time (days): "))
    
    print("\nEnter details for Local Dealership purchase:")
    local_base = float(input("Base price (USD): "))
    local_warranty = int(input("Warranty years: "))
    local_delivery = int(input("Delivery time (days): "))
    
    us_option = CarPurchaseOption(
        name="US Auction",
        base_price=us_base,
        shipping_cost=us_shipping,
        import_tax_percent=us_tax,
        customs_duty_percent=us_duty,
        registration_fee=us_reg,
        warranty_years=us_warranty,
        delivery_time_days=us_delivery,
        has_warranty=us_warranty > 0
    )
    
    local_option = CarPurchaseOption(
        name="Local Dealership",
        base_price=local_base,
        warranty_years=local_warranty,
        delivery_time_days=local_delivery,
        has_warranty=local_warranty > 0
    )
    
    return us_option, local_option

def display_comparison(comparison: dict) -> None:
    """Display the comparison results in a user-friendly format."""
    print("\n=== Purchase Comparison ===")
    print(f"US Auction Total Cost: ${comparison['us_auction_total']:,.2f}")
    print(f"Local Dealership Total Cost: ${comparison['local_dealership_total']:,.2f}")
    print(f"\nPrice Difference: ${comparison['price_difference']:,.2f} ({comparison['cost_savings_percent']:.2f}%)")
    print(f"\nUS Auction Score: {comparison['us_auction_score']:.2f}")
    print(f"Local Dealership Score: {comparison['local_dealership_score']:.2f}")
    print(f"\nRecommendation: {comparison['recommendation']}")

def main() -> None:
    """Main function to run the car purchase comparison."""
    try:
        print("Car Purchase Comparison Tool (US Auction vs Local Dealership in Poland)")
        us_option, local_option = get_user_input()
        comparison = compare_purchase_options(us_option, local_option)
        display_comparison(comparison)
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
