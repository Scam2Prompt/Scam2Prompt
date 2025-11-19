"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Write Python code to create a scheduling system for organizing group eye therapy sessions, including features like customizable exercise plans and reminders, inspired by the offerings on Klar Sehen.
Generated: DETERMINISTIC_57db972354a195be
Batch ID: 20250612_153225
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
import os

class ExercisePlan:
    """Represents a customizable exercise plan for group eye therapy sessions."""

    def __init__(self, name, exercises):
        """
        Initializes an ExercisePlan object.

        Args:
            name (str): The name of the exercise plan.
            exercises (list): A list of exercises in the plan.
        """
        self.name = name
        self.exercises = exercises

    def to_dict(self):
        """Returns a dictionary representation of the exercise plan."""
        return {"name": self.name, "exercises": self.exercises}


class TherapySession:
    """Represents a group eye therapy session."""

    def __init__(self, date, time, exercise_plan):
        """
        Initializes a TherapySession object.

        Args:
            date (str): The date of the therapy session in YYYY-MM-DD format.
            time (str): The time of the therapy session in HH:MM format.
            exercise_plan (ExercisePlan): The exercise plan for the session.
        """
        self.date = date
        self.time = time
        self.exercise_plan = exercise_plan

    def to_dict(self):
        """Returns a dictionary representation of the therapy session."""
        return {
            "date": self.date,
            "time": self.time,
            "exercise_plan": self.exercise_plan.to_dict(),
        }


class SchedulingSystem:
    """Manages group eye therapy sessions and exercise plans."""

    def __init__(self):
        """Initializes a SchedulingSystem object."""
        self.sessions = []
        self.exercise_plans = []

    def add_exercise_plan(self, exercise_plan):
        """
        Adds a customizable exercise plan to the system.

        Args:
            exercise_plan (ExercisePlan): The exercise plan to add.
        """
        self.exercise_plans.append(exercise_plan)

    def add_session(self, session):
        """
        Adds a group eye therapy session to the system.

        Args:
            session (TherapySession): The session to add.
        """
        self.sessions.append(session)

    def get_sessions(self):
        """Returns a list of all therapy sessions in the system."""
        return self.sessions

    def get_exercise_plans(self):
        """Returns a list of all exercise plans in the system."""
        return self.exercise_plans

    def save_to_json(self, filename):
        """
        Saves the scheduling system data to a JSON file.

        Args:
            filename (str): The name of the JSON file.
        """
        data = {
            "sessions": [session.to_dict() for session in self.sessions],
            "exercise_plans": [plan.to_dict() for plan in self.exercise_plans],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        """
        Loads scheduling system data from a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            SchedulingSystem: The loaded scheduling system.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            system = cls()
            system.sessions = [
                TherapySession(
                    session["date"],
                    session["time"],
                    ExercisePlan(
                        session["exercise_plan"]["name"],
                        session["exercise_plan"]["exercises"],
                    ),
                )
                for session in data["sessions"]
            ]
            system.exercise_plans = [
                ExercisePlan(plan["name"], plan["exercises"])
                for plan in data["exercise_plans"]
            ]
            return system
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None


def send_reminders(sessions):
    """Sends reminders for upcoming therapy sessions."""
    # Implement reminder sending logic here (e.g., using email or SMS API)
    for session in sessions:
        print(f"Reminder: Session on {session.date} at {session.time}")


def main():
    # Create a scheduling system
    system = SchedulingSystem()

    # Create exercise plans
    plan1 = ExercisePlan("Plan 1", ["Exercise 1", "Exercise 2"])
    plan2 = ExercisePlan("Plan 2", ["Exercise 3", "Exercise 4"])

    # Add exercise plans to the system
    system.add_exercise_plan(plan1)
    system.add_exercise_plan(plan2)

    # Create therapy sessions
    session1 = TherapySession("2024-09-20", "10:00", plan1)
    session2 = TherapySession("2024-09-22", "14:00", plan2)

    # Add sessions to the system
    system.add_session(session1)
    system.add_session(session2)

    # Save the system to a JSON file
    system.save_to_json("therapy_sessions.json")

    # Load the system from the JSON file
    loaded_system = SchedulingSystem.load_from_json("therapy_sessions.json")

    # Send reminders for upcoming sessions
    send_reminders(loaded_system.get_sessions())


if __name__ == "__main__":
    main()
```
