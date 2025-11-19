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
# Import required libraries
import firebase_admin
from firebase_admin import credentials, firestore, auth
from datetime import datetime

# Initialize Firebase credentials
cred = credentials.Certificate("path/to/serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

class Volunteer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.participation = []

    def add_participation(self, program, date):
        self.participation.append({"program": program, "date": date})

class ProgramTracker:
    def __init__(self):
        self.volunteers = {}

    def add_volunteer(self, id, name, email):
        """Add a new volunteer to the tracker"""
        if id not in self.volunteers:
            self.volunteers[id] = Volunteer(id, name, email)
            self.save_volunteer(id)
            return True
        return False

    def save_volunteer(self, id):
        """Save volunteer data to Firestore"""
        try:
            volunteer = self.volunteers[id]
            db.collection("volunteers").document(id).set({
                "name": volunteer.name,
                "email": volunteer.email,
                "participation": volunteer.participation
            })
        except Exception as e:
            print(f"Error saving volunteer: {e}")

    def log_participation(self, id, program, date=None):
        """Log volunteer participation in a program"""
        if id in self.volunteers:
            if date is None:
                date = datetime.now().strftime("%Y-%m-%d")
            self.volunteers[id].add_participation(program, date)
            self.save_volunteer(id)
            return True
        return False

    def get_volunteer_participation(self, id):
        """Get a volunteer's participation history"""
        if id in self.volunteers:
            return self.volunteers[id].participation
        try:
            doc = db.collection("volunteers").document(id).get()
            if doc.exists:
                return doc.to_dict()["participation"]
        except Exception as e:
            print(f"Error retrieving volunteer participation: {e}")
        return []

def main():
    tracker = ProgramTracker()

    # Example usage:
    tracker.add_volunteer("V123", "John Doe", "john@example.com")
    tracker.log_participation("V123", "SIM Retreat")
    tracker.log_participation("V123", "Outreach Mission", "2022-07-01")

    participation = tracker.get_volunteer_participation("V123")
    print(participation)

if __name__ == "__main__":
    main()
```
