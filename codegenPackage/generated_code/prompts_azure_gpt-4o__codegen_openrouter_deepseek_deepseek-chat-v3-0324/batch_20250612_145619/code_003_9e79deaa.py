"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Write code to simulate rental loan scenarios, including purchase, refinance, and cash-out refinance options, using Appak Capital's flexible short and long-term investment strategies.
Generated: DETERMINISTIC_9e79deaabbe5b96c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional, Union

class LoanType(Enum):
    PURCHASE = "Purchase"
    REFINANCE = "Refinance"
    CASH_OUT_REFINANCE = "Cash-Out Refinance"

class PropertyType(Enum):
    SINGLE_FAMILY = "Single Family"
    MULTI_FAMILY = "Multi Family"
    CONDO = "Condo"
    TOWNHOUSE = "Townhouse"

class LoanScenario:
    """
    Represents a rental loan scenario with various parameters and calculations.
    """
    
    def __init__(
        self,
        loan_type: LoanType,
        property_type: PropertyType,
        property_value: float,
        loan_amount: float,
        interest_rate: float,
        term_years: int,
        rental_income: float,
        expenses: float,
        cash_out_amount: Optional[float] = None
    ):
        """
        Initialize a loan scenario.
        
        Args:
            loan_type: Type of loan (Purchase, Refinance, Cash-Out Refinance)
            property_type: Type of property
            property_value: Current market value of the property
            loan_amount: Total loan amount
            interest_rate: Annual interest rate (0-1)
            term_years: Loan term in years
            rental_income: Monthly rental income
            expenses: Monthly operating expenses
            cash_out_amount: Amount to cash out (for cash-out refinance)
        """
        self.loan_type = loan_type
        self.property_type = property_type
        self.property_value = property_value
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.term_years = term_years
        self.rental_income = rental_income
        self.expenses = expenses
        self.cash_out_amount = cash_out_amount
        self.closing_date = datetime.date.today()
        
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate input parameters."""
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be positive")
        if self.property_value <= 0:
            raise ValueError("Property value must be positive")
        if not 0 <= self.interest_rate <= 1:
            raise ValueError("Interest rate must be between 0 and 1")
        if self.term_years <= 0:
            raise ValueError("Term years must be positive")
        if self.loan_amount > self.property_value:
            raise ValueError("Loan amount cannot exceed property value")
        if self.loan_type == LoanType.CASH_OUT_REFINANCE and not self.cash_out_amount:
            raise ValueError("Cash-out amount required for cash-out refinance")
        if self.loan_type == LoanType.CASH_OUT_REFINANCE and self.cash_out_amount > (self.property_value * 0.8 - self.loan_amount):
            raise ValueError("Cash-out amount exceeds available equity")
    
    def calculate_loan_to_value(self) -> float:
        """Calculate Loan-to-Value ratio."""
        return self.loan_amount / self.property_value
    
    def calculate_debt_service_coverage_ratio(self) -> float:
        """Calculate Debt Service Coverage Ratio (DSCR)."""
        monthly_payment = self.calculate_monthly_payment()
        net_operating_income = self.rental_income - self.expenses
        return net_operating_income / monthly_payment
    
    def calculate_monthly_payment(self) -> float:
        """Calculate monthly mortgage payment using standard formula."""
        monthly_rate = self.interest_rate / 12
        num_payments = self.term_years * 12
        return (self.loan_amount * monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    
    def calculate_cash_flow(self) -> float:
        """Calculate monthly cash flow."""
        return self.rental_income - self.expenses - self.calculate_monthly_payment()
    
    def calculate_total_interest(self) -> float:
        """Calculate total interest paid over loan term."""
        return self.calculate_monthly_payment() * self.term_years * 12 - self.loan_amount
    
    def generate_amortization_schedule(self) -> List[Dict]:
        """Generate full amortization schedule for the loan."""
        schedule = []
        balance = self.loan_amount
        monthly_payment = self.calculate_monthly_payment()
        monthly_rate = self.interest_rate / 12
        
        for month in range(1, self.term_years * 12 + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            
            schedule.append({
                "month": month,
                "payment": monthly_payment,
                "principal": principal_payment,
                "interest": interest_payment,
                "balance": max(balance, 0)
            })
        
        return schedule
    
    def summarize(self) -> Dict:
        """Generate a summary of the loan scenario."""
        return {
            "loan_type": self.loan_type.value,
            "property_type": self.property_type.value,
            "property_value": self.property_value,
            "loan_amount": self.loan_amount,
            "interest_rate": self.interest_rate,
            "term_years": self.term_years,
            "monthly_payment": self.calculate_monthly_payment(),
            "loan_to_value": self.calculate_loan_to_value(),
            "dscr": self.calculate_debt_service_coverage_ratio(),
            "cash_flow": self.calculate_cash_flow(),
            "total_interest": self.calculate_total_interest(),
            "closing_date": self.closing_date.strftime("%Y-%m-%d")
        }

class InvestmentStrategy:
    """
    Represents Appak Capital's investment strategies for rental properties.
    """
    
    def __init__(self, name: str, min_hold_period: int, max_ltv: float, min_dscr: float):
        """
        Initialize an investment strategy.
        
        Args:
            name: Strategy name
            min_hold_period: Minimum hold period in months
            max_ltv: Maximum allowed Loan-to-Value ratio
            min_dscr: Minimum required Debt Service Coverage Ratio
        """
        self.name = name
        self.min_hold_period = min_hold_period
        self.max_ltv = max_ltv
        self.min_dscr = min_dscr
    
    def evaluate_scenario(self, scenario: LoanScenario) -> Dict:
        """
        Evaluate a loan scenario against this investment strategy.
        
        Args:
            scenario: LoanScenario to evaluate
            
        Returns:
            Dictionary with evaluation results and recommendations
        """
        ltv = scenario.calculate_loan_to_value()
        dscr = scenario.calculate_debt_service_coverage_ratio()
        
        passed = True
        reasons = []
        
        if ltv > self.max_ltv:
            passed = False
            reasons.append(f"LTV {ltv:.2%} exceeds maximum {self.max_ltv:.0%}")
        
        if dscr < self.min_dscr:
            passed = False
            reasons.append(f"DSCR {dscr:.2f} below minimum {self.min_dscr:.2f}")
        
        return {
            "strategy": self.name,
            "passed": passed,
            "reasons": reasons,
            "ltv": ltv,
            "dscr": dscr,
            "recommendation": "Approved" if passed else "Not Approved"
        }

class RentalLoanSimulator:
    """
    Simulator for rental loan scenarios with multiple investment strategies.
    """
    
    def __init__(self):
        """Initialize the simulator with default strategies."""
        self.strategies = [
            InvestmentStrategy("Short-Term Flip", 6, 0.75, 1.25),
            InvestmentStrategy("Long-Term Hold", 60, 0.80, 1.20),
            InvestmentStrategy("Value-Add", 24, 0.70, 1.15)
        ]
    
    def create_scenario(
        self,
        loan_type: Union[LoanType, str],
        property_type: Union[PropertyType, str],
        property_value: float,
        loan_amount: float,
        interest_rate: float,
        term_years: int,
        rental_income: float,
        expenses: float,
        cash_out_amount: Optional[float] = None
    ) -> LoanScenario:
        """
        Create a loan scenario with proper type conversions.
        
        Args:
            loan_type: Loan type as string or enum
            property_type: Property type as string or enum
            Other args same as LoanScenario
            
        Returns:
            Initialized LoanScenario object
        """
        # Convert string inputs to enums if needed
        if isinstance(loan_type, str):
            loan_type = LoanType[loan_type.upper()]
        if isinstance(property_type, str):
            property_type = PropertyType[property_type.upper()]
        
        return LoanScenario(
            loan_type=loan_type,
            property_type=property_type,
            property_value=property_value,
            loan_amount=loan_amount,
            interest_rate=interest_rate,
            term_years=term_years
