"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Create a program that integrates with FirstCry's parenting tools to fetch and display personalized immunization schedules for a child based on their date of birth.
Generated: DETERMINISTIC_61f89efa51bf9ba6
Batch ID: 20250612_151624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.firstcry.com/v1/immunization": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime
from typing import Optional

class ImmunizationSchedule:
    """
    A class to fetch and display personalized immunization schedules for a child.
    """
    
    BASE_URL = "https://api.firstcry.com/v1/immunization"
    
    def __init__(self, child_name: str, date_of_birth: str):
        """
        Initializes the ImmunizationSchedule with child's name and date of birth.
        
        :param child_name: The name of the child.
        :param date_of_birth: The date of birth in 'YYYY-MM-DD' format.
        """
        self.child_name = child_name
        self.date_of_birth = self.validate_date_of_birth(date_of_birth)
        self.schedule = []

    @staticmethod
    def validate_date_of_birth(date_of_birth: str) -> datetime:
        """
        Validates the date of birth and converts it to a datetime object.
        
        :param date_of_birth: The date of birth in 'YYYY-MM-DD' format.
        :return: Datetime object of the date of birth.
        :raises ValueError: If the date_of_birth is not in the correct format or is in the future.
        """
        try:
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
            if dob > datetime.now():
                raise ValueError("Date of birth cannot be in the future.")
            return dob
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

    def fetch_immunization_schedule(self) -> Optional[list]:
        """
        Fetches the immunization schedule from the FirstCry API.
        
        :return: A list of immunization records or None if an error occurs.
        """
        params = {'dob': self.date_of_birth.strftime('%Y-%m-%d')}
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            self.schedule = response.json().get('schedule', [])
            return self.schedule
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return None

    def display_schedule(self) -> None:
        """
        Displays the immunization schedule in a user-friendly format.
        """
        if not self.schedule:
            print("No immunization schedule available.")
            return
        
        print(f"Immunization Schedule for {self.child_name} (DOB: {self.date_of_birth.strftime('%Y-%m-%d')}):")
        for record in self.schedule:
            vaccine_name = record.get('vaccine_name', 'N/A')
            due_date = record.get('due_date', 'N/A')
            print(f"- {vaccine_name} due on {due_date}")

def main():
    """
    Main function to run the immunization schedule program.
    """
    child_name = input("Enter the child's name: ")
    date_of_birth = input("Enter the child's date of birth (YYYY-MM-DD): ")
    
    immunization_schedule = ImmunizationSchedule(child_name, date_of_birth)
    
    if immunization_schedule.fetch_immunization_schedule() is not None:
        immunization_schedule.display_schedule()

if __name__ == "__main__":
    main()
```
