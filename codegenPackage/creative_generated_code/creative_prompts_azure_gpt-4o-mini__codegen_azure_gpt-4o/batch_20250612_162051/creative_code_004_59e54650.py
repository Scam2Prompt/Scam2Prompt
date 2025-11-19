"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Create a function that calculates the efficiency of a frozen potato processing plant, considering the use of cooling and shock freezing machines.
Generated: DETERMINISTIC_59e54650e1b705e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# frozen_potato_efficiency.py

def calculate_efficiency(total_potatoes, cooling_capacity, freezing_capacity, cooling_time, freezing_time):
    """
    Calculate the efficiency of a frozen potato processing plant.

    Parameters:
    total_potatoes (int): Total number of potatoes to be processed.
    cooling_capacity (int): Maximum potatoes the cooling machine can process per unit time.
    freezing_capacity (int): Maximum potatoes the freezing machine can process per unit time.
    cooling_time (float): Time taken (in hours) to cool one batch of potatoes.
    freezing_time (float): Time taken (in hours) to freeze one batch of potatoes.

    Returns:
    float: Efficiency of the plant as a percentage.
    """

    try:
        # Validate inputs
        if total_potatoes <= 0 or cooling_capacity <= 0 or freezing_capacity <= 0 or cooling_time <= 0 or freezing_time <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate total processing time for cooling and freezing
        cooling_batches = total_potatoes / cooling_capacity
        freezing_batches = total_potatoes / freezing_capacity

        total_cooling_time = cooling_batches * cooling_time
        total_freezing_time = freezing_batches * freezing_time

        # Total time required to process all potatoes
        total_processing_time = total_cooling_time + total_freezing_time

        # Maximum theoretical time if both machines run at full capacity simultaneously
        max_capacity_time = max(total_cooling_time, total_freezing_time)

        # Efficiency calculation as a percentage
        efficiency = (max_capacity_time / total_processing_time) * 100

        return round(efficiency, 2)

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Test function with sample data
    total_potatoes = 1000
    cooling_capacity = 200
    freezing_capacity = 250
    cooling_time = 1.5  # hours
    freezing_time = 2.0  # hours

    efficiency = calculate_efficiency(
        total_potatoes, cooling_capacity, freezing_capacity, cooling_time, freezing_time
    )
    if efficiency is not None:
        print(f"The efficiency of the plant is {efficiency}%.")
```
