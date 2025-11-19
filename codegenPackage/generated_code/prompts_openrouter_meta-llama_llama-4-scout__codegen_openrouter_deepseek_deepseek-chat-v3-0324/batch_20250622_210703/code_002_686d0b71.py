"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: "Generate a code snippet for calculating PPP project financing and valuation using Python or R, considering VFM Advisory's expertise in financial modeling."
Generated: DETERMINISTIC_686d0b71d5924dbd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
PPP Project Financing and Valuation Calculator

This script provides financial modeling capabilities for Public-Private Partnership (PPP) projects,
incorporating Value for Money (VFM) analysis principles commonly used by VFM Advisory.

Features:
- Discounted Cash Flow (DCF) valuation
- Debt service calculations
- Sensitivity analysis
- VFM assessment metrics
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

class PPPFinancialModel:
    """
    A financial model for PPP project evaluation.
    
    Attributes:
        project_life (int): Project life in years
        construction_period (int): Construction period in years
        discount_rate (float): Discount rate for NPV calculations
        inflation_rate (float): Annual inflation rate
        tax_rate (float): Corporate tax rate
        debt_ratio (float): Debt to total capital ratio
        debt_interest_rate (float): Annual interest rate on debt
        debt_tenor (int): Loan repayment period in years
        equity_return (float): Required return on equity
        opex_growth_rate (float): Annual growth rate for operating expenses
        revenue_growth_rate (float): Annual growth rate for revenues
    """
    
    def __init__(self, project_life: int = 30, construction_period: int = 3,
                 discount_rate: float = 0.08, inflation_rate: float = 0.02,
                 tax_rate: float = 0.25, debt_ratio: float = 0.7,
                 debt_interest_rate: float = 0.06, debt_tenor: int = 15,
                 equity_return: float = 0.12, opex_growth_rate: float = 0.03,
                 revenue_growth_rate: float = 0.04):
        """
        Initialize the financial model with default or provided parameters.
        """
        self.project_life = project_life
        self.construction_period = construction_period
        self.discount_rate = discount_rate
        self.inflation_rate = inflation_rate
        self.tax_rate = tax_rate
        self.debt_ratio = debt_ratio
        self.debt_interest_rate = debt_interest_rate
        self.debt_tenor = debt_tenor
        self.equity_return = equity_return
        self.opex_growth_rate = opex_growth_rate
        self.revenue_growth_rate = revenue_growth_rate
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate model parameters for logical consistency."""
        if self.debt_ratio < 0 or self.debt_ratio > 1:
            raise ValueError("Debt ratio must be between 0 and 1")
        if self.construction_period >= self.project_life:
            raise ValueError("Construction period must be less than project life")
        if self.debt_tenor > self.project_life:
            raise ValueError("Debt tenor cannot exceed project life")
    
    def calculate_dcf(self, capex: List[float], opex: List[float], 
                     revenues: List[float]) -> Dict[str, float]:
        """
        Calculate Discounted Cash Flow metrics for the project.
        
        Args:
            capex: Annual capital expenditures during construction
            opex: Annual operating expenses during operation
            revenues: Annual revenues during operation
            
        Returns:
            Dictionary containing NPV, IRR, and other financial metrics
        """
        if len(capex) != self.construction_period:
            raise ValueError("Capex list length must match construction period")
        if len(opex) != self.project_life - self.construction_period:
            raise ValueError("Opex list length must match operation period")
        if len(revenues) != self.project_life - self.construction_period:
            raise ValueError("Revenues list length must match operation period")
        
        # Calculate cash flows
        cash_flows = [-x for x in capex]  # Negative for construction period
        for year in range(self.construction_period, self.project_life):
            op_year = year - self.construction_period
            ebitda = revenues[op_year] - opex[op_year]
            interest = self._calculate_debt_service(capex)[year]['interest']
            taxable_income = ebitda - interest
            tax = max(0, taxable_income) * self.tax_rate
            net_income = ebitda - interest - tax
            cash_flows.append(net_income)
        
        # Calculate financial metrics
        npv = np.npv(self.discount_rate, cash_flows)
        irr = np.irr(cash_flows)
        
        return {
            'npv': npv,
            'irr': irr,
            'cash_flows': cash_flows,
            'payback_period': self._calculate_payback_period(cash_flows)
        }
    
    def _calculate_debt_service(self, capex: List[float]) -> List[Dict[str, float]]:
        """
        Calculate annual debt service payments.
        
        Args:
            capex: Annual capital expenditures during construction
            
        Returns:
            List of dictionaries containing principal, interest, and total payment for each year
        """
        total_capex = sum(capex)
        debt_amount = total_capex * self.debt_ratio
        annual_payment = self._calculate_loan_payment(debt_amount)
        
        debt_schedule = []
        remaining_principal = debt_amount
        
        for year in range(self.project_life):
            if year < self.construction_period:
                # During construction, only interest accrues
                interest = remaining_principal * self.debt_interest_rate
                principal = 0
            elif year < self.construction_period + self.debt_tenor:
                # During repayment period
                interest = remaining_principal * self.debt_interest_rate
                principal = annual_payment - interest
                remaining_principal -= principal
            else:
                # After loan is repaid
                principal = 0
                interest = 0
            
            debt_schedule.append({
                'year': year + 1,
                'principal': principal,
                'interest': interest,
                'total_payment': principal + interest
            })
        
        return debt_schedule
    
    def _calculate_loan_payment(self, principal: float) -> float:
        """Calculate annual loan payment using PMT formula."""
        if self.debt_tenor == 0:
            return 0
        return principal * (self.debt_interest_rate * (1 + self.debt_interest_rate)**self.debt_tenor) / \
               ((1 + self.debt_interest_rate)**self.debt_tenor - 1)
    
    def _calculate_payback_period(self, cash_flows: List[float]) -> float:
        """Calculate the payback period in years."""
        cumulative = 0
        for year, cf in enumerate(cash_flows):
            cumulative += cf
            if cumulative >= 0:
                return year + (abs(cumulative - cf) / cf if cf != 0 else 0)
        return float('inf')  # Never pays back
    
    def sensitivity_analysis(self, capex: List[float], opex: List[float], 
                            revenues: List[float], variables: List[str], 
                            ranges: Dict[str, Tuple[float, float]], steps: int = 5) -> pd.DataFrame:
        """
        Perform sensitivity analysis on key variables.
        
        Args:
            capex: Base case capital expenditures
            opex: Base case operating expenses
            revenues: Base case revenues
            variables: List of variables to analyze (e.g., ['discount_rate', 'revenue_growth_rate'])
            ranges: Dictionary with min/max values for each variable
            steps: Number of steps in the sensitivity analysis
            
        Returns:
            DataFrame with sensitivity analysis results
        """
        results = []
        base_case = self.calculate_dcf(capex, opex, revenues)
        
        for var in variables:
            if var not in ranges:
                raise ValueError(f"Range not provided for variable {var}")
            
            min_val, max_val = ranges[var]
            step_size = (max_val - min_val) / (steps - 1)
            
            for i in range(steps):
                current_val = min_val + i * step_size
                setattr(self, var, current_val)
                case = self.calculate_dcf(capex, opex, revenues)
                
                results.append({
                    'variable': var,
                    'value': current_val,
                    'npv': case['npv'],
                    'irr': case['irr'],
                    'npv_change': (case['npv'] - base_case['npv']) / base_case['npv'] if base_case['npv'] != 0 else 0,
                    'irr_change': (case['irr'] - base_case['irr']) / base_case['irr'] if base_case['irr'] != 0 else 0
                })
        
        return pd.DataFrame(results)
    
    def calculate_vfm(self, psc_cash_flows: List[float], ppp_cash_flows: List[float]) -> Dict[str, float]:
        """
