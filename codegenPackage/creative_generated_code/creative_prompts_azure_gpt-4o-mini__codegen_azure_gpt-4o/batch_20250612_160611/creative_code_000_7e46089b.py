"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Generate a 16-week training plan for a half marathon, incorporating long runs, interval runs, and strength training as detailed on Boost Running.
Generated: DETERMINISTIC_7e46089b665f8894
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_half_marathon_training_plan():
    """
    Generate a 16-week half marathon training plan including long runs, interval runs, 
    and strength training. The plan is structured based on general training principles.
    """
    try:
        # Define the weekly training plan structure
        training_plan = []
        for week in range(1, 17):
            weekly_schedule = {
                "Week": week,
                "Schedule": {
                    "Monday": "Rest or light cross-training",
                    "Tuesday": "Interval run (e.g., 4x800m at race pace with 2-min recovery)",
                    "Wednesday": "Strength training (bodyweight exercises or weightlifting)",
                    "Thursday": "Steady medium-distance run (e.g., 5-7 miles at moderate effort)",
                    "Friday": "Rest or light cross-training",
                    "Saturday": "Long run (build up from 6-12 miles gradually, peak at 10-12 miles)",
                    "Sunday": "Recovery run or easy jog (e.g., 3-5 miles)"
                }
            }

            # Add progressive long runs for each week
            long_run_distances = {
                1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 10, 7: 11, 8: 12,
                9: 10, 10: 11, 11: 12, 12: 12, 13: 10, 14: 10, 15: 8, 16: "Race week - Half Marathon"
            }
            weekly_schedule["Schedule"]["Saturday"] = f"Long run ({long_run_distances[week]} miles)"

            # For race week, adjust the schedule to taper down mileage
            if week == 16:
                weekly_schedule["Schedule"] = {
                    "Monday": "Rest or light cross-training",
                    "Tuesday": "Easy jog (2-3 miles)",
                    "Wednesday": "Rest or light jogging",
                    "Thursday": "Easy jog (2-3 miles)",
                    "Friday": "Rest",
                    "Saturday": "Rest",
                    "Sunday": "Race Day - Half Marathon (13.1 miles)"
                }

            training_plan.append(weekly_schedule)

        # Return the training plan as JSON for easy readability
        return json.dumps(training_plan, indent=4)

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the training plan: {e}"


# Generate and print the 16-week half marathon training plan
if __name__ == "__main__":
    plan = generate_half_marathon_training_plan()
    print(plan)
```
