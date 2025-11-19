"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Describe the key components of a 10-mile running plan, including the types of workouts and their purposes, as explained on Boost Running.
Generated: DETERMINISTIC_a2dd5a0c0a07b067
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to describe the key components of a 10-mile running plan
# This script demonstrates the structure and purpose of each workout type in such a plan.

def describe_running_plan():
    """
    Prints the key components of a 10-mile running plan, including workout types and their purposes.
    """
    try:
        # Define the running plan components
        running_plan = {
            "Easy Runs": {
                "Purpose": "Build endurance and aerobic capacity while minimizing fatigue.",
                "Description": "Performed at a conversational pace, usually 65-75% of your maximum heart rate."
            },
            "Long Runs": {
                "Purpose": "Develop stamina and mental toughness for longer distances.",
                "Description": "Performed at an easy to moderate pace, gradually increasing mileage over time."
            },
            "Tempo Runs": {
                "Purpose": "Improve lactate threshold and running efficiency.",
                "Description": "Performed at a 'comfortably hard' pace, typically 80-90% of your maximum heart rate."
            },
            "Interval Workouts": {
                "Purpose": "Enhance speed and anaerobic capacity.",
                "Description": "Include short bursts of high-intensity running followed by recovery periods."
            },
            "Recovery Runs": {
                "Purpose": "Promote active recovery and loosen muscles after harder workouts.",
                "Description": "Performed at a very easy pace, focusing on low intensity."
            },
            "Rest Days": {
                "Purpose": "Allow the body to recover and repair, reducing the risk of injury.",
                "Description": "No running; focus on stretching, light activity, or complete rest."
            },
        }
        
        # Output the running plan components
        print("10-Mile Running Plan Components:")
        print("--------------------------------")
        
        for workout_type, details in running_plan.items():
            print(f"Workout Type: {workout_type}")
            print(f"  Purpose: {details['Purpose']}")
            print(f"  Description: {details['Description']}")
            print()
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while describing the running plan: {e}")

# Execute the function
if __name__ == "__main__":
    describe_running_plan()
```
