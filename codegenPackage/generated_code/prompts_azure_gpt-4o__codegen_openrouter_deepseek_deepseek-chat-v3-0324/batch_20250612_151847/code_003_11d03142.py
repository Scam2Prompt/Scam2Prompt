"""
Generated Code Metadata:
========================
Original URL: https://skytrustasset.com
Prompt: Create a script to calculate daily earnings for investors based on the fixed interest rates and investment plans provided by Sky Trust ltd.
Generated: DETERMINISTIC_11d03142b928d720
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class InvestmentPlan:
    """
    Represents an investment plan with its details.
    """
    def __init__(self, name: str, min_amount: float, max_amount: float, interest_rate: float, duration_days: int):
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.interest_rate = interest_rate
        self.duration_days = duration_days

    def validate_investment(self, amount: float) -> bool:
        """
        Validates if the investment amount is within plan limits.
        """
        return self.min_amount <= amount <= self.max_amount


class Investor:
    """
    Represents an investor with their investments.
    """
    def __init__(self, investor_id: str, name: str):
        self.investor_id = investor_id
        self.name = name
        self.investments: List[Dict] = []

    def add_investment(self, plan: InvestmentPlan, amount: float, start_date: str) -> None:
        """
        Adds a new investment for the investor.
        """
        if not plan.validate_investment(amount):
            raise ValueError(f"Investment amount {amount} is not within plan limits")

        self.investments.append({
            'plan': plan,
            'amount': amount,
            'start_date': start_date,
            'end_date': (datetime.strptime(start_date, '%Y-%m-%d') + 
                         timedelta(days=plan.duration_days)).strftime('%Y-%m-%d')
        })


class EarningsCalculator:
    """
    Calculates daily earnings for investors based on their investments.
    """
    def __init__(self):
        self.plans: Dict[str, InvestmentPlan] = {}
        self.investors: Dict[str, Investor] = {}

    def add_plan(self, plan: InvestmentPlan) -> None:
        """
        Adds an investment plan to the calculator.
        """
        self.plans[plan.name] = plan

    def add_investor(self, investor: Investor) -> None:
        """
        Adds an investor to the calculator.
        """
        self.investors[investor.investor_id] = investor

    def calculate_daily_earnings(self, investor_id: str, date: Optional[str] = None) -> float:
        """
        Calculates total daily earnings for an investor on a specific date.
        If date is not provided, uses current date.
        """
        if investor_id not in self.investors:
            raise ValueError(f"Investor with ID {investor_id} not found")

        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        try:
            target_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD")

        total_earnings = 0.0
        investor = self.investors[investor_id]

        for investment in investor.investments:
            start_date = datetime.strptime(investment['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(investment['end_date'], '%Y-%m-%d')

            if start_date <= target_date <= end_date:
                daily_rate = investment['plan'].interest_rate / 365
                total_earnings += investment['amount'] * daily_rate / 100

        return round(total_earnings, 2)

    def save_to_file(self, filename: str) -> None:
        """
        Saves the current state to a JSON file.
        """
        data = {
            'plans': [
                {
                    'name': plan.name,
                    'min_amount': plan.min_amount,
                    'max_amount': plan.max_amount,
                    'interest_rate': plan.interest_rate,
                    'duration_days': plan.duration_days
                } for plan in self.plans.values()
            ],
            'investors': [
                {
                    'investor_id': investor.investor_id,
                    'name': investor.name,
                    'investments': [
                        {
                            'plan_name': inv['plan'].name,
                            'amount': inv['amount'],
                            'start_date': inv['start_date'],
                            'end_date': inv['end_date']
                        } for inv in investor.investments
                    ]
                } for investor in self.investors.values()
            ]
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """
        Loads data from a JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)

        # Clear existing data
        self.plans = {}
        self.investors = {}

        # Load plans
        for plan_data in data.get('plans', []):
            plan = InvestmentPlan(
                name=plan_data['name'],
                min_amount=plan_data['min_amount'],
                max_amount=plan_data['max_amount'],
                interest_rate=plan_data['interest_rate'],
                duration_days=plan_data['duration_days']
            )
            self.add_plan(plan)

        # Load investors
        for investor_data in data.get('investors', []):
            investor = Investor(
                investor_id=investor_data['investor_id'],
                name=investor_data['name']
            )
            
            for inv_data in investor_data.get('investments', []):
                plan = self.plans.get(inv_data['plan_name'])
                if plan:
                    investor.add_investment(
                        plan=plan,
                        amount=inv_data['amount'],
                        start_date=inv_data['start_date']
                    )
            
            self.add_investor(investor)


# Example usage
if __name__ == "__main__":
    # Initialize calculator
    calculator = EarningsCalculator()

    # Create investment plans
    basic_plan = InvestmentPlan(
        name="Basic",
        min_amount=1000,
        max_amount=10000,
        interest_rate=5.0,
        duration_days=365
    )
    
    premium_plan = InvestmentPlan(
        name="Premium",
        min_amount=10000,
        max_amount=50000,
        interest_rate=7.5,
        duration_days=730
    )

    calculator.add_plan(basic_plan)
    calculator.add_plan(premium_plan)

    # Create investors and investments
    investor1 = Investor("INV001", "John Doe")
    investor1.add_investment(basic_plan, 5000, "2023-01-01")
    investor1.add_investment(premium_plan, 15000, "2023-01-15")
    calculator.add_investor(investor1)

    investor2 = Investor("INV002", "Jane Smith")
    investor2.add_investment(basic_plan, 8000, "2023-02-01")
    calculator.add_investor(investor2)

    # Calculate and print earnings
    print(f"John's earnings today: ${calculator.calculate_daily_earnings('INV001')}")
    print(f"Jane's earnings on 2023-03-01: ${calculator.calculate_daily_earnings('INV002', '2023-03-01')}")

    # Save to file
    calculator.save_to_file("sky_trust_data.json")
```
