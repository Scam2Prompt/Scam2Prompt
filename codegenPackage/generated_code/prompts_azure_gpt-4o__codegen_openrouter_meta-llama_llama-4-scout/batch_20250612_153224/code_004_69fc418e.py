"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Write code to generate a template for a Special Power of Attorney (SPA) for minors, as required by the Schengen Apostille service.
Generated: DETERMINISTIC_69fc418ebcf063a0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date
from typing import Optional

class SpecialPowerOfAttorney:
    def __init__(self, 
                 minor_name: str, 
                 minor_date_of_birth: str, 
                 parent_name: str, 
                 parent_id: str, 
                 attorney_name: str, 
                 attorney_id: str, 
                 scope_of_power: str, 
                 validity_period: str):
        """
        Initialize the Special Power of Attorney template.

        Args:
        - minor_name (str): The name of the minor.
        - minor_date_of_birth (str): The date of birth of the minor (DD/MM/YYYY).
        - parent_name (str): The name of the parent or guardian.
        - parent_id (str): The ID of the parent or guardian.
        - attorney_name (str): The name of the attorney.
        - attorney_id (str): The ID of the attorney.
        - scope_of_power (str): The scope of the power of attorney.
        - validity_period (str): The validity period of the power of attorney.
        """

        self.minor_name = minor_name
        self.minor_date_of_birth = minor_date_of_birth
        self.parent_name = parent_name
        self.parent_id = parent_id
        self.attorney_name = attorney_name
        self.attorney_id = attorney_id
        self.scope_of_power = scope_of_power
        self.validity_period = validity_period

    def generate_template(self) -> str:
        """
        Generate the Special Power of Attorney template.

        Returns:
        - str: The generated template.
        """

        today = date.today()
        formatted_date = today.strftime("%d/%m/%Y")

        template = f"""
SPECIAL POWER OF ATTORNEY FOR MINORS

I, {self.parent_name}, 
with ID {self.parent_id}, 
being the parent/guardian of {self.minor_name}, 
born on {self.minor_date_of_birth},

HEREBY APPOINT {self.attorney_name}, 
with ID {self.attorney_id}, 
as my attorney-in-fact to act on behalf of {self.minor_name} 
in matters related to {self.scope_of_power}.

This Special Power of Attorney is valid for a period of {self.validity_period} 
from {formatted_date}.

I hereby declare that I have not been deprived of my parental rights 
and that {self.minor_name} is under my care.

Signature of the parent/guardian: ______________________________

Date: {formatted_date}
"""

        return template


def main(minor_name: Optional[str] = None, 
         minor_date_of_birth: Optional[str] = None, 
         parent_name: Optional[str] = None, 
         parent_id: Optional[str] = None, 
         attorney_name: Optional[str] = None, 
         attorney_id: Optional[str] = None, 
         scope_of_power: Optional[str] = None, 
         validity_period: Optional[str] = None):
    try:
        if not all([minor_name, minor_date_of_birth, parent_name, parent_id, 
                     attorney_name, attorney_id, scope_of_power, validity_period]):
            raise ValueError("All fields are required.")

        spa = SpecialPowerOfAttorney(minor_name, minor_date_of_birth, 
                                     parent_name, parent_id, 
                                     attorney_name, attorney_id, 
                                     scope_of_power, validity_period)

        template = spa.generate_template()
        print(template)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main(minor_name="John Doe", 
          minor_date_of_birth="01/01/2010", 
          parent_name="Jane Doe", 
          parent_id="ID12345", 
          attorney_name="Bob Smith", 
          attorney_id="ID67890", 
          scope_of_power="travel and medical decisions", 
          validity_period="6 months")
```
