"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Write a Python script to manage volunteer registrations for a community outreach program like Springs International Ministries' Mission 2030.
Generated: DETERMINISTIC_f823df468ce97656
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class VolunteerRegistration:
    """Class to manage volunteer registrations for community outreach programs."""
    
    def __init__(self, data_file: str = "volunteers.csv"):
        """Initialize the registration system with a data file.
        
        Args:
            data_file: Path to the CSV file storing volunteer data.
        """
        self.data_file = data_file
        self.fieldnames = [
            "id", "first_name", "last_name", "email", 
            "phone", "skills", "availability", 
            "registration_date", "status"
        ]
        
        # Create data file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for a new volunteer.
        
        Returns:
            A string representing the unique ID.
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"VOL-{timestamp}"
    
    def register_volunteer(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        skills: List[str],
        availability: List[str],
    ) -> Dict[str, str]:
        """Register a new volunteer.
        
        Args:
            first_name: Volunteer's first name.
            last_name: Volunteer's last name.
            email: Volunteer's email address.
            phone: Volunteer's phone number.
            skills: List of skills the volunteer has.
            availability: List of days/times the volunteer is available.
            
        Returns:
            Dictionary containing the volunteer's registration details.
            
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        if not all([first_name, last_name, email, phone]):
            raise ValueError("All fields are required")
        
        volunteer = {
            "id": self._generate_id(),
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "email": email.strip().lower(),
            "phone": phone.strip(),
            "skills": ",".join(skills),
            "availability": ",".join(availability),
            "registration_date": datetime.now().isoformat(),
            "status": "active"
        }
        
        try:
            with open(self.data_file, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writerow(volunteer)
        except IOError as e:
            raise IOError(f"Failed to save volunteer data: {str(e)}")
        
        return volunteer
    
    def get_volunteers(self, status: Optional[str] = None) -> List[Dict[str, str]]:
        """Retrieve all volunteers or filter by status.
        
        Args:
            status: Optional status filter ('active', 'inactive', etc.)
            
        Returns:
            List of dictionaries containing volunteer data.
        """
        volunteers = []
        
        try:
            with open(self.data_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if status is None or row['status'].lower() == status.lower():
                        volunteers.append(row)
        except FileNotFoundError:
            return []
        
        return volunteers
    
    def update_volunteer_status(self, volunteer_id: str, new_status: str) -> bool:
        """Update a volunteer's status.
        
        Args:
            volunteer_id: ID of the volunteer to update.
            new_status: New status ('active', 'inactive', etc.)
            
        Returns:
            True if update was successful, False otherwise.
        """
        updated = False
        temp_file = f"{self.data_file}.tmp"
        
        try:
            with open(self.data_file, 'r') as infile, open(temp_file, 'w', newline='') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=self.fieldnames)
                writer.writeheader()
                
                for row in reader:
                    if row['id'] == volunteer_id:
                        row['status'] = new_status
                        updated = True
                    writer.writerow(row)
            
            if updated:
                os.replace(temp_file, self.data_file)
            else:
                os.remove(temp_file)
                
        except Exception as e:
            if os.path.exists(temp_file):
                os.remove(temp_file)
            raise IOError(f"Failed to update volunteer status: {str(e)}")
        
        return updated
    
    def search_volunteers(
        self,
        skill: Optional[str] = None,
        availability: Optional[str] = None,
        name: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """Search volunteers by skill, availability, or name.
        
        Args:
            skill: Skill to search for.
            availability: Availability to search for.
            name: Name to search for (partial match).
            
        Returns:
            List of matching volunteers.
        """
        volunteers = self.get_volunteers(status='active')
        results = []
        
        for volunteer in volunteers:
            match = True
            
            if skill and skill.lower() not in volunteer['skills'].lower():
                match = False
                
            if availability and availability.lower() not in volunteer['availability'].lower():
                match = False
                
            if name and name.lower() not in f"{volunteer['first_name']} {volunteer['last_name']}".lower():
                match = False
                
            if match:
                results.append(volunteer)
        
        return results

# Example usage
if __name__ == "__main__":
    registration = VolunteerRegistration()
    
    # Register a new volunteer
    try:
        new_volunteer = registration.register_volunteer(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="555-123-4567",
            skills=["teaching", "cooking"],
            availability=["weekends", "evenings"]
        )
        print(f"Registered volunteer: {new_volunteer['id']}")
    except Exception as e:
        print(f"Registration failed: {str(e)}")
    
    # List all active volunteers
    active_volunteers = registration.get_volunteers(status='active')
    print(f"\nActive volunteers: {len(active_volunteers)}")
    
    # Search for volunteers with specific skills
    teachers = registration.search_volunteers(skill="teaching")
    print(f"\nVolunteers with teaching skills: {len(teachers)}")
```
