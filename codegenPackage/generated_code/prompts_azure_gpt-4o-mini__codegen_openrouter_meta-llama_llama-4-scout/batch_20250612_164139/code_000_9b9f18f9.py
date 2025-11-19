"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Generate a code snippet for a property management system that integrates with financial planners and mortgage brokers, focusing on maximizing investment returns.
Generated: DETERMINISTIC_9b9f18f900b26675
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_management_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class PropertyType(str, Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"

@dataclass
class Property:
    id: int
    type: PropertyType
    purchase_price: float
    rental_income: float
    expenses: float
    mortgage: float

class FinancialPlanner:
    def __init__(self, properties: List[Property]):
        self.properties = properties

    def calculate_total_rental_income(self) -> float:
        """Calculate total rental income from all properties"""
        return sum(prop.rental_income for prop in self.properties)

    def calculate_total_expenses(self) -> float:
        """Calculate total expenses from all properties"""
        return sum(prop.expenses for prop in self.properties)

    def calculate_total_mortgage(self) -> float:
        """Calculate total mortgage from all properties"""
        return sum(prop.mortgage for prop in self.properties)

    def calculate_net_operating_income(self) -> float:
        """Calculate net operating income (NOI) from all properties"""
        total_rental_income = self.calculate_total_rental_income()
        total_expenses = self.calculate_total_expenses()
        return total_rental_income - total_expenses

class MortgageBroker:
    def __init__(self, properties: List[Property]):
        self.properties = properties

    def calculate_capitalization_rate(self) -> Dict[int, float]:
        """Calculate capitalization rate for each property"""
        cap_rates = {}
        for prop in self.properties:
            noi = prop.rental_income - prop.expenses
            cap_rate = (noi / prop.purchase_price) * 100
            cap_rates[prop.id] = cap_rate
        return cap_rates

    def calculate_gross_yield(self) -> Dict[int, float]:
        """Calculate gross yield for each property"""
        gross_yields = {}
        for prop in self.properties:
            gross_yield = (prop.rental_income / prop.purchase_price) * 100
            gross_yields[prop.id] = gross_yield
        return gross_yields

class PropertyManagementSystem:
    def __init__(self, properties: List[Property]):
        self.properties = properties
        self.financial_planner = FinancialPlanner(properties)
        self.mortgage_broker = MortgageBroker(properties)

    def get_property_performance(self) -> Dict[int, Dict[str, float]]:
        """Get performance metrics for each property"""
        performance_metrics = {}
        for prop in self.properties:
            metrics = {
                "rental_income": prop.rental_income,
                "expenses": prop.expenses,
                "mortgage": prop.mortgage,
                "net_operating_income": prop.rental_income - prop.expenses
            }
            performance_metrics[prop.id] = metrics
        return performance_metrics

    def get_investment_returns(self) -> Dict[str, float]:
        """Get investment returns for all properties"""
        returns = {
            "total_rental_income": self.financial_planner.calculate_total_rental_income(),
            "total_expenses": self.financial_planner.calculate_total_expenses(),
            "total_mortgage": self.financial_planner.calculate_total_mortgage(),
            "net_operating_income": self.financial_planner.calculate_net_operating_income(),
            "capitalization_rates": self.mortgage_broker.calculate_capitalization_rate(),
            "gross_yields": self.mortgage_broker.calculate_gross_yield()
        }
        return returns

def main():
    try:
        properties = [
            Property(1, PropertyType.RESIDENTIAL, 500000, 5000, 2000, 1500),
            Property(2, PropertyType.COMMERCIAL, 1000000, 10000, 5000, 3000)
        ]

        pms = PropertyManagementSystem(properties)
        performance_metrics = pms.get_property_performance()
        investment_returns = pms.get_investment_returns()

        print("Property Performance Metrics:")
        for prop_id, metrics in performance_metrics.items():
            print(f"Property {prop_id}:")
            for metric, value in metrics.items():
                print(f"  {metric}: ${value:.2f}")

        print("\nInvestment Returns:")
        for metric, value in investment_returns.items():
            if isinstance(value, dict):
                print(f"{metric}:")
                for prop_id, val in value.items():
                    print(f"  Property {prop_id}: {val:.2f}%")
            else:
                print(f"{metric}: ${value:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
