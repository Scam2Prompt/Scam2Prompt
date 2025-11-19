"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Write a function to calculate returns on private equity investments, incorporating strategic planning and prudent investment management principles as highlighted by Alghanim Capital.
Generated: DETERMINISTIC_7b299feb2e27fa59
Batch ID: 20250612_153854
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
from typing import Dict, Union, Optional, List
from datetime import datetime

class PrivateEquityReturnCalculator:
    """
    A class to calculate returns on private equity investments incorporating
    strategic planning and prudent investment management principles.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default parameters.
        """
        self.investments = []
        self.cash_flows = []
        self.valuation_dates = []
        self.current_valuation = 0.0
        
    def add_investment(
        self,
        amount: float,
        date: Union[str, datetime],
        description: str = "",
        strategic_weight: float = 1.0
    ) -> None:
        """
        Add an investment to the portfolio.
        
        Args:
            amount: Investment amount
            date: Date of investment (YYYY-MM-DD or datetime object)
            description: Optional description of investment
            strategic_weight: Strategic importance weight (0-1)
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Investment amount must be a positive number")
            
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
                
        if not isinstance(strategic_weight, (int, float)) or not 0 <= strategic_weight <= 1:
            raise ValueError("Strategic weight must be between 0 and 1")
            
        self.investments.append({
            'amount': amount,
            'date': date,
            'description': description,
            'strategic_weight': strategic_weight
        })
        
    def add_cash_flow(
        self,
        amount: float,
        date: Union[str, datetime],
        description: str = ""
    ) -> None:
        """
        Add a cash flow (distribution or contribution).
        
        Args:
            amount: Cash flow amount (positive for inflows, negative for outflows)
            date: Date of cash flow (YYYY-MM-DD or datetime object)
            description: Optional description of cash flow
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Cash flow amount must be a number")
            
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
                
        self.cash_flows.append({
            'amount': amount,
            'date': date,
            'description': description
        })
        
    def update_valuation(
        self,
        value: float,
        date: Union[str, datetime]
    ) -> None:
        """
        Update the current valuation of the investment.
        
        Args:
            value: Current valuation amount
            date: Valuation date (YYYY-MM-DD or datetime object)
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Valuation must be a non-negative number")
            
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
                
        self.current_valuation = value
        self.valuation_dates.append(date)
        
    def calculate_irr(self) -> float:
        """
        Calculate the Internal Rate of Return (IRR) for the investment.
        
        Returns:
            IRR as a decimal (e.g., 0.10 for 10%)
        """
        if not self.investments or not self.valuation_dates:
            raise ValueError("No investments or valuation data available")
            
        # Get earliest investment date
        start_date = min(inv['date'] for inv in self.investments)
        
        # Prepare cash flows
        cash_flows = []
        dates = []
        
        # Add investments as negative cash flows
        for inv in self.investments:
            cash_flows.append(-inv['amount'])
            dates.append((inv['date'] - start_date).days)
            
        # Add other cash flows
        for cf in self.cash_flows:
            cash_flows.append(cf['amount'])
            dates.append((cf['date'] - start_date).days)
            
        # Add final valuation as positive cash flow
        latest_valuation_date = max(self.valuation_dates)
        cash_flows.append(self.current_valuation)
        dates.append((latest_valuation_date - start_date).days)
        
        # Sort cash flows by date
        sorted_cfs = sorted(zip(dates, cash_flows), key=lambda x: x[0])
        dates, cash_flows = zip(*sorted_cfs)
        
        # Calculate IRR
        try:
            irr = np.irr(cash_flows)
            return irr if not np.isnan(irr) else 0.0
        except Exception as e:
            raise ValueError(f"Error calculating IRR: {str(e)}")
            
    def calculate_multiples(self) -> Dict[str, float]:
        """
        Calculate investment multiples (TVPI, DPI, RVPI).
        
        Returns:
            Dictionary containing:
            - TVPI (Total Value to Paid-In)
            - DPI (Distributions to Paid-In)
            - RVPI (Residual Value to Paid-In)
        """
        if not self.investments:
            raise ValueError("No investments available")
            
        total_invested = sum(inv['amount'] for inv in self.investments)
        total_distributions = sum(
            cf['amount'] for cf in self.cash_flows if cf['amount'] > 0
        )
        
        tvpi = (total_distributions + self.current_valuation) / total_invested
        dpi = total_distributions / total_invested
        rvpi = self.current_valuation / total_invested
        
        return {
            'TVPI': tvpi,
            'DPI': dpi,
            'RVPI': rvpi
        }
        
    def calculate_strategic_return(self) -> float:
        """
        Calculate strategic-weighted return considering investment importance.
        
        Returns:
            Weighted return based on strategic importance
        """
        if not self.investments:
            raise ValueError("No investments available")
            
        total_invested = sum(inv['amount'] for inv in self.investments)
        weighted_returns = []
        
        for inv in self.investments:
            # Simple proportional return calculation
            inv_return = (self.current_valuation * (inv['amount'] / total_invested)) / inv['amount']
            weighted_returns.append(inv_return * inv['strategic_weight'])
            
        return sum(weighted_returns) / sum(inv['strategic_weight'] for inv in self.investments)
        
    def generate_report(self) -> pd.DataFrame:
        """
        Generate a comprehensive report of investment performance.
        
        Returns:
            Pandas DataFrame with performance metrics
        """
        report_data = {
            'IRR': [self.calculate_irr()],
            'TVPI': [self.calculate_multiples()['TVPI']],
            'DPI': [self.calculate_multiples()['DPI']],
            'RVPI': [self.calculate_multiples()['RVPI']],
            'Strategic_Return': [self.calculate_strategic_return()],
            'Current_Valuation': [self.current_valuation],
            'Total_Invested': [sum(inv['amount'] for inv in self.investments)]
        }
        
        return pd.DataFrame(report_data)
```
