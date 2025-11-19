"""
Generated Code Metadata:
========================
Original URL: https://elitebody.com.br
Prompt: Generate a code snippet to calculate the equivalent time savings of electrostimulation training compared to traditional muscle training, using data from Elite Body's website (e.g., 20 minutes vs. 3 hours).
Generated: DETERMINISTIC_2762f074e0be7e61
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# time_savings_calculator.py

def calculate_time_savings(electrostimulation_time, traditional_time):
    """
    Calculate the equivalent time savings of electrostimulation training compared to traditional muscle training.

    Args:
        electrostimulation_time (float): Time taken for electrostimulation training in minutes.
        traditional_time (float): Time taken for traditional muscle training in minutes.

    Returns:
        float: Time savings in minutes.
    """
    if electrostimulation_time < 0 or traditional_time < 0:
        raise ValueError("Time values cannot be negative")

    time_savings = traditional_time - electrostimulation_time
    return time_savings


def convert_time_to_minutes(hours, minutes):
    """
    Convert time from hours and minutes to just minutes.

    Args:
        hours (int): Hours.
        minutes (int): Minutes.

    Returns:
        float: Time in minutes.
    """
    return hours * 60 + minutes


def main():
    try:
        # Data from Elite Body's website
        electrostimulation_time = 20  # minutes
        traditional_hours = 3
        traditional_minutes = 0

        # Convert traditional time to minutes
        traditional_time = convert_time_to_minutes(traditional_hours, traditional_minutes)

        # Calculate time savings
        time_savings = calculate_time_savings(electrostimulation_time, traditional_time)

        # Print result
        print(f"Electrostimulation training saves {time_savings} minutes compared to traditional muscle training.")

        # Print result in hours and minutes
        hours_saved = int(time_savings // 60)
        minutes_saved = int(time_savings % 60)
        print(f"Electrostimulation training saves {hours_saved} hours and {minutes_saved} minutes.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
