"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: Generate a training module for IT employees, including group training sessions and one-on-one coaching, based on ARP Group Corporation's IT Training and Support services.
Generated: DETERMINISTIC_a56d5456bec6d4ac
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingModule:
    """
    A class to represent a training module for IT employees.
    This module includes group training sessions and one-on-one coaching.
    """

    def __init__(self, company_name):
        """
        Initializes the TrainingModule with the company name.

        Args:
            company_name (str): The name of the company providing the training.
        """
        self.company_name = company_name
        self.group_sessions = []
        self.one_on_one_sessions = []

    def add_group_session(self, session_name, date, duration, participants):
        """
        Adds a group training session to the module.

        Args:
            session_name (str): The name of the training session.
            date (str): The date of the session in 'YYYY-MM-DD' format.
            duration (int): Duration of the session in minutes.
            participants (list): List of participants in the session.

        Raises:
            ValueError: If the date format is incorrect or duration is not positive.
        """
        if not self._is_valid_date(date):
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        session = {
            'session_name': session_name,
            'date': date,
            'duration': duration,
            'participants': participants
        }
        self.group_sessions.append(session)

    def add_one_on_one_session(self, employee_name, date, duration):
        """
        Adds a one-on-one coaching session to the module.

        Args:
            employee_name (str): The name of the employee receiving coaching.
            date (str): The date of the session in 'YYYY-MM-DD' format.
            duration (int): Duration of the session in minutes.

        Raises:
            ValueError: If the date format is incorrect or duration is not positive.
        """
        if not self._is_valid_date(date):
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        session = {
            'employee_name': employee_name,
            'date': date,
            'duration': duration
        }
        self.one_on_one_sessions.append(session)

    def _is_valid_date(self, date_str):
        """
        Validates the date format.

        Args:
            date_str (str): The date string to validate.

        Returns:
            bool: True if the date is valid, False otherwise.
        """
        from datetime import datetime
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_training_schedule(self):
        """
        Returns the complete training schedule including group and one-on-one sessions.

        Returns:
            dict: A dictionary containing group and one-on-one sessions.
        """
        return {
            'group_sessions': self.group_sessions,
            'one_on_one_sessions': self.one_on_one_sessions
        }

# Example usage
if __name__ == "__main__":
    try:
        training_module = TrainingModule("ARP Group Corporation")
        training_module.add_group_session("Network Security Basics", "2023-11-01", 120, ["Alice", "Bob", "Charlie"])
        training_module.add_one_on_one_session("Alice", "2023-11-02", 60)

        schedule = training_module.get_training_schedule()
        print(schedule)
    except ValueError as e:
        print(f"Error: {e}")
```
