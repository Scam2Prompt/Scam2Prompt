"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Write a Python script to manage volunteer information for a local civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_3820ce944e5ae6a8
Batch ID: 20250622_210803
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
from typing import Dict, List, Optional

class VolunteerManager:
    """
    A class to manage volunteer information for a civil protection group.
    Handles adding, updating, searching, and reporting on volunteer data.
    """
    
    def __init__(self, data_file: str = "volunteers.csv"):
        """
        Initialize the VolunteerManager with a data file.
        
        Args:
            data_file: Path to the CSV file storing volunteer data.
        """
        self.data_file = data_file
        self.fieldnames = [
            'id', 'first_name', 'last_name', 'birth_date', 
            'phone', 'email', 'skills', 'availability', 
            'join_date', 'active'
        ]
        
        # Create data file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

    def _generate_id(self) -> str:
        """
        Generate a unique ID for a new volunteer.
        
        Returns:
            A string representing the new ID.
        """
        existing_ids = set()
        with open(self.data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_ids.add(row['id'])
        
        new_id = 1
        while str(new_id) in existing_ids:
            new_id += 1
            
        return str(new_id)

    def add_volunteer(self, volunteer_data: Dict) -> str:
        """
        Add a new volunteer to the system.
        
        Args:
            volunteer_data: Dictionary containing volunteer information.
            
        Returns:
            The ID of the newly added volunteer.
            
        Raises:
            ValueError: If required fields are missing.
        """
        required_fields = ['first_name', 'last_name', 'phone']
        for field in required_fields:
            if field not in volunteer_data or not volunteer_data[field]:
                raise ValueError(f"Missing required field: {field}")
        
        volunteer_data['id'] = self._generate_id()
        volunteer_data['join_date'] = datetime.now().strftime('%Y-%m-%d')
        volunteer_data['active'] = 'True'
        
        # Set default values for optional fields
        volunteer_data.setdefault('skills', '')
        volunteer_data.setdefault('availability', '')
        volunteer_data.setdefault('email', '')
        volunteer_data.setdefault('birth_date', '')
        
        with open(self.data_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(volunteer_data)
            
        return volunteer_data['id']

    def update_volunteer(self, volunteer_id: str, updated_data: Dict) -> bool:
        """
        Update information for an existing volunteer.
        
        Args:
            volunteer_id: ID of the volunteer to update.
            updated_data: Dictionary containing fields to update.
            
        Returns:
            True if update was successful, False if volunteer not found.
        """
        volunteers = []
        updated = False
        
        with open(self.data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] == volunteer_id:
                    for key, value in updated_data.items():
                        if key in self.fieldnames and key != 'id':
                            row[key] = value
                    updated = True
                volunteers.append(row)
        
        if updated:
            with open(self.data_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(volunteers)
                
        return updated

    def get_volunteer(self, volunteer_id: str) -> Optional[Dict]:
        """
        Retrieve a volunteer's information by ID.
        
        Args:
            volunteer_id: ID of the volunteer to retrieve.
            
        Returns:
            Dictionary with volunteer data or None if not found.
        """
        with open(self.data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] == volunteer_id:
                    return row
        return None

    def list_volunteers(self, active_only: bool = True) -> List[Dict]:
        """
        List all volunteers in the system.
        
        Args:
            active_only: If True, only return active volunteers.
            
        Returns:
            List of dictionaries containing volunteer data.
        """
        volunteers = []
        with open(self.data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not active_only or row['active'] == 'True':
                    volunteers.append(row)
        return volunteers

    def search_volunteers(self, search_term: str, field: str = 'last_name') -> List[Dict]:
        """
        Search for volunteers by a specific field.
        
        Args:
            search_term: Value to search for.
            field: Field to search in (default: 'last_name').
            
        Returns:
            List of matching volunteers.
            
        Raises:
            ValueError: If field is not valid.
        """
        if field not in self.fieldnames:
            raise ValueError(f"Invalid field: {field}")
            
        results = []
        with open(self.data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if search_term.lower() in row[field].lower():
                    results.append(row)
        return results

    def deactivate_volunteer(self, volunteer_id: str) -> bool:
        """
        Deactivate a volunteer (mark as inactive).
        
        Args:
            volunteer_id: ID of the volunteer to deactivate.
            
        Returns:
            True if deactivation was successful, False if volunteer not found.
        """
        return self.update_volunteer(volunteer_id, {'active': 'False'})

    def generate_report(self, report_type: str = 'active') -> str:
        """
        Generate a report of volunteers.
        
        Args:
            report_type: Type of report ('active', 'all', or 'skills').
            
        Returns:
            Formatted report string.
            
        Raises:
            ValueError: If report_type is invalid.
        """
        if report_type not in ['active', 'all', 'skills']:
            raise ValueError("Invalid report type. Must be 'active', 'all', or 'skills'")
            
        volunteers = self.list_volunteers(active_only=(report_type != 'all'))
        
        if report_type == 'skills':
            skills_report = {}
            for volunteer in volunteers:
                skills = volunteer['skills'].split(',') if volunteer['skills'] else []
                for skill in skills:
                    skill = skill.strip()
                    if skill:
                        if skill not in skills_report:
                            skills_report[skill] = 0
                        skills_report[skill] += 1
            
            report_lines = ["Skills Report:", "============="]
            for skill, count in sorted(skills_report.items()):
                report_lines.append(f"{skill}: {count} volunteers")
            return "\n".join(report_lines)
        else:
            report_lines = [
                f"{'Active' if report_type == 'active' else 'All'} Volunteers Report:",
                "=================================",
                f"{'ID':<5} {'Name':<25} {'Phone':<15} {'Skills'}"
            ]
            
            for volunteer in volunteers:
                name = f"{volunteer['first_name']} {volunteer['last_name']}"
                report_lines.append(
                    f"{volunteer['id']:<5} {name:<25} {volunteer['phone']:<15} {volunteer['skills']}"
                )
            
            return "\n".join(report_lines)

    def backup_data(self, backup_file: str = None) -> str:
        """
        Create a backup of the volunteer data.
        
        Args:
            backup_file: Path to save the backup. If None, generates a timestamped filename.
            
        Returns:
            Path to the backup file.
        """
        if backup_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = f"volunteers_backup_{timestamp}.csv"
            
        with open(self.data_file, 'r') as source, open(backup_file, 'w', newline='') as dest:
            dest.write(source.read())
            
        return backup_file


def main_menu():
    """
    Display a simple command-line interface for the volunteer manager.
    """
    manager = VolunteerManager()
    
    while True:
        print("\nCivil Protection Volunteer Management")
        print("====================================")
        print("1. Add new volunteer")
        print("2. Update volunteer information")
        print("3. View volunteer details")
        print("4. List all volunteers")
        print("5. Search volunteers")
        print("6. Deactivate volunteer")
        print("7. Generate report")
        print("8. Backup data")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                data = {
                    'first
