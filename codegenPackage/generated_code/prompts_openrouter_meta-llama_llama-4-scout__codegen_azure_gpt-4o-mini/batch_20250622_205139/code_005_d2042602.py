"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Design an executive coaching program using OSI-type methods, focusing on sustainable and ethical growth for C-level executives and entrepreneurs.
Generated: DETERMINISTIC_d20426024cee0446
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ExecutiveCoachingProgram:
    """
    A class to represent an executive coaching program focused on sustainable and ethical growth
    for C-level executives and entrepreneurs using OSI-type methods.
    """

    def __init__(self, client_name, goals):
        """
        Initializes the coaching program with the client's name and their specific goals.

        :param client_name: str - The name of the client (C-level executive or entrepreneur)
        :param goals: list - A list of goals the client wants to achieve through coaching
        """
        self.client_name = client_name
        self.goals = goals
        self.sessions = []
        self.progress = {}

    def add_session(self, session_date, session_topic):
        """
        Adds a coaching session to the program.

        :param session_date: str - The date of the session in 'YYYY-MM-DD' format
        :param session_topic: str - The topic of the coaching session
        :raises ValueError: If the session date is not in the correct format
        """
        try:
            from datetime import datetime
            # Validate the date format
            datetime.strptime(session_date, '%Y-%m-%d')
            self.sessions.append({'date': session_date, 'topic': session_topic})
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    def track_progress(self, goal, status):
        """
        Tracks the progress of a specific goal.

        :param goal: str - The goal to track
        :param status: str - The current status of the goal (e.g., 'In Progress', 'Achieved')
        :raises KeyError: If the goal is not in the list of goals
        """
        if goal not in self.goals:
            raise KeyError(f"Goal '{goal}' not found in the client's goals.")
        self.progress[goal] = status

    def generate_report(self):
        """
        Generates a summary report of the coaching program, including sessions and progress.

        :return: dict - A summary report containing client name, goals, sessions, and progress
        """
        report = {
            'client_name': self.client_name,
            'goals': self.goals,
            'sessions': self.sessions,
            'progress': self.progress
        }
        return report

    def display_report(self):
        """
        Displays the summary report of the coaching program in a readable format.
        """
        report = self.generate_report()
        print("Executive Coaching Program Report")
        print("=" * 40)
        print(f"Client Name: {report['client_name']}")
        print("Goals:")
        for goal in report['goals']:
            print(f" - {goal}")
        print("Sessions:")
        for session in report['sessions']:
            print(f" - Date: {session['date']}, Topic: {session['topic']}")
        print("Progress:")
        for goal, status in report['progress'].items():
            print(f" - {goal}: {status}")
        print("=" * 40)


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the coaching program
        coaching_program = ExecutiveCoachingProgram("John Doe", ["Improve leadership skills", "Enhance strategic thinking"])

        # Add sessions
        coaching_program.add_session("2023-10-01", "Leadership Styles")
        coaching_program.add_session("2023-10-15", "Strategic Decision Making")

        # Track progress
        coaching_program.track_progress("Improve leadership skills", "In Progress")
        coaching_program.track_progress("Enhance strategic thinking", "Not Started")

        # Display the report
        coaching_program.display_report()

    except Exception as e:
        print(f"An error occurred: {e}")
```
