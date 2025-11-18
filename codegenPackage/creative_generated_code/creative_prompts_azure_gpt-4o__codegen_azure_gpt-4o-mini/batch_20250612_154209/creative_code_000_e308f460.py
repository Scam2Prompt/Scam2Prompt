"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-globale-maprimerenov.aides-gouv-fr.info
Prompt: Write Python code to calculate eligibility for Ma Prime Renov' subsidies based on income, property type, and energy savings criteria as described in the BAR-TH-164 program.
Generated: DETERMINISTIC_e308f460d3b24839
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaPrimeRenovEligibility:
    """
    A class to check eligibility for Ma Prime Renov' subsidies based on income,
    property type, and energy savings criteria as specified in the BAR-TH-164 program.
    """

    def __init__(self, income, property_type, energy_savings):
        """
        Initializes the eligibility checker with income, property type, and energy savings.

        :param income: Annual household income in euros.
        :param property_type: Type of property (e.g., 'primary', 'secondary').
        :param energy_savings: Estimated energy savings from renovations in kilowatt-hours (kWh).
        """
        self.income = income
        self.property_type = property_type.lower()
        self.energy_savings = energy_savings

    def check_eligibility(self):
        """
        Checks eligibility for the Ma Prime Renov' subsidy based on provided criteria.

        :return: A tuple containing a boolean indicating eligibility and a message.
        """
        try:
            # Define income thresholds for eligibility
            income_thresholds = {
                'primary': 30000,
                'secondary': 40000
            }

            # Check property type and corresponding income criteria
            if self.property_type not in income_thresholds:
                raise ValueError(f"Invalid property type: {self.property_type}. Must be 'primary' or 'secondary'.")

            threshold = income_thresholds[self.property_type]

            # Check if income is below the threshold and energy savings criteria is met
            if self.income <= threshold and self.energy_savings >= 3000:
                return True, "Eligible for Ma Prime Renov' subsidies."
            else:
                return False, "Not eligible for Ma Prime Renov' subsidies: " \
                              "Income exceeds limit or energy savings criteria not met."

        except ValueError as ve:
            return False, str(ve)
        except Exception as e:
            return False, f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Example data (you can modify these values to test different scenarios)
    annual_income = 28000  # Annual household income in euros
    property_type = 'primary'  # Type of property
    energy_savings = 3500  # Energy savings in kWh

    eligibility_checker = MaPrimeRenovEligibility(annual_income, property_type, energy_savings)
    eligible, message = eligibility_checker.check_eligibility()
    
    print(f"Eligibility: {eligible}, Message: {message}")
```
