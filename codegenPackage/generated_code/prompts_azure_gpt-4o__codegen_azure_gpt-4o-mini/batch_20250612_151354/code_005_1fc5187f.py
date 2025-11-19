"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Develop a script to track volunteer participation in programs like SIM retreats and outreach missions, using a cloud-based database service such as Firebase.
Generated: DETERMINISTIC_1fc5187f8c75705d
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

class VolunteerTracker:
    def __init__(self):
        """Initialize the VolunteerTracker with Firestore database reference."""
        self.volunteers_ref = db.collection('volunteers')

    def add_volunteer(self, name, email, program):
        """
        Add a new volunteer to the database.

        Args:
            name (str): The name of the volunteer.
            email (str): The email of the volunteer.
            program (str): The program the volunteer is participating in.

        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        if not name or not email or not program:
            raise ValueError("Name, email, and program must be provided.")

        volunteer_data = {
            'name': name,
            'email': email,
            'program': program,
            'participation_date': firestore.SERVER_TIMESTAMP
        }

        try:
            self.volunteers_ref.add(volunteer_data)
            print(f"Volunteer {name} added successfully.")
        except Exception as e:
            print(f"Error adding volunteer: {e}")

    def get_volunteers(self, program):
        """
        Retrieve a list of volunteers for a specific program.

        Args:
            program (str): The program to filter volunteers by.

        Returns:
            list: A list of volunteers participating in the specified program.
        """
        if not program:
            raise ValueError("Program must be provided.")

        try:
            volunteers = self.volunteers_ref.where('program', '==', program).stream()
            return [vol.to_dict() for vol in volunteers]
        except Exception as e:
            print(f"Error retrieving volunteers: {e}")
            return []

    def remove_volunteer(self, volunteer_id):
        """
        Remove a volunteer from the database.

        Args:
            volunteer_id (str): The ID of the volunteer to remove.

        Raises:
            ValueError: If the volunteer_id is invalid.
        """
        if not volunteer_id:
            raise ValueError("Volunteer ID must be provided.")

        try:
            self.volunteers_ref.document(volunteer_id).delete()
            print(f"Volunteer {volunteer_id} removed successfully.")
        except Exception as e:
            print(f"Error removing volunteer: {e}")

# Example usage
if __name__ == "__main__":
    tracker = VolunteerTracker()
    
    # Add a volunteer
    tracker.add_volunteer("John Doe", "john.doe@example.com", "SIM Retreat 2023")
    
    # Get volunteers for a specific program
    volunteers = tracker.get_volunteers("SIM Retreat 2023")
    print(volunteers)
    
    # Remove a volunteer (replace 'volunteer_id' with actual ID)
    # tracker.remove_volunteer('volunteer_id')
```

**Note:** Replace `'path/to/your/serviceAccountKey.json'` with the actual path to your Firebase service account key JSON file.
