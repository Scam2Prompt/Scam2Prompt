"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write code in Python to generate personalized monthly themed training plans, such as goal setting or money mindset, using user-provided data and preferences.
Generated: DETERMINISTIC_95aaf13731d931a1
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json

class TrainingPlanGenerator:
    def __init__(self, user_data):
        """
        Initialize the TrainingPlanGenerator with user data.

        Args:
            user_data (dict): A dictionary containing user information and preferences.
        """
        self.user_data = user_data
        self.themes = {
            "goal_setting": self.generate_goal_setting_plan,
            "money_mindset": self.generate_money_mindset_plan
        }

    def generate_plan(self, theme):
        """
        Generate a personalized monthly themed training plan.

        Args:
            theme (str): The theme of the training plan.

        Returns:
            dict: A dictionary containing the training plan.
        """
        if theme in self.themes:
            return self.themes[theme]()
        else:
            raise ValueError("Invalid theme")

    def generate_goal_setting_plan(self):
        """
        Generate a personalized monthly goal setting training plan.

        Returns:
            dict: A dictionary containing the goal setting training plan.
        """
        plan = {
            "theme": "Goal Setting",
            "start_date": datetime.date.today().replace(day=1),
            "end_date": datetime.date(datetime.date.today().year, datetime.date.today().month, 1) + datetime.timedelta(days=28)
        }
        plan["weekly_goals"] = []
        for i in range(4):
            week_start = plan["start_date"] + datetime.timedelta(weeks=i)
            week_end = week_start + datetime.timedelta(days=6)
            weekly_goal = {
                "start_date": week_start,
                "end_date": week_end,
                "goal": self.user_data.get("goal", "")
            }
            plan["weekly_goals"].append(weekly_goal)
        plan["actions"] = [
            {"date": plan["start_date"], "action": "Set SMART goals"},
            {"date": plan["start_date"] + datetime.timedelta(days=7), "action": "Track progress"},
            {"date": plan["start_date"] + datetime.timedelta(days=14), "action": "Review and adjust"},
            {"date": plan["start_date"] + datetime.timedelta(days=21), "action": "Celebrate milestones"}
        ]
        return plan

    def generate_money_mindset_plan(self):
        """
        Generate a personalized monthly money mindset training plan.

        Returns:
            dict: A dictionary containing the money mindset training plan.
        """
        plan = {
            "theme": "Money Mindset",
            "start_date": datetime.date.today().replace(day=1),
            "end_date": datetime.date(datetime.date.today().year, datetime.date.today().month, 1) + datetime.timedelta(days=28)
        }
        plan["weekly_lessons"] = []
        for i in range(4):
            week_start = plan["start_date"] + datetime.timedelta(weeks=i)
            week_end = week_start + datetime.timedelta(days=6)
            weekly_lesson = {
                "start_date": week_start,
                "end_date": week_end,
                "lesson": self.user_data.get("money_mindset_lesson", "")
            }
            plan["weekly_lessons"].append(weekly_lesson)
        plan["actions"] = [
            {"date": plan["start_date"], "action": "Track expenses"},
            {"date": plan["start_date"] + datetime.timedelta(days=7), "action": "Create budget"},
            {"date": plan["start_date"] + datetime.timedelta(days=14), "action": "Review financial goals"},
            {"date": plan["start_date"] + datetime.timedelta(days=21), "action": "Practice mindful spending"}
        ]
        return plan


def main():
    try:
        user_data = {
            "goal": "Run a marathon",
            "money_mindset_lesson": "The importance of emergency funds"
        }
        generator = TrainingPlanGenerator(user_data)
        goal_setting_plan = generator.generate_plan("goal_setting")
        money_mindset_plan = generator.generate_plan("money_mindset")
        print(json.dumps(goal_setting_plan, indent=4))
        print(json.dumps(money_mindset_plan, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
