"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Write a Python script to simulate an asset finance calculator that includes seasonal payment options for industries like construction, manufacturing, or agriculture, as described on Rhino Asset Finance's website.
Generated: DETERMINISTIC_d2a333da6d8acce8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, Dict, List, Tuple

class Season(Enum):
    """Enum representing different seasons for seasonal payments."""
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"

class AssetType(Enum):
    """Enum representing different types of assets."""
    CONSTRUCTION = "Construction Equipment"
    MANUFACTURING = "Manufacturing Machinery"
    AGRICULTURE = "Agricultural Equipment"

class PaymentFrequency(Enum):
    """Enum representing payment frequencies."""
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEASONAL = "Seasonal"

class AssetFinanceCalculator:
    """
    A calculator for asset financing with seasonal payment options.
    
    Attributes:
        asset_type (AssetType): Type of asset being financed
        asset_value (float): Total value of the asset
        deposit (float): Initial deposit amount
        term_years (int): Loan term in years
        interest_rate (float): Annual interest rate (as decimal)
        payment_frequency (PaymentFrequency): Frequency of payments
        seasonal_payment_season (Optional[Season]): Season for seasonal payments
    """
    
    def __init__(
        self,
        asset_type: AssetType,
        asset_value: float,
        deposit: float,
        term_years: int,
        interest_rate: float,
        payment_frequency: PaymentFrequency,
        seasonal_payment_season: Optional[Season] = None
    ):
        """Initialize the calculator with financing parameters."""
        self.asset_type = asset_type
        self.asset_value = asset_value
        self.deposit = deposit
        self.term_years = term_years
        self.interest_rate = interest_rate
        self.payment_frequency = payment_frequency
        self.seasonal_payment_season = seasonal_payment_season
        
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if self.asset_value <= 0:
            raise ValueError("Asset value must be positive")
        if self.deposit < 0:
            raise ValueError("Deposit cannot be negative")
        if self.deposit >= self.asset_value:
            raise ValueError("Deposit must be less than asset value")
        if self.term_years <= 0:
            raise ValueError("Term must be positive")
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if self.payment_frequency == PaymentFrequency.SEASONAL and not self.seasonal_payment_season:
            raise ValueError("Seasonal payment season must be specified for seasonal payments")
    
    def calculate_loan_amount(self) -> float:
        """Calculate the loan amount after deposit."""
        return self.asset_value - self.deposit
    
    def calculate_total_payments(self) -> float:
        """Calculate total payments over the loan term."""
        loan_amount = self.calculate_loan_amount()
        total_interest = loan_amount * self.interest_rate * self.term_years
        return loan_amount + total_interest
    
    def calculate_payment_schedule(self) -> List[Dict[str, str]]:
        """
        Calculate the payment schedule based on payment frequency.
        
        Returns:
            List of dictionaries containing payment date and amount
        """
        loan_amount = self.calculate_loan_amount()
        total_payments = self.calculate_total_payments()
        
        if self.payment_frequency == PaymentFrequency.MONTHLY:
            return self._calculate_monthly_payments(loan_amount, total_payments)
        elif self.payment_frequency == PaymentFrequency.QUARTERLY:
            return self._calculate_quarterly_payments(loan_amount, total_payments)
        elif self.payment_frequency == PaymentFrequency.SEASONAL:
            return self._calculate_seasonal_payments(loan_amount, total_payments)
        else:
            raise ValueError("Invalid payment frequency")
    
    def _calculate_monthly_payments(self, loan_amount: float, total_payments: float) -> List[Dict[str, str]]:
        """Calculate monthly payment schedule."""
        num_payments = self.term_years * 12
        payment_amount = total_payments / num_payments
        schedule = []
        
        today = datetime.date.today()
        for i in range(1, num_payments + 1):
            payment_date = today + datetime.timedelta(days=30 * i)
            schedule.append({
                "date": payment_date.strftime("%Y-%m-%d"),
                "amount": f"£{payment_amount:.2f}"
            })
        
        return schedule
    
    def _calculate_quarterly_payments(self, loan_amount: float, total_payments: float) -> List[Dict[str, str]]:
        """Calculate quarterly payment schedule."""
        num_payments = self.term_years * 4
        payment_amount = total_payments / num_payments
        schedule = []
        
        today = datetime.date.today()
        for i in range(1, num_payments + 1):
            payment_date = today + datetime.timedelta(days=90 * i)
            schedule.append({
                "date": payment_date.strftime("%Y-%m-%d"),
                "amount": f"£{payment_amount:.2f}"
            })
        
        return schedule
    
    def _calculate_seasonal_payments(self, loan_amount: float, total_payments: float) -> List[Dict[str, str]]:
        """Calculate seasonal payment schedule."""
        num_payments = self.term_years * 4
        payment_amount = total_payments / num_payments
        schedule = []
        
        today = datetime.date.today()
        current_year = today.year
        
        # Determine starting season based on current month
        current_month = today.month
        if current_month < 3:
            current_season = Season.WINTER
        elif current_month < 6:
            current_season = Season.SPRING
        elif current_month < 9:
            current_season = Season.SUMMER
        else:
            current_season = Season.AUTUMN
        
        # Find the first payment season
        seasons = list(Season)
        start_idx = seasons.index(self.seasonal_payment_season)
        current_idx = seasons.index(current_season)
        
        # Calculate first payment date
        if start_idx == current_idx:
            # Payment is this season
            first_payment_date = self._get_season_start_date(current_year, current_season)
        else:
            # Payment is next occurrence of the season
            if start_idx > current_idx:
                first_payment_date = self._get_season_start_date(current_year, self.seasonal_payment_season)
            else:
                first_payment_date = self._get_season_start_date(current_year + 1, self.seasonal_payment_season)
        
        # Generate schedule
        for i in range(num_payments):
            payment_year = first_payment_date.year + (i // 4)
            season_idx = (start_idx + i) % 4
            season = seasons[season_idx]
            
            payment_date = self._get_season_start_date(payment_year, season)
            schedule.append({
                "date": payment_date.strftime("%Y-%m-%d"),
                "amount": f"£{payment_amount:.2f}"
            })
        
        return schedule
    
    def _get_season_start_date(self, year: int, season: Season) -> datetime.date:
        """Get the approximate start date for a season in a given year."""
        if season == Season.SPRING:
            return datetime.date(year, 3, 1)
        elif season == Season.SUMMER:
            return datetime.date(year, 6, 1)
        elif season == Season.AUTUMN:
            return datetime.date(year, 9, 1)
        else:  # WINTER
            return datetime.date(year, 12, 1)
    
    def generate_summary(self) -> Dict[str, str]:
        """Generate a summary of the financing terms."""
        return {
            "Asset Type": self.asset_type.value,
            "Asset Value": f"£{self.asset_value:,.2f}",
            "Deposit": f"£{self.deposit:,.2f}",
            "Loan Amount": f"£{self.calculate_loan_amount():,.2f}",
            "Term": f"{self.term_years} years",
            "Interest Rate": f"{self.interest_rate * 100:.2f}%",
            "Payment Frequency": self.payment_frequency.value,
            "Seasonal Payment Season": self.seasonal_payment_season.value if self.seasonal_payment_season else "N/A",
            "Total Payments": f"£{self.calculate_total_payments():,.2f}"
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a calculator for agricultural equipment with seasonal payments in summer
        calculator = AssetFinanceCalculator(
            asset_type=AssetType.AGRICULTURE,
            asset_value=50000,
            deposit=10000,
            term_years=5,
            interest_rate=0.05,
            payment_frequency=PaymentFrequency.SEASONAL,
            seasonal_p
