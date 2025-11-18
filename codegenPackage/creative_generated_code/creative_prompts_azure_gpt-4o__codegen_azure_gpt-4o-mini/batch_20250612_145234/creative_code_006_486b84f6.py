"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Write code to calculate the total BTC earnings for a user over a year if they purchase the best package (Tier4) on Coinmining. Include considerations for affiliate bonuses.
Generated: DETERMINISTIC_486b84f62d9c11f8
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoinMiningCalculator:
    def __init__(self, initial_investment, daily_earning_rate, affiliate_bonus_rate, days=365):
        """
        Initialize the CoinMiningCalculator with investment details.
        
        :param initial_investment: The amount of BTC invested in Tier 4.
        :param daily_earning_rate: Daily earning rate as a percentage (e.g., 0.01 for 1%).
        :param affiliate_bonus_rate: Affiliate bonus rate as a percentage (e.g., 0.05 for 5%).
        :param days: Total number of days for the calculation (default is 365 for a year).
        """
        self.initial_investment = initial_investment
        self.daily_earning_rate = daily_earning_rate
        self.affiliate_bonus_rate = affiliate_bonus_rate
        self.days = days

    def calculate_total_earnings(self):
        """
        Calculate the total earnings from the investment over the specified period.
        
        :return: Total BTC earnings including affiliate bonuses.
        """
        try:
            # Calculate total earnings without affiliate bonuses
            total_earnings = self.initial_investment * (1 + self.daily_earning_rate) ** self.days
            
            # Calculate affiliate bonuses (assuming bonuses are earned on total earnings)
            affiliate_earnings = total_earnings * self.affiliate_bonus_rate
            
            # Combine earnings and affiliate bonuses
            total_with_affiliates = total_earnings + affiliate_earnings
            
            return total_with_affiliates
            
        except (TypeError, ValueError) as e:
            raise ValueError("Invalid input values. Ensure all inputs are numerical and positive.") from e

    def display_results(self):
        """
        Display the total earnings in a formatted manner.
        """
        try:
            total_earnings = self.calculate_total_earnings()
            print(f"Total BTC earnings after {self.days} days with Tier 4 package: {total_earnings:.8f} BTC")
        except ValueError as e:
            print(f"Error calculating earnings: {e}")

# Example usage
if __name__ == "__main__":
    # Constants for Tier 4 package
    INITIAL_INVESTMENT = 1.0  # BTC
    DAILY_EARNING_RATE = 0.01  # 1% daily earnings
    AFFILIATE_BONUS_RATE = 0.05  # 5% affiliate bonus

    # Create a calculator instance
    calculator = CoinMiningCalculator(INITIAL_INVESTMENT, DAILY_EARNING_RATE, AFFILIATE_BONUS_RATE)

    # Display the results
    calculator.display_results()
```
