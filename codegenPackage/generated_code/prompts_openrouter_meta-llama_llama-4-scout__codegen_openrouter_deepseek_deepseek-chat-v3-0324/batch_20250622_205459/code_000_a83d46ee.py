"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Write a Python code snippet to calculate the benefits of using freight factoring for a small trucking company, considering same-day funding and non-recourse programs.
Generated: DETERMINISTIC_a83d46ee9ce6c9e2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class FreightFactoringBenefits:
    """
    Represents the financial benefits of freight factoring for a trucking company.
    """
    same_day_funding_benefit: float
    non_recourse_benefit: float
    total_benefit: float

class FreightFactoringCalculator:
    """
    Calculates the benefits of freight factoring for a trucking company.
    """
    
    def __init__(self, annual_revenue: float, average_invoice_amount: float, 
                 invoice_processing_days: int, bad_debt_percentage: float):
        """
        Initialize the calculator with company financial metrics.
        
        Args:
            annual_revenue: Annual revenue of the trucking company in USD
            average_invoice_amount: Average invoice amount in USD
            invoice_processing_days: Average days to get paid without factoring
            bad_debt_percentage: Percentage of invoices that become bad debt (0-100)
        """
        if annual_revenue <= 0:
            raise ValueError("Annual revenue must be positive")
        if average_invoice_amount <= 0:
            raise ValueError("Average invoice amount must be positive")
        if invoice_processing_days < 0:
            raise ValueError("Invoice processing days cannot be negative")
        if not 0 <= bad_debt_percentage <= 100:
            raise ValueError("Bad debt percentage must be between 0 and 100")
            
        self.annual_revenue = annual_revenue
        self.average_invoice_amount = average_invoice_amount
        self.invoice_processing_days = invoice_processing_days
        self.bad_debt_percentage = bad_debt_percentage / 100  # Convert to decimal
        
    def calculate_same_day_funding_benefit(self, cost_of_capital: float) -> float:
        """
        Calculate the benefit of same-day funding by reducing cash flow delays.
        
        Args:
            cost_of_capital: Annual cost of capital as a decimal (e.g., 0.08 for 8%)
            
        Returns:
            Estimated annual benefit from same-day funding in USD
        """
        if cost_of_capital < 0:
            raise ValueError("Cost of capital cannot be negative")
            
        # Calculate the benefit from reduced payment delays
        daily_cost_of_capital = cost_of_capital / 365
        annual_benefit = self.annual_revenue * daily_cost_of_capital * self.invoice_processing_days
        return annual_benefit
    
    def calculate_non_recourse_benefit(self) -> float:
        """
        Calculate the benefit of non-recourse factoring by eliminating bad debt.
        
        Returns:
            Estimated annual benefit from bad debt elimination in USD
        """
        return self.annual_revenue * self.bad_debt_percentage
    
    def calculate_benefits(self, cost_of_capital: float) -> FreightFactoringBenefits:
        """
        Calculate all factoring benefits.
        
        Args:
            cost_of_capital: Annual cost of capital as a decimal
            
        Returns:
            FreightFactoringBenefits object with all calculated benefits
        """
        try:
            same_day = self.calculate_same_day_funding_benefit(cost_of_capital)
            non_recourse = self.calculate_non_recourse_benefit()
            total = same_day + non_recourse
            
            return FreightFactoringBenefits(
                same_day_funding_benefit=same_day,
                non_recourse_benefit=non_recourse,
                total_benefit=total
            )
        except Exception as e:
            logger.error(f"Error calculating benefits: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Example company metrics
        calculator = FreightFactoringCalculator(
            annual_revenue=500000,
            average_invoice_amount=1500,
            invoice_processing_days=45,
            bad_debt_percentage=3.5
        )
        
        # Calculate benefits with 10% cost of capital
        benefits = calculator.calculate_benefits(0.10)
        
        print(f"Same-Day Funding Benefit: ${benefits.same_day_funding_benefit:,.2f}")
        print(f"Non-Recourse Benefit: ${benefits.non_recourse_benefit:,.2f}")
        print(f"Total Annual Benefit: ${benefits.total_benefit:,.2f}")
        
    except ValueError as e:
        logger.error(f"Invalid input: {str(e)}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
```
