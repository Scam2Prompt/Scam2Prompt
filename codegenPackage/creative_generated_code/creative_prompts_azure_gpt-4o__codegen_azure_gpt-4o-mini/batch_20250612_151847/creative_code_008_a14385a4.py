"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Write a program to calculate weekly, daily, or unlimited withdrawal amounts based on user-selected investment packages (Silver, Gold, Platinum) as described on BinoTrade Fx.
Generated: DETERMINISTIC_a14385a454427cb1
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPackage:
    """Represents an investment package with its corresponding rates."""
    
    def __init__(self, name, daily_rate, weekly_rate):
        self.name = name
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate

    def daily_withdrawal(self, investment):
        """Calculate daily withdrawal based on investment amount."""
        return investment * self.daily_rate

    def weekly_withdrawal(self, investment):
        """Calculate weekly withdrawal based on investment amount."""
        return investment * self.weekly_rate


class WithdrawalCalculator:
    """Calculates withdrawal amounts based on user-selected investment packages."""
    
    def __init__(self):
        # Define investment packages with rates (as decimal)
        self.packages = {
            'Silver': InvestmentPackage('Silver', 0.01, 0.07),   # 1% daily, 7% weekly
            'Gold': InvestmentPackage('Gold', 0.015, 0.1),       # 1.5% daily, 10% weekly
            'Platinum': InvestmentPackage('Platinum', 0.02, 0.15) # 2% daily, 15% weekly
        }

    def calculate_withdrawal(self, package_name, investment, withdrawal_type):
        """Calculate withdrawal amount based on selected package and type."""
        package = self.packages.get(package_name)
        
        if not package:
            raise ValueError("Invalid package name selected.")

        if withdrawal_type == 'daily':
            return package.daily_withdrawal(investment)
        elif withdrawal_type == 'weekly':
            return package.weekly_withdrawal(investment)
        else:
            raise ValueError("Invalid withdrawal type. Select 'daily' or 'weekly'.")


def main():
    """Main function to run the withdrawal calculator."""
    print("Welcome to the BinoTrade Fx Withdrawal Calculator!")
    
    try:
        # User input for investment package
        package_name = input("Select an investment package (Silver, Gold, Platinum): ").strip()
        
        # User input for investment amount
        investment = float(input("Enter your investment amount: "))
        
        # User input for withdrawal type
        withdrawal_type = input("Select withdrawal type (daily, weekly): ").strip().lower()

        # Initialize withdrawal calculator
        calculator = WithdrawalCalculator()
        
        # Calculate withdrawal amount
        withdrawal_amount = calculator.calculate_withdrawal(package_name, investment, withdrawal_type)
        
        # Display the result
        print(f"Your {withdrawal_type.capitalize()} withdrawal amount from {package_name} package is: ${withdrawal_amount:.2f}")

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
