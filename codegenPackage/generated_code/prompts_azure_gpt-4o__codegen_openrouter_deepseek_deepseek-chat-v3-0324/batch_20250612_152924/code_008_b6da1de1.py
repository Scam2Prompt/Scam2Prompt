"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a script to calculate rental profitability for property owners, incorporating insurance coverage as mentioned in Inmobiliaria Capri's services.
Generated: DETERMINISTIC_b6da1de172cfa33d
Batch ID: 20250612_152924
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
from typing import Optional, List, Dict
from datetime import datetime, timedelta
import math

@dataclass
class Property:
    """Represents a rental property with financial details."""
    purchase_price: float
    monthly_rent: float
    property_tax_rate: float  # annual rate
    maintenance_rate: float  # percentage of rent
    insurance_cost: float  # annual cost
    vacancy_rate: float  # percentage
    management_fee_rate: float  # percentage of rent
    mortgage_rate: Optional[float] = None  # annual interest rate
    mortgage_term: Optional[int] = None  # years
    down_payment: Optional[float] = None  # percentage

@dataclass
class RentalAnalysis:
    """Contains the results of rental profitability analysis."""
    monthly_cash_flow: float
    annual_cash_flow: float
    cap_rate: float  # capitalization rate
    cash_on_cash_return: float
    break_even_ratio: float
    insurance_coverage_impact: Dict[str, float]
    monthly_expenses: Dict[str, float]
    annual_expenses: Dict[str, float]

class RentalProfitabilityCalculator:
    """Calculates rental property profitability metrics."""
    
    def __init__(self, property: Property):
        self.property = property
    
    def calculate_mortgage_payment(self) -> float:
        """Calculate monthly mortgage payment using the loan formula."""
        if not all([self.property.mortgage_rate, self.property.mortgage_term, self.property.down_payment]):
            return 0.0
        
        principal = self.property.purchase_price * (1 - self.property.down_payment / 100)
        monthly_rate = (self.property.mortgage_rate / 100) / 12
        num_payments = self.property.mortgage_term * 12
        
        if monthly_rate == 0:
            return principal / num_payments
        
        mortgage_payment = principal * (monthly_rate * math.pow(1 + monthly_rate, num_payments)) / (math.pow(1 + monthly_rate, num_payments) - 1)
        return mortgage_payment
    
    def calculate_vacancy_loss(self) -> float:
        """Calculate monthly loss due to vacancy."""
        return self.property.monthly_rent * (self.property.vacancy_rate / 100)
    
    def calculate_property_tax(self) -> float:
        """Calculate monthly property tax."""
        return (self.property.purchase_price * (self.property.property_tax_rate / 100)) / 12
    
    def calculate_maintenance(self) -> float:
        """Calculate monthly maintenance cost."""
        return self.property.monthly_rent * (self.property.maintenance_rate / 100)
    
    def calculate_management_fee(self) -> float:
        """Calculate monthly property management fee."""
        return self.property.monthly_rent * (self.property.management_fee_rate / 100)
    
    def calculate_insurance_cost(self) -> float:
        """Calculate monthly insurance cost."""
        return self.property.insurance_cost / 12
    
    def calculate_expenses(self) -> Dict[str, float]:
        """Calculate all monthly expenses."""
        mortgage = self.calculate_mortgage_payment()
        vacancy = self.calculate_vacancy_loss()
        tax = self.calculate_property_tax()
        maintenance = self.calculate_maintenance()
        management = self.calculate_management_fee()
        insurance = self.calculate_insurance_cost()
        
        return {
            "mortgage": mortgage,
            "vacancy": vacancy,
            "property_tax": tax,
            "maintenance": maintenance,
            "management": management,
            "insurance": insurance,
            "total": mortgage + vacancy + tax + maintenance + management + insurance
        }
    
    def calculate_insurance_coverage_impact(self, base_insurance: float) -> Dict[str, float]:
        """Calculate the financial impact of insurance coverage."""
        current_insurance = self.property.insurance_cost
        difference = current_insurance - base_insurance
        
        return {
            "base_insurance_cost": base_insurance,
            "current_insurance_cost": current_insurance,
            "monthly_difference": difference / 12,
            "annual_difference": difference,
            "impact_on_cash_flow": difference / 12  # monthly impact
        }
    
    def analyze(self, base_insurance_cost: Optional[float] = None) -> RentalAnalysis:
        """Perform complete rental profitability analysis."""
        monthly_expenses = self.calculate_expenses()
        monthly_cash_flow = self.property.monthly_rent - monthly_expenses["total"]
        annual_cash_flow = monthly_cash_flow * 12
        
        # Calculate Cap Rate (NOI / Property Value)
        noi = (self.property.monthly_rent * 12) - (monthly_expenses["total"] * 12) + monthly_expenses["mortgage"] * 12
        cap_rate = (noi / self.property.purchase_price) * 100
        
        # Calculate Cash on Cash Return (Annual Cash Flow / Total Cash Invested)
        if self.property.down_payment:
            cash_invested = (self.property.down_payment / 100) * self.property.purchase_price
            cash_on_cash_return = (annual_cash_flow / cash_invested) * 100
        else:
            cash_on_cash_return = 0.0
        
        # Calculate Break-even Ratio (Expenses / Gross Income)
        break_even_ratio = (monthly_expenses["total"] / self.property.monthly_rent) * 100
        
        # Calculate insurance impact if base insurance is provided
        insurance_impact = {}
        if base_insurance_cost is not None:
            insurance_impact = self.calculate_insurance_coverage_impact(base_insurance_cost)
        
        # Prepare annual expenses
        annual_expenses = {k: v * 12 for k, v in monthly_expenses.items()}
        
        return RentalAnalysis(
            monthly_cash_flow=monthly_cash_flow,
            annual_cash_flow=annual_cash_flow,
            cap_rate=cap_rate,
            cash_on_cash_return=cash_on_cash_return,
            break_even_ratio=break_even_ratio,
            insurance_coverage_impact=insurance_impact,
            monthly_expenses=monthly_expenses,
            annual_expenses=annual_expenses
        )

def load_property_from_json(file_path: str) -> Property:
    """Load property data from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return Property(
        purchase_price=data.get('purchase_price', 0),
        monthly_rent=data.get('monthly_rent', 0),
        property_tax_rate=data.get('property_tax_rate', 0),
        maintenance_rate=data.get('maintenance_rate', 0),
        insurance_cost=data.get('insurance_cost', 0),
        vacancy_rate=data.get('vacancy_rate', 0),
        management_fee_rate=data.get('management_fee_rate', 0),
        mortgage_rate=data.get('mortgage_rate'),
        mortgage_term=data.get('mortgage_term'),
        down_payment=data.get('down_payment')
    )

def save_analysis_to_json(analysis: RentalAnalysis, file_path: str) -> None:
    """Save analysis results to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump({
            "monthly_cash_flow": analysis.monthly_cash_flow,
            "annual_cash_flow": analysis.annual_cash_flow,
            "cap_rate": analysis.cap_rate,
            "cash_on_cash_return": analysis.cash_on_cash_return,
            "break_even_ratio": analysis.break_even_ratio,
            "insurance_coverage_impact": analysis.insurance_coverage_impact,
            "monthly_expenses": analysis.monthly_expenses,
            "annual_expenses": analysis.annual_expenses
        }, f, indent=2)

def main():
    """Main execution function for command-line use."""
    try:
        # Example property data (in production, this would come from user input or config)
        property_data = Property(
            purchase_price=300000,
            monthly_rent=2000,
            property_tax_rate=1.2,
            maintenance_rate=5,
            insurance_cost=1200,
            vacancy_rate=5,
            management_fee_rate=8,
            mortgage_rate=3.5,
            mortgage_term=30,
            down_payment=20
        )
        
        calculator = RentalProfitabilityCalculator(property_data)
        analysis = calculator.analyze(base_insurance_cost=1000)  # Compare with base insurance cost
        
        print("\nRental Property Analysis:")
        print(f"Monthly Cash Flow: ${analysis.monthly_cash_flow:,.2f}")
        print(f"Annual Cash Flow: ${analysis.annual_cash_flow:,.2f}")
        print(f"Cap Rate: {analysis.cap_rate:.2f}%")
        print(f"Cash on Cash Return: {analysis.cash_on_cash_return:.2f}%")
        print(f"Break-even Ratio: {analysis.break_even_ratio:.
