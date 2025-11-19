"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write code to simulate various long-term insurance scenarios, including premium calculations and coverage options, based on TSM Wealth's insurance services.
Generated: DETERMINISTIC_7f37334dab5accce
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum

class PolicyType(Enum):
    """Enumeration of available insurance policy types."""
    TERM_LIFE = "Term Life Insurance"
    WHOLE_LIFE = "Whole Life Insurance"
    UNIVERSAL_LIFE = "Universal Life Insurance"
    CRITICAL_ILLNESS = "Critical Illness Insurance"
    DISABILITY = "Disability Insurance"

class Gender(Enum):
    """Enumeration for gender classification."""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class PremiumFrequency(Enum):
    """Enumeration for premium payment frequencies."""
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMI_ANNUALLY = "Semi-Annually"
    ANNUALLY = "Annually"

class UnderwritingStatus(Enum):
    """Enumeration for underwriting status."""
    PENDING = "Pending"
    APPROVED = "Approved"
    DECLINED = "Declined"
    RATED = "Rated"

class InsurancePolicy:
    """Base class for insurance policy simulation."""
    
    def __init__(
        self,
        policy_type: PolicyType,
        coverage_amount: float,
        start_date: datetime,
        end_date: datetime,
        insured_name: str,
        insured_age: int,
        insured_gender: Gender,
        premium_frequency: PremiumFrequency,
        smoker_status: bool,
        underwriting_status: UnderwritingStatus = UnderwritingStatus.PENDING
    ):
        """Initialize an insurance policy.
        
        Args:
            policy_type: Type of insurance policy
            coverage_amount: Total coverage amount
            start_date: Policy start date
            end_date: Policy end date
            insured_name: Name of insured individual
            insured_age: Age of insured individual
            insured_gender: Gender of insured individual
            premium_frequency: Frequency of premium payments
            smoker_status: Whether the insured is a smoker
            underwriting_status: Current underwriting status
        """
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
        self.start_date = start_date
        self.end_date = end_date
        self.insured_name = insured_name
        self.insured_age = insured_age
        self.insured_gender = insured_gender
        self.premium_frequency = premium_frequency
        self.smoker_status = smoker_status
        self.underwriting_status = underwriting_status
        self.premium_history = []
        self.claims_history = []
        
    def calculate_base_premium(self) -> float:
        """Calculate base premium based on policy type and insured attributes."""
        base_rate = 0
        
        if self.policy_type == PolicyType.TERM_LIFE:
            base_rate = 0.05  # 5 per 1000 coverage
        elif self.policy_type == PolicyType.WHOLE_LIFE:
            base_rate = 0.15  # 15 per 1000 coverage
        elif self.policy_type == PolicyType.UNIVERSAL_LIFE:
            base_rate = 0.10  # 10 per 1000 coverage
        elif self.policy_type == PolicyType.CRITICAL_ILLNESS:
            base_rate = 0.08  # 8 per 1000 coverage
        elif self.policy_type == PolicyType.DISABILITY:
            base_rate = 0.12  # 12 per 1000 coverage
            
        # Apply age factor
        age_factor = 1 + (self.insured_age - 18) * 0.02
        
        # Apply gender factor
        if self.insured_gender == Gender.MALE:
            gender_factor = 1.1
        elif self.insured_gender == Gender.FEMALE:
            gender_factor = 0.9
        else:
            gender_factor = 1.0
            
        # Apply smoker factor
        smoker_factor = 1.5 if self.smoker_status else 1.0
        
        # Calculate annual premium
        annual_premium = (self.coverage_amount / 1000) * base_rate * age_factor * gender_factor * smoker_factor
        
        return annual_premium
    
    def calculate_frequency_adjusted_premium(self) -> float:
        """Adjust premium based on payment frequency."""
        annual_premium = self.calculate_base_premium()
        
        if self.premium_frequency == PremiumFrequency.MONTHLY:
            return annual_premium / 12 * 1.05  # 5% loading for monthly payments
        elif self.premium_frequency == PremiumFrequency.QUARTERLY:
            return annual_premium / 4 * 1.03  # 3% loading for quarterly
        elif self.premium_frequency == PremiumFrequency.SEMI_ANNUALLY:
            return annual_premium / 2 * 1.02  # 2% loading for semi-annual
        else:  # Annual
            return annual_premium
    
    def record_premium_payment(self, amount: float, payment_date: datetime) -> None:
        """Record a premium payment.
        
        Args:
            amount: Amount paid
            payment_date: Date of payment
        """
        if amount <= 0:
            raise ValueError("Premium payment amount must be positive")
            
        expected_amount = self.calculate_frequency_adjusted_premium()
        if abs(amount - expected_amount) > 0.01 * expected_amount:
            raise ValueError(f"Premium payment amount {amount} differs significantly from expected {expected_amount}")
            
        self.premium_history.append({
            "date": payment_date,
            "amount": amount,
            "frequency": self.premium_frequency.value
        })
    
    def record_claim(self, claim_amount: float, claim_date: datetime, claim_reason: str) -> None:
        """Record an insurance claim.
        
        Args:
            claim_amount: Amount claimed
            claim_date: Date of claim
            claim_reason: Reason for claim
        """
        if claim_amount <= 0:
            raise ValueError("Claim amount must be positive")
            
        if claim_amount > self.coverage_amount:
            raise ValueError("Claim amount exceeds coverage")
            
        self.claims_history.append({
            "date": claim_date,
            "amount": claim_amount,
            "reason": claim_reason,
            "status": "Pending"
        })
    
    def get_policy_summary(self) -> Dict:
        """Get a summary of the policy details."""
        return {
            "policy_type": self.policy_type.value,
            "coverage_amount": self.coverage_amount,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "insured_name": self.insured_name,
            "insured_age": self.insured_age,
            "insured_gender": self.insured_gender.value,
            "premium_frequency": self.premium_frequency.value,
            "smoker_status": self.smoker_status,
            "underwriting_status": self.underwriting_status.value,
            "current_premium": self.calculate_frequency_adjusted_premium(),
            "total_premiums_paid": sum(p["amount"] for p in self.premium_history),
            "total_claims": sum(c["amount"] for c in self.claims_history)
        }

class TermLifePolicy(InsurancePolicy):
    """Specialized class for Term Life Insurance policies."""
    
    def __init__(
        self,
        coverage_amount: float,
        start_date: datetime,
        term_years: int,
        insured_name: str,
        insured_age: int,
        insured_gender: Gender,
        premium_frequency: PremiumFrequency,
        smoker_status: bool,
        convertible: bool = False,
        renewable: bool = False
    ):
        """Initialize a term life policy.
        
        Args:
            coverage_amount: Total coverage amount
            start_date: Policy start date
            term_years: Duration of term in years
            insured_name: Name of insured individual
            insured_age: Age of insured individual
            insured_gender: Gender of insured individual
            premium_frequency: Frequency of premium payments
            smoker_status: Whether the insured is a smoker
            convertible: Whether policy is convertible to permanent insurance
            renewable: Whether policy is renewable without medical underwriting
        """
        end_date = start_date + timedelta(days=365 * term_years)
        super().__init__(
            policy_type=PolicyType.TERM_LIFE,
            coverage_amount=coverage_amount,
            start_date=start_date,
            end_date=end_date,
            insured_name=insured_name,
            insured_age=insured_age,
            insured_gender=insured_gender,
            premium_frequency=premium_frequency,
            smoker_status=smoker_status
        )
        self.convertible = convertible
        self.renewable = renewable
        
    def calculate_base_premium(self) -> float:
        """Calculate base premium with term life specific adjustments."""
        base_premium = super().calculate_base_premium()
        
        # Apply term life specific factors
        if self.convertible:
            base_premium *= 1.1  # 10% loading for convertible
