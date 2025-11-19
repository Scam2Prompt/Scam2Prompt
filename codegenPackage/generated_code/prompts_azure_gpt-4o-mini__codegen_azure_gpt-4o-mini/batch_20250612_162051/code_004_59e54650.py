"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Create a function that calculates the efficiency of a frozen potato processing plant, considering the use of cooling and shock freezing machines.
Generated: DETERMINISTIC_59e54650e1b705e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FrozenPotatoProcessingPlant:
    def __init__(self, total_potatoes: int, cooling_time: float, shock_freezing_time: float):
        """
        Initializes the FrozenPotatoProcessingPlant with the given parameters.

        :param total_potatoes: Total number of potatoes to be processed.
        :param cooling_time: Time taken for cooling in hours.
        :param shock_freezing_time: Time taken for shock freezing in hours.
        """
        if total_potatoes <= 0:
            raise ValueError("Total potatoes must be a positive integer.")
        if cooling_time < 0 or shock_freezing_time < 0:
            raise ValueError("Cooling and shock freezing times must be non-negative.")

        self.total_potatoes = total_potatoes
        self.cooling_time = cooling_time
        self.shock_freezing_time = shock_freezing_time

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the frozen potato processing plant.

        Efficiency is defined as the ratio of total potatoes processed to the total time taken
        for cooling and shock freezing.

        :return: Efficiency of the processing plant (potatoes per hour).
        """
        total_time = self.cooling_time + self.shock_freezing_time
        
        if total_time == 0:
            raise ZeroDivisionError("Total time cannot be zero when calculating efficiency.")

        efficiency = self.total_potatoes / total_time
        return efficiency

# Example usage:
if __name__ == "__main__":
    try:
        plant = FrozenPotatoProcessingPlant(total_potatoes=1000, cooling_time=2.5, shock_freezing_time=1.5)
        efficiency = plant.calculate_efficiency()
        print(f"Efficiency of the processing plant: {efficiency:.2f} potatoes per hour")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
