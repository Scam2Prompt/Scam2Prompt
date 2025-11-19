"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: Provide an example of a case study where ultrasonic cleaning significantly reduced downtime and costs for a manufacturing company.
Generated: DETERMINISTIC_a5003f9bb4927a90
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for manufacturing parts.
    """

    def __init__(self, cleaning_time: float, cost_per_clean: float):
        """
        Initializes the UltrasonicCleaner with cleaning time and cost per cleaning.

        :param cleaning_time: Time taken to clean a part (in minutes)
        :param cost_per_clean: Cost incurred for each cleaning operation
        """
        self.cleaning_time = cleaning_time
        self.cost_per_clean = cost_per_clean

    def clean_parts(self, number_of_parts: int) -> float:
        """
        Cleans the specified number of parts and returns the total cost.

        :param number_of_parts: Number of parts to be cleaned
        :return: Total cost of cleaning
        """
        if number_of_parts <= 0:
            raise ValueError("Number of parts must be greater than zero.")
        
        total_cost = number_of_parts * self.cost_per_clean
        return total_cost

    def calculate_downtime_reduction(self, old_cleaning_time: float, number_of_parts: int) -> float:
        """
        Calculates the reduction in downtime due to ultrasonic cleaning.

        :param old_cleaning_time: Previous cleaning time per part (in minutes)
        :param number_of_parts: Number of parts to be cleaned
        :return: Reduction in downtime (in minutes)
        """
        if old_cleaning_time <= 0:
            raise ValueError("Old cleaning time must be greater than zero.")
        
        old_total_time = old_cleaning_time * number_of_parts
        new_total_time = self.cleaning_time * number_of_parts
        downtime_reduction = old_total_time - new_total_time
        
        return downtime_reduction


def main():
    """
    Main function to demonstrate the ultrasonic cleaning case study.
    """
    try:
        # Initialize the ultrasonic cleaner with cleaning time and cost
        ultrasonic_cleaner = UltrasonicCleaner(cleaning_time=10, cost_per_clean=5)

        # Define the number of parts to be cleaned
        number_of_parts = 100

        # Calculate the total cleaning cost
        total_cost = ultrasonic_cleaner.clean_parts(number_of_parts)
        print(f"Total cleaning cost for {number_of_parts} parts: ${total_cost:.2f}")

        # Calculate the downtime reduction
        old_cleaning_time = 30  # Old cleaning time per part in minutes
        downtime_reduction = ultrasonic_cleaner.calculate_downtime_reduction(old_cleaning_time, number_of_parts)
        print(f"Downtime reduction for cleaning {number_of_parts} parts: {downtime_reduction:.2f} minutes")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
