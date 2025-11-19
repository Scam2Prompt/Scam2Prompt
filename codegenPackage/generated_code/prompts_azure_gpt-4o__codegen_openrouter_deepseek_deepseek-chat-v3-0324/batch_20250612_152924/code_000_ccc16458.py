"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: Write Python code to simulate a corporate valuation model for mergers and acquisitions, incorporating strategic planning principles as described by Maximus Limited.
Generated: DETERMINISTIC_ccc1645893b942eb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum, auto

class ValuationMethod(Enum):
    DISCOUNTED_CASH_FLOW = auto()
    COMPARABLE_COMPANY_ANALYSIS = auto()
    PRECEDENT_TRANSACTIONS = auto()
    LEVERAGED_BUYOUT = auto()

@dataclass
class FinancialProjection:
    revenue_growth: np.ndarray  # Array of annual growth rates
    ebitda_margin: np.ndarray   # Array of annual EBITDA margins
    capex: np.ndarray           # Array of annual capital expenditures
    nwc_percent: float          # Net working capital as % of revenue
    tax_rate: float             # Corporate tax rate
    projection_years: int       # Number of projection years

@dataclass
class CostOfCapital:
    risk_free_rate: float       # Risk-free rate (e.g., 10-yr Treasury)
    equity_risk_premium: float  # Market risk premium
    beta: float                 # Company beta
    cost_of_debt: float         # Pre-tax cost of debt
    debt_to_equity: float       # Target debt-to-equity ratio

@dataclass
class TerminalValue:
    growth_rate: float          # Terminal growth rate
    method: str                 # 'perpetuity' or 'exit_multiple'

@dataclass
class SynergyAssumptions:
    revenue_synergies: np.ndarray  # Annual revenue synergies
    cost_synergies: np.ndarray     # Annual cost synergies
    realization_year: int          # Year synergies start being realized

class MergerValuationModel:
    """
    Corporate valuation model for M&A incorporating strategic planning principles.
    Implements DCF as primary valuation method with optional secondary methods.
    """
    
    def __init__(self, financials: FinancialProjection, cost_of_capital: CostOfCapital,
                 terminal_value: TerminalValue, synergies: Optional[SynergyAssumptions] = None):
        self.financials = financials
        self.cost_of_capital = cost_of_capital
        self.terminal_value = terminal_value
        self.synergies = synergies
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate model inputs for consistency and reasonableness."""
        if len(self.financials.revenue_growth) != self.financials.projection_years:
            raise ValueError("Revenue growth array length must match projection years")
        if len(self.financials.ebitda_margin) != self.financials.projection_years:
            raise ValueError("EBITDA margin array length must match projection years")
        if len(self.financials.capex) != self.financials.projection_years:
            raise ValueError("Capex array length must match projection years")
        if self.terminal_value.growth_rate >= self.cost_of_capital.risk_free_rate + self.cost_of_capital.equity_risk_premium:
            raise ValueError("Terminal growth rate must be lower than discount rate")
            
    def calculate_wacc(self) -> float:
        """Calculate weighted average cost of capital (WACC)."""
        cost_of_equity = (self.cost_of_capital.risk_free_rate + 
                         self.cost_of_capital.beta * self.cost_of_capital.equity_risk_premium)
        
        after_tax_cost_of_debt = self.cost_of_capital.cost_of_debt * (1 - self.financials.tax_rate)
        
        equity_ratio = 1 / (1 + self.cost_of_capital.debt_to_equity)
        debt_ratio = 1 - equity_ratio
        
        wacc = (equity_ratio * cost_of_equity) + (debt_ratio * after_tax_cost_of_debt)
        return wacc
    
    def _calculate_unlevered_free_cash_flow(self) -> np.ndarray:
        """Calculate unlevered free cash flows for projection period."""
        years = self.financials.projection_years
        revenue = np.zeros(years)
        ebitda = np.zeros(years)
        nwc = np.zeros(years)
        ufcf = np.zeros(years)
        
        # Base year assumptions (year 0)
        revenue[0] = 1000  # Base revenue (can be parameterized)
        
        for t in range(years):
            if t > 0:
                revenue[t] = revenue[t-1] * (1 + self.financials.revenue_growth[t])
            
            ebitda[t] = revenue[t] * self.financials.ebitda_margin[t]
            nwc[t] = revenue[t] * self.financials.nwc_percent
            
            # Calculate UFCF: EBITDA - Taxes - Capex - ΔNWC
            taxes = ebitda[t] * self.financials.tax_rate
            delta_nwc = nwc[t] - (nwc[t-1] if t > 0 else 0)
            ufcf[t] = ebitda[t] - taxes - self.financials.capex[t] - delta_nwc
            
            # Apply synergies if available
            if self.synergies and t >= self.synergies.realization_year:
                ufcf[t] += (self.synergies.revenue_synergies[t] * (1 - self.financials.tax_rate) +
                           self.synergies.cost_synergies[t] * (1 - self.financials.tax_rate))
        
        return ufcf
    
    def _calculate_terminal_value(self, final_ufcf: float) -> float:
        """Calculate terminal value using specified method."""
        wacc = self.calculate_wacc()
        
        if self.terminal_value.method == 'perpetuity':
            return final_ufcf * (1 + self.terminal_value.growth_rate) / (wacc - self.terminal_value.growth_rate)
        elif self.terminal_value.method == 'exit_multiple':
            # Assuming exit multiple is based on final year EBITDA
            final_ebitda = final_ufcf / (1 - self.financials.tax_rate)  # Simplified approximation
            exit_multiple = 8.0  # Could be parameterized
            return final_ebitda * exit_multiple
        else:
            raise ValueError("Invalid terminal value method")
    
    def dcf_valuation(self) -> Tuple[float, pd.DataFrame]:
        """Perform discounted cash flow valuation."""
        ufcf = self._calculate_unlevered_free_cash_flow()
        wacc = self.calculate_wacc()
        
        # Discount projected cash flows
        discounted_cash_flows = np.zeros(self.financials.projection_years)
        for t in range(self.financials.projection_years):
            discounted_cash_flows[t] = ufcf[t] / ((1 + wacc) ** (t + 1))
        
        # Calculate terminal value and discount it
        terminal_value = self._calculate_terminal_value(ufcf[-1])
        discounted_terminal_value = terminal_value / ((1 + wacc) ** self.financials.projection_years)
        
        # Sum components for enterprise value
        enterprise_value = np.sum(discounted_cash_flows) + discounted_terminal_value
        
        # Create output DataFrame
        results = pd.DataFrame({
            'Year': range(1, self.financials.projection_years + 1),
            'Revenue': [1000 * (1 + self.financials.revenue_growth[0]) ** t for t in range(self.financials.projection_years)],
            'EBITDA': [1000 * (1 + self.financials.revenue_growth[0]) ** t * self.financials.ebitda_margin[t] 
                      for t in range(self.financials.projection_years)],
            'UFCF': ufcf,
            'Discounted UFCF': discounted_cash_flows
        })
        
        return enterprise_value, results
    
    def comparable_companies_analysis(self, multiples: Dict[str, float]) -> float:
        """Valuation based on comparable companies multiples."""
        # Calculate relevant metrics (using final projection year)
        final_revenue = 1000 * (1 + self.financials.revenue_growth[-1]) ** self.financials.projection_years
        final_ebitda = final_revenue * self.financials.ebitda_margin[-1]
        
        # Apply multiples
        valuation = {}
        if 'EV/Revenue' in multiples:
            valuation['EV/Revenue'] = final_revenue * multiples['EV/Revenue']
        if 'EV/EBITDA' in multiples:
            valuation['EV/EBITDA'] = final_ebitda * multiples['EV/EBITDA']
        
        # Return average of available multiples
        if not valuation:
            raise ValueError("No valid multiples provided")
        return sum(valuation.values()) / len(valuation)
    
    def precedent_transactions
