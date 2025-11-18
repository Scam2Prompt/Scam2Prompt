"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Create a Python program to schedule and manage consultations for immigration law services, including support for Skype, phone, and in-person appointments.
Generated: DETERMINISTIC_042f32ce49be3dcf
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os
from typing import List, Optional

class Consultation:
    """Represents a consultation appointment."""
    
    def __init__(self, client_name: str, consultation_type: str, date_time: datetime.datetime, notes: Optional[str] = None):
        self.client_name = client_name
        self.consultation_type = consultation_type  # E.g., 'Skype', 'Phone', 'In-Person'
        self.date_time = date_time
        self.notes = notes

    def to_dict(self) -> dict:
        """Converts the Consultation instance to a dictionary for easy serialization."""
        return {
            'client_name': self.client_name,
            'consultation_type': self.consultation_type,
            'date_time': self.date_time.isoformat(),
            'notes': self.notes
        }

class ConsultationManager:
    """Manages a list of consultations and provides functionality to add, remove, and list consultations."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.consultations: List[Consultation] = []
        self.load_data()

    def load_data(self):
        """Loads consultations from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.consultations = [Consultation(**item) for item in data]
    
    def save_data(self):
        """Saves consultations to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([consultation.to_dict() for consultation in self.consultations], file, indent=4)

    def add_consultation(self, consultation: Consultation):
        """Adds a new consultation to the list and saves it."""
        self.consultations.append(consultation)
        self.save_data()

    def remove_consultation(self, client_name: str, date_time: datetime.datetime):
        """Removes a consultation from the list based on client name and date/time."""
        self.consultations = [c for c in self.consultations if not (c.client_name == client_name and c.date_time == date_time)]
        self.save_data()

    def list_consultations(self) -> List[Consultation]:
        """Returns a list of all consultations."""
        return self.consultations

def main():
    """Main function to manage consultations."""
    data_file = 'consultations.json'
    manager = ConsultationManager(data_file)

    # Example usage
    try:
        # Adding a consultation
        new_consultation = Consultation(
            client_name='John Doe',
            consultation_type='Skype',
            date_time=datetime.datetime(2023, 11, 20, 10, 0),
            notes='Discuss visa options'
        )
        manager.add_consultation(new_consultation)

        # Listing all consultations
        print("Current consultations:")
        for consultation in manager.list_consultations():
            print(consultation.to_dict())

        # Removing a consultation
        manager.remove_consultation('John Doe', new_consultation.date_time)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
