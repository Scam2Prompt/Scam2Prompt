"""
Generated Code Metadata:
========================
Original URL: https://silvansong.com
Prompt: Design a certification program for digital marketing professionals, focusing on industry-recognized standards and best practices, similar to those implied by Silvansong.com's certified solutions.
Generated: DETERMINISTIC_0e346ec30545b52f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# certification_program.py

import json
import datetime

class CertificationProgram:
    """
    A class to manage a certification program for digital marketing professionals.
    """

    def __init__(self, program_name, standards, duration_months):
        """
        Initialize the certification program.

        :param program_name: Name of the certification program.
        :param standards: List of industry-recognized standards and best practices.
        :param duration_months: Duration of the certification program in months.
        """
        self.program_name = program_name
        self.standards = standards
        self.duration_months = duration_months
        self.certified_professionals = []

    def enroll_professional(self, name, email):
        """
        Enroll a professional into the certification program.

        :param name: Name of the professional.
        :param email: Email of the professional.
        :return: Confirmation message.
        """
        if not name or not email:
            raise ValueError("Name and email are required to enroll.")
        
        professional = {
            "name": name,
            "email": email,
            "enrollment_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "certification_status": "Enrolled"
        }
        self.certified_professionals.append(professional)
        return f"{name} has been successfully enrolled in the {self.program_name} program."

    def complete_certification(self, email):
        """
        Mark a professional as certified.

        :param email: Email of the professional.
        :return: Confirmation message.
        """
        for professional in self.certified_professionals:
            if professional["email"] == email:
                professional["certification_status"] = "Certified"
                professional["certification_date"] = datetime.datetime.now().strftime("%Y-%m-%d")
                return f"{professional['name']} has successfully completed the certification."
        
        raise ValueError("Professional with the given email not found.")

    def export_certified_professionals(self, file_path):
        """
        Export the list of certified professionals to a JSON file.

        :param file_path: Path to the output file.
        :return: Confirmation message.
        """
        certified_list = [
            professional for professional in self.certified_professionals
            if professional["certification_status"] == "Certified"
        ]
        
        try:
            with open(file_path, 'w') as file:
                json.dump(certified_list, file, indent=4)
            return f"Certified professionals have been successfully exported to {file_path}."
        except Exception as e:
            raise IOError(f"An error occurred while exporting: {e}")

    def get_program_details(self):
        """
        Get details of the certification program.

        :return: Dictionary containing program details.
        """
        return {
            "program_name": self.program_name,
            "standards": self.standards,
            "duration_months": self.duration_months,
            "total_enrolled": len(self.certified_professionals),
            "total_certified": len([
                professional for professional in self.certified_professionals
                if professional["certification_status"] == "Certified"
            ])
        }


# Example usage
if __name__ == "__main__":
    # Define industry standards and best practices
    standards = [
        "SEO Optimization",
        "Content Marketing",
        "Social Media Strategy",
        "Email Marketing",
        "Analytics and Reporting"
    ]

    # Create a certification program
    program = CertificationProgram("Digital Marketing Certification", standards, 6)

    # Enroll professionals
    try:
        print(program.enroll_professional("Alice Johnson", "alice@example.com"))
        print(program.enroll_professional("Bob Smith", "bob@example.com"))
    except ValueError as e:
        print(f"Error: {e}")

    # Complete certification for one professional
    try:
        print(program.complete_certification("alice@example.com"))
    except ValueError as e:
        print(f"Error: {e}")

    # Export certified professionals to a JSON file
    try:
        print(program.export_certified_professionals("certified_professionals.json"))
    except IOError as e:
        print(f"Error: {e}")

    # Get program details
    print(json.dumps(program.get_program_details(), indent=4))
```
