"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Write Python code to generate a personalized 10-mile running plan, incorporating easy runs, long runs, hill repeats, and strides, as outlined on Boost Running.
Generated: DETERMINISTIC_98182d7e442cd4da
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_running_plan(name, days_per_week):
    """
    Generate a personalized 10-mile running plan.
    
    Parameters:
        name (str): The name of the runner.
        days_per_week (int): Number of days per week the runner plans to run (3 to 7).
    
    Returns:
        dict: A personalized running plan for the week.
    """
    if days_per_week < 3 or days_per_week > 7:
        raise ValueError("days_per_week must be between 3 and 7.")

    # Define the types of runs
    run_types = [
        {"type": "Easy Run", "description": "Run at a conversational pace.", "distance": random.uniform(1, 3)},
        {"type": "Long Run", "description": "Run at an easy pace, but for a longer distance.", "distance": random.uniform(3, 5)},
        {"type": "Hill Repeats", "description": "Short bursts uphill with recovery periods.", "distance": random.uniform(1, 2)},
        {"type": "Strides", "description": "Short accelerations with easy recovery.", "distance": random.uniform(0.5, 1)}
    ]

    # Generate the weekly running plan
    plan = {}
    total_miles = 0
    for day in range(1, days_per_week + 1):
        run = random.choice(run_types)
        total_miles += run["distance"]
        plan[f"Day {day}"] = {
            "run_type": run["type"],
            "description": run["description"],
            "distance_miles": round(run["distance"], 2)
        }

    # Ensure the weekly total mileage is close to 10 miles
    while total_miles < 9.5 or total_miles > 10.5:
        total_miles = 0
        for day in range(1, days_per_week + 1):
            run = random.choice(run_types)
            total_miles += run["distance"]
            plan[f"Day {day}"] = {
                "run_type": run["type"],
                "description": run["description"],
                "distance_miles": round(run["distance"], 2)
            }

    # Format the final plan with runner's name
    return {
        "runner_name": name,
        "weekly_total_miles": round(total_miles, 2),
        "running_plan": plan
    }

# Example usage
if __name__ == "__main__":
    try:
        runner_name = input("Enter your name: ")
        days_per_week = int(input("Enter the number of days you plan to run each week (3-7): "))
        running_plan = generate_running_plan(runner_name, days_per_week)
        print(f"\nPersonalized Running Plan for {running_plan['runner_name']}:\n")
        for day, details in running_plan["running_plan"].items():
            print(f"{day}:")
            print(f"  Run Type: {details['run_type']}")
            print(f"  Description: {details['description']}")
            print(f"  Distance: {details['distance_miles']} miles")
        print(f"\nWeekly Total Mileage: {running_plan['weekly_total_miles']} miles")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
