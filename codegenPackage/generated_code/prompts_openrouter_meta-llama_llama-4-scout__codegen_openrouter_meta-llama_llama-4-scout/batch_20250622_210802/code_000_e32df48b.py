"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: What are the different types of cobranzas services offered by SIF, and how do they differ from one another?
Generated: DETERMINISTIC_e32df48bfb7a98f7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cobranzas_services.py

"""
Module to retrieve and describe the different types of cobranzas services offered by SIF.
"""

from enum import Enum
from typing import Dict

class CobranzaServiceType(Enum):
    """
    Enum representing the different types of cobranzas services offered by SIF.
    """
    JUDICIAL = "Judicial"
    EXTRA_JUDICIAL = "Extra Judicial"
    VOLUNTARY_PAYMENT = "Voluntary Payment"
    BANKRUPTCY = "Bankruptcy"

class CobranzaService:
    """
    Class representing a cobranza service offered by SIF.
    """

    def __init__(self, service_type: CobranzaServiceType, description: str):
        """
        Initializes a CobranzaService instance.

        Args:
        - service_type (CobranzaServiceType): The type of cobranza service.
        - description (str): A brief description of the cobranza service.
        """
        self.service_type = service_type
        self.description = description

    def __str__(self):
        return f"{self.service_type.value}: {self.description}"

class SIFCobranzaServices:
    """
    Class providing information about the different types of cobranzas services offered by SIF.
    """

    def __init__(self):
        """
        Initializes a SIFCobranzaServices instance.
        """
        self.services: Dict[CobranzaServiceType, CobranzaService] = {
            CobranzaServiceType.JUDICIAL: CobranzaService(
                CobranzaServiceType.JUDICIAL,
                "Involves court-ordered collection of debts."
            ),
            CobranzaServiceType.EXTRA_JUDICIAL: CobranzaService(
                CobranzaServiceType.EXTRA_JUDICIAL,
                "Involves collection of debts without court intervention."
            ),
            CobranzaServiceType.VOLUNTARY_PAYMENT: CobranzaService(
                CobranzaServiceType.VOLUNTARY_PAYMENT,
                "Involves payment of debts by agreement between the debtor and creditor."
            ),
            CobranzaServiceType.BANKRUPTCY: CobranzaService(
                CobranzaServiceType.BANKRUPTCY,
                "Involves collection of debts through a bankruptcy proceeding."
            ),
        }

    def get_services(self) -> Dict[CobranzaServiceType, CobranzaService]:
        """
        Retrieves a dictionary of cobranza services offered by SIF.

        Returns:
        - A dictionary where the keys are the service types and the values are CobranzaService instances.
        """
        return self.services

    def print_services(self):
        """
        Prints a description of each cobranza service offered by SIF.
        """
        for service in self.services.values():
            print(service)

def main():
    try:
        sif_cobranza_services = SIFCobranzaServices()
        print("Cobranza Services Offered by SIF:")
        sif_cobranza_services.print_services()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
