"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Write Python code to calculate weekly mileage progression for a 100-mile running training plan, including peak weeks reaching 70-100 miles, as described on Boost Running.
Generated: DETERMINISTIC_4c147cf41878c65d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the weekly mileage progression for a 100-mile running training plan.
The plan includes peak weeks reaching 70-100 miles, with gradual mileage increases 
to avoid injury and ensure proper training adaptation.

Author: Boost Running-inspired logic
"""

def calculate_training_plan(starting_mileage: int, peak_weeks: int, total_weeks: int) -> list:
    """
    Calculate weekly mileage progression for a running training plan.
    
    Args:
        starting_mileage (int): The mileage to start the training plan.
        peak_weeks (int): The number of weeks with peak mileage (70-100 miles).
        total_weeks (int): The total duration of the training plan in weeks.
        
    Returns:
        list: A list containing weekly mileage progression.
    """
    try:
        if starting_mileage < 0 or peak_weeks <= 0 or total_weeks <= 0:
            raise ValueError("Invalid input: All values must be positive integers.")
        if starting_mileage > 100:
            raise ValueError("Starting mileage cannot exceed 100 miles.")

        weekly_mileage = []
        peak_start_week = total_weeks - peak_weeks  # Determine when peak weeks begin
        
        for week in range(1, total_weeks + 1):
            if week <= peak_start_week:
                # Gradual mileage increase before peak weeks
                mileage = starting_mileage + (week - 1) * (50 / peak_start_week)
            else:
                # Peak weeks mileage progression between 70 and 100 miles
                mileage = 70 + ((week - peak_start_week - 1) * (30 / (total_weeks - peak_start_week)))

            weekly_mileage.append(round(mileage))  # Round mileage for simplicity

        return weekly_mileage
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_training_plan(mileage_plan: list) -> None:
    """
    Display the training plan in a readable format.

    Args:
        mileage_plan (list): A list of weekly mileage progression.
    """
    if not mileage_plan:
        print("No training plan available to display.")
        return

    print("\nWeekly Mileage Progression:")
    for week, mileage in enumerate(mileage_plan, start=1):
        print(f"Week {week}: {mileage} miles")

if __name__ == "__main__":
    # User-defined parameters for the training plan
    STARTING_MILEAGE = 20  # Assumes starting mileage is 20 miles per week
    PEAK_WEEKS = 6         # Number of peak weeks
    TOTAL_WEEKS = 16       # Total duration of the training plan in weeks

    # Calculate and display the training plan
    training_plan = calculate_training_plan(STARTING_MILEAGE, PEAK_WEEKS, TOTAL_WEEKS)
    display_training_plan(training_plan)
```
