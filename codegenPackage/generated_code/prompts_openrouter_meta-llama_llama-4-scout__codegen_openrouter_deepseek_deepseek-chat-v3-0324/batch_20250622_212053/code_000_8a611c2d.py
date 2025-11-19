"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Write a Python script to calculate the total cost of purchasing a 3 BHK apartment in L&T Elara Celestia, considering a 10% down payment and flexible installment payment plans.
Generated: DETERMINISTIC_8a611c2d3fbdd842
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PaymentPlan:
    """Represents a payment installment plan for the apartment."""
    name: str
    months: int  # Duration in months
    interest_rate: float  # Annual interest rate (0 if no interest)

class ApartmentPurchaseCalculator:
    """
    Calculates the total cost of purchasing a 3 BHK apartment in L&T Elara Celestia
    with a 10% down payment and flexible installment payment plans.
    """
    
    def __init__(self, base_price: float):
        """
        Initialize the calculator with the base price of the apartment.
        
        Args:
            base_price (float): The total base price of the apartment in INR.
        """
        if base_price <= 0:
            raise ValueError("Base price must be positive.")
        self.base_price = base_price
        self.down_payment_percent = 10  # 10% down payment
        self.payment_plans = [
            PaymentPlan("12 Months", 12, 0),
            PaymentPlan("24 Months", 24, 5),
            PaymentPlan("36 Months", 36, 7),
        ]
    
    def calculate_down_payment(self) -> float:
        """Calculate the 10% down payment amount."""
        return self.base_price * (self.down_payment_percent / 100)
    
    def calculate_installment(self, plan: PaymentPlan) -> dict:
        """
        Calculate monthly installment details for a given payment plan.
        
        Args:
            plan (PaymentPlan): The selected payment plan.
            
        Returns:
            dict: Dictionary containing payment details including:
                - monthly_payment
                - total_interest
                - total_amount_paid
        """
        remaining_amount = self.base_price - self.calculate_down_payment()
        
        if plan.interest_rate == 0:
            monthly_payment = remaining_amount / plan.months
            total_interest = 0
        else:
            monthly_rate = plan.interest_rate / 100 / 12
            monthly_payment = remaining_amount * (monthly_rate * (1 + monthly_rate) ** plan.months) / ((1 + monthly_rate) ** plan.months - 1)
            total_interest = (monthly_payment * plan.months) - remaining_amount
        
        total_amount_paid = self.calculate_down_payment() + (monthly_payment * plan.months)
        
        return {
            "plan_name": plan.name,
            "down_payment": self.calculate_down_payment(),
            "monthly_payment": monthly_payment,
            "total_interest": total_interest,
            "total_amount_paid": total_amount_paid,
            "base_price": self.base_price
        }
    
    def get_all_payment_options(self) -> List[dict]:
        """Return all available payment plans with calculations."""
        return [self.calculate_installment(plan) for plan in self.payment_plans]
    
    def to_json(self) -> str:
        """Return all payment options as JSON string."""
        return json.dumps(self.get_all_payment_options(), indent=2)

def main():
    """Main function to demonstrate the apartment purchase calculator."""
    try:
        # Example: Base price of 1.5 Crore INR
        base_price = 15000000  # 1.5 Crore INR
        calculator = ApartmentPurchaseCalculator(base_price)
        
        print(f"Base Price: ₹{base_price:,.2f}")
        print(f"Down Payment (10%): ₹{calculator.calculate_down_payment():,.2f}\n")
        
        print("Available Payment Plans:")
        for option in calculator.get_all_payment_options():
            print(f"\nPlan: {option['plan_name']}")
            print(f"Monthly Payment: ₹{option['monthly_payment']:,.2f}")
            print(f"Total Interest: ₹{option['total_interest']:,.2f}")
            print(f"Total Amount Paid: ₹{option['total_amount_paid']:,.2f}")
        
        # Uncomment to print JSON output
        # print("\nJSON Output:")
        # print(calculator.to_json())
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
