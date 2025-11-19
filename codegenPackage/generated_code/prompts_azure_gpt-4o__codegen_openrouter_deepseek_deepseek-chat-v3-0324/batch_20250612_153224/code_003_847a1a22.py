"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: Create a program that calculates distribution costs and eliminates hidden fees, inspired by the transparent operations model of VIDA TRADE LLC.
Generated: DETERMINISTIC_847a1a2224566f43
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Distribution Cost Calculator with Transparent Fee Structure

This program calculates the total distribution costs for a product,
ensuring all fees are transparent and visible to the customer.
Inspired by VIDA TRADE LLC's transparent operations model.
"""

import sys
from decimal import Decimal, getcontext
from typing import Dict, Union

# Set precision for decimal calculations
getcontext().prec = 6

class DistributionCostCalculator:
    """
    A calculator for transparent distribution costs with no hidden fees.
    
    Attributes:
        base_cost (Decimal): The base manufacturing cost of the product
        shipping_cost (Decimal): Shipping cost per unit
        customs_duty (Decimal): Customs duty percentage (0-1)
        vat_rate (Decimal): VAT percentage (0-1)
        handling_fee (Decimal): Fixed handling fee per unit
        markup_percentage (Decimal): Markup percentage (0-1)
    """
    
    def __init__(
        self,
        base_cost: Union[Decimal, float, str],
        shipping_cost: Union[Decimal, float, str],
        customs_duty: Union[Decimal, float, str] = Decimal('0'),
        vat_rate: Union[Decimal, float, str] = Decimal('0'),
        handling_fee: Union[Decimal, float, str] = Decimal('0'),
        markup_percentage: Union[Decimal, float, str] = Decimal('0')
    ):
        """
        Initialize the calculator with all cost components.
        
        Args:
            base_cost: Base manufacturing cost per unit
            shipping_cost: Shipping cost per unit
            customs_duty: Customs duty percentage (default 0)
            vat_rate: VAT percentage (default 0)
            handling_fee: Fixed handling fee per unit (default 0)
            markup_percentage: Markup percentage (default 0)
        """
        try:
            self.base_cost = Decimal(str(base_cost))
            self.shipping_cost = Decimal(str(shipping_cost))
            self.customs_duty = Decimal(str(customs_duty))
            self.vat_rate = Decimal(str(vat_rate))
            self.handling_fee = Decimal(str(handling_fee))
            self.markup_percentage = Decimal(str(markup_percentage))
            
            self._validate_inputs()
            
        except Exception as e:
            raise ValueError(f"Invalid input value: {str(e)}")
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are non-negative and percentages are <= 1."""
        if any(val < Decimal('0') for val in [
            self.base_cost,
            self.shipping_cost,
            self.handling_fee
        ]):
            raise ValueError("Cost values cannot be negative")
            
        if any(val < Decimal('0') or val > Decimal('1') for val in [
            self.customs_duty,
            self.vat_rate,
            self.markup_percentage
        ]):
            raise ValueError("Percentage values must be between 0 and 1")
    
    def calculate_total_cost(self, quantity: int = 1) -> Dict[str, Decimal]:
        """
        Calculate the total distribution cost with transparent breakdown.
        
        Args:
            quantity: Number of units (default 1)
            
        Returns:
            Dictionary with cost breakdown and total
            
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        try:
            # Calculate base components
            total_base = self.base_cost * quantity
            total_shipping = self.shipping_cost * quantity
            total_handling = self.handling_fee * quantity
            
            # Calculate duties and taxes
            customs_duty_amount = (total_base + total_shipping) * self.customs_duty
            subtotal = total_base + total_shipping + total_handling + customs_duty_amount
            vat_amount = subtotal * self.vat_rate
            
            # Calculate final amounts
            pre_markup_total = subtotal + vat_amount
            markup_amount = pre_markup_total * self.markup_percentage
            total_cost = pre_markup_total + markup_amount
            
            return {
                'base_cost': total_base,
                'shipping_cost': total_shipping,
                'handling_fee': total_handling,
                'customs_duty': customs_duty_amount,
                'vat': vat_amount,
                'markup': markup_amount,
                'total_cost': total_cost,
                'cost_per_unit': total_cost / quantity
            }
            
        except Exception as e:
            raise ValueError(f"Error in calculation: {str(e)}")

def main():
    """Command-line interface for the distribution cost calculator."""
    print("Distribution Cost Calculator - Transparent Pricing Model")
    print("Inspired by VIDA TRADE LLC's operations\n")
    
    try:
        # Get user inputs
        base_cost = Decimal(input("Enter base product cost per unit: "))
        shipping_cost = Decimal(input("Enter shipping cost per unit: "))
        handling_fee = Decimal(input("Enter handling fee per unit (0 if none): ") or "0")
        customs_duty = Decimal(input("Enter customs duty percentage (0-1, e.g., 0.1 for 10%): ") or "0")
        vat_rate = Decimal(input("Enter VAT percentage (0-1, e.g., 0.2 for 20%): ") or "0")
        markup = Decimal(input("Enter markup percentage (0-1, e.g., 0.15 for 15%): ") or "0")
        quantity = int(input("Enter quantity (default 1): ") or "1")
        
        # Create calculator and calculate costs
        calculator = DistributionCostCalculator(
            base_cost=base_cost,
            shipping_cost=shipping_cost,
            customs_duty=customs_duty,
            vat_rate=vat_rate,
            handling_fee=handling_fee,
            markup_percentage=markup
        )
        
        costs = calculator.calculate_total_cost(quantity)
        
        # Display results
        print("\n--- Cost Breakdown (Transparent) ---")
        print(f"Base Cost: {costs['base_cost']:.2f}")
        print(f"Shipping: {costs['shipping_cost']:.2f}")
        print(f"Handling Fee: {costs['handling_fee']:.2f}")
        print(f"Customs Duty: {costs['customs_duty']:.2f}")
        print(f"VAT: {costs['vat']:.2f}")
        print(f"Markup: {costs['markup']:.2f}")
        print("-----------------------------------")
        print(f"TOTAL COST: {costs['total_cost']:.2f}")
        print(f"COST PER UNIT: {costs['cost_per_unit']:.2f}")
        
    except ValueError as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
