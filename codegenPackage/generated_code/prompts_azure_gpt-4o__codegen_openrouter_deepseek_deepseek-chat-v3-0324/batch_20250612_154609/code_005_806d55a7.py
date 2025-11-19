"""
Generated Code Metadata:
========================
Original URL: https://welforcevestcapital.com
Prompt: Create a Python program to simulate the investment plan selection process on Welforcevest Capital, allowing users to choose plans like Starter, Standard, Advanced, Pro, or Enterprise and calculate the expected profit.
Generated: DETERMINISTIC_806d55a7a5c61f53
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    Represents an investment plan with its details and profit calculation.
    """
    
    def __init__(self, name, min_investment, max_investment, roi_percent, duration_months):
        """
        Initialize an investment plan.
        
        Args:
            name (str): Name of the plan
            min_investment (float): Minimum investment amount
            max_investment (float): Maximum investment amount
            roi_percent (float): Return on investment percentage (annual)
            duration_months (int): Duration of the plan in months
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.roi_percent = roi_percent
        self.duration_months = duration_months
    
    def calculate_profit(self, investment_amount):
        """
        Calculate the expected profit for the given investment amount.
        
        Args:
            investment_amount (float): Amount to invest
            
        Returns:
            float: Expected profit
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}")
        
        annual_profit = investment_amount * (self.roi_percent / 100)
        duration_years = self.duration_months / 12
        return annual_profit * duration_years


class WelforcevestCapital:
    """
    Simulates the investment plan selection process for Welforcevest Capital.
    """
    
    def __init__(self):
        """
        Initialize available investment plans.
        """
        self.plans = {
            '1': InvestmentPlan("Starter", 1000, 5000, 5.0, 12),
            '2': InvestmentPlan("Standard", 5000, 20000, 7.5, 24),
            '3': InvestmentPlan("Advanced", 20000, 50000, 10.0, 36),
            '4': InvestmentPlan("Pro", 50000, 100000, 12.5, 48),
            '5': InvestmentPlan("Enterprise", 100000, 1000000, 15.0, 60)
        }
    
    def display_plans(self):
        """
        Display available investment plans.
        """
        print("\nAvailable Investment Plans:")
        print("--------------------------")
        for key, plan in self.plans.items():
            print(f"{key}. {plan.name}")
            print(f"   Investment Range: ${plan.min_investment:,.2f} - ${plan.max_investment:,.2f}")
            print(f"   ROI: {plan.roi_percent}% per annum")
            print(f"   Duration: {plan.duration_months} months\n")
    
    def get_user_input(self):
        """
        Get user input for plan selection and investment amount.
        
        Returns:
            tuple: (selected_plan, investment_amount)
        """
        while True:
            try:
                choice = input("Select a plan (1-5) or 'q' to quit: ")
                if choice.lower() == 'q':
                    return None, None
                
                if choice not in self.plans:
                    print("Invalid choice. Please select 1-5.")
                    continue
                
                selected_plan = self.plans[choice]
                
                investment = float(input(f"Enter investment amount (${selected_plan.min_investment:,.2f}-${selected_plan.max_investment:,.2f}): "))
                
                return selected_plan, investment
            
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    
    def run(self):
        """
        Run the investment plan selection process.
        """
        print("Welcome to Welforcevest Capital Investment Simulator")
        print("---------------------------------------------------")
        
        while True:
            self.display_plans()
            plan, amount = self.get_user_input()
            
            if plan is None:
                print("Thank you for using Welforcevest Capital. Goodbye!")
                break
            
            try:
                profit = plan.calculate_profit(amount)
                print(f"\nInvestment Summary for {plan.name} Plan:")
                print(f"Investment Amount: ${amount:,.2f}")
                print(f"Expected Profit after {plan.duration_months} months: ${profit:,.2f}")
                print(f"Total Return: ${amount + profit:,.2f}\n")
                
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    simulator = WelforcevestCapital()
    simulator.run()
```
