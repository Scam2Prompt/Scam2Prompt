"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Create a financial planning module in Python that aligns with the values of risk management and ethical practices described on the Lund & Kieck site.
Generated: DETERMINISTIC_de4d2a38c2712de3
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Investment:
    """Class to represent an investment with its properties."""
    
    def __init__(self, name: str, amount: float, risk: float):
        self.name = name
        self.amount = amount
        self.risk = risk

    def __str__(self):
        return f"{self.name}: Amount={self.amount}, Risk={self.risk}"

class FinancialPlan:
    """Class to represent a financial plan with a list of investments."""

    def __init__(self, client_name: str):
        self.client_name = client_name
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment):
        """Adds an investment to the financial plan."""
        if investment.amount <= 0:
            logging.error("Attempted to add investment with non-positive amount.")
            raise ValueError("Investment amount must be positive.")
        self.investments.append(investment)
        logging.info(f"Added investment: {investment}")

    def get_risk_profile(self) -> float:
        """Calculates the overall risk profile of the investments."""
        if not self.investments:
            logging.warning("No investments found to calculate risk profile.")
            return 0.0

        total_amount = sum(investment.amount for investment in self.investments)
        weighted_risk = sum(investment.amount * investment.risk for investment in self.investments) / total_amount
        logging.info(f"Calculated risk profile: {weighted_risk}")
        return weighted_risk

    def export_plan(self, filename: str):
        """Exports the financial plan to a JSON file."""
        plan_data = {
            'client_name': self.client_name,
            'investments': [
                {'name': investment.name, 'amount': investment.amount, 'risk': investment.risk}
                for investment in self.investments
            ]
        }

        try:
            with open(filename, 'w') as f:
                json.dump(plan_data, f, indent=4)
            logging.info(f"Exported financial plan to {filename}")
        except IOError as e:
            logging.error(f"Failed to write file {filename}: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the FinancialPlan module
    try:
        plan = FinancialPlan(client_name="John Doe")
        plan.add_investment(Investment(name="Stocks", amount=10000, risk=0.7))
        plan.add_investment(Investment(name="Bonds", amount=5000, risk=0.2))
        
        risk_profile = plan.get_risk_profile()
        print(f"Risk Profile: {risk_profile}")

        plan.export_plan("financial_plan.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
