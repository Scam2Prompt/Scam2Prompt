"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Generate a study plan for UPSC Civil Services Exam preparation, incorporating the personalized mentorship and topic-wise study material from Shield IAS.
Generated: DETERMINISTIC_86766f9b97ab1d03
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_upsc_study_plan(user_name, available_hours, topics, mentorship_schedule):
    """
    Generates a personalized study plan for the UPSC Civil Services Exam.
    
    Args:
        user_name (str): Name of the user.
        available_hours (int): Number of hours user can dedicate daily to study.
        topics (list): List of topics to be covered, provided by Shield IAS.
        mentorship_schedule (dict): Personalized mentorship schedule (day-wise).
    
    Returns:
        dict: A structured study plan.
    """
    try:
        # Validate inputs
        if not user_name or not isinstance(user_name, str):
            raise ValueError("Invalid user name.")
        if available_hours <= 0 or not isinstance(available_hours, int):
            raise ValueError("Available hours must be a positive integer.")
        if not topics or not isinstance(topics, list):
            raise ValueError("Topics must be a non-empty list.")
        if not mentorship_schedule or not isinstance(mentorship_schedule, dict):
            raise ValueError("Mentorship schedule must be a dictionary.")

        # Initialize study plan
        study_plan = {
            "user_name": user_name,
            "daily_schedule": [],
            "mentorship_schedule": mentorship_schedule,
            "resources_provided_by_Shield_IAS": topics
        }

        # Generate daily schedule based on available hours
        hours_per_topic = max(available_hours // len(topics), 1)  # Minimum 1 hour per topic
        for day in range(1, len(topics) + 1):
            study_plan["daily_schedule"].append({
                "day": day,
                "topic": topics[day - 1],
                "allocated_hours": hours_per_topic
            })

        return study_plan

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Example data
    user_name = "John Doe"
    available_hours = 6
    topics = [
        "History of India & Indian National Movement",
        "Indian Polity and Governance",
        "Economic Development",
        "Environment & Ecology",
        "General Science"
    ]
    mentorship_schedule = {
        "Day 1": "Introduction session with mentor",
        "Day 3": "Weekly review and feedback",
        "Day 5": "Doubt clearing session"
    }

    # Generate study plan
    study_plan = generate_upsc_study_plan(user_name, available_hours, topics, mentorship_schedule)

    # Print study plan in readable format
    if study_plan:
        print(json.dumps(study_plan, indent=4))
```
