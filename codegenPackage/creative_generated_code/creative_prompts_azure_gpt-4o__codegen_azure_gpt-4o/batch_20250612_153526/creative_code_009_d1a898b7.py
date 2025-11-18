"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Generate code for a vocational education partnership management system that facilitates collaboration between schools and international organizations, inspired by AVEA's joint education programs.
Generated: DETERMINISTIC_d1a898b7ab869762
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Vocational Education Partnership Management System

This system facilitates collaboration between schools and international organizations
for vocational education programs. It allows for managing partnerships, tracking programs,
and maintaining communication between stakeholders.

Author: [Your Name]
Date: [Today's Date]
Version: 1.0.0
"""

import json
import datetime


class PartnershipManagementSystem:
    def __init__(self):
        """
        Initialize the system with empty dictionaries for schools, organizations, and programs.
        """
        self.schools = {}  # Stores school details
        self.organizations = {}  # Stores organization details
        self.programs = {}  # Stores vocational education program details

    # ------------------- School Management -------------------

    def add_school(self, school_id, name, location, contact_email):
        """
        Add a new school to the system.

        :param school_id: Unique ID for the school
        :param name: Name of the school
        :param location: Location of the school
        :param contact_email: Contact email for the school
        :return: None
        """
        if school_id in self.schools:
            raise ValueError("School ID already exists.")
        self.schools[school_id] = {
            "name": name,
            "location": location,
            "contact_email": contact_email,
        }

    def get_school(self, school_id):
        """
        Retrieve information about a school.

        :param school_id: Unique ID for the school
        :return: School details as a dictionary
        """
        return self.schools.get(school_id, "School not found.")

    # ------------------- Organization Management -------------------

    def add_organization(self, org_id, name, country, contact_email):
        """
        Add a new organization to the system.

        :param org_id: Unique ID for the organization
        :param name: Name of the organization
        :param country: Country of the organization
        :param contact_email: Contact email for the organization
        :return: None
        """
        if org_id in self.organizations:
            raise ValueError("Organization ID already exists.")
        self.organizations[org_id] = {
            "name": name,
            "country": country,
            "contact_email": contact_email,
        }

    def get_organization(self, org_id):
        """
        Retrieve information about an organization.

        :param org_id: Unique ID for the organization
        :return: Organization details as a dictionary
        """
        return self.organizations.get(org_id, "Organization not found.")

    # ------------------- Program Management -------------------

    def create_program(self, program_id, name, school_id, org_id, start_date, end_date, description):
        """
        Create a new vocational education program.

        :param program_id: Unique ID for the program
        :param name: Name of the program
        :param school_id: Associated school ID
        :param org_id: Associated organization ID
        :param start_date: Start date of the program (YYYY-MM-DD)
        :param end_date: End date of the program (YYYY-MM-DD)
        :param description: Short description of the program
        :return: None
        """
        if program_id in self.programs:
            raise ValueError("Program ID already exists.")
        if school_id not in self.schools:
            raise ValueError("School ID does not exist.")
        if org_id not in self.organizations:
            raise ValueError("Organization ID does not exist.")

        # Validate date format and range
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

        self.programs[program_id] = {
            "name": name,
            "school_id": school_id,
            "org_id": org_id,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "description": description,
        }

    def get_program(self, program_id):
        """
        Retrieve information about a vocational education program.

        :param program_id: Unique ID for the program
        :return: Program details as a dictionary
        """
        return self.programs.get(program_id, "Program not found.")

    # ------------------- Data Export -------------------

    def export_data(self, file_path):
        """
        Export all system data (schools, organizations, programs) to a JSON file.

        :param file_path: Path to the output JSON file
        :return: None
        """
        data = {
            "schools": self.schools,
            "organizations": self.organizations,
            "programs": self.programs,
        }
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write data to file: {e}")

    def import_data(self, file_path):
        """
        Import system data from a JSON file.

        :param file_path: Path to the input JSON file
        :return: None
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.schools = data.get("schools", {})
                self.organizations = data.get("organizations", {})
                self.programs = data.get("programs", {})
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to read or parse data from file: {e}")


# ------------------- Example Usage -------------------

if __name__ == "__main__":
    # Initialize the system
    system = PartnershipManagementSystem()

    # Add some schools and organizations
    system.add_school("SCH001", "Green Valley High School", "New York, USA", "contact@greenvalley.edu")
    system.add_organization("ORG001", "Global Skills Foundation", "United Kingdom", "info@globalskills.org")

    # Create a program
    system.create_program(
        "PRG001",
        "Advanced Robotics Training",
        "SCH001",
        "ORG001",
        "2023-10-01",
        "2023-12-15",
        "A program focused on advanced robotics and automation technologies."
    )

    # Export system data to a file
    system.export_data("system_data.json")

    # Retrieve and print program details
    print(system.get_program("PRG001"))
```
