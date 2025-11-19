"""
Generated Code Metadata:
========================
Original URL: https://jiofibers.com
Prompt: Write a Python script to calculate the cost of JioFiber postpaid plans in Bangalore based on the provided plan prices.
Generated: DETERMINISTIC_e4fd83feab7db845
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JioFiber Postpaid Plan Calculator for Bangalore

This script calculates the cost of JioFiber postpaid plans based on the provided
plan prices and GST rate. It includes error handling for invalid inputs and
provides a clean output format.
"""

class JioFiberPlanCalculator:
    """Calculator for JioFiber postpaid plans in Bangalore."""
    
    def __init__(self):
        """Initialize plan details and GST rate."""
        self.plans = {
            'Silver': {
                'monthly_rental': 399,
                'data': '100 GB',
                'speed': '30 Mbps',
                'ott_benefits': False
            },
            'Gold': {
                'monthly_rental': 599,
                'data': '200 GB',
                'speed': '100 Mbps',
                'ott_benefits': True
            },
            'Diamond': {
                'monthly_rental': 849,
                'data': '300 GB',
                'speed': '150 Mbps',
                'ott_benefits': True
            },
            'Platinum': {
                'monthly_rental': 1299,
                'data': '500 GB',
                'speed': '300 Mbps',
                'ott_benefits': True
            },
            'Titanium': {
                'monthly_rental': 2499,
                'data': '1000 GB',
                'speed': '500 Mbps',
                'ott_benefits': True
            }
        }
        self.gst_rate = 0.18  # 18% GST
    
    def calculate_total_cost(self, plan_name, months=1):
        """
        Calculate total cost including GST for a given plan and duration.
        
        Args:
            plan_name (str): Name of the plan (case-insensitive)
            months (int): Duration in months (default: 1)
            
        Returns:
            dict: Plan details with calculated costs or None if invalid plan
        """
        plan_name = plan_name.capitalize()
        
        if plan_name not in self.plans:
            return None
            
        plan = self.plans[plan_name].copy()
        base_cost = plan['monthly_rental'] * months
        gst_amount = base_cost * self.gst_rate
        total_cost = base_cost + gst_amount
        
        plan.update({
            'duration_months': months,
            'base_cost': base_cost,
            'gst_amount': round(gst_amount, 2),
            'total_cost': round(total_cost, 2)
        })
        
        return plan
    
    def display_plan_details(self, plan_name, months=1):
        """
        Display formatted plan details and calculated costs.
        
        Args:
            plan_name (str): Name of the plan
            months (int): Duration in months
        """
        plan = self.calculate_total_cost(plan_name, months)
        
        if not plan:
            print(f"Error: Plan '{plan_name}' not found.")
            return
            
        print("\nJioFiber Postpaid Plan Details:")
        print("=" * 40)
        print(f"Plan Name: {plan_name}")
        print(f"Monthly Rental: ₹{plan['monthly_rental']}")
        print(f"Data: {plan['data']}")
        print(f"Speed: {plan['speed']}")
        print(f"OTT Benefits: {'Yes' if plan['ott_benefits'] else 'No'}")
        print(f"Duration: {months} month(s)")
        print("-" * 40)
        print(f"Base Cost: ₹{plan['base_cost']}")
        print(f"GST (18%): ₹{plan['gst_amount']}")
        print(f"Total Cost: ₹{plan['total_cost']}")
        print("=" * 40)


def main():
    """Main function to run the calculator."""
    calculator = JioFiberPlanCalculator()
    
    print("JioFiber Postpaid Plan Calculator for Bangalore")
    print("Available Plans:")
    for plan in calculator.plans:
        print(f"- {plan}")
    
    while True:
        try:
            print("\nEnter plan name (or 'exit' to quit):")
            plan_input = input().strip()
            
            if plan_input.lower() == 'exit':
                break
                
            print("Enter duration in months (default: 1):")
            duration_input = input().strip()
            months = int(duration_input) if duration_input else 1
            
            calculator.display_plan_details(plan_input, months)
            
        except ValueError:
            print("Error: Please enter a valid number for months.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
```
