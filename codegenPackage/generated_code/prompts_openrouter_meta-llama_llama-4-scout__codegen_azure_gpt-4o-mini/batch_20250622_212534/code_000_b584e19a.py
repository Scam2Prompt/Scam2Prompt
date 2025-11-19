"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Write a Python script to calculate the cost savings of using ultrasonic cleaning services for industrial parts cleaning, considering factors like part longevity and reduced downtime."
Generated: DETERMINISTIC_b584e19a33fdd24e
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UltrasonicCleaningCostSavingsCalculator:
    """
    A class to calculate the cost savings of using ultrasonic cleaning services
    for industrial parts cleaning.
    """

    def __init__(self, part_cost, cleaning_frequency, downtime_cost, part_longevity_increase):
        """
        Initializes the calculator with the necessary parameters.

        :param part_cost: Cost of a single part
        :param cleaning_frequency: Frequency of cleaning (times per year)
        :param downtime_cost: Cost incurred due to downtime (per hour)
        :param part_longevity_increase: Increase in part longevity (in hours)
        """
        self.part_cost = part_cost
        self.cleaning_frequency = cleaning_frequency
        self.downtime_cost = downtime_cost
        self.part_longevity_increase = part_longevity_increase

    def calculate_savings(self):
        """
        Calculates the total cost savings from using ultrasonic cleaning services.

        :return: Total cost savings
        """
        try:
            # Calculate the cost of replacing parts without ultrasonic cleaning
            replacement_cost = self.part_cost * self.cleaning_frequency
            
            # Calculate the cost savings from increased part longevity
            longevity_savings = (self.part_longevity_increase * self.downtime_cost) * self.cleaning_frequency
            
            # Total savings is the difference between replacement cost and longevity savings
            total_savings = longevity_savings - replacement_cost
            
            logging.info(f"Replacement Cost: ${replacement_cost:.2f}")
            logging.info(f"Longevity Savings: ${longevity_savings:.2f}")
            logging.info(f"Total Savings: ${total_savings:.2f}")

            return total_savings

        except Exception as e:
            logging.error("An error occurred while calculating savings: %s", e)
            return None

def main():
    """
    Main function to execute the cost savings calculation.
    """
    # Example parameters
    part_cost = 100.0  # Cost of a single part
    cleaning_frequency = 12  # Clean once a month
    downtime_cost = 50.0  # Cost incurred due to downtime per hour
    part_longevity_increase = 10  # Increase in part longevity in hours

    # Create an instance of the calculator
    calculator = UltrasonicCleaningCostSavingsCalculator(part_cost, cleaning_frequency, downtime_cost, part_longevity_increase)

    # Calculate and print the savings
    savings = calculator.calculate_savings()
    if savings is not None:
        print(f"Total Cost Savings from Ultrasonic Cleaning: ${savings:.2f}")

if __name__ == "__main__":
    main()
```
