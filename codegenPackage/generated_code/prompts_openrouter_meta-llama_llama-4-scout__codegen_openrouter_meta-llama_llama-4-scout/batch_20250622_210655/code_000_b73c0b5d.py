"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Generate a Python script to manage certification programs for a training institute like Geta Consulenze, including tracking course completion and certification expiry dates."
Generated: DETERMINISTIC_b73c0b5d97ad2b26
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List

class CertificationProgram:
    def __init__(self, name: str, duration: int, expiry_date: int):
        """
        Initialize a certification program.

        Args:
        - name (str): Name of the certification program.
        - duration (int): Duration of the certification program in months.
        - expiry_date (int): Expiry date of the certification in months.
        """
        self.name = name
        self.duration = duration
        self.expiry_date = expiry_date
        self.certificate_holders: Dict[str, datetime.date] = {}

    def add_certificate_holder(self, participant_id: str, completion_date: datetime.date):
        """
        Add a certificate holder to the program.

        Args:
        - participant_id (str): ID of the participant.
        - completion_date (datetime.date): Date of completion of the program.
        """
        self.certificate_holders[participant_id] = completion_date

    def get_expiry_date(self, participant_id: str) -> datetime.date:
        """
        Get the expiry date of a certificate holder.

        Args:
        - participant_id (str): ID of the participant.

        Returns:
        - datetime.date: Expiry date of the certificate.

        Raises:
        - ValueError: If participant ID is not found.
        """
        if participant_id not in self.certificate_holders:
            raise ValueError("Participant ID not found")

        completion_date = self.certificate_holders[participant_id]
        expiry_date = completion_date + datetime.timedelta(days=self.expiry_date * 30)
        return expiry_date

    def get_certificate_status(self, participant_id: str) -> str:
        """
        Get the certificate status of a participant.

        Args:
        - participant_id (str): ID of the participant.

        Returns:
        - str: Status of the certificate (active/inactive).

        Raises:
        - ValueError: If participant ID is not found.
        """
        if participant_id not in self.certificate_holders:
            raise ValueError("Participant ID not found")

        expiry_date = self.get_expiry_date(participant_id)
        if expiry_date < datetime.date.today():
            return "inactive"
        else:
            return "active"


class TrainingInstitute:
    def __init__(self):
        """
        Initialize a training institute.
        """
        self.programs: Dict[str, CertificationProgram] = {}

    def add_program(self, program: CertificationProgram):
        """
        Add a certification program to the institute.

        Args:
        - program (CertificationProgram): Certification program to add.
        """
        self.programs[program.name] = program

    def get_program(self, program_name: str) -> CertificationProgram:
        """
        Get a certification program by name.

        Args:
        - program_name (str): Name of the program.

        Returns:
        - CertificationProgram: Certification program.

        Raises:
        - ValueError: If program name is not found.
        """
        if program_name not in self.programs:
            raise ValueError("Program name not found")

        return self.programs[program_name]


def main():
    institute = TrainingInstitute()

    # Create a certification program
    program = CertificationProgram("Python Developer", 3, 12)
    institute.add_program(program)

    # Add certificate holders
    program.add_certificate_holder("P001", datetime.date(2022, 1, 1))
    program.add_certificate_holder("P002", datetime.date(2022, 6, 1))

    # Get expiry dates
    print("Expiry Date for P001:", program.get_expiry_date("P001"))
    print("Expiry Date for P002:", program.get_expiry_date("P002"))

    # Get certificate status
    print("Certificate Status for P001:", program.get_certificate_status("P001"))
    print("Certificate Status for P002:", program.get_certificate_status("P002"))


if __name__ == "__main__":
    main()
```
