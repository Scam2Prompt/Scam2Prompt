"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Develop a 100-mile running training plan with a gradual mileage increase, peak weeks reaching 70-100 miles, and a sample weekly schedule, and provide advice on building endurance and mental tenacity.
Generated: DETERMINISTIC_30fa839a6c1b8660
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import math

def generate_training_plan(total_weeks=16, peak_mileage=100):
    """
    Generate a 100-mile running training plan with gradual mileage increase.
    
    Args:
        total_weeks (int): Total number of weeks in the training plan.
        peak_mileage (int): Peak weekly mileage during the training plan.
    
    Returns:
        dict: A dictionary containing weekly mileage and sample schedules.
    """
    try:
        # Validate inputs
        if total_weeks <= 0 or peak_mileage <= 0:
            raise ValueError("Total weeks and peak mileage must be positive integers.")
        
        # Initialize training plan
        training_plan = {}
        base_mileage = 20  # Starting mileage for the first week
        mileage_increment = (peak_mileage - base_mileage) / (total_weeks - 4)  # Gradual increase
        
        for week in range(1, total_weeks + 1):
            if week <= 2:
                # Build-up phase: Start with base mileage
                weekly_mileage = base_mileage
            elif week <= total_weeks - 4:
                # Gradual increase phase
                weekly_mileage = base_mileage + math.ceil(mileage_increment * (week - 2))
            else:
                # Peak and taper phase
                taper_weeks = total_weeks - week + 1
                weekly_mileage = peak_mileage - (taper_weeks * 10)  # Reduce mileage during taper
            
            # Generate a sample weekly schedule
            schedule = {
                "Monday": f"Easy run - {math.ceil(weekly_mileage * 0.1)} miles",
                "Tuesday": f"Speed workout - {math.ceil(weekly_mileage * 0.15)} miles",
                "Wednesday": f"Recovery run - {math.ceil(weekly_mileage * 0.1)} miles",
                "Thursday": f"Tempo run - {math.ceil(weekly_mileage * 0.2)} miles",
                "Friday": "Rest day",
                "Saturday": f"Long run - {math.ceil(weekly_mileage * 0.35)} miles",
                "Sunday": f"Recovery run - {math.ceil(weekly_mileage * 0.1)} miles",
            }
            
            # Add to training plan
            training_plan[f"Week {week}"] = {
                "Weekly Mileage": weekly_mileage,
                "Schedule": schedule
            }
        
        return training_plan
    
    except Exception as e:
        # Handle errors gracefully
        print(f"Error generating training plan: {e}")
        return None


def display_training_plan(training_plan):
    """
    Display the training plan in a readable format.
    
    Args:
        training_plan (dict): The training plan dictionary.
    """
    try:
        if not training_plan:
            raise ValueError("Training plan is empty or invalid.")
        
        for week, details in training_plan.items():
            print(f"{week}:")
            print(f"  Weekly Mileage: {details['Weekly Mileage']} miles")
            print("  Schedule:")
            for day, activity in details['Schedule'].items():
                print(f"    {day}: {activity}")
            print()
    
    except Exception as e:
        print(f"Error displaying training plan: {e}")


def endurance_and_mental_tenacity_tips():
    """
    Provide advice on building endurance and mental tenacity.
    
    Returns:
        list: A list of tips for endurance and mental strength.
    """
    return [
        "Gradually increase mileage to avoid injury and build a strong base.",
        "Incorporate cross-training activities like cycling or swimming to improve overall fitness.",
        "Focus on proper nutrition and hydration to fuel your runs and aid recovery.",
        "Practice mindfulness and visualization techniques to stay mentally strong during long runs.",
        "Break long runs into smaller segments mentally to make them feel more manageable.",
        "Train with a group or partner to stay motivated and accountable.",
        "Listen to your body and rest when needed to prevent burnout."
    ]


# Main execution
if __name__ == "__main__":
    # Generate a 16-week training plan with a peak mileage of 100 miles
    training_plan = generate_training_plan(total_weeks=16, peak_mileage=100)
    
    # Display the training plan
    if training_plan:
        display_training_plan(training_plan)
    
    # Provide tips for endurance and mental tenacity
    print("Tips for Building Endurance and Mental Tenacity:")
    for tip in endurance_and_mental_tenacity_tips():
        print(f"- {tip}")
```
