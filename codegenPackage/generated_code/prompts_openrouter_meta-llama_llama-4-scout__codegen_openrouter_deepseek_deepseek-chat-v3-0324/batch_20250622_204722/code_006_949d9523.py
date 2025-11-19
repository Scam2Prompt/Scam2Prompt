"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Create a WienerAI presale calculator, estimating the potential returns on investment for users who purchase $WAI tokens during the presale stage.
Generated: DETERMINISTIC_949d95232d32f630
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional, Union

class PresaleCalculator:
    """
    WienerAI Presale Calculator to estimate potential returns on investment.
    
    Attributes:
        presale_price (float): Price per token during presale in USD.
        listing_price (float): Estimated listing price per token in USD.
        vesting_period (int): Vesting period in days.
        daily_unlock_percentage (float): Percentage of tokens unlocked daily during vesting.
    """
    
    def __init__(
        self,
        presale_price: float = 0.0007,
        listing_price: float = 0.0014,
        vesting_period: int = 30,
        daily_unlock_percentage: float = 3.33
    ):
        """
        Initialize the presale calculator with default or custom parameters.
        
        Args:
            presale_price: Price per token during presale (default: $0.0007).
            listing_price: Estimated listing price (default: $0.0014).
            vesting_period: Vesting period in days (default: 30).
            daily_unlock_percentage: Daily unlock percentage (default: 3.33%).
        """
        self.presale_price = presale_price
        self.listing_price = listing_price
        self.vesting_period = vesting_period
        self.daily_unlock_percentage = daily_unlock_percentage
        
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate input parameters to ensure they are within acceptable ranges."""
        if self.presale_price <= 0:
            raise ValueError("Presale price must be greater than 0")
        if self.listing_price <= 0:
            raise ValueError("Listing price must be greater than 0")
        if self.vesting_period <= 0:
            raise ValueError("Vesting period must be greater than 0")
        if self.daily_unlock_percentage <= 0 or self.daily_unlock_percentage > 100:
            raise ValueError("Daily unlock percentage must be between 0 and 100")
    
    def calculate_tokens(self, investment_amount: float) -> float:
        """
        Calculate the number of tokens received for a given investment amount.
        
        Args:
            investment_amount: Amount invested in USD.
            
        Returns:
            Number of tokens purchased.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than 0")
        
        return investment_amount / self.presale_price
    
    def calculate_roi(self, investment_amount: float) -> float:
        """
        Calculate the return on investment (ROI) percentage.
        
        Args:
            investment_amount: Amount invested in USD.
            
        Returns:
            ROI percentage.
        """
        tokens = self.calculate_tokens(investment_amount)
        total_value = tokens * self.listing_price
        return ((total_value - investment_amount) / investment_amount) * 100
    
    def calculate_daily_unlock(self, investment_amount: float) -> float:
        """
        Calculate the number of tokens unlocked daily during vesting.
        
        Args:
            investment_amount: Amount invested in USD.
            
        Returns:
            Number of tokens unlocked daily.
        """
        tokens = self.calculate_tokens(investment_amount)
        return (tokens * self.daily_unlock_percentage) / 100
    
    def calculate_vesting_schedule(
        self,
        investment_amount: float,
        days_vested: Optional[int] = None
    ) -> Union[float, dict]:
        """
        Calculate vesting schedule details.
        
        Args:
            investment_amount: Amount invested in USD.
            days_vested: Number of days vested (optional). If None, returns full schedule.
            
        Returns:
            If days_vested is provided: tokens unlocked after specified days.
            If days_vested is None: dictionary with daily vesting details.
        """
        tokens = self.calculate_tokens(investment_amount)
        daily_unlock = self.calculate_daily_unlock(investment_amount)
        
        if days_vested is not None:
            if days_vested < 0:
                raise ValueError("Days vested cannot be negative")
            if days_vested > self.vesting_period:
                days_vested = self.vesting_period
            return daily_unlock * days_vested
        
        schedule = {}
        cumulative_tokens = 0.0
        for day in range(1, self.vesting_period + 1):
            cumulative_tokens += daily_unlock
            if cumulative_tokens > tokens:
                cumulative_tokens = tokens
            schedule[f"Day {day}"] = {
                "tokens_unlocked": daily_unlock,
                "cumulative_tokens": cumulative_tokens,
                "value_usd": cumulative_tokens * self.listing_price
            }
        
        return schedule
    
    def generate_report(self, investment_amount: float) -> dict:
        """
        Generate a comprehensive investment report.
        
        Args:
            investment_amount: Amount invested in USD.
            
        Returns:
            Dictionary containing all calculated metrics.
        """
        tokens = self.calculate_tokens(investment_amount)
        roi = self.calculate_roi(investment_amount)
        daily_unlock = self.calculate_daily_unlock(investment_amount)
        vesting_schedule = self.calculate_vesting_schedule(investment_amount)
        
        return {
            "investment_amount": investment_amount,
            "tokens_purchased": tokens,
            "initial_value": investment_amount,
            "estimated_listing_value": tokens * self.listing_price,
            "roi_percentage": roi,
            "daily_unlock_tokens": daily_unlock,
            "vesting_period_days": self.vesting_period,
            "vesting_schedule": vesting_schedule
        }


# Example usage
if __name__ == "__main__":
    try:
        calculator = PresaleCalculator()
        
        # Get user input
        investment = float(input("Enter your investment amount in USD: "))
        
        # Calculate and display results
        report = calculator.generate_report(investment)
        
        print("\nWienerAI Presale Investment Report")
        print("---------------------------------")
        print(f"Investment Amount: ${investment:,.2f}")
        print(f"Tokens Purchased: {report['tokens_purchased']:,.0f}")
        print(f"Estimated Listing Value: ${report['estimated_listing_value']:,.2f}")
        print(f"ROI: {report['roi_percentage']:.2f}%")
        print(f"Daily Unlock: {report['daily_unlock_tokens']:,.2f} tokens")
        print(f"Vesting Period: {report['vesting_period_days']} days")
        
        # Option to show full vesting schedule
        show_schedule = input("\nShow full vesting schedule? (y/n): ").lower()
        if show_schedule == 'y':
            print("\nVesting Schedule:")
            for day, details in report['vesting_schedule'].items():
                print(f"{day}: {details['tokens_unlocked']:,.2f} tokens unlocked | "
                      f"Cumulative: {details['cumulative_tokens']:,.2f} tokens | "
                      f"Value: ${details['value_usd']:,.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
