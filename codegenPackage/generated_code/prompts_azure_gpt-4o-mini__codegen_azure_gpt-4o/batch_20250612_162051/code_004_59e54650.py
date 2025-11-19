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
# frozen_potato_efficiency.py

def calculate_efficiency(total_potatoes, processed_potatoes, cooling_machine_uptime, shock_freezing_uptime):
    """
    Calculate the efficiency of a frozen potato processing plant.

    Parameters:
        total_potatoes (int): Total number of potatoes received by the plant.
        processed_potatoes (int): Number of potatoes successfully processed.
        cooling_machine_uptime (float): Uptime of the cooling machine as a percentage (0-100).
        shock_freezing_uptime (float): Uptime of the shock freezing machine as a percentage (0-100).

    Returns:
        float: Efficiency of the plant as a percentage (0-100).

    Raises:
        ValueError: If any input is invalid (e.g., negative values or percentages out of range).
    """
    # Input validation
    if total_potatoes < 0 or processed_potatoes < 0:
        raise ValueError("Total and processed potatoes must be non-negative.")
    if cooling_machine_uptime < 0 or cooling_machine_uptime > 100:
        raise ValueError("Cooling machine uptime must be between 0 and 100.")
    if shock_freezing_uptime < 0 or shock_freezing_uptime > 100:
        raise ValueError("Shock freezing uptime must be between 0 and 100.")
    if total_potatoes == 0:
        raise ValueError("Total potatoes cannot be zero.")

    # Calculate processing rate
    processing_rate = (processed_potatoes / total_potatoes) * 100

    # Calculate machine efficiency
    machine_efficiency = (cooling_machine_uptime + shock_freezing_uptime) / 2

    # Overall efficiency is the average of processing rate and machine efficiency
    overall_efficiency = (processing_rate + machine_efficiency) / 2

    return round(overall_efficiency, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        total_potatoes = 1000
        processed_potatoes = 850
        cooling_machine_uptime = 95.0
        shock_freezing_uptime = 90.0

        # Calculate and print efficiency
        efficiency = calculate_efficiency(
            total_potatoes, processed_potatoes, cooling_machine_uptime, shock_freezing_uptime
        )
        print(f"Plant Efficiency: {efficiency}%")
    except ValueError as e:
        print(f"Error: {e}")
```
