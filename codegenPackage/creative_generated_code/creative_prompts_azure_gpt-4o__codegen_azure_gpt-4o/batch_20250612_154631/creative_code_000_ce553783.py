"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write Python code to simulate a water filtration process using UF (Ultra-Filtration) technology, referencing Econopure's UF system features like automatic cleaning and high efficiency.
Generated: DETERMINISTIC_ce553783a42ee320
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class UltraFiltrationSystem:
    """
    Simulates a water filtration process using Ultra-Filtration (UF) technology.
    Features:
    - Automatic cleaning mechanism.
    - High filtration efficiency.
    """

    def __init__(self, filtration_capacity_liters_per_hour: int, cleaning_interval_minutes: int):
        """
        Initializes the UF system.

        :param filtration_capacity_liters_per_hour: Capacity of filtration in liters per hour.
        :param cleaning_interval_minutes: Time interval for automatic cleaning in minutes.
        """
        self.filtration_capacity = filtration_capacity_liters_per_hour
        self.cleaning_interval = cleaning_interval_minutes
        self.filtered_water = 0  # Total volume of filtered water (in liters)
        self.last_cleaned = time.time()  # Tracks the last cleaning time

    def filter_water(self, liters: int) -> int:
        """
        Simulates filtering water through the UF system.

        :param liters: Amount of water to filter (in liters).
        :return: Amount of filtered water (in liters).
        """
        if liters <= 0:
            raise ValueError("The amount of water to filter must be greater than zero.")

        # Simulate filtration efficiency (99% filtration rate)
        filtered = int(liters * 0.99)
        self.filtered_water += filtered
        print(f"{filtered} liters of water filtered successfully.")
        self._check_cleaning()
        return filtered

    def _check_cleaning(self):
        """
        Checks if the system needs cleaning based on the cleaning interval.
        """
        current_time = time.time()
        time_since_last_cleaning = (current_time - self.last_cleaned) / 60  # Convert seconds to minutes

        if time_since_last_cleaning >= self.cleaning_interval:
            self._automatic_cleaning()

    def _automatic_cleaning(self):
        """
        Simulates the automatic cleaning process of the UF system.
        """
        print("Initiating automatic cleaning process...")
        time.sleep(2)  # Simulate cleaning duration
        self.last_cleaned = time.time()  # Reset cleaning time
        print("Cleaning completed successfully.")

    def status_report(self):
        """
        Provides a status report of the UF system.

        :return: A dictionary containing system status.
        """
        current_time = time.time()
        time_since_last_cleaned = (current_time - self.last_cleaned) / 60  # Convert seconds to minutes

        status = {
            "Filtration Capacity (liters/hour)": self.filtration_capacity,
            "Total Filtered Water (liters)": self.filtered_water,
            "Time Since Last Cleaning (minutes)": round(time_since_last_cleaned, 2),
            "Next Cleaning In (minutes)": max(0, round(self.cleaning_interval - time_since_last_cleaned, 2)),
        }

        return status


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the UF system with 1000 liters/hour capacity and cleaning every 5 minutes
        uf_system = UltraFiltrationSystem(filtration_capacity_liters_per_hour=1000, cleaning_interval_minutes=5)

        # Simulate the filtration process for 500 liters of water
        uf_system.filter_water(500)

        # Print a status report
        status = uf_system.status_report()
        print("Status Report:", status)

        # Simulate filtering more water after some time
        time.sleep(300)  # Wait for 5 minutes to trigger cleaning
        uf_system.filter_water(1000)

        # Print another status report
        status = uf_system.status_report()
        print("Status Report:", status)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
