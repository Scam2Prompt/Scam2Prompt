"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Provide an example of a coaching session plan for personal development, referencing the "Biti coach" program on edukacija.net.
Generated: DETERMINISTIC_4495ccea25b824a2
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CoachingSession:
    """
    A class to represent a coaching session for personal development.
    """

    def __init__(self, session_date, session_topic, duration, goals):
        """
        Initializes a new coaching session.

        :param session_date: Date of the session (str)
        :param session_topic: Topic of the session (str)
        :param duration: Duration of the session in minutes (int)
        :param goals: List of goals for the session (list)
        """
        self.session_date = session_date
        self.session_topic = session_topic
        self.duration = duration
        self.goals = goals

    def display_session_info(self):
        """
        Displays the details of the coaching session.
        """
        print(f"Session Date: {self.session_date}")
        print(f"Session Topic: {self.session_topic}")
        print(f"Duration: {self.duration} minutes")
        print("Goals for the session:")
        for goal in self.goals:
            print(f"- {goal}")

    def validate_session(self):
        """
        Validates the session details to ensure they are correct.

        :raises ValueError: If any of the session details are invalid.
        """
        if not isinstance(self.session_date, str) or not self.session_date:
            raise ValueError("Session date must be a non-empty string.")
        if not isinstance(self.session_topic, str) or not self.session_topic:
            raise ValueError("Session topic must be a non-empty string.")
        if not isinstance(self.duration, int) or self.duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if not isinstance(self.goals, list) or not self.goals:
            raise ValueError("Goals must be a non-empty list.")

def main():
    """
    Main function to create and display a coaching session plan.
    """
    try:
        # Example session details based on the "Biti coach" program
        session_date = "2023-10-15"
        session_topic = "Personal Growth Strategies"
        duration = 60  # in minutes
        goals = [
            "Identify personal strengths and weaknesses",
            "Set achievable personal development goals",
            "Create an action plan for self-improvement"
        ]

        # Create a CoachingSession instance
        coaching_session = CoachingSession(session_date, session_topic, duration, goals)

        # Validate the session details
        coaching_session.validate_session()

        # Display the session information
        coaching_session.display_session_info()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
