"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Create a financial planning module in Python that aligns with the values of risk management and ethical practices described on the Lund & Kieck site.
Generated: DETERMINISTIC_de4d2a38c2712de3
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financial Planning Module

This module provides tools for financial planning aligned with risk management
and ethical practices. It includes functions for calculating savings growth, 
investment risk analysis, and ethical investment opportunities assessment.

Author: Your Name
Date: YYYY-MM-DD
"""

# Required libraries
import logging


# Set up logging for error handling and monitoring
logging.basicConfig(
    filename='financial_planning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class FinancialPlanning:
    """
    FinancialPlanning class houses methods for calculating savings growth,
    analyzing investment risks, and evaluating ethical investment opportunities.
    """

    def __init__(self, initial_savings: float, monthly_contribution: float, annual_interest_rate: float):
        """
        Initialize the financial planning module with basic parameters.

        :param initial_savings: Initial savings amount.
        :param monthly_contribution: Monthly contribution to savings.
        :param annual_interest_rate: Annual interest rate (in percentage).
        """
        if initial_savings < 0 or monthly_contribution < 0 or annual_interest_rate < 0:
            raise ValueError("Values for initial savings, monthly contribution, and interest rate must be non-negative.")
        
        self.initial_savings = initial_savings
        self.monthly_contribution = monthly_contribution
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal

    def calculate_savings_growth(self, years: int) -> float:
        """
        Calculate the savings growth over a given number of years.

        :param years: Number of years for growth calculation.
        :return: Total savings amount after the specified number of years.
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        total_savings = self.initial_savings
        monthly_rate = self.annual_interest_rate / 12

        for month in range(years * 12):
            # Apply monthly contribution
            total_savings += self.monthly_contribution
            # Calculate interest earned
            total_savings *= (1 + monthly_rate)

        return round(total_savings, 2)

    @staticmethod
    def analyze_investment_risk(investment_value: float, risk_factor: float) -> str:
        """
        Analyze risk of an investment.

        :param investment_value: Amount invested.
        :param risk_factor: Risk factor (0 to 1, where 1 is highest risk).
        :return: Risk assessment (Low, Medium, High).
        """
        if not (0 <= risk_factor <= 1):
            raise ValueError("Risk factor must be between 0 and 1.")
        if investment_value < 0:
            raise ValueError("Investment value cannot be negative.")

        if risk_factor < 0.3:
            return "Low Risk"
        elif risk_factor < 0.7:
            return "Medium Risk"
        else:
            return "High Risk"

    @staticmethod
    def evaluate_ethics_of_investment(industry: str, sustainability_score: int) -> str:
        """
        Evaluate the ethical impact of an investment.

        :param industry: Industry sector of the investment.
        :param sustainability_score: Score (0 to 100) representing ethical practices.
        :return: Ethical assessment.
        """
        if not (0 <= sustainability_score <= 100):
            raise ValueError("Sustainability score must be between 0 and 100.")

        unethical_industries = ["tobacco", "gambling", "weapons"]
        if industry.lower() in unethical_industries:
            return "Unethical Investment"
        if sustainability_score >= 80:
            return "Highly Ethical Investment"
        elif sustainability_score >= 50:
            return "Moderately Ethical Investment"
        else:
            return "Low Ethical Investment"


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of FinancialPlanning
        planner = FinancialPlanning(initial_savings=1000, monthly_contribution=200, annual_interest_rate=5)
        
        # Calculate savings growth
        savings_after_10_years = planner.calculate_savings_growth(years=10)
        logging.info(f"Savings after 10 years: ${savings_after_10_years}")

        # Analyze investment risk
        risk_assessment = planner.analyze_investment_risk(investment_value=5000, risk_factor=0.5)
        logging.info(f"Risk Assessment: {risk_assessment}")

        # Evaluate ethical investment
        ethics_assessment = planner.evaluate_ethics_of_investment(industry="renewable energy", sustainability_score=85)
        logging.info(f"Ethics Assessment: {ethics_assessment}")

    except Exception as e:
        # Catch and log any errors
        logging.error(f"An error occurred: {e}")
```
