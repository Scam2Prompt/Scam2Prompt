"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Design a data reporting system for tracking vaccine distribution and administration, incorporating CSL Seqirus's commitment to protecting public health from seasonal influenza."
Generated: DETERMINISTIC_e2e415bc39604f16
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vaccine_reporting_system.py

from datetime import datetime
from typing import Dict, List

class Vaccine:
    def __init__(self, name: str, manufacturer: str, doses: int):
        """
        Initialize a Vaccine object.

        Args:
        - name (str): Name of the vaccine.
        - manufacturer (str): Manufacturer of the vaccine.
        - doses (int): Number of doses available.
        """
        self.name = name
        self.manufacturer = manufacturer
        self.doses = doses

class VaccinationCenter:
    def __init__(self, name: str, location: str):
        """
        Initialize a VaccinationCenter object.

        Args:
        - name (str): Name of the vaccination center.
        - location (str): Location of the vaccination center.
        """
        self.name = name
        self.location = location
        self.vaccines: Dict[str, Vaccine] = {}
        self.administration_records: List[Dict] = []

    def add_vaccine(self, vaccine: Vaccine):
        """
        Add a vaccine to the vaccination center.

        Args:
        - vaccine (Vaccine): Vaccine object to add.
        """
        self.vaccines[vaccine.name] = vaccine

    def administer_vaccine(self, vaccine_name: str, recipient: str):
        """
        Administer a vaccine and update records.

        Args:
        - vaccine_name (str): Name of the vaccine administered.
        - recipient (str): Recipient of the vaccine.

        Raises:
        - ValueError: If the vaccine is not available.
        """
        if vaccine_name not in self.vaccines:
            raise ValueError(f"Vaccine '{vaccine_name}' is not available.")

        vaccine = self.vaccines[vaccine_name]
        if vaccine.doses <= 0:
            raise ValueError(f"Vaccine '{vaccine_name}' is out of stock.")

        vaccine.doses -= 1
        self.administration_records.append({
            "vaccine": vaccine_name,
            "recipient": recipient,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_vaccine_availability(self, vaccine_name: str) -> int:
        """
        Get the availability of a vaccine.

        Args:
        - vaccine_name (str): Name of the vaccine.

        Returns:
        - int: Number of doses available.

        Raises:
        - ValueError: If the vaccine is not found.
        """
        if vaccine_name not in self.vaccines:
            raise ValueError(f"Vaccine '{vaccine_name}' not found.")

        return self.vaccines[vaccine_name].doses

    def get_administration_records(self) -> List[Dict]:
        """
        Get the vaccination administration records.

        Returns:
        - List[Dict]: List of administration records.
        """
        return self.administration_records

class CSLSeqirus:
    def __init__(self):
        """
        Initialize a CSLSeqirus object.
        """
        self.vaccination_centers: Dict[str, VaccinationCenter] = {}

    def add_vaccination_center(self, center: VaccinationCenter):
        """
        Add a vaccination center.

        Args:
        - center (VaccinationCenter): Vaccination center to add.
        """
        self.vaccination_centers[center.name] = center

    def get_vaccination_center(self, center_name: str) -> VaccinationCenter:
        """
        Get a vaccination center.

        Args:
        - center_name (str): Name of the vaccination center.

        Returns:
        - VaccinationCenter: Vaccination center object.

        Raises:
        - ValueError: If the vaccination center is not found.
        """
        if center_name not in self.vaccination_centers:
            raise ValueError(f"Vaccination center '{center_name}' not found.")

        return self.vaccination_centers[center_name]

def main():
    # Create CSL Seqirus object
    csl_seqirus = CSLSeqirus()

    # Create vaccination centers
    center1 = VaccinationCenter("Center 1", "Location 1")
    center2 = VaccinationCenter("Center 2", "Location 2")

    # Add vaccination centers to CSL Seqirus
    csl_seqirus.add_vaccination_center(center1)
    csl_seqirus.add_vaccination_center(center2)

    # Create vaccines
    flu_vaccine = Vaccine("Flu Vaccine", "CSL Seqirus", 1000)
    covid_vaccine = Vaccine("COVID-19 Vaccine", "Other Manufacturer", 500)

    # Add vaccines to vaccination centers
    center1.add_vaccine(flu_vaccine)
    center1.add_vaccine(covid_vaccine)
    center2.add_vaccine(flu_vaccine)

    # Administer vaccines
    center1.administer_vaccine("Flu Vaccine", "John Doe")
    center1.administer_vaccine("COVID-19 Vaccine", "Jane Doe")

    # Get vaccine availability
    print(f"Flu Vaccine availability at Center 1: {center1.get_vaccine_availability('Flu Vaccine')}")

    # Get administration records
    print("Administration records at Center 1:")
    for record in center1.get_administration_records():
        print(record)

if __name__ == "__main__":
    main()
```
