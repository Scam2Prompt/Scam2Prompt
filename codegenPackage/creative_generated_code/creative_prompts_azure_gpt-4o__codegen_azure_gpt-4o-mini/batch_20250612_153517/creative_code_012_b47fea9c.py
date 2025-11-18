"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a function to calculate the passive income earned from staking $TGC tokens over time, factoring in APY and staking duration.
Generated: DETERMINISTIC_b47fea9c175f759f
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate passive income earned from staking TGC tokens.
    """

    def __init__(self, principal: float, annual_percentage_yield: float, duration_years: float):
        """
        Initializes the StakingCalculator with principal, APY, and duration.

        :param principal: The initial amount of TGC tokens staked.
        :param annual_percentage_yield: The annual percentage yield as a decimal (e.g., 0.05 for 5%).
        :param duration_years: The duration for which the tokens are staked, in years.
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if not (0 <= annual_percentage_yield <= 1):
            raise ValueError("Annual percentage yield must be between 0 and 1.")
        if duration_years < 0:
            raise ValueError("Duration cannot be negative.")

        self.principal = principal
        self.annual_percentage_yield = annual_percentage_yield
        self.duration_years = duration_years

    def calculate_passive_income(self) -> float:
        """
        Calculates the passive income earned from staking TGC tokens.

        :return: The passive income earned after the specified duration.
        """
        # Compound interest formula: A = P * (1 + r/n)^(nt)
        # Here, we assume n (number of times interest is compounded per year) is 1 for simplicity.
        # Thus, A = P * (1 + r)^t
        total_amount = self.principal * (1 + self.annual_percentage_yield) ** self.duration_years
        passive_income = total_amount - self.principal
        
        return passive_income

# Example usage
if __name__ == "__main__":
    try:
        # Define the parameters for staking
        principal_amount = 1000  # Amount in TGC tokens
        apy = 0.05               # 5% annual percentage yield
        duration = 3             # Staking duration in years

        # Create an instance of StakingCalculator
        staking_calculator = StakingCalculator(principal_amount, apy, duration)

        # Calculate and print the passive income
        income = staking_calculator.calculate_passive_income()
        print(f"Passive income earned from staking: ${income:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
