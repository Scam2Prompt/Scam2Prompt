"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Create a detailed plan for a corporate media training program, incorporating Cara Productions' training services to improve media relations skills in Kenya.
Generated: DETERMINISTIC_98e0b5dd8e66b4b8
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Corporate Media Training Program Plan Generator

This script generates a detailed corporate media training program plan. 
It incorporates Cara Productions’ training services to improve media relations skills in Kenya.
"""

import datetime


def generate_training_plan(company_name, location, duration_weeks, target_skills, trainers):
    """
    Generates a detailed training plan for a corporate media training program.

    Args:
        company_name (str): Name of the company hosting the training.
        location (str): Location where the training will take place.
        duration_weeks (int): Number of weeks the training will run.
        target_skills (list): Skills to be targeted during the program.
        trainers (list): List of trainers from Cara Productions handling the program.

    Returns:
        dict: A structured training plan.
    """
    try:
        # Validate inputs
        if not company_name or not location or duration_weeks <= 0 or not target_skills or not trainers:
            raise ValueError("Invalid input. Ensure all fields are correctly populated.")

        # Training program details
        training_plan = {
            "Company": company_name,
            "Location": location,
            "Duration (weeks)": duration_weeks,
            "Start Date": datetime.date.today().isoformat(),
            "End Date": (datetime.date.today() + datetime.timedelta(weeks=duration_weeks)).isoformat(),
            "Target Skills": target_skills,
            "Trainers": trainers,
            "Schedule": generate_schedule(duration_weeks, target_skills),
            "Contact Info": {
                "Cara Productions": {
                    "Email": "info@caraproductions.com",
                    "Phone": "+254-700-123456"
                }
            }
        }

        return training_plan

    except Exception as e:
        print(f"Error generating training plan: {e}")
        return None


def generate_schedule(duration_weeks, target_skills):
    """
    Generates a weekly schedule for the training program.

    Args:
        duration_weeks (int): Number of weeks the training will run.
        target_skills (list): Skills to be targeted during the program.

    Returns:
        list: A weekly schedule outlining skills to be covered.
    """
    try:
        schedule = []
        skill_count = len(target_skills)
        if skill_count == 0:
            raise ValueError("No target skills provided.")

        for week in range(1, duration_weeks + 1):
            skill_index = (week - 1) % skill_count
            schedule.append({
                "Week": week,
                "Focus Skill": target_skills[skill_index],
                "Activities": [
                    "Interactive workshops",
                    "Role-playing exercises",
                    "Media interviews simulations",
                    "Feedback and assessment"
                ]
            })

        return schedule

    except Exception as e:
        print(f"Error generating schedule: {e}")
        return []


def display_training_plan(plan):
    """
    Displays the training plan in a readable format.

    Args:
        plan (dict): The training plan to display.
    """
    if not plan:
        print("No training plan to display.")
        return

    print("\nCorporate Media Training Program Plan")
    print("=" * 40)
    print(f"Company: {plan['Company']}")
    print(f"Location: {plan['Location']}")
    print(f"Duration: {plan['Duration (weeks)']} weeks")
    print(f"Start Date: {plan['Start Date']}")
    print(f"End Date: {plan['End Date']}")
    print("\nTarget Skills:")
    for skill in plan["Target Skills"]:
        print(f"- {skill}")
    print("\nTrainers from Cara Productions:")
    for trainer in plan["Trainers"]:
        print(f"- {trainer}")
    print("\nWeekly Schedule:")
    for week in plan["Schedule"]:
        print(f"Week {week['Week']}: {week['Focus Skill']}")
        for activity in week["Activities"]:
            print(f"  - {activity}")
    print("\nContact Info:")
    for key, value in plan["Contact Info"]["Cara Productions"].items():
        print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    # Input data
    COMPANY_NAME = "ABC Corp Kenya"
    LOCATION = "Nairobi, Kenya"
    DURATION_WEEKS = 4
    TARGET_SKILLS = ["Media Interview Techniques", "Crisis Communication", "Public Speaking", "Content Creation"]
    TRAINERS = ["John Doe", "Jane Smith", "Alice Johnson"]

    # Generate training plan
    training_plan = generate_training_plan(COMPANY_NAME, LOCATION, DURATION_WEEKS, TARGET_SKILLS, TRAINERS)

    # Display training plan
    display_training_plan(training_plan)
```
