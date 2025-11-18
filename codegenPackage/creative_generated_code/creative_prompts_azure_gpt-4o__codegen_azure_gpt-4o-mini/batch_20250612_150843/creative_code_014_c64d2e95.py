"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-urex-gpt.com
Prompt: Develop a Python program to calculate investment risk tolerance and budget allocation for crypto trading, inspired by the risk warnings provided by the Bit GPT Urex platform.
Generated: DETERMINISTIC_c64d2e955a679fb1
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentRiskCalculator:
    """
    A class to calculate investment risk tolerance and budget allocation for crypto trading.
    """

    def __init__(self, risk_profile, total_investment):
        """
        Initializes the InvestmentRiskCalculator with a risk profile and total investment amount.

        :param risk_profile: A string indicating the risk profile ('low', 'medium', 'high').
        :param total_investment: A float indicating the total investment amount in USD.
        """
        self.risk_profile = risk_profile.lower()
        self.total_investment = total_investment
        self.allocation = self.calculate_allocation()

    def calculate_allocation(self):
        """
        Calculates the budget allocation based on the risk profile.

        :return: A dictionary containing the allocation for different risk categories.
        """
        allocation = {}
        try:
            if self.risk_profile == 'low':
                allocation = {
                    'low_risk': self.total_investment * 0.70,
                    'medium_risk': self.total_investment * 0.20,
                    'high_risk': self.total_investment * 0.10
                }
            elif self.risk_profile == 'medium':
                allocation = {
                    'low_risk': self.total_investment * 0.50,
                    'medium_risk': self.total_investment * 0.30,
                    'high_risk': self.total_investment * 0.20
                }
            elif self.risk_profile == 'high':
                allocation = {
                    'low_risk': self.total_investment * 0.30,
                    'medium_risk': self.total_investment * 0.30,
                    'high_risk': self.total_investment * 0.40
                }
            else:
                raise ValueError("Invalid risk profile. Choose 'low', 'medium', or 'high'.")
        except Exception as e:
            print(f"Error calculating allocation: {e}")
        return allocation

    def display_allocation(self):
        """
        Displays the allocation for each risk category.
        """
        print("Investment Allocation based on Risk Profile:")
        for risk_category, amount in self.allocation.items():
            print(f"{risk_category.capitalize()}: ${amount:.2f}")

def main():
    """
    Main function to run the Investment Risk Calculator.
    """
    try:
        risk_profile = input("Enter your risk profile (low, medium, high): ")
        total_investment = float(input("Enter your total investment amount in USD: "))

        # Instantiate the InvestmentRiskCalculator
        calculator = InvestmentRiskCalculator(risk_profile, total_investment)
        
        # Display the calculated allocation
        calculator.display_allocation()
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
