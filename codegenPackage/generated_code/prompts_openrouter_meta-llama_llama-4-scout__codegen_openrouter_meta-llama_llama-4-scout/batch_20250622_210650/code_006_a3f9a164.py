"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: What are the key factors that determine the price of a hair transplantation procedure at Clínica Harmonie, and how can a patient get a personalized quote?
Generated: DETERMINISTIC_a3f9a164fe73cdc0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hair_transplantation_pricing.py

class HairTransplantationProcedure:
    def __init__(self, num_grafts, technique, location, doctor_fee):
        """
        Initialize a HairTransplantationProcedure object.

        Args:
            num_grafts (int): The number of grafts required for the procedure.
            technique (str): The technique used for the procedure (e.g., FUT, FUE).
            location (str): The location of the clinic.
            doctor_fee (float): The doctor's fee for the procedure.
        """
        self.num_grafts = num_grafts
        self.technique = technique
        self.location = location
        self.doctor_fee = doctor_fee

    def calculate_price(self):
        """
        Calculate the price of the hair transplantation procedure.

        Returns:
            float: The total price of the procedure.
        """
        # Define the price per graft based on the technique
        if self.technique == "FUT":
            price_per_graft = 2.5
        elif self.technique == "FUE":
            price_per_graft = 3.5
        else:
            raise ValueError("Invalid technique")

        # Calculate the total price
        total_price = self.num_grafts * price_per_graft + self.doctor_fee

        return total_price


class ClinicaHarmonie:
    def __init__(self):
        """
        Initialize a ClinicaHarmonie object.
        """
        self.procedures = {}

    def add_procedure(self, procedure_id, num_grafts, technique, location, doctor_fee):
        """
        Add a hair transplantation procedure to the clinic's catalog.

        Args:
            procedure_id (str): The ID of the procedure.
            num_grafts (int): The number of grafts required for the procedure.
            technique (str): The technique used for the procedure (e.g., FUT, FUE).
            location (str): The location of the clinic.
            doctor_fee (float): The doctor's fee for the procedure.
        """
        procedure = HairTransplantationProcedure(num_grafts, technique, location, doctor_fee)
        self.procedures[procedure_id] = procedure

    def get_personalized_quote(self, procedure_id):
        """
        Get a personalized quote for a patient.

        Args:
            procedure_id (str): The ID of the procedure.

        Returns:
            float: The total price of the procedure.

        Raises:
            ValueError: If the procedure ID is not found.
        """
        if procedure_id not in self.procedures:
            raise ValueError("Procedure not found")

        procedure = self.procedures[procedure_id]
        price = procedure.calculate_price()

        return price


def main():
    # Create a ClinicaHarmonie object
    clinica_harmonie = ClinicaHarmonie()

    # Add procedures to the clinic's catalog
    clinica_harmonie.add_procedure("procedure1", 1000, "FUT", "New York", 1000.0)
    clinica_harmonie.add_procedure("procedure2", 2000, "FUE", "Los Angeles", 2000.0)

    # Get a personalized quote for a patient
    try:
        procedure_id = "procedure1"
        price = clinica_harmonie.get_personalized_quote(procedure_id)
        print(f"The price of procedure {procedure_id} is ${price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
