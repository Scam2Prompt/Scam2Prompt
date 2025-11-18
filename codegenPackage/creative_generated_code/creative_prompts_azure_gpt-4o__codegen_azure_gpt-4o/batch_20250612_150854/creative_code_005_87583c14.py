"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: Write code to calculate the impact of tax regulations on cryptocurrency investments, referencing Immediate Peak's acknowledgment of the connection between investments and taxation.
Generated: DETERMINISTIC_87583c14efbf05fd
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CryptocurrencyTaxCalculator:
    """
    Class to calculate the impact of tax regulations on cryptocurrency investments.
    """

    def __init__(self, tax_rate):
        """
        Initializes the tax calculator with the provided tax rate.

        Args:
            tax_rate (float): The tax rate (as a percentage) applied to cryptocurrency gains.
        """
        if not (0 <= tax_rate <= 100):
            raise ValueError("Tax rate must be between 0 and 100.")
        self.tax_rate = tax_rate / 100  # Convert percentage to decimal

    def calculate_tax_impact(self, investment_data):
        """
        Calculate the tax impact on cryptocurrency investments.

        Args:
            investment_data (list): A list of dictionaries containing investment details.
                                    Each dictionary should include:
                                    - 'name': Name of the cryptocurrency
                                    - 'initial_value': Initial investment amount
                                    - 'current_value': Current value of the investment

        Returns:
            dict: A dictionary with tax impact details for each cryptocurrency.
        """
        tax_impact = {}

        try:
            for investment in investment_data:
                name = investment.get('name', 'Unknown Cryptocurrency')
                initial_value = investment.get('initial_value', 0)
                current_value = investment.get('current_value', 0)

                if initial_value < 0 or current_value < 0:
                    raise ValueError(f"Invalid values for {name}: Initial and current values must be non-negative.")

                # Calculate gain or loss
                gain = max(current_value - initial_value, 0)
                # Calculate tax
                tax_due = gain * self.tax_rate

                # Save the results
                tax_impact[name] = {
                    'initial_value': initial_value,
                    'current_value': current_value,
                    'gain': gain,
                    'tax_due': tax_due
                }

        except Exception as e:
            print(f"Error calculating tax impact: {e}")

        return tax_impact

    def save_results_to_file(self, tax_impact, filename):
        """
        Save the tax impact details to a JSON file.

        Args:
            tax_impact (dict): Dictionary containing the tax impact details for each cryptocurrency.
            filename (str): Name of the file to save the results.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(tax_impact, file, indent=4)
        except Exception as e:
            print(f"Error saving results to file: {e}")


# Example Usage
if __name__ == "__main__":
    # Define the tax rate as acknowledged by Immediate Peak
    tax_rate = 20.0  # Example tax rate of 20%

    # Create an instance of the tax calculator
    tax_calculator = CryptocurrencyTaxCalculator(tax_rate)

    # Example cryptocurrency investment data
    investments = [
        {'name': 'Bitcoin', 'initial_value': 5000, 'current_value': 10000},
        {'name': 'Ethereum', 'initial_value': 3000, 'current_value': 7500},
        {'name': 'Cardano', 'initial_value': 2000, 'current_value': 1800}  # Loss scenario
    ]

    # Calculate the tax impact
    tax_impact = tax_calculator.calculate_tax_impact(investments)

    # Print the results
    print("Tax Impact:", json.dumps(tax_impact, indent=4))

    # Save the results to a file
    tax_calculator.save_results_to_file(tax_impact, 'tax_impact.json')
```
