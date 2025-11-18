"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Develop a script to track volunteer participation in programs like SIM retreats and outreach missions, using a cloud-based database service such as Firebase.
Generated: DETERMINISTIC_1fc5187f8c75705d
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

class VolunteerTracker:
    def __init__(self):
        """Initializes the VolunteerTracker with a reference to the Firestore collection."""
        self.collection = db.collection("volunteer_participation")

    def add_volunteer(self, volunteer_name, program_name, date, hours):
        """
        Adds a new volunteer entry to the Firestore database.
        
        Args:
            volunteer_name (str): The name of the volunteer.
            program_name (str): The name of the program the volunteer participated in.
            date (str): The date of participation in 'YYYY-MM-DD' format.
            hours (float): The number of hours volunteered.
        
        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        if not isinstance(volunteer_name, str) or not volunteer_name:
            raise ValueError("Volunteer name must be a non-empty string.")
        if not isinstance(program_name, str) or not program_name:
            raise ValueError("Program name must be a non-empty string.")
        if not self._is_valid_date(date):
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        if not isinstance(hours, (int, float)) or hours < 0:
            raise ValueError("Hours must be a non-negative number.")

        # Prepare the document data
        doc_data = {
            "volunteer_name": volunteer_name,
            "program_name": program_name,
            "date": datetime.strptime(date, '%Y-%m-%d'),
            "hours": hours
        }

        # Add the volunteer entry to Firestore
        try:
            self.collection.add(doc_data)
            print("Volunteer entry added successfully.")
        except Exception as e:
            print(f"An error occurred while adding the volunteer entry: {e}")

    def _is_valid_date(self, date_str):
        """Checks if the date string is in the valid 'YYYY-MM-DD' format."""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_volunteer_records(self, volunteer_name):
        """
        Retrieves all volunteer records for a specific volunteer.
        
        Args:
            volunteer_name (str): The name of the volunteer.
        
        Returns:
            list: A list of volunteer records.
        """
        if not isinstance(volunteer_name, str) or not volunteer_name:
            raise ValueError("Volunteer name must be a non-empty string.")
        
        try:
            records = self.collection.where("volunteer_name", "==", volunteer_name).stream()
            return [record.to_dict() for record in records]
        except Exception as e:
            print(f"An error occurred while retrieving volunteer records: {e}")
            return []

# Example usage
if __name__ == "__main__":
    tracker = VolunteerTracker()
    
    # Adding a volunteer entry
    tracker.add_volunteer("Alice Johnson", "SIM Retreat", "2023-08-15", 5.5)

    # Retrieving volunteer records
    records = tracker.get_volunteer_records("Alice Johnson")
    print(records)
```
