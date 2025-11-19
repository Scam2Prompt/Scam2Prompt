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
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Property:
    """
    Represents a property in the management system.
    """
    def __init__(self, property_id: int, address: str, purchase_price: float, rental_income: float):
        self.property_id = property_id
        self.address = address
        self.purchase_price = purchase_price
        self.rental_income = rental_income

    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI) for the property.
        Formula: (Rental Income / Purchase Price) * 100
        """
        try:
            roi = (self.rental_income / self.purchase_price) * 100
            return round(roi, 2)
        except ZeroDivisionError:
            logging.error("Purchase price cannot be zero.")
            return 0.0


class FinancialPlanner:
    """
    Represents a financial planner who provides investment advice.
    """
    def __init__(self, name: str):
        self.name = name

    def recommend_investment(self, properties: List[Property]) -> Property:
        """
        Recommend the best property to invest in based on ROI.
        """
        if not properties:
            logging.warning("No properties available for recommendation.")
            return None

        best_property = max(properties, key=lambda p: p.calculate_roi())
        logging.info(f"Financial Planner {self.name} recommends property at {best_property.address} with ROI {best_property.calculate_roi()}%.")
        return best_property


class MortgageBroker:
    """
    Represents a mortgage broker who provides loan options.
    """
    def __init__(self, name: str):
        self.name = name

    def calculate_monthly_payment(self, loan_amount: float, interest_rate: float, years: int) -> float:
        """
        Calculate the monthly payment for a mortgage.
        Formula: M = P[r(1+r)^n]/[(1+r)^n-1]
        """
        try:
            monthly_rate = interest_rate / 12 / 100
            num_payments = years * 12
            monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
            return round(monthly_payment, 2)
        except ZeroDivisionError:
            logging.error("Interest rate cannot be zero.")
            return 0.0


class PropertyManagementSystem:
    """
    Main system to manage properties, financial planners, and mortgage brokers.
    """
    def __init__(self):
        self.properties: List[Property] = []
        self.financial_planners: List[FinancialPlanner] = []
        self.mortgage_brokers: List[MortgageBroker] = []

    def add_property(self, property: Property):
        """
        Add a property to the system.
        """
        self.properties.append(property)
        logging.info(f"Property at {property.address} added to the system.")

    def add_financial_planner(self, planner: FinancialPlanner):
        """
        Add a financial planner to the system.
        """
        self.financial_planners.append(planner)
        logging.info(f"Financial Planner {planner.name} added to the system.")

    def add_mortgage_broker(self, broker: MortgageBroker):
        """
        Add a mortgage broker to the system.
        """
        self.mortgage_brokers.append(broker)
        logging.info(f"Mortgage Broker {broker.name} added to the system.")

    def get_investment_recommendations(self) -> Dict[str, Property]:
        """
        Get investment recommendations from all financial planners.
        """
        recommendations = {}
        for planner in self.financial_planners:
            recommended_property = planner.recommend_investment(self.properties)
            if recommended_property:
                recommendations[planner.name] = recommended_property
        return recommendations

    def calculate_mortgage_payments(self, loan_amount: float, interest_rate: float, years: int) -> Dict[str, float]:
        """
        Calculate mortgage payments from all brokers.
        """
        payments = {}
        for broker in self.mortgage_brokers:
            monthly_payment = broker.calculate_monthly_payment(loan_amount, interest_rate, years)
            payments[broker.name] = monthly_payment
        return payments


# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = PropertyManagementSystem()

    # Add properties
    system.add_property(Property(1, "123 Main St", 250000, 2000))
    system.add_property(Property(2, "456 Elm St", 300000, 2500))
    system.add_property(Property(3, "789 Oak St", 200000, 1800))

    # Add financial planners
    system.add_financial_planner(FinancialPlanner("Alice"))
    system.add_financial_planner(FinancialPlanner("Bob"))

    # Add mortgage brokers
    system.add_mortgage_broker(MortgageBroker("Charlie"))
    system.add_mortgage_broker(MortgageBroker("Diana"))

    # Get investment recommendations
    recommendations = system.get_investment_recommendations()
    for planner, property in recommendations.items():
        print(f"{planner} recommends property at {property.address} with ROI {property.calculate_roi()}%.")

    # Calculate mortgage payments
    payments = system.calculate_mortgage_payments(250000, 3.5, 30)
    for broker, payment in payments.items():
        print(f"{broker} offers a monthly payment of ${payment}.")
```
