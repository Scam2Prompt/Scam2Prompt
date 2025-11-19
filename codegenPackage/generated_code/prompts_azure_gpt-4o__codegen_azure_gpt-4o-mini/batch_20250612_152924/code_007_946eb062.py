"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Develop a script to calculate the financial benefits of joining a member-owned pharmacy cooperative, including profit sharing and purchasing power, as outlined by PharmaChoice Canada.
Generated: DETERMINISTIC_946eb06208266fff
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PharmacyCooperative:
    def __init__(self, initial_investment, annual_profit_share, purchasing_power_increase):
        """
        Initialize the PharmacyCooperative with the necessary financial parameters.

        :param initial_investment: Initial investment made by the member
        :param annual_profit_share: Expected annual profit share from the cooperative
        :param purchasing_power_increase: Percentage increase in purchasing power
        """
        self.initial_investment = initial_investment
        self.annual_profit_share = annual_profit_share
        self.purchasing_power_increase = purchasing_power_increase

    def calculate_total_benefits(self, years):
        """
        Calculate the total financial benefits over a specified number of years.

        :param years: Number of years to calculate benefits for
        :return: Total financial benefits
        """
        if years < 0:
            raise ValueError("Number of years must be a non-negative integer.")
        
        total_profit_share = self.annual_profit_share * years
        total_investment_return = self.initial_investment + total_profit_share
        total_purchasing_power = self.initial_investment * (1 + self.purchasing_power_increase / 100) ** years
        
        return {
            "Total Profit Share": total_profit_share,
            "Total Investment Return": total_investment_return,
            "Total Purchasing Power": total_purchasing_power
        }

def main():
    """
    Main function to execute the financial benefit calculation.
    """
    try:
        # Example parameters for the cooperative
        initial_investment = 10000  # Initial investment in dollars
        annual_profit_share = 1500   # Expected annual profit share in dollars
        purchasing_power_increase = 5 # Expected increase in purchasing power in percentage

        # Create an instance of the PharmacyCooperative
        cooperative = PharmacyCooperative(initial_investment, annual_profit_share, purchasing_power_increase)

        # Calculate benefits over a specified number of years
        years = 5  # Example: Calculate benefits over 5 years
        benefits = cooperative.calculate_total_benefits(years)

        # Output the results
        print(json.dumps(benefits, indent=4))

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
