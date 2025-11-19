"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yifistake.finance
Prompt: Create a script that calculates the annual percentage yield (APY) for YI12 staking based on the provided data.
Generated: DETERMINISTIC_6f28d529e98384f6
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# apy_calculator.py

class APYCalculator:
    """
    A class to calculate the Annual Percentage Yield (APY) for staking.

    Attributes:
        principal (float): The initial amount of money staked.
        rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        times_compounded (int): The number of times that interest is compounded per year.
    """

    def __init__(self, principal: float, rate: float, times_compounded: int):
        """
        Initializes the APYCalculator with the principal, rate, and times_compounded.

        Args:
            principal (float): The initial amount staked.
            rate (float): The annual interest rate percentage.
            times_compounded (int): Number of times interest is compounded per year.
        
        Raises:
            ValueError: If principal, rate or times_compounded are invalid.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than 0.")
        if rate < 0:
            raise ValueError("Rate must be non-negative.")
        if times_compounded <= 0:
            raise ValueError("Times compounded must be greater than 0.")

        self.principal = principal
        self.rate = rate / 100  # Convert percentage to decimal
        self.times_compounded = times_compounded

    def calculate_apy(self) -> float:
        """
        Calculates the annual percentage yield (APY).

        Returns:
            float: The calculated APY.
        """
        # Using the formula: APY = (1 + r/n)^(nt) - 1
        apy = (1 + self.rate / self.times_compounded) ** (self.times_compounded) - 1
        return apy * 100  # Convert decimal back to percentage

def main():
    """
    Main function to execute the APY calculation based on user input.
    """
    try:
        # Example data for YI12 staking
        principal = float(input("Enter the principal amount staked: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        times_compounded = int(input("Enter the number of times interest is compounded per year: "))

        # Create an instance of APYCalculator
        apy_calculator = APYCalculator(principal, rate, times_compounded)

        # Calculate APY
        apy = apy_calculator.calculate_apy()
        print(f"The Annual Percentage Yield (APY) for your staking is: {apy:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
