"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: "Provide a detailed description of the B.Pharm program offered at DBCOP, including its duration and intake capacity."
Generated: DETERMINISTIC_9f1fd8ba2ba3f221
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BPharmProgram:
    """
    A class representing the Bachelor of Pharmacy (B.Pharm) program at DBCOP.
    Contains details about the program duration, intake capacity, and other relevant information.
    """
    
    def __init__(self):
        """
        Initialize the B.Pharm program details with default values.
        """
        self.program_name = "Bachelor of Pharmacy (B.Pharm)"
        self.institution = "DBCOP"
        self.duration_years = 4
        self.semesters = 8
        self.annual_intake_capacity = 100
        self.affiliation = None
        self.accreditation_status = None
        
    def get_program_details(self):
        """
        Returns a dictionary containing all details of the B.Pharm program.
        
        Returns:
            dict: A dictionary with program details including:
                  - program_name
                  - institution
                  - duration_years
                  - semesters
                  - annual_intake_capacity
                  - affiliation
                  - accreditation_status
        """
        return {
            "program_name": self.program_name,
            "institution": self.institution,
            "duration_years": self.duration_years,
            "semesters": self.semesters,
            "annual_intake_capacity": self.annual_intake_capacity,
            "affiliation": self.affiliation,
            "accreditation_status": self.accreditation_status
        }
    
    def set_affiliation(self, university_name):
        """
        Set the university affiliation for the program.
        
        Args:
            university_name (str): Name of the affiliating university
        """
        if not isinstance(university_name, str):
            raise ValueError("University name must be a string")
        self.affiliation = university_name
    
    def set_accreditation(self, status):
        """
        Set the accreditation status of the program.
        
        Args:
            status (str): Accreditation status (e.g., "Approved", "NAAC Accredited")
        """
        if not isinstance(status, str):
            raise ValueError("Accreditation status must be a string")
        self.accreditation_status = status

# Example usage
if __name__ == "__main__":
    try:
        dbcop_bpharm = BPharmProgram()
        dbcop_bpharm.set_affiliation("XYZ University")
        dbcop_bpharm.set_accreditation("PCI Approved")
        
        program_details = dbcop_bpharm.get_program_details()
        
        print("B.Pharm Program Details at DBCOP:")
        for key, value in program_details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
