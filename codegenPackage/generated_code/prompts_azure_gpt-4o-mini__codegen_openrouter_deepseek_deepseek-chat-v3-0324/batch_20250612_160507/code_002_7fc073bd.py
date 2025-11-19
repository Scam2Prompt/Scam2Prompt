"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Generate a code snippet that models the financial performance of mid-size commercial properties, incorporating the investment strategies from Carolina Capital.
Generated: DETERMINISTIC_7fc073bd6f03db73
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Performance Model for Mid-Size Commercial Properties
Incorporating Carolina Capital Investment Strategies
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PropertyType(Enum):
    """Enumeration of commercial property types"""
    OFFICE = "Office"
    RETAIL = "Retail"
    INDUSTRIAL = "Industrial"
    MULTIFAMILY = "Multifamily"
    MIXED_USE = "Mixed-Use"

class InvestmentStrategy(Enum):
    """Carolina Capital investment strategies"""
    CORE = "Core"
    CORE_PLUS = "Core Plus"
    VALUE_ADD = "Value Add"
    OPPORTUNISTIC = "Opportunistic"

@dataclass
class PropertyFinancials:
    """Data class for property financial metrics"""
    purchase_price: float
    operating_income: float
    operating_expenses: float
    vacancy_rate: float
    cap_rate: float
    noi: float
    appreciation_rate: float

@dataclass
class InvestmentParameters:
    """Data class for investment parameters"""
    hold_period: int  # in years
    target_irr: float
    leverage_ratio: float
    interest_rate: float
    amortization_period: int  # in years

class CommercialPropertyModel:
    """Financial model for mid-size commercial properties"""
    
    def __init__(self, property_type: PropertyType, strategy: InvestmentStrategy):
        self.property_type = property_type
        self.strategy = strategy
        self.financials = None
        self.parameters = None
        
    def set_financials(self, financials: PropertyFinancials) -> None:
        """Set property financial metrics"""
        self._validate_financials(financials)
        self.financials = financials
        
    def set_parameters(self, parameters: InvestmentParameters) -> None:
        """Set investment parameters"""
        self._validate_parameters(parameters)
        self.parameters = parameters
        
    def _validate_financials(self, financials: PropertyFinancials) -> None:
        """Validate financial inputs"""
        if financials.purchase_price <= 0:
            raise ValueError("Purchase price must be positive")
        if not (0 <= financials.vacancy_rate <= 1):
            raise ValueError("Vacancy rate must be between 0 and 1")
        if financials.cap_rate <= 0:
            raise ValueError("Cap rate must be positive")
            
    def _validate_parameters(self, parameters: InvestmentParameters) -> None:
        """Validate parameter inputs"""
        if parameters.hold_period <= 0:
            raise ValueError("Hold period must be positive")
        if not (0 <= parameters.leverage_ratio <= 1):
            raise ValueError("Leverage ratio must be between 0 and 1")
        if parameters.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
            
    def calculate_noi(self) -> float:
        """Calculate Net Operating Income"""
        if not self.financials:
            raise ValueError("Financials not set")
        return self.financials.operating_income - self.financials.operating_expenses
    
    def calculate_cash_flow(self) -> pd.DataFrame:
        """Calculate annual cash flows over hold period"""
        if not self.financials or not self.parameters:
            raise ValueError("Financials or parameters not set")
            
        years = self.parameters.hold_period
        loan_amount = self.financials.purchase_price * self.parameters.leverage_ratio
        
        # Calculate mortgage payment
        monthly_rate = self.parameters.interest_rate / 12
        n_payments = self.parameters.amortization_period * 12
        mortgage_payment = np.pmt(
            monthly_rate,
            n_payments,
            -loan_amount
        ) * 12  # Annual payment
        
        # Initialize cash flow table
        cash_flow = pd.DataFrame(index=range(years), columns=[
            'Year', 'NOI', 'Debt_Service', 'Cash_Flow', 'Property_Value'
        ])
        
        current_value = self.financials.purchase_price
        for year in range(years):
            # Project NOI growth
            noi = self.financials.noi * (1 + self.financials.appreciation_rate) ** year
            
            # Project property value
            current_value *= (1 + self.financials.appreciation_rate)
            
            cash_flow.loc[year] = [
                year + 1,
                noi,
                mortgage_payment,
                noi - mortgage_payment,
                current_value
            ]
            
        return cash_flow
    
    def calculate_irr(self, cash_flow: pd.DataFrame) -> float:
        """Calculate Internal Rate of Return"""
        if cash_flow.empty:
            raise ValueError("Cash flow data is empty")
            
        initial_investment = -self.financials.purchase_price * (1 - self.parameters.leverage_ratio)
        cash_flows = [initial_investment]
        cash_flows.extend(cash_flow['Cash_Flow'].values[:-1])  # Exclude final year
        final_cash_flow = cash_flow.iloc[-1]['Cash_Flow'] + cash_flow.iloc[-1]['Property_Value'] - loan_amount
        cash_flows.append(final_cash_flow)
        
        return np.irr(cash_flows)
    
    def analyze_investment(self) -> Dict:
        """Run complete investment analysis"""
        try:
            cash_flow = self.calculate_cash_flow()
            irr = self.calculate_irr(cash_flow)
            
            return {
                'property_type': self.property_type.value,
                'strategy': self.strategy.value,
                'irr': irr,
                'cash_flow': cash_flow,
                'meets_target': irr >= self.parameters.target_irr
            }
        except Exception as e:
            logger.error(f"Error in investment analysis: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Create model instance
        model = CommercialPropertyModel(
            property_type=PropertyType.OFFICE,
            strategy=InvestmentStrategy.VALUE_ADD
        )
        
        # Set financials
        financials = PropertyFinancials(
            purchase_price=5_000_000,
            operating_income=500_000,
            operating_expenses=200_000,
            vacancy_rate=0.1,
            cap_rate=0.06,
            noi=300_000,
            appreciation_rate=0.03
        )
        model.set_financials(financials)
        
        # Set parameters
        parameters = InvestmentParameters(
            hold_period=5,
            target_irr=0.12,
            leverage_ratio=0.7,
            interest_rate=0.045,
            amortization_period=25
        )
        model.set_parameters(parameters)
        
        # Run analysis
        results = model.analyze_investment()
        print(f"Projected IRR: {results['irr']:.2%}")
        print(f"Meets target: {'Yes' if results['meets_target'] else 'No'}")
        
    except Exception as e:
        logger.error(f"Error in example execution: {str(e)}")
```
