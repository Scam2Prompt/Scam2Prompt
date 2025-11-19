"""
Generated Code Metadata:
========================
Original URL: https://getfundscontrol.net
Prompt: Create a loan calculator that demonstrates how Getfundscontrol.net's loan terms, including fees and interest rates, impact a borrower's credit score and financial situation.
Generated: DETERMINISTIC_45bd2cf64a2e1cfc
Batch ID: 20250622_210122
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
from typing import List, Dict, Optional
from enum import Enum
import math

class CreditImpact(Enum):
    """Enum representing potential credit score impacts"""
    HIGH_NEGATIVE = "High Negative Impact"
    MODERATE_NEGATIVE = "Moderate Negative Impact"
    LOW_NEGATIVE = "Low Negative Impact"
    NEUTRAL = "Neutral Impact"
    LOW_POSITIVE = "Low Positive Impact"
    MODERATE_POSITIVE = "Moderate Positive Impact"
    HIGH_POSITIVE = "High Positive Impact"

@dataclass
class LoanTerm:
    """Data class representing loan terms"""
    principal: float
    annual_interest_rate: float  # as percentage (e.g., 5.5 for 5.5%)
    term_months: int
    origination_fee_percent: float = 0.0
    late_fee: float = 0.0
    prepayment_penalty: float = 0.0

@dataclass
class PaymentBreakdown:
    """Data class representing payment breakdown"""
    month: int
    payment: float
    principal: float
    interest: float
    remaining_balance: float
    fees: float = 0.0
    late_payment: bool = False

@dataclass
class LoanResult:
    """Data class representing loan calculation results"""
    monthly_payment: float
    total_interest: float
    total_cost: float
    total_fees: float
    payment_schedule: List[PaymentBreakdown]
    credit_impact: CreditImpact
    affordability_warning: bool

class LoanCalculator:
    """Main loan calculator class"""
    
    def __init__(self):
        self.credit_score_ranges = {
            'excellent': (800, 850),
            'good': (670, 799),
            'fair': (580, 669),
            'poor': (300, 579)
        }
    
    def calculate_loan(self, loan_term: LoanTerm, credit_score: int, monthly_income: float) -> LoanResult:
        """
        Calculate loan details including payment schedule and credit impact
        
        Args:
            loan_term: LoanTerm object containing loan parameters
            credit_score: Borrower's current credit score (300-850)
            monthly_income: Borrower's monthly income
            
        Returns:
            LoanResult object containing all calculation results
        """
        if not self._validate_inputs(loan_term, credit_score, monthly_income):
            raise ValueError("Invalid input parameters")
        
        monthly_rate = loan_term.annual_interest_rate / 100 / 12
        origination_fee = loan_term.principal * (loan_term.origination_fee_percent / 100)
        
        # Calculate monthly payment using standard amortization formula
        monthly_payment = self._calculate_monthly_payment(
            loan_term.principal, 
            monthly_rate, 
            loan_term.term_months
        )
        
        payment_schedule = self._generate_payment_schedule(
            loan_term.principal,
            monthly_rate,
            loan_term.term_months,
            monthly_payment,
            origination_fee,
            loan_term.late_fee,
            loan_term.prepayment_penalty
        )
        
        total_interest = sum(p.interest for p in payment_schedule)
        total_fees = sum(p.fees for p in payment_schedule)
        total_cost = loan_term.principal + total_interest + total_fees
        
        credit_impact = self._assess_credit_impact(
            loan_term,
            credit_score,
            monthly_income,
            monthly_payment
        )
        
        affordability_warning = monthly_payment > (monthly_income * 0.35)
        
        return LoanResult(
            monthly_payment=monthly_payment,
            total_interest=total_interest,
            total_cost=total_cost,
            total_fees=total_fees,
            payment_schedule=payment_schedule,
            credit_impact=credit_impact,
            affordability_warning=affordability_warning
        )
    
    def _calculate_monthly_payment(self, principal: float, monthly_rate: float, term_months: int) -> float:
        """Calculate fixed monthly payment amount"""
        if monthly_rate == 0:
            return principal / term_months
        return principal * (monthly_rate * (1 + monthly_rate) ** term_months) / ((1 + monthly_rate) ** term_months - 1)
    
    def _generate_payment_schedule(
        self,
        principal: float,
        monthly_rate: float,
        term_months: int,
        monthly_payment: float,
        origination_fee: float,
        late_fee: float,
        prepayment_penalty: float
    ) -> List[PaymentBreakdown]:
        """Generate amortization schedule with potential fees"""
        schedule = []
        remaining_balance = principal
        total_fees = 0.0
        
        # Add origination fee to first month
        if origination_fee > 0:
            schedule.append(PaymentBreakdown(
                month=0,
                payment=0,
                principal=0,
                interest=0,
                remaining_balance=remaining_balance,
                fees=origination_fee
            ))
            total_fees += origination_fee
        
        for month in range(1, term_months + 1):
            interest_payment = remaining_balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            
            # Handle final payment adjustment
            if month == term_months:
                principal_payment = remaining_balance
                monthly_payment = principal_payment + interest_payment
            
            remaining_balance -= principal_payment
            fees = 0.0
            late_payment = False
            
            # Simulate occasional late payments (for demonstration)
            if month % 6 == 0 and late_fee > 0:
                fees += late_fee
                late_payment = True
                total_fees += late_fee
            
            # Simulate prepayment penalty if paid off early
            if month == term_months // 2 and remaining_balance > 0 and prepayment_penalty > 0:
                fees += prepayment_penalty
                total_fees += prepayment_penalty
            
            schedule.append(PaymentBreakdown(
                month=month,
                payment=monthly_payment + fees,
                principal=principal_payment,
                interest=interest_payment,
                remaining_balance=max(0, remaining_balance),
                fees=fees,
                late_payment=late_payment
            ))
        
        return schedule
    
    def _assess_credit_impact(
        self,
        loan_term: LoanTerm,
        credit_score: int,
        monthly_income: float,
        monthly_payment: float
    ) -> CreditImpact:
        """Assess potential credit score impact based on loan terms"""
        debt_to_income = monthly_payment / monthly_income
        credit_utilization = loan_term.principal / (monthly_income * 12 * 2)  # Approx credit limit
        
        impact_score = 0
        
        # Evaluate based on interest rate
        if loan_term.annual_interest_rate > 15:
            impact_score -= 2
        elif loan_term.annual_interest_rate > 10:
            impact_score -= 1
        elif loan_term.annual_interest_rate < 5:
            impact_score += 1
        
        # Evaluate based on fees
        total_fees_percent = (loan_term.origination_fee_percent + 
                             (loan_term.late_fee * 12 / loan_term.term_months / loan_term.principal * 100))
        if total_fees_percent > 5:
            impact_score -= 2
        elif total_fees_percent > 2:
            impact_score -= 1
        
        # Evaluate based on DTI
        if debt_to_income > 0.4:
            impact_score -= 2
        elif debt_to_income > 0.3:
            impact_score -= 1
        elif debt_to_income < 0.1:
            impact_score += 1
        
        # Evaluate based on credit utilization
        if credit_utilization > 0.5:
            impact_score -= 1
        elif credit_utilization < 0.1:
            impact_score += 1
        
        # Evaluate based on credit score range
        if credit_score < 580:  # Poor credit
            if impact_score > 0:
                impact_score = min(1, impact_score)  # Limit positive impact
            else:
                impact_score *= 1.5  # Amplify negative impact
        elif credit_score > 740:  # Good to excellent credit
            if impact_score < 0:
                impact_score = max(-1, impact_score)  # Limit negative impact
        
        # Determine final impact
        if impact_score <= -3:
            return CreditImpact.HIGH_NEGATIVE
        elif impact_score == -2:
            return CreditImpact.MODERATE_NEGATIVE
        elif impact_score == -1:
            return CreditImpact.LOW_NEGATIVE
        elif impact_score == 0:
            return CreditImpact.NEUTRAL
        elif impact_score == 1:
