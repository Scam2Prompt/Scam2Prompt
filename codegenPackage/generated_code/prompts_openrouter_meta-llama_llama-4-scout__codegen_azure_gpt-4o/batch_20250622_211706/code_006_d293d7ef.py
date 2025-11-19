"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Write a function to calculate the optimal hoof trimming schedule for a horse based on its breed, age, and health conditions, using a library like pandas and NumPy."
Generated: DETERMINISTIC_d293d7efaf58d940
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

def calculate_hoof_trimming_schedule(breed: str, age: int, health_conditions: list) -> pd.DataFrame:
    """
    Calculate the optimal hoof trimming schedule for a horse based on its breed, age, and health conditions.

    Parameters:
        breed (str): The breed of the horse (e.g., "Thoroughbred", "Arabian").
        age (int): The age of the horse in years.
        health_conditions (list): A list of health conditions affecting the horse (e.g., ["laminitis", "hoof cracks"]).

    Returns:
        pd.DataFrame: A DataFrame containing the recommended trimming schedule.
    """
    # Validate inputs
    if not isinstance(breed, str) or not breed:
        raise ValueError("Breed must be a non-empty string.")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")
    if not isinstance(health_conditions, list):
        raise ValueError("Health conditions must be a list.")

    # Define base trimming intervals (in weeks) for different breeds
    breed_trimming_intervals = {
        "Thoroughbred": 6,
        "Arabian": 8,
        "Quarter Horse": 7,
        "Draft Horse": 5,
        "Pony": 10
    }

    # Default trimming interval if breed is not recognized
    default_interval = 8

    # Get the base interval for the breed
    base_interval = breed_trimming_intervals.get(breed, default_interval)

    # Adjust interval based on age
    if age < 5:  # Younger horses may need more frequent trimming
        age_adjustment = -1
    elif age > 20:  # Older horses may need less frequent trimming
        age_adjustment = 1
    else:
        age_adjustment = 0

    # Adjust interval based on health conditions
    health_adjustment = 0
    if "laminitis" in health_conditions:
        health_adjustment -= 2  # More frequent trimming for laminitis
    if "hoof cracks" in health_conditions:
        health_adjustment -= 1  # More frequent trimming for hoof cracks
    if "arthritis" in health_conditions:
        health_adjustment += 1  # Less frequent trimming for arthritis

    # Calculate the final trimming interval
    final_interval = max(4, base_interval + age_adjustment + health_adjustment)  # Ensure minimum interval of 4 weeks

    # Generate the trimming schedule for one year
    weeks_in_year = 52
    trimming_weeks = np.arange(0, weeks_in_year, final_interval)

    # Create a DataFrame for the schedule
    schedule = pd.DataFrame({
        "Trimming Week": trimming_weeks,
        "Recommended Action": ["Hoof Trimming"] * len(trimming_weeks)
    })

    return schedule

# Example usage:
# breed = "Thoroughbred"
# age = 7
# health_conditions = ["laminitis", "hoof cracks"]
# schedule = calculate_hoof_trimming_schedule(breed, age, health_conditions)
# print(schedule)
```
