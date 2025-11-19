"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: What are the key components to consider when developing a web application for DBT therapy that includes both individual and group sessions?
Generated: DETERMINISTIC_e6d0de49aed95194
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List, Dict

class DBTSession:
    """Represents a DBT therapy session."""
    
    def __init__(self, session_type: str, attendees: List[str], date: str, time: str):
        """
        Initializes a DBTSession object.

        Args:
        session_type (str): Type of session (individual or group).
        attendees (List[str]): List of attendees for the session.
        date (str): Date of the session.
        time (str): Time of the session.
        """
        self.session_type = session_type
        self.attendees = attendees
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.session_type} session on {self.date} at {self.time} with {', '.join(self.attendees)}"


class DBTProgram:
    """Represents a DBT therapy program."""
    
    def __init__(self):
        """
        Initializes a DBTProgram object.
        """
        self.individual_sessions: List[DBTSession] = []
        self.group_sessions: List[DBTSession] = []

    def add_session(self, session: DBTSession):
        """
        Adds a session to the program.

        Args:
        session (DBTSession): Session to add.

        Raises:
        ValueError: If session type is not 'individual' or 'group'.
        """
        if session.session_type.lower() == 'individual':
            self.individual_sessions.append(session)
        elif session.session_type.lower() == 'group':
            self.group_sessions.append(session)
        else:
            raise ValueError("Invalid session type. Must be 'individual' or 'group'.")

    def get_sessions(self, session_type: str = None) -> List[DBTSession]:
        """
        Gets sessions of a specific type.

        Args:
        session_type (str): Type of session to retrieve (individual or group). If None, returns all sessions.

        Returns:
        List[DBTSession]: List of sessions.

        Raises:
        ValueError: If session type is not 'individual', 'group', or None.
        """
        if session_type is None:
            return self.individual_sessions + self.group_sessions
        elif session_type.lower() == 'individual':
            return self.individual_sessions
        elif session_type.lower() == 'group':
            return self.group_sessions
        else:
            raise ValueError("Invalid session type. Must be 'individual', 'group', or None.")

def main():
    try:
        # Create a DBT program
        program = DBTProgram()

        # Create individual sessions
        individual_session1 = DBTSession('individual', ['John Doe'], '2024-09-16', '10:00 AM')
        individual_session2 = DBTSession('individual', ['Jane Doe'], '2024-09-17', '11:00 AM')

        # Create group sessions
        group_session1 = DBTSession('group', ['Group 1', 'Group 2'], '2024-09-18', '2:00 PM')

        # Add sessions to the program
        program.add_session(individual_session1)
        program.add_session(individual_session2)
        program.add_session(group_session1)

        # Get and print all sessions
        all_sessions = program.get_sessions()
        print("All Sessions:")
        for session in all_sessions:
            print(session)

        # Get and print individual sessions
        individual_sessions = program.get_sessions('individual')
        print("\nIndividual Sessions:")
        for session in individual_sessions:
            print(session)

        # Get and print group sessions
        group_sessions = program.get_sessions('group')
        print("\nGroup Sessions:")
        for session in group_sessions:
            print(session)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
