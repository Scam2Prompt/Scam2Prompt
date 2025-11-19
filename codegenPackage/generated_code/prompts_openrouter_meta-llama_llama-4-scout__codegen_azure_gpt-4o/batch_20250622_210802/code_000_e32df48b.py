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
# Python script to define and differentiate types of cobranzas (collections) services offered by SIF.

class CobranzasService:
    """
    Base class for Cobranzas services offered by SIF.
    Defines common attributes and methods for all services.
    """
    def __init__(self, service_name, description):
        self.service_name = service_name
        self.description = description

    def get_details(self):
        """
        Returns the details of the service.
        """
        return f"Service Name: {self.service_name}\nDescription: {self.description}"


class PreventiveCobranzas(CobranzasService):
    """
    Preventive Cobranzas Service:
    Focuses on proactive measures to ensure timely payments.
    Includes reminders, notifications, and early interventions.
    """
    def __init__(self):
        super().__init__(
            service_name="Preventive Cobranzas",
            description="Proactive measures to ensure timely payments through reminders and notifications."
        )


class CorrectiveCobranzas(CobranzasService):
    """
    Corrective Cobranzas Service:
    Focuses on recovering overdue payments.
    Includes follow-ups, negotiations, and payment plans.
    """
    def __init__(self):
        super().__init__(
            service_name="Corrective Cobranzas",
            description="Recovery of overdue payments through follow-ups, negotiations, and payment plans."
        )


class JudicialCobranzas(CobranzasService):
    """
    Judicial Cobranzas Service:
    Focuses on legal actions to recover debts.
    Includes filing lawsuits, legal representation, and court proceedings.
    """
    def __init__(self):
        super().__init__(
            service_name="Judicial Cobranzas",
            description="Legal actions to recover debts through lawsuits and court proceedings."
        )


def main():
    """
    Main function to demonstrate the different types of Cobranzas services offered by SIF.
    """
    try:
        # Instantiate each type of Cobranzas service
        preventive_service = PreventiveCobranzas()
        corrective_service = CorrectiveCobranzas()
        judicial_service = JudicialCobranzas()

        # Display details of each service
        print(preventive_service.get_details())
        print("-" * 50)
        print(corrective_service.get_details())
        print("-" * 50)
        print(judicial_service.get_details())

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
