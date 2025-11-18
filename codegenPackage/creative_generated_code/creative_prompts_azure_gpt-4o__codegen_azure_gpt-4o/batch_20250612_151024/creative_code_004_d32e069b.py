"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Write a Python script to calculate the average recovery time for patients undergoing surgeries at Jinling Hospital, using sample data for minimally invasive procedures and complex surgeries.
Generated: DETERMINISTIC_d32e069b094bb02d
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def calculate_average_recovery_times(data):
    """
    Calculate the average recovery times for different types of surgeries.

    Args:
        data (dict): A dictionary containing surgery data of the format:
                     {
                         "minimally_invasive": [recovery_times],
                         "complex_surgeries": [recovery_times]
                     }

    Returns:
        dict: A dictionary containing the average recovery times for each surgery type.
    """
    try:
        # Validate that the data contains the required keys
        if not all(key in data for key in ["minimally_invasive", "complex_surgeries"]):
            raise ValueError("Data dictionary must contain 'minimally_invasive' and 'complex_surgeries' keys.")

        # Validate that the values are lists and are non-empty
        for key, recovery_times in data.items():
            if not isinstance(recovery_times, list):
                raise ValueError(f"The value for {key} must be a list.")
            if not recovery_times:
                raise ValueError(f"The recovery time list for {key} cannot be empty.")

        # Calculate the averages using statistics.mean
        average_recovery_times = {
            "minimally_invasive": statistics.mean(data["minimally_invasive"]),
            "complex_surgeries": statistics.mean(data["complex_surgeries"])
        }

        return average_recovery_times

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except statistics.StatisticsError as se:
        print(f"StatisticsError: {se}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Sample data for recovery times in days
    surgery_data = {
        "minimally_invasive": [3, 4, 5, 2, 3],  # Recovery times for minimally invasive procedures
        "complex_surgeries": [12, 15, 10, 14, 13]  # Recovery times for complex surgeries
    }

    # Calculate and display the average recovery times
    averages = calculate_average_recovery_times(surgery_data)
    if averages:
        print("Average Recovery Times:")
        print(f"Minimally Invasive: {averages['minimally_invasive']} days")
        print(f"Complex Surgeries: {averages['complex_surgeries']} days")
```
