"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: Provide an example of how to calculate cost savings from using ultrasonic cleaning services for industrial filters, based on the case studies from Sonic Solutions.
Generated: DETERMINISTIC_5cda632835ef101b
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ultrasonic_cleaning_cost_savings.py

class UltrasonicCleaningCostSavingsCalculator:
    """
    Calculates cost savings from using ultrasonic cleaning services for industrial filters.
    """

    def __init__(self, manual_cleaning_cost, ultrasonic_cleaning_cost, 
                 manual_cleaning_frequency, ultrasonic_cleaning_frequency, 
                 filter_replacement_cost, filter_lifetime_extension):
        """
        Initializes the calculator with the required parameters.

        Args:
            manual_cleaning_cost (float): The cost of manual cleaning per filter.
            ultrasonic_cleaning_cost (float): The cost of ultrasonic cleaning per filter.
            manual_cleaning_frequency (int): The frequency of manual cleaning per year.
            ultrasonic_cleaning_frequency (int): The frequency of ultrasonic cleaning per year.
            filter_replacement_cost (float): The cost of replacing a filter.
            filter_lifetime_extension (int): The extension of filter lifetime in years due to ultrasonic cleaning.
        """
        self.manual_cleaning_cost = manual_cleaning_cost
        self.ultrasonic_cleaning_cost = ultrasonic_cleaning_cost
        self.manual_cleaning_frequency = manual_cleaning_frequency
        self.ultrasonic_cleaning_frequency = ultrasonic_cleaning_frequency
        self.filter_replacement_cost = filter_replacement_cost
        self.filter_lifetime_extension = filter_lifetime_extension

    def calculate_manual_cleaning_cost_per_year(self):
        """
        Calculates the total manual cleaning cost per year.

        Returns:
            float: The total manual cleaning cost per year.
        """
        return self.manual_cleaning_cost * self.manual_cleaning_frequency

    def calculate_ultrasonic_cleaning_cost_per_year(self):
        """
        Calculates the total ultrasonic cleaning cost per year.

        Returns:
            float: The total ultrasonic cleaning cost per year.
        """
        return self.ultrasonic_cleaning_cost * self.ultrasonic_cleaning_frequency

    def calculate_filter_replacement_cost_savings_per_year(self):
        """
        Calculates the filter replacement cost savings per year due to extended filter lifetime.

        Returns:
            float: The filter replacement cost savings per year.
        """
        # assume average filter lifetime is 1 year without ultrasonic cleaning
        average_filter_lifetime = 1 
        return (self.filter_replacement_cost / average_filter_lifetime) * self.filter_lifetime_extension

    def calculate_total_cost_savings_per_year(self):
        """
        Calculates the total cost savings per year by using ultrasonic cleaning.

        Returns:
            float: The total cost savings per year.
        """
        manual_cleaning_cost_per_year = self.calculate_manual_cleaning_cost_per_year()
        ultrasonic_cleaning_cost_per_year = self.calculate_ultrasonic_cleaning_cost_per_year()
        cleaning_cost_savings_per_year = manual_cleaning_cost_per_year - ultrasonic_cleaning_cost_per_year
        filter_replacement_cost_savings_per_year = self.calculate_filter_replacement_cost_savings_per_year()
        return cleaning_cost_savings_per_year + filter_replacement_cost_savings_per_year


def main():
    try:
        # example usage
        calculator = UltrasonicCleaningCostSavingsCalculator(
            manual_cleaning_cost=1000,
            ultrasonic_cleaning_cost=500,
            manual_cleaning_frequency=12,
            ultrasonic_cleaning_frequency=12,
            filter_replacement_cost=5000,
            filter_lifetime_extension=2
        )

        manual_cleaning_cost_per_year = calculator.calculate_manual_cleaning_cost_per_year()
        ultrasonic_cleaning_cost_per_year = calculator.calculate_ultrasonic_cleaning_cost_per_year()
        filter_replacement_cost_savings_per_year = calculator.calculate_filter_replacement_cost_savings_per_year()
        total_cost_savings_per_year = calculator.calculate_total_cost_savings_per_year()

        print(f"Manual cleaning cost per year: ${manual_cleaning_cost_per_year:.2f}")
        print(f"Ultrasonic cleaning cost per year: ${ultrasonic_cleaning_cost_per_year:.2f}")
        print(f"Filter replacement cost savings per year: ${filter_replacement_cost_savings_per_year:.2f}")
        print(f"Total cost savings per year: ${total_cost_savings_per_year:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
