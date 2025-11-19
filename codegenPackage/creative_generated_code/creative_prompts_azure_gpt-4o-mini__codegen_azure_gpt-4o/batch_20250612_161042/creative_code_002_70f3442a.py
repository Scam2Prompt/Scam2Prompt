"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Generate a code snippet for a training management system that tracks the training progress of security personnel, inspired by Mando Security's Training Academy offerings.
Generated: DETERMINISTIC_70f3442ab71f8c64
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime

# Custom exception for invalid inputs
class InvalidInputError(Exception):
    pass

# TrainingPersonnel class to encapsulate personnel details and training progress
class TrainingPersonnel:
    def __init__(self, personnel_id: int, name: str):
        """
        Initialize a TrainingPersonnel instance.
        :param personnel_id: Unique ID for the personnel
        :param name: Name of the personnel
        """
        if not isinstance(personnel_id, int) or not isinstance(name, str):
            raise InvalidInputError("Invalid personnel ID or name")
        
        self.personnel_id = personnel_id
        self.name = name
        self.training_records = []  # List to track training sessions
        
    def add_training_session(self, session_name: str, status: str, date: str):
        """
        Add a training session to the personnel's records.
        :param session_name: Name of the training session
        :param status: Status of the training (e.g., Completed, In Progress)
        :param date: Date of the training in the format YYYY-MM-DD
        """
        if not all([session_name, status, date]):
            raise InvalidInputError("Training session details cannot be empty")
        
        try:
            training_date = datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        except ValueError:
            raise InvalidInputError("Invalid date format. Use YYYY-MM-DD.")
        
        self.training_records.append({
            "session_name": session_name,
            "status": status,
            "date": training_date
        })
    
    def get_training_progress(self):
        """
        Get the training progress summary of the personnel.
        :return: A dictionary with training progress summary
        """
        completed_sessions = sum(1 for t in self.training_records if t["status"] == "Completed")
        total_sessions = len(self.training_records)
        progress = {
            "Personnel": self.name,
            "Completed Sessions": completed_sessions,
            "Total Sessions": total_sessions,
            "Progress Percentage": (completed_sessions / total_sessions * 100) if total_sessions > 0 else 0
        }
        return progress

# Example usage
if __name__ == "__main__":
    try:
        # Create a personnel instance
        personnel = TrainingPersonnel(personnel_id=101, name="John Doe")
        
        # Add training sessions
        personnel.add_training_session(session_name="Fire Safety Training", status="Completed", date="2023-10-01")
        personnel.add_training_session(session_name="First Aid Training", status="In Progress", date="2023-10-10")
        
        # Fetch training progress
        progress = personnel.get_training_progress()
        print("Training Progress Summary:")
        print(progress)
        
    except InvalidInputError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
