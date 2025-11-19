"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Create a study plan for the ENEM exam using the Maratona do ENEM methodology, including video lessons, practice exercises, and simulated exams."
Generated: DETERMINISTIC_54b89d33174e75c1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

# Define the study plan structure
class StudyPlan:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.plan = []

    def generate_plan(self):
        try:
            # Calculate the total number of days for the study plan
            total_days = (self.end_date - self.start_date).days
            if total_days <= 0:
                raise ValueError("End date must be after start date.")

            # Define the subjects and their respective weights
            subjects = {
                "Mathematics": 0.25,
                "Science": 0.25,
                "Humanities": 0.25,
                "Languages": 0.25
            }

            # Generate daily study plan
            for day in range(total_days):
                current_date = self.start_date + timedelta(days=day)
                daily_plan = {
                    "date": current_date.strftime("%Y-%m-%d"),
                    "tasks": []
                }

                # Add tasks for each subject
                for subject, weight in subjects.items():
                    daily_plan["tasks"].append({
                        "subject": subject,
                        "video_lessons": int(weight * 4),  # Example: 4 lessons per day
                        "practice_exercises": int(weight * 20),  # Example: 20 exercises per day
                        "simulated_exams": 1 if day % 7 == 0 else 0  # Simulated exams every 7 days
                    })

                self.plan.append(daily_plan)
        except Exception as e:
            print(f"Error generating study plan: {e}")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Study plan saved to {filename}")
        except Exception as e:
            print(f"Error saving study plan to file: {e}")

    def display_plan(self):
        try:
            for day in self.plan:
                print(f"Date: {day['date']}")
                for task in day['tasks']:
                    print(f"  Subject: {task['subject']}")
                    print(f"    Video Lessons: {task['video_lessons']}")
                    print(f"    Practice Exercises: {task['practice_exercises']}")
                    print(f"    Simulated Exams: {task['simulated_exams']}")
                print()
        except Exception as e:
            print(f"Error displaying study plan: {e}")


# Main function to create and manage the study plan
def main():
    try:
        # Define the start and end dates for the study plan
        start_date = datetime.strptime("2023-10-01", "%Y-%m-%d")
        end_date = datetime.strptime("2023-11-30", "%Y-%m-%d")

        # Create the study plan
        study_plan = StudyPlan(start_date, end_date)
        study_plan.generate_plan()

        # Display the study plan
        study_plan.display_plan()

        # Save the study plan to a file
        study_plan.save_to_file("enem_study_plan.json")
    except Exception as e:
        print(f"Error in main function: {e}")


# Run the program
if __name__ == "__main__":
    main()
```
