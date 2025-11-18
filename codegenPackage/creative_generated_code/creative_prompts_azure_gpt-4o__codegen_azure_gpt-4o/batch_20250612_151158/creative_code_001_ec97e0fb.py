"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cronos-a7i.pages.dev
Prompt: Generate code to calculate the zkCRO exchange rate based on accrued staking yield over time, ensuring accurate conversion between zkCRO and CRO.
Generated: DETERMINISTIC_ec97e0fb72d0b0dc
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ZkCroExchangeRateCalculator:
    def __init__(self, initial_rate: float, annual_yield: float):
        """
        Initializes the exchange rate calculator.

        :param initial_rate: Initial exchange rate (zkCRO per CRO).
        :param annual_yield: Annual staking yield as a percentage (e.g., 10 for 10% annual yield).
        """
        if initial_rate <= 0 or annual_yield < 0:
            raise ValueError("Initial rate must be positive and annual yield must be non-negative.")
        self.initial_rate = initial_rate
        self.annual_yield = annual_yield

    def calculate_rate(self, start_date: datetime.date, end_date: datetime.date) -> float:
        """
        Calculates the zkCRO exchange rate based on accrued staking yield.

        :param start_date: The starting date of staking.
        :param end_date: The ending date of staking.
        :return: The calculated zkCRO exchange rate.
        """
        if end_date <= start_date:
            raise ValueError("End date must be after the start date.")

        # Calculate the number of days between the start and end dates
        days_staked = (end_date - start_date).days

        # Convert annual yield to daily yield (compounded daily)
        daily_yield = self.annual_yield / 100 / 365

        # Calculate the accrued yield using compound interest formula
        accrued_multiplier = (1 + daily_yield) ** days_staked

        # Calculate the final exchange rate
        final_rate = self.initial_rate * accrued_multiplier
        return final_rate


# Example usage
if __name__ == "__main__":
    try:
        # Define initial parameters
        initial_rate = 1.0  # 1 zkCRO = 1 CRO initially
        annual_yield = 10.0  # 10% annual staking yield
        
        # Initialize the calculator
        calculator = ZkCroExchangeRateCalculator(initial_rate, annual_yield)
        
        # Define staking period
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 12, 31)
        
        # Calculate and print the exchange rate
        final_rate = calculator.calculate_rate(start_date, end_date)
        print(f"Exchange rate (zkCRO per CRO) after staking: {final_rate:.6f}")
    except Exception as e:
        print(f"Error: {e}")
```
