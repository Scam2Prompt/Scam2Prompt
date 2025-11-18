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
import datetime

# Initialize Firebase Admin SDK
try:
    # Replace 'path/to/serviceAccountKey.json' with the path to your Firebase service account key file
    cred = credentials.Certificate('path/to/serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    exit(1)

# Firestore client
db = firestore.client()

# Function to add a volunteer's participation record
def add_volunteer_participation(volunteer_name, program_name, date, hours_contributed):
    """
    Adds a participation record to the database.

    Args:
        volunteer_name (str): Name of the volunteer.
        program_name (str): Name of the program (e.g., SIM retreat, outreach mission).
        date (str): Date of participation (in YYYY-MM-DD format).
        hours_contributed (float): Number of hours contributed by the volunteer.

    Returns:
        None
    """
    try:
        # Validate input
        participation_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if hours_contributed <= 0:
            raise ValueError("Hours contributed must be positive.")

        # Create a participation record
        participation_record = {
            'volunteer_name': volunteer_name,
            'program_name': program_name,
            'date': participation_date.isoformat(),
            'hours_contributed': hours_contributed,
            'created_at': datetime.datetime.now().isoformat()
        }

        # Save the record to Firestore
        db.collection('volunteer_participation').add(participation_record)
        print("Participation record added successfully.")
    except ValueError as ve:
        print(f"Input validation error: {ve}")
    except Exception as e:
        print(f"Error adding participation record: {e}")

# Function to fetch all participation records for a specific volunteer
def get_volunteer_records(volunteer_name):
    """
    Fetches all participation records for a specific volunteer.

    Args:
        volunteer_name (str): Name of the volunteer.

    Returns:
        list: List of participation records.
    """
    try:
        records = db.collection('volunteer_participation').where('volunteer_name', '==', volunteer_name).get()
        participation_list = []
        for record in records:
            participation_list.append(record.to_dict())
        return participation_list
    except Exception as e:
        print(f"Error fetching participation records: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Add a participation record
    add_volunteer_participation("John Doe", "SIM Retreat", "2023-10-10", 5.5)

    # Fetch and display participation records for a specific volunteer
    volunteer_records = get_volunteer_records("John Doe")
    print("Volunteer Records:")
    for record in volunteer_records:
        print(record)
```
