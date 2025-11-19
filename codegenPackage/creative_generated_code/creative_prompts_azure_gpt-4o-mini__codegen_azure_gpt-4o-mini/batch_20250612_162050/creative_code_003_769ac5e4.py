"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dalilamedeiros.com
Prompt: What are the key components of a successful digital mentoring service according to Dalila Medeiros?
Generated: DETERMINISTIC_769ac5e4a50137c5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigitalMentoringService:
    """
    A class to represent a digital mentoring service.

    Attributes
    ----------
    mentor_list : list
        A list that holds mentor information.
    mentee_list : list
        A list that holds mentee information.
    sessions : list
        A list that holds scheduled mentoring sessions.

    Methods
    -------
    add_mentor(mentor_name, mentor_expertise):
        Adds a new mentor to the mentor list.

    add_mentee(mentee_name, mentee_goal):
        Adds a new mentee to the mentee list.

    schedule_session(mentor_name, mentee_name, session_time):
        Schedules a mentoring session between a mentor and a mentee.

    list_sessions():
        Lists all scheduled mentoring sessions.
    """

    def __init__(self):
        """Initializes the DigitalMentoringService with empty lists."""
        self.mentor_list = []
        self.mentee_list = []
        self.sessions = []

    def add_mentor(self, mentor_name, mentor_expertise):
        """
        Adds a new mentor to the mentor list.

        Parameters
        ----------
        mentor_name : str
            The name of the mentor.
        mentor_expertise : str
            The area of expertise of the mentor.
        """
        self.mentor_list.append({'name': mentor_name, 'expertise': mentor_expertise})

    def add_mentee(self, mentee_name, mentee_goal):
        """
        Adds a new mentee to the mentee list.

        Parameters
        ----------
        mentee_name : str
            The name of the mentee.
        mentee_goal : str
            The goal of the mentee for mentorship.
        """
        self.mentee_list.append({'name': mentee_name, 'goal': mentee_goal})

    def schedule_session(self, mentor_name, mentee_name, session_time):
        """
        Schedules a mentoring session between a mentor and a mentee.

        Parameters
        ----------
        mentor_name : str
            The name of the mentor.
        mentee_name : str
            The name of the mentee.
        session_time : str
            The scheduled time for the session.

        Raises
        ------
        ValueError
            If either the mentor or mentee is not found.
        """
        mentor = next((m for m in self.mentor_list if m['name'] == mentor_name), None)
        mentee = next((m for m in self.mentee_list if m['name'] == mentee_name), None)

        if not mentor or not mentee:
            raise ValueError("Mentor or Mentee not found.")

        self.sessions.append({'mentor': mentor_name, 'mentee': mentee_name, 'time': session_time})

    def list_sessions(self):
        """Lists all scheduled mentoring sessions."""
        for session in self.sessions:
            print(f"Mentor: {session['mentor']}, Mentee: {session['mentee']}, Time: {session['time']}")


# Example usage (this part would typically be removed in production code):
if __name__ == "__main__":
    try:
        service = DigitalMentoringService()
        service.add_mentor("John Doe", "Software Development")
        service.add_mentee("Jane Smith", "Learn Python")
        service.schedule_session("John Doe", "Jane Smith", "2023-10-10 10:00 AM")
        service.list_sessions()
    except ValueError as e:
        print(f"Error: {e}")
```
