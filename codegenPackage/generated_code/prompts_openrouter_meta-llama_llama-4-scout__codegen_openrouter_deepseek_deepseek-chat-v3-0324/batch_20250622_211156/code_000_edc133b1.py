"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: "Write a Python script to calculate asset finance payments for a construction company purchasing a new crane, considering seasonal payment options."
Generated: DETERMINISTIC_edc133b121983a8f
Batch ID: 20250622_211156
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
from typing import Optional, Tuple, Dict

class AssetFinanceCalculator:
    """
    A class to calculate asset finance payments for a construction company purchasing a new crane.
    Supports seasonal payment options based on construction seasons.
    """

    def __init__(self, asset_cost: float, annual_interest_rate: float, loan_term_years: int):
        """
        Initialize the calculator with loan parameters.

        Args:
            asset_cost: Total cost of the crane (positive float)
            annual_interest_rate: Annual interest rate as decimal (e.g., 0.05 for 5%)
            loan_term_years: Duration of the loan in years (positive integer)
        """
        if asset_cost <= 0:
            raise ValueError("Asset cost must be positive")
        if annual_interest_rate <= 0:
            raise ValueError("Interest rate must be positive")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be positive")

        self.asset_cost = asset_cost
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_months = loan_term_years * 12
        self.monthly_interest_rate = annual_interest_rate / 12

    def calculate_monthly_payment(self) -> float:
        """
        Calculate fixed monthly payment using standard loan formula.

        Returns:
            Monthly payment amount
        """
        if self.monthly_interest_rate == 0:
            return self.asset_cost / self.loan_term_months

        discount_factor = ((1 + self.monthly_interest_rate) ** self.loan_term_months - 1) / \
                         (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.loan_term_months)
        return self.asset_cost / discount_factor

    def calculate_seasonal_payments(self, peak_season_months: Tuple[int, ...] = (4, 5, 6, 7, 8, 9),
                                   peak_season_multiplier: float = 1.5) -> Dict[str, float]:
        """
        Calculate seasonal payments with higher payments during peak construction months.

        Args:
            peak_season_months: Tuple of month numbers (1-12) considered peak season
            peak_season_multiplier: Multiplier applied to payments during peak season

        Returns:
            Dictionary with 'monthly_payment' (base amount) and 'peak_season_payment' (higher amount)
        """
        if not all(1 <= month <= 12 for month in peak_season_months):
            raise ValueError("Month numbers must be between 1 and 12")
        if peak_season_multiplier <= 0:
            raise ValueError("Peak season multiplier must be positive")

        base_payment = self.calculate_monthly_payment()
        total_peak_months = len(peak_season_months)
        total_off_months = self.loan_term_months - total_peak_months

        # Solve for adjusted payments that satisfy total loan amount
        if total_peak_months == 0:
            return {'monthly_payment': base_payment, 'peak_season_payment': base_payment}

        adjusted_base = self.asset_cost / (
            total_off_months + total_peak_months * peak_season_multiplier
        )
        peak_payment = adjusted_base * peak_season_multiplier

        return {
            'monthly_payment': adjusted_base,
            'peak_season_payment': peak_payment,
            'peak_season_months': peak_season_months
        }

    def generate_payment_schedule(self, start_date: Optional[datetime] = None,
                                 seasonal: bool = False,
                                 peak_season_months: Tuple[int, ...] = (4, 5, 6, 7, 8, 9),
                                 peak_season_multiplier: float = 1.5) -> list:
        """
        Generate a payment schedule with dates and amounts.

        Args:
            start_date: First payment date (defaults to current date)
            seasonal: Whether to use seasonal payment plan
            peak_season_months: Months with higher payments
            peak_season_multiplier: Multiplier for peak season payments

        Returns:
            List of dictionaries with payment details
        """
        if start_date is None:
            start_date = datetime.now()

        schedule = []
        if seasonal:
            payments = self.calculate_seasonal_payments(peak_season_months, peak_season_multiplier)
            base_payment = payments['monthly_payment']
            peak_payment = payments['peak_season_payment']
        else:
            base_payment = self.calculate_monthly_payment()
            peak_payment = base_payment

        current_date = start_date
        for month in range(1, self.loan_term_months + 1):
            is_peak = current_date.month in peak_season_months if seasonal else False
            amount = peak_payment if is_peak else base_payment

            schedule.append({
                'payment_number': month,
                'date': current_date.strftime('%Y-%m-%d'),
                'amount': round(amount, 2),
                'is_peak_season': is_peak
            })

            # Move to next month (handles year transitions)
            next_month = current_date.month % 12 + 1
            next_year = current_date.year + (1 if next_month == 1 else 0)
            current_date = current_date.replace(year=next_year, month=next_month)

        return schedule


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator for a $500,000 crane at 5% interest over 5 years
        calculator = AssetFinanceCalculator(
            asset_cost=500000,
            annual_interest_rate=0.05,
            loan_term_years=5
        )

        # Calculate standard monthly payment
        monthly_payment = calculator.calculate_monthly_payment()
        print(f"Standard monthly payment: ${monthly_payment:,.2f}")

        # Calculate seasonal payment options
        seasonal_payments = calculator.calculate_seasonal_payments()
        print("\nSeasonal payment plan:")
        print(f"Off-season monthly payment: ${seasonal_payments['monthly_payment']:,.2f}")
        print(f"Peak-season monthly payment: ${seasonal_payments['peak_season_payment']:,.2f}")

        # Generate full payment schedule
        print("\nPayment schedule (first 12 months):")
        schedule = calculator.generate_payment_schedule(seasonal=True)
        for payment in schedule[:12]:
            peak_flag = " (PEAK)" if payment['is_peak_season'] else ""
            print(f"{payment['payment_number']}: {payment['date']} - ${payment['amount']:,.2f}{peak_flag}")

    except ValueError as e:
        print(f"Error: {e}")
```
