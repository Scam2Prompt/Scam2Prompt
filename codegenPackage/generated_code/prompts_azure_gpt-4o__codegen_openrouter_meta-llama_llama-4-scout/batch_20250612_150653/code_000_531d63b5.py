"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Write Python code to analyze the impact of advocacy programs like Sauti Kenya's clean energy initiative using data from community training sessions. Include functions for calculating the number of people impacted based on cascade training metrics.
Generated: DETERMINISTIC_531d63b5f0467b3f
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# advocacy_program_analysis.py

class AdvocacyProgram:
    def __init__(self, program_name, training_sessions):
        """
        Initialize an AdvocacyProgram instance.

        Args:
            program_name (str): Name of the advocacy program.
            training_sessions (list): List of dictionaries containing training session data.
        """
        self.program_name = program_name
        self.training_sessions = training_sessions

    def calculate_people_impacted(self):
        """
        Calculate the total number of people impacted by the advocacy program.

        Returns:
            int: Total number of people impacted.
        """
        total_impacted = 0
        for session in self.training_sessions:
            total_impacted += self._calculate_session_impact(session)
        return total_impacted

    def _calculate_session_impact(self, session):
        """
        Calculate the number of people impacted by a single training session.

        Args:
            session (dict): Dictionary containing training session data.
                Expected keys: 'attendees', 'cascade_rate'

        Returns:
            int: Number of people impacted by the session.
        """
        attendees = session.get('attendees', 0)
        cascade_rate = session.get('cascade_rate', 0)
        impacted = attendees * (1 + cascade_rate)
        return int(impacted)

    def get_session_details(self):
        """
        Get details about each training session.

        Returns:
            list: List of dictionaries containing session details.
        """
        session_details = []
        for session in self.training_sessions:
            details = {
                'session_id': session.get('session_id'),
                'attendees': session.get('attendees'),
                'cascade_rate': session.get('cascade_rate'),
                'impacted': self._calculate_session_impact(session)
            }
            session_details.append(details)
        return session_details


def load_training_sessions(data_source):
    """
    Load training session data from a data source.

    Args:
        data_source (str): Path to the data source (e.g., CSV file).

    Returns:
        list: List of dictionaries containing training session data.
    """
    try:
        import pandas as pd
        data = pd.read_csv(data_source)
        training_sessions = data.to_dict(orient='records')
        return training_sessions
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return []


def main():
    data_source = 'training_sessions.csv'  # Replace with actual data source
    training_sessions = load_training_sessions(data_source)

    if not training_sessions:
        print("No training session data available.")
        return

    program = AdvocacyProgram('Sauti Kenya Clean Energy Initiative', training_sessions)
    total_impacted = program.calculate_people_impacted()
    print(f"Total people impacted: {total_impacted}")

    session_details = program.get_session_details()
    print("Session Details:")
    for details in session_details:
        print(details)


if __name__ == '__main__':
    main()
```

```python
# training_sessions.csv example

session_id,attendees,cascade_rate
1,50,2
2,75,1.5
3,30,3
```
