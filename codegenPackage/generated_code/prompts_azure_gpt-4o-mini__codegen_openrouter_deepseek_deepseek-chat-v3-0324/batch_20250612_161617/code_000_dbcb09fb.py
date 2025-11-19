"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python script that calculates the potential return on investment for properties in the $2 million to $20 million range, as described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dbcb09fbf4bae916
Batch ID: 20250612_161617
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
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PropertyROICalculator:
    """
    A calculator for estimating potential return on investment (ROI) for high-value properties.
    """
    
    def __init__(self, property_value: float, annual_rent: float, holding_period: int = 5):
        """
        Initialize the calculator with property details.
        
        Args:
            property_value: The purchase price of the property (2M to 20M range)
            annual_rent: Expected annual rental income
            holding_period: Number of years to hold the property (default: 5)
        """
        self.property_value = property_value
        self.annual_rent = annual_rent
        self.holding_period = holding_period
        self.validate_inputs()
        
    def validate_inputs(self) -> None:
        """Validate that inputs are within expected ranges."""
        if not (2_000_000 <= self.property_value <= 20_000_000):
            raise ValueError("Property value must be between $2M and $20M")
        if self.annual_rent <= 0:
            raise ValueError("Annual rent must be positive")
        if self.holding_period <= 0:
            raise ValueError("Holding period must be at least 1 year")
            
    def calculate_annual_expenses(self, expense_ratio: float = 0.35) -> float:
        """
        Calculate estimated annual expenses.
        
        Args:
            expense_ratio: Percentage of rent that goes to expenses (default: 35%)
            
        Returns:
            Estimated annual expenses
        """
        return self.annual_rent * expense_ratio
    
    def calculate_net_operating_income(self) -> float:
        """
        Calculate annual Net Operating Income (NOI).
        
        Returns:
            Annual NOI
        """
        expenses = self.calculate_annual_expenses()
        return self.annual_rent - expenses
    
    def calculate_cash_flow(self, mortgage_rate: float = 0.05, down_payment: float = 0.3) -> Dict[int, float]:
        """
        Calculate annual cash flows over the holding period.
        
        Args:
            mortgage_rate: Annual mortgage interest rate (default: 5%)
            down_payment: Percentage of property value as down payment (default: 30%)
            
        Returns:
            Dictionary of year to cash flow
        """
        loan_amount = self.property_value * (1 - down_payment)
        annual_payment = self._calculate_mortgage_payment(loan_amount, mortgage_rate)
        noi = self.calculate_net_operating_income()
        
        cash_flows = {}
        for year in range(1, self.holding_period + 1):
            cash_flows[year] = noi - annual_payment
            
        return cash_flows
    
    def _calculate_mortgage_payment(self, principal: float, rate: float, years: int = 30) -> float:
        """
        Calculate annual mortgage payment.
        
        Args:
            principal: Loan amount
            rate: Annual interest rate
            years: Loan term in years (default: 30)
            
        Returns:
            Annual mortgage payment
        """
        monthly_rate = rate / 12
        months = years * 12
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        return monthly_payment * 12
    
    def calculate_roi(
        self,
        appreciation_rate: float = 0.03,
        selling_cost: float = 0.06,
        mortgage_rate: float = 0.05,
        down_payment: float = 0.3
    ) -> Dict[str, float]:
        """
        Calculate comprehensive ROI metrics.
        
        Args:
            appreciation_rate: Annual property value appreciation rate (default: 3%)
            selling_cost: Percentage of sale price for selling costs (default: 6%)
            mortgage_rate: Annual mortgage interest rate (default: 5%)
            down_payment: Percentage of property value as down payment (default: 30%)
            
        Returns:
            Dictionary of ROI metrics
        """
        try:
            # Initial investment
            initial_investment = self.property_value * down_payment
            
            # Calculate cash flows
            cash_flows = self.calculate_cash_flow(mortgage_rate, down_payment)
            total_cash_flow = sum(cash_flows.values())
            
            # Calculate sale proceeds
            future_value = self.property_value * (1 + appreciation_rate) ** self.holding_period
            remaining_loan = self._calculate_remaining_loan(
                self.property_value * (1 - down_payment),
                mortgage_rate
            )
            sale_proceeds = future_value * (1 - selling_cost) - remaining_loan
            
            # Total return
            total_return = total_cash_flow + sale_proceeds
            
            # ROI calculations
            simple_roi = (total_return - initial_investment) / initial_investment
            annualized_roi = ((1 + simple_roi) ** (1 / self.holding_period)) - 1
            
            return {
                "initial_investment": initial_investment,
                "total_cash_flow": total_cash_flow,
                "sale_proceeds": sale_proceeds,
                "total_return": total_return,
                "simple_roi": simple_roi,
                "annualized_roi": annualized_roi,
                "future_property_value": future_value
            }
            
        except Exception as e:
            logger.error(f"Error calculating ROI: {str(e)}")
            raise
            
    def _calculate_remaining_loan(self, principal: float, rate: float) -> float:
        """
        Calculate remaining loan balance after holding period.
        
        Args:
            principal: Original loan amount
            rate: Annual interest rate
            
        Returns:
            Remaining loan balance
        """
        monthly_rate = rate / 12
        months = 30 * 12  # 30-year loan
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        
        remaining_months = months - (self.holding_period * 12)
        if remaining_months <= 0:
            return 0.0
            
        remaining_balance = (monthly_payment * (1 - (1 + monthly_rate) ** -remaining_months)) / monthly_rate
        return remaining_balance
        
    def generate_report(self, roi_metrics: Dict[str, float]) -> pd.DataFrame:
        """
        Generate a detailed ROI report.
        
        Args:
            roi_metrics: Dictionary of ROI metrics from calculate_roi()
            
        Returns:
            DataFrame containing the ROI report
        """
        report_data = {
            "Metric": [
                "Initial Investment",
                "Total Cash Flow (Hold Period)",
                "Estimated Sale Proceeds",
                "Total Return",
                "Simple ROI",
                "Annualized ROI",
                "Future Property Value"
            ],
            "Value": [
                f"${roi_metrics['initial_investment']:,.2f}",
                f"${roi_metrics['total_cash_flow']:,.2f}",
                f"${roi_metrics['sale_proceeds']:,.2f}",
                f"${roi_metrics['total_return']:,.2f}",
                f"{roi_metrics['simple_roi']:.2%}",
                f"{roi_metrics['annualized_roi']:.2%}",
                f"${roi_metrics['future_property_value']:,.2f}"
            ]
        }
        
        return pd.DataFrame(report_data)

def analyze_property_portfolio(properties: List[Dict[str, float]]) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """
    Analyze a portfolio of properties.
    
    Args:
        properties: List of property dictionaries with 'value' and 'rent' keys
        
    Returns:
        Tuple of (individual property reports, aggregate metrics)
    """
    individual_reports = []
    aggregate_metrics = {
        "total_initial_investment": 0,
        "total_cash_flow": 0,
        "total_sale_proceeds": 0,
        "total_return": 0,
        "weighted_annualized_roi": 0
    }
    
    for prop in properties:
        try:
            calculator = PropertyROICalculator(
                property_value=prop['value'],
                annual_rent=prop['rent'],
                holding_period=5
            )
            roi = calculator.calculate_roi()
            report = calculator.generate_report(roi)
            individual_reports.append(report)
            
            # Aggregate metrics
            initial_investment = roi['initial_investment']
            aggregate_metrics['total_initial_investment'] += initial_investment
            aggregate_metrics['total_cash_flow'] += roi['total_cash_flow']
            aggregate_metrics['total_sale_proceeds'] += roi['s
