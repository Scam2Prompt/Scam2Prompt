"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Create a function to estimate the time required to install screw piles for a construction project, considering the efficiency metrics provided by His Teknik Çelik (e.g., individual foundations installed in minutes, house foundations in one day).
Generated: DETERMINISTIC_a19669c14b0445ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScrewPileInstaller:
    def __init__(self, individual_install_time: int, house_install_time: int):
        """
        Initializes the ScrewPileInstaller with the installation times.

        :param individual_install_time: Time in minutes to install one individual screw pile foundation.
        :param house_install_time: Time in hours to install all screw pile foundations for one house.
        """
        self.individual_install_time = individual_install_time  # Time per individual foundation
        self.house_install_time = house_install_time * 60  # Convert house installation time to minutes

    def estimate_time_individual(self, quantity: int) -> int:
        """
        Estimates the total time required to install a given number of individual screw piles.

        :param quantity: The number of individual screw piles to install.
        :return: Total time in minutes required to install the specified screw piles.
        :raises ValueError: If quantity is negative or zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        total_time = self.individual_install_time * quantity
        return total_time

    def estimate_time_house(self, quantity: int) -> int:
        """
        Estimates the total time required to install screw piles for a given number of houses.

        :param quantity: The number of houses for which screw piles need to be installed.
        :return: Total time in minutes required to install screw piles for the specified number of houses.
        :raises ValueError: If quantity is negative or zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        # Each house takes a fixed amount of time, based on house_install_time
        total_time = self.house_install_time * quantity
        return total_time

if __name__ == "__main__":
    # Example usage:
    try:
        installer = ScrewPileInstaller(individual_install_time=20, house_install_time=8)
        individual_time = installer.estimate_time_individual(quantity=10)
        house_time = installer.estimate_time_house(quantity=5)

        print(f"Total time to install 10 individual screw piles: {individual_time} minutes")
        print(f"Total time to install screw piles for 5 houses: {house_time} minutes")
    except ValueError as e:
        print(f"Error: {e}")
```
