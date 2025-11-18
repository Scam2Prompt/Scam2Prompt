"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write a script to schedule and manage fundraising activities, including assigning volunteers and tracking progress, inspired by CRM.f's activity planning tools.
Generated: DETERMINISTIC_5728e84d86fb2fd2
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to schedule and manage fundraising activities, assign volunteers, and track progress.
Inspired by CRM-like activity planning tools.

Features:
1. Add fundraising activities.
2. Assign volunteers to activities.
3. Track progress of activities.
"""

import datetime
import uuid

# Define a class for fundraising activities
class FundraisingActivity:
    def __init__(self, name, description, goal_amount, date):
        """
        Initialize a fundraising activity.
        :param name: Name of the activity.
        :param description: Description of the activity.
        :param goal_amount: Target fundraising goal.
        :param date: Scheduled date for the activity.
        """
        self.activity_id = str(uuid.uuid4())  # Unique identifier for the activity
        self.name = name
        self.description = description
        self.goal_amount = goal_amount
        self.date = date
        self.volunteers = []  # List of assigned volunteers
        self.raised_amount = 0  # Amount raised so far

    def assign_volunteer(self, volunteer_name):
        """
        Assign a volunteer to the activity.
        :param volunteer_name: Name of the volunteer to assign.
        """
        if volunteer_name not in self.volunteers:
            self.volunteers.append(volunteer_name)

    def update_progress(self, amount):
        """
        Update the progress of the fundraising activity.
        :param amount: Amount raised to be added.
        """
        if amount < 0:
            raise ValueError("Amount raised cannot be negative.")
        self.raised_amount += amount

    def __str__(self):
        """
        String representation of the activity.
        """
        return (
            f"Activity ID: {self.activity_id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Goal Amount: ${self.goal_amount:.2f}\n"
            f"Raised Amount: ${self.raised_amount:.2f}\n"
            f"Date: {self.date.strftime('%Y-%m-%d')}\n"
            f"Volunteers: {', '.join(self.volunteers) if self.volunteers else 'None'}\n"
        )


# Define a class to manage fundraising activities
class FundraisingManager:
    def __init__(self):
        """
        Initialize the fundraising manager with an empty list of activities.
        """
        self.activities = []

    def add_activity(self, name, description, goal_amount, date):
        """
        Add a new fundraising activity.
        :param name: Name of the activity.
        :param description: Description of the activity.
        :param goal_amount: Target fundraising goal.
        :param date: Scheduled date for the activity.
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object.")
        activity = FundraisingActivity(name, description, goal_amount, date)
        self.activities.append(activity)
        return activity

    def get_activity_by_id(self, activity_id):
        """
        Retrieve an activity by its unique ID.
        :param activity_id: Unique identifier of the activity.
        """
        for activity in self.activities:
            if activity.activity_id == activity_id:
                return activity
        raise ValueError(f"Activity with ID {activity_id} not found.")

    def list_activities(self):
        """
        List all fundraising activities.
        """
        if not self.activities:
            print("No activities found.")
        else:
            for activity in self.activities:
                print(activity)


# Error handling demo and script execution
if __name__ == "__main__":
    try:
        # Initialize the fundraising manager
        manager = FundraisingManager()

        # Add activities
        activity1 = manager.add_activity(
            name="Charity Run",
            description="A fundraising run for local charities.",
            goal_amount=5000.00,
            date=datetime.date(2023, 12, 15),
        )
        activity2 = manager.add_activity(
            name="Bake Sale",
            description="Selling baked goods to support the community center.",
            goal_amount=2000.00,
            date=datetime.date(2023, 11, 25),
        )

        # Assign volunteers
        activity1.assign_volunteer("Alice")
        activity1.assign_volunteer("Bob")
        activity2.assign_volunteer("Charlie")

        # Update progress
        activity1.update_progress(1500.00)
        activity2.update_progress(500.00)

        # List all activities
        print("\nAll Fundraising Activities:")
        manager.list_activities()

    except Exception as e:
        print(f"An error occurred: {e}")
```
