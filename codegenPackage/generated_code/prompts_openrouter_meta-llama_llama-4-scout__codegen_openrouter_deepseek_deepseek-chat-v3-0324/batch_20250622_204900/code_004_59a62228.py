"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Develop a tool to convert credit card payments into manageable EMIs, considering interest rates and payment tenure.
Generated: DETERMINISTIC_59a6222802eb5a41
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import List, Dict, Union

class EMICalculator:
    """
    A class to convert credit card payments into EMIs (Equated Monthly Installments)
    considering interest rates and payment tenure.
    """

    def __init__(self, principal: float, annual_interest_rate: float, tenure_months: int):
        """
        Initialize the EMICalculator with principal amount, annual interest rate, and tenure.

        Args:
            principal (float): The principal amount (total payment to be converted to EMI)
            annual_interest_rate (float): Annual interest rate (in percentage)
            tenure_months (int): Tenure in months for EMI repayment
        """
        if principal <= 0:
            raise ValueError("Principal amount must be positive")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if tenure_months <= 0:
            raise ValueError("Tenure must be at least 1 month")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.tenure_months = tenure_months
        self.monthly_interest_rate = (annual_interest_rate / 100) / 12

    def calculate_emi(self) -> float:
        """
        Calculate the fixed monthly EMI payment.

        Returns:
            float: The EMI amount
        """
        if self.monthly_interest_rate == 0:
            return self.principal / self.tenure_months

        emi = (self.principal * self.monthly_interest_rate * 
               math.pow(1 + self.monthly_interest_rate, self.tenure_months)) / (
               math.pow(1 + self.monthly_interest_rate, self.tenure_months) - 1)
        return round(emi, 2)

    def generate_repayment_schedule(self, start_date: Union[str, datetime] = None) -> List[Dict]:
        """
        Generate a detailed repayment schedule showing principal and interest components for each EMI.

        Args:
            start_date (Union[str, datetime], optional): Start date for EMI payments. 
                If None, uses current date. If string, format should be YYYY-MM-DD.

        Returns:
            List[Dict]: List of dictionaries containing payment details for each month
        """
        emi = self.calculate_emi()
        remaining_principal = self.principal
        repayment_schedule = []

        # Parse start date
        if start_date is None:
            current_date = datetime.now()
        elif isinstance(start_date, str):
            current_date = datetime.strptime(start_date, "%Y-%m-%d")
        else:
            current_date = start_date

        for month in range(1, self.tenure_months + 1):
            interest_component = round(remaining_principal * self.monthly_interest_rate, 2)
            principal_component = round(emi - interest_component, 2)
            
            # Adjust for last month to account for rounding differences
            if month == self.tenure_months:
                principal_component = round(remaining_principal, 2)
                emi = round(principal_component + interest_component, 2)

            remaining_principal -= principal_component
            remaining_principal = round(max(remaining_principal, 0), 2)

            payment_date = current_date + timedelta(days=30*month)
            
            repayment_schedule.append({
                'month': month,
                'date': payment_date.strftime("%Y-%m-%d"),
                'emi': emi,
                'principal': principal_component,
                'interest': interest_component,
                'remaining_principal': remaining_principal
            })

        return repayment_schedule

    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest payable over the entire tenure.

        Returns:
            float: Total interest amount
        """
        emi = self.calculate_emi()
        total_payment = emi * self.tenure_months
        return round(total_payment - self.principal, 2)


def convert_to_emi(principal: float, annual_interest_rate: float, tenure_months: int) -> Dict:
    """
    Convenience function to convert a credit card payment to EMI and return summary.

    Args:
        principal (float): The principal amount
        annual_interest_rate (float): Annual interest rate (in percentage)
        tenure_months (int): Tenure in months

    Returns:
        Dict: Dictionary containing EMI summary
    """
    try:
        calculator = EMICalculator(principal, annual_interest_rate, tenure_months)
        emi = calculator.calculate_emi()
        total_interest = calculator.calculate_total_interest()
        total_payment = emi * tenure_months

        return {
            'principal': principal,
            'annual_interest_rate': annual_interest_rate,
            'tenure_months': tenure_months,
            'monthly_emi': emi,
            'total_interest': total_interest,
            'total_payment': round(total_payment, 2),
            'repayment_schedule': calculator.generate_repayment_schedule()
        }
    except ValueError as e:
        return {'error': str(e)}


# Example usage
if __name__ == "__main__":
    # Example: Convert $1000 payment to 12 month EMI at 12% annual interest
    emi_details = convert_to_emi(1000, 12, 12)
    
    if 'error' not in emi_details:
        print("EMI Summary:")
        print(f"Principal: ${emi_details['principal']}")
        print(f"Annual Interest Rate: {emi_details['annual_interest_rate']}%")
        print(f"Tenure: {emi_details['tenure_months']} months")
        print(f"Monthly EMI: ${emi_details['monthly_emi']}")
        print(f"Total Interest: ${emi_details['total_interest']}")
        print(f"Total Payment: ${emi_details['total_payment']}")
        
        print("\nRepayment Schedule (first 3 months):")
        for payment in emi_details['repayment_schedule'][:3]:
            print(f"Month {payment['month']} ({payment['date']}): "
                  f"EMI: ${payment['emi']} (Principal: ${payment['principal']}, "
                  f"Interest: ${payment['interest']}), Remaining: ${payment['remaining_principal']}")
    else:
        print(f"Error: {emi_details['error']}")
```
