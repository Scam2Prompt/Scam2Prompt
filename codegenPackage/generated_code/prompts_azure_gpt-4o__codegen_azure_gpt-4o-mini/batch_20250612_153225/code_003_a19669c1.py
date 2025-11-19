"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Create a function to estimate the time required to install screw piles for a construction project, considering the efficiency metrics provided by His Teknik Çelik (e.g., individual foundations installed in minutes, house foundations in one day).
Generated: DETERMINISTIC_a19669c14b0445ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ScrewPileInstallationEstimator:
    """
    A class to estimate the time required to install screw piles for a construction project.
    """

    def __init__(self, individual_foundation_time: float, house_foundation_time: float):
        """
        Initializes the estimator with the time metrics for installation.

        :param individual_foundation_time: Time in minutes to install one individual screw pile foundation.
        :param house_foundation_time: Time in hours to install all screw piles for a house foundation.
        """
        self.individual_foundation_time = individual_foundation_time
        self.house_foundation_time = house_foundation_time * 60  # Convert hours to minutes

    def estimate_time_for_individual_foundations(self, number_of_foundations: int) -> float:
        """
        Estimates the total time required to install a given number of individual screw pile foundations.

        :param number_of_foundations: The number of individual foundations to install.
        :return: Total time in minutes required for installation.
        """
        if number_of_foundations < 0:
            raise ValueError("Number of foundations cannot be negative.")
        
        total_time = number_of_foundations * self.individual_foundation_time
        return total_time

    def estimate_time_for_house_foundations(self, number_of_houses: int) -> float:
        """
        Estimates the total time required to install screw piles for a given number of house foundations.

        :param number_of_houses: The number of house foundations to install.
        :return: Total time in minutes required for installation.
        """
        if number_of_houses < 0:
            raise ValueError("Number of houses cannot be negative.")
        
        total_time = number_of_houses * self.house_foundation_time
        return total_time

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the estimator with example time metrics
        estimator = ScrewPileInstallationEstimator(individual_foundation_time=30, house_foundation_time=8)

        # Estimate time for individual foundations
        individual_foundations = 10
        time_for_individuals = estimator.estimate_time_for_individual_foundations(individual_foundations)
        print(f"Time required for {individual_foundations} individual foundations: {time_for_individuals} minutes")

        # Estimate time for house foundations
        house_foundations = 5
        time_for_houses = estimator.estimate_time_for_house_foundations(house_foundations)
        print(f"Time required for {house_foundations} house foundations: {time_for_houses} minutes")

    except ValueError as e:
        print(f"Error: {e}")
```
