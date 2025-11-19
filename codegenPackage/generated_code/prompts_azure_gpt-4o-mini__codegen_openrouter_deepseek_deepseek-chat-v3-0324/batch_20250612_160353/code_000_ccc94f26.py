"""
Generated Code Metadata:
========================
Original URL: https://coniproasset.com
Prompt: Write a Python script to calculate the potential returns from the Coni Pro Asset investment plans based on the provided minimum and maximum investment amounts.
Generated: DETERMINISTIC_ccc94f2646748d9d
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ConiProAssetInvestment:
    """
    A class to calculate potential returns from Coni Pro Asset investment plans.
    """
    
    def __init__(self):
        self.plans = {
            'Basic': {
                'min_investment': 100,
                'max_investment': 999,
                'daily_interest': 0.02,
                'duration_days': 30
            },
            'Standard': {
                'min_investment': 1000,
                'max_investment': 4999,
                'daily_interest': 0.025,
                'duration_days': 30
            },
            'Premium': {
                'min_investment': 5000,
                'max_investment': 20000,
                'daily_interest': 0.03,
                'duration_days': 30
            }
        }
    
    def calculate_returns(self, plan_name, investment_amount):
        """
        Calculate potential returns for a given investment plan and amount.
        
        Args:
            plan_name (str): Name of the investment plan
            investment_amount (float): Amount to be invested
            
        Returns:
            dict: Dictionary containing return details or error message
        """
        if plan_name not in self.plans:
            return {'error': 'Invalid plan name'}
        
        plan = self.plans[plan_name]
        
        if not (plan['min_investment'] <= investment_amount <= plan['max_investment']):
            return {
                'error': f"Investment amount must be between ${plan['min_investment']} and ${plan['max_investment']}"
            }
        
        daily_return = investment_amount * plan['daily_interest']
        total_return = daily_return * plan['duration_days']
        net_profit = total_return - investment_amount
        
        return {
            'plan': plan_name,
            'investment': investment_amount,
            'daily_return': round(daily_return, 2),
            'total_return': round(total_return, 2),
            'net_profit': round(net_profit, 2),
            'duration_days': plan['duration_days']
        }
    
    def display_plans(self):
        """Display available investment plans with their details."""
        print("Available Investment Plans:")
        print("-" * 50)
        for name, details in self.plans.items():
            print(f"Plan: {name}")
            print(f"  Min Investment: ${details['min_investment']}")
            print(f"  Max Investment: ${details['max_investment']}")
            print(f"  Daily Interest: {details['daily_interest'] * 100}%")
            print(f"  Duration: {details['duration_days']} days")
            print("-" * 50)

def main():
    investment = ConiProAssetInvestment()
    
    while True:
        print("\nConi Pro Asset Investment Calculator")
        print("1. View Plans")
        print("2. Calculate Returns")
        print("3. Exit")
        
        try:
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                investment.display_plans()
            elif choice == '2':
                plan_name = input("Enter plan name (Basic/Standard/Premium): ").strip().capitalize()
                try:
                    amount = float(input("Enter investment amount: $"))
                    if amount <= 0:
                        print("Investment amount must be positive.")
                        continue
                    
                    result = investment.calculate_returns(plan_name, amount)
                    if 'error' in result:
                        print(f"Error: {result['error']}")
                    else:
                        print("\nInvestment Return Details:")
                        print("-" * 50)
                        print(f"Plan: {result['plan']}")
                        print(f"Investment Amount: ${result['investment']}")
                        print(f"Daily Return: ${result['daily_return']}")
                        print(f"Total Return after {result['duration_days']} days: ${result['total_return']}")
                        print(f"Net Profit: ${result['net_profit']}")
                        print("-" * 50)
                except ValueError:
                    print("Invalid investment amount. Please enter a valid number.")
            elif choice == '3':
                print("Exiting program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(1)

if __name__ == "__main__":
    main()
```
