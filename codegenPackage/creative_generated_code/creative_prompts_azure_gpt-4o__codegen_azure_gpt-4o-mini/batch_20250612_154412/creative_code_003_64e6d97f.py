"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Generate Python code to calculate APY (Annual Percentage Yield) for a DeFi platform, as described in the "디파이 수익률, APY만 보면 안 되는 이유!" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_64e6d97f8e612c49
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class APYCalculator:
    """
    A class to calculate the Annual Percentage Yield (APY) for a DeFi platform.
    The APY is calculated based on the interest earned over a specific period, 
    taking into account compounding frequency.
    """
    
    def __init__(self, principal: float, rate: float, periods_per_year: int):
        """
        Initializes the APYCalculator with the principal amount, interest rate, 
        and number of compounding periods per year.

        :param principal: The initial amount of money (float)
        :param rate: The annual interest rate as a decimal (float)
        :param periods_per_year: The number of times that interest is compounded per year (int)
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if periods_per_year <= 0:
            raise ValueError("Periods per year must be a positive integer.")

        self.principal = principal
        self.rate = rate
        self.periods_per_year = periods_per_year

    def calculate_apy(self) -> float:
        """
        Calculates the Annual Percentage Yield (APY).

        :return: The calculated APY as a decimal (float)
        """
        # Formula for APY: APY = (1 + (r/n))^n - 1
        try:
            apy = (1 + (self.rate / self.periods_per_year)) ** self.periods_per_year - 1
            return apy
        except Exception as e:
            raise RuntimeError(f"An error occurred during APY calculation: {str(e)}")

    def apy_to_percentage(self) -> float:
        """
        Converts the APY to a percentage format.

        :return: The APY in percentage format (float)
        """
        return self.calculate_apy() * 100

def main():
    """
    The main function to execute the APY calculation.
    """
    try:
        # Example usage
        principal_amount = 1000.0  # Principal amount in currency units
        annual_rate = 0.05          # Annual interest rate (5%)
        compounding_periods = 12     # Compounded monthly

        apy_calculator = APYCalculator(principal_amount, annual_rate, compounding_periods)

        # Calculate APY and convert to percentage
        apy = apy_calculator.calculate_apy()
        apy_percentage = apy_calculator.apy_to_percentage()

        print(f"APY: {apy:.4f} (as decimal), {apy_percentage:.2f}% (percentage)")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")

if __name__ == "__main__":
    main()
```
