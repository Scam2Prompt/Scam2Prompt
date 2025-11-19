"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Generate Python code to calculate the annual cost savings for a grocery market using the XT70 densifier, based on its foam processing capacity and waste hauling cost reduction.
Generated: DETERMINISTIC_a29234d5ff1f660f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# xt70_densifier_calculator.py

class XTDensifierCalculator:
    """
    Calculates annual cost savings for a grocery market using the XT70 densifier.
    """

    def __init__(self, foam_processing_capacity_lbs_per_hour, 
                 waste_hauling_cost_per_ton, operating_hours_per_year=2080):
        """
        Initializes the calculator.

        Args:
            foam_processing_capacity_lbs_per_hour (float): 
                The XT70 densifier's foam processing capacity in lbs/hour.
            waste_hauling_cost_per_ton (float): 
                The waste hauling cost reduction per ton.
            operating_hours_per_year (int, optional): 
                The number of hours the densifier operates per year. Defaults to 2080.
        """
        self.foam_processing_capacity_lbs_per_hour = foam_processing_capacity_lbs_per_hour
        self.waste_hauling_cost_per_ton = waste_hauling_cost_per_ton
        self.operating_hours_per_year = operating_hours_per_year

    def calculate_annual_foam_processed(self):
        """
        Calculates the annual foam processed in tons.

        Returns:
            float: The annual foam processed in tons.
        """
        # Convert lbs to tons (1 ton = 2000 lbs)
        foam_processing_capacity_tons_per_hour = self.foam_processing_capacity_lbs_per_hour / 2000
        annual_foam_processed_tons = foam_processing_capacity_tons_per_hour * self.operating_hours_per_year
        return annual_foam_processed_tons

    def calculate_annual_cost_savings(self):
        """
        Calculates the annual cost savings.

        Returns:
            float: The annual cost savings.
        """
        annual_foam_processed_tons = self.calculate_annual_foam_processed()
        annual_cost_savings = annual_foam_processed_tons * self.waste_hauling_cost_per_ton
        return annual_cost_savings


def main():
    try:
        # Example usage
        foam_processing_capacity_lbs_per_hour = 200  # lbs/hour
        waste_hauling_cost_per_ton = 50  # $/ton

        calculator = XTDensifierCalculator(foam_processing_capacity_lbs_per_hour, 
                                           waste_hauling_cost_per_ton)

        annual_cost_savings = calculator.calculate_annual_cost_savings()
        print(f"Annual cost savings: ${annual_cost_savings:,.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
