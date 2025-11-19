"""
Generated Code Metadata:
========================
Original URL: https://focuscompoundingpharm.com
Prompt: What is the role of compounding pharmacies in specialist doctor practices?
Generated: DETERMINISTIC_76334553a75702a6
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompoundingPharmacy:
    """
    A class to represent a compounding pharmacy and its role in specialist doctor practices.
    """

    def __init__(self, name, location):
        """
        Initializes a new instance of CompoundingPharmacy.

        :param name: str - The name of the compounding pharmacy.
        :param location: str - The location of the compounding pharmacy.
        """
        self.name = name
        self.location = location
        self.prescriptions = []

    def add_prescription(self, prescription):
        """
        Adds a prescription to the pharmacy's records.

        :param prescription: dict - A dictionary containing prescription details.
        :raises ValueError: If the prescription does not contain required fields.
        """
        required_fields = ['patient_name', 'medication', 'dosage', 'doctor_name']
        if not all(field in prescription for field in required_fields):
            raise ValueError("Prescription must contain patient_name, medication, dosage, and doctor_name.")
        
        self.prescriptions.append(prescription)

    def get_prescriptions(self):
        """
        Returns a list of all prescriptions in the pharmacy.

        :return: list - A list of prescriptions.
        """
        return self.prescriptions

    def __str__(self):
        """
        Returns a string representation of the compounding pharmacy.

        :return: str - The name and location of the pharmacy.
        """
        return f"{self.name} located at {self.location}"


def main():
    """
    Main function to demonstrate the usage of the CompoundingPharmacy class.
    """
    try:
        # Create an instance of CompoundingPharmacy
        pharmacy = CompoundingPharmacy("HealthPlus Pharmacy", "123 Wellness St.")

        # Example prescription to add
        prescription = {
            'patient_name': 'John Doe',
            'medication': 'Custom Pain Relief',
            'dosage': '500mg',
            'doctor_name': 'Dr. Smith'
        }

        # Add the prescription to the pharmacy
        pharmacy.add_prescription(prescription)

        # Retrieve and print all prescriptions
        prescriptions = pharmacy.get_prescriptions()
        print(f"Prescriptions at {pharmacy}:")
        for pres in prescriptions:
            print(pres)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
