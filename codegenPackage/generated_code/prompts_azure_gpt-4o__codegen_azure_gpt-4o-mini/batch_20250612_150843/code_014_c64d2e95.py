"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-urex-gpt.com
Prompt: Develop a Python program to calculate investment risk tolerance and budget allocation for crypto trading, inspired by the risk warnings provided by the Bit GPT Urex platform.
Generated: DETERMINISTIC_c64d2e955a679fb1
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InvestmentRiskTolerance:
    """
    A class to calculate investment risk tolerance and budget allocation for crypto trading.
    """

    def __init__(self, risk_profile: str, total_investment: float):
        """
        Initializes the InvestmentRiskTolerance class.

        :param risk_profile: A string representing the risk profile ('low', 'medium', 'high').
        :param total_investment: A float representing the total amount available for investment.
        """
        self.risk_profile = risk_profile.lower()
        self.total_investment = total_investment
        self.allocation = {}

    def validate_inputs(self):
        """
        Validates the input parameters for correctness.

        :raises ValueError: If the risk profile is invalid or total investment is negative.
        """
        valid_profiles = ['low', 'medium', 'high']
        if self.risk_profile not in valid_profiles:
            raise ValueError(f"Invalid risk profile: {self.risk_profile}. Must be one of {valid_profiles}.")
        if self.total_investment < 0:
            raise ValueError("Total investment must be a non-negative value.")

    def calculate_allocation(self):
        """
        Calculates the budget allocation based on the risk profile.

        :raises ValueError: If inputs are not validated before calling this method.
        """
        self.validate_inputs()
        
        if self.risk_profile == 'low':
            self.allocation = {
                'crypto': self.total_investment * 0.2,
                'stocks': self.total_investment * 0.5,
                'bonds': self.total_investment * 0.3
            }
        elif self.risk_profile == 'medium':
            self.allocation = {
                'crypto': self.total_investment * 0.4,
                'stocks': self.total_investment * 0.4,
                'bonds': self.total_investment * 0.2
            }
        elif self.risk_profile == 'high':
            self.allocation = {
                'crypto': self.total_investment * 0.7,
                'stocks': self.total_investment * 0.2,
                'bonds': self.total_investment * 0.1
            }

    def get_allocation(self) -> dict:
        """
        Returns the calculated budget allocation.

        :return: A dictionary containing the allocation for crypto, stocks, and bonds.
        """
        return self.allocation

def main():
    """
    Main function to execute the investment risk tolerance calculation.
    """
    try:
        # Example input values
        risk_profile = input("Enter your risk profile (low, medium, high): ")
        total_investment = float(input("Enter your total investment amount: "))

        # Create an instance of InvestmentRiskTolerance
        investment = InvestmentRiskTolerance(risk_profile, total_investment)

        # Calculate allocation
        investment.calculate_allocation()

        # Output the allocation
        allocation = investment.get_allocation()
        print("Your budget allocation is as follows:")
        print(json.dumps(allocation, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
