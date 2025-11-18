"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Write Python code to simulate a standard exam preparation schedule for medical admission coaching, incorporating Retina's updated preparation strategies and class effectiveness metrics.
Generated: DETERMINISTIC_3258f070ffee55f1
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

# Constants for the schedule
TOTAL_DAYS = 180  # Total days for exam preparation
SUBJECTS = ['Biology', 'Physics', 'Chemistry']  # Core subjects
DAILY_HOURS = {'Biology': 4, 'Physics': 3, 'Chemistry': 3}  # Study hours per subject
RETINA_STRATEGIES = {
    'Biology': {'focus_topics': ['Genetics', 'Cell Biology'], 'revision_weight': 0.6},
    'Physics': {'focus_topics': ['Mechanics', 'Optics'], 'revision_weight': 0.5},
    'Chemistry': {'focus_topics': ['Organic Chemistry', 'Inorganic Chemistry'], 'revision_weight': 0.7},
}

# Effectiveness metrics for morning, afternoon, and evening study sessions
SESSION_EFFECTIVENESS = {
    'Morning': 0.8,
    'Afternoon': 0.6,
    'Evening': 0.7
}


class ExamPreparationSchedule:
    """
    Class to simulate an exam preparation schedule for medical admission coaching.
    """

    def __init__(self):
        self.schedule = {}

    def generate_daily_schedule(self, start_date):
        """
        Generates a daily study schedule based on Retina's updated preparation strategies.
        :param start_date: The starting date for the schedule
        """
        current_date = start_date
        for day in range(TOTAL_DAYS):
            daily_plan = []
            for subject in SUBJECTS:
                # Assign study strategies to the subject
                strategies = RETINA_STRATEGIES.get(subject, {})
                focus_topics = strategies.get('focus_topics', [])
                revision_weight = strategies.get('revision_weight', 0.5)

                # Allocate study hours
                study_hours = DAILY_HOURS[subject]

                # Determine the effectiveness of study sessions
                session = self._select_study_session()
                effectiveness = SESSION_EFFECTIVENESS[session]

                daily_plan.append({
                    'subject': subject,
                    'study_hours': study_hours,
                    'focus_topics': focus_topics,
                    'revision_weight': revision_weight,
                    'session': session,
                    'effectiveness': effectiveness
                })

            # Add the daily plan to the schedule
            self.schedule[current_date.strftime('%Y-%m-%d')] = daily_plan
            current_date += datetime.timedelta(days=1)

    def display_schedule(self):
        """
        Displays the generated study schedule.
        """
        for date, plans in self.schedule.items():
            print(f"Date: {date}")
            for plan in plans:
                print(f"  Subject: {plan['subject']}")
                print(f"    Study Hours: {plan['study_hours']}")
                print(f"    Focus Topics: {', '.join(plan['focus_topics'])}")
                print(f"    Revision Weight: {plan['revision_weight']}")
                print(f"    Session: {plan['session']}")
                print(f"    Effectiveness: {plan['effectiveness']:.2f}")
            print()

    @staticmethod
    def _select_study_session():
        """
        Randomly selects a study session (Morning, Afternoon, Evening).
        :return: A study session string
        """
        return random.choice(list(SESSION_EFFECTIVENESS.keys()))


# Error handling for invalid inputs
def validate_start_date(date_str):
    """
    Validates the start date input format.
    :param date_str: Date string in 'YYYY-MM-DD' format
    :return: datetime object if valid, else raises ValueError
    """
    try:
        start_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return start_date
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")


if __name__ == "__main__":
    try:
        # Input start date for schedule generation
        start_date_input = input("Enter the start date for the schedule (YYYY-MM-DD): ").strip()
        start_date = validate_start_date(start_date_input)

        # Create and generate the exam preparation schedule
        schedule = ExamPreparationSchedule()
        schedule.generate_daily_schedule(start_date)

        # Display the schedule
        print("\nGenerated Exam Preparation Schedule:\n")
        schedule.display_schedule()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
