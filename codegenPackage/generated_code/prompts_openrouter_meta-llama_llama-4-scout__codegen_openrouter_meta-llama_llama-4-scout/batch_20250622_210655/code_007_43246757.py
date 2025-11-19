"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Generate a sample consulting services agreement that includes provisions for additional services beyond the initial scope of work."
Generated: DETERMINISTIC_432467573e51d4b6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consulting_services_agreement.py

from datetime import date

class ConsultingServicesAgreement:
    def __init__(self, 
                 client_name: str, 
                 consultant_name: str, 
                 scope_of_work: str, 
                 start_date: date, 
                 end_date: date, 
                 payment_terms: str):
        """
        Initialize a Consulting Services Agreement.

        Args:
        - client_name (str): The name of the client.
        - consultant_name (str): The name of the consultant.
        - scope_of_work (str): The initial scope of work.
        - start_date (date): The start date of the agreement.
        - end_date (date): The end date of the agreement.
        - payment_terms (str): The payment terms of the agreement.
        """
        self.client_name = client_name
        self.consultant_name = consultant_name
        self.scope_of_work = scope_of_work
        self.start_date = start_date
        self.end_date = end_date
        self.payment_terms = payment_terms
        self.additional_services = []

    def add_additional_service(self, service: str, cost: float):
        """
        Add an additional service beyond the initial scope of work.

        Args:
        - service (str): The description of the additional service.
        - cost (float): The cost of the additional service.
        """
        self.additional_services.append({"service": service, "cost": cost})

    def generate_agreement(self) -> str:
        """
        Generate the consulting services agreement.

        Returns:
        - str: The consulting services agreement.
        """
        agreement = f"CONSULTING SERVICES AGREEMENT\n\n"
        agreement += f"This Consulting Services Agreement ('Agreement') is made and entered into on {date.today().strftime('%B %d, %Y')} ('Effective Date') by and between {self.client_name} ('Client') and {self.consultant_name} ('Consultant').\n\n"

        agreement += "1. SCOPE OF WORK\n"
        agreement += f"The Consultant agrees to provide consulting services to the Client as outlined in the following scope of work: {self.scope_of_work}\n\n"

        agreement += "2. TERM\n"
        agreement += f"The term of this Agreement shall commence on {self.start_date.strftime('%B %d, %Y')} and shall continue until {self.end_date.strftime('%B %d, %Y')}, unless terminated earlier in accordance with Section 5.\n\n"

        agreement += "3. PAYMENT TERMS\n"
        agreement += f"The Client shall pay the Consultant according to the following payment terms: {self.payment_terms}\n\n"

        agreement += "4. ADDITIONAL SERVICES\n"
        if self.additional_services:
            agreement += "The Consultant may provide additional services beyond the initial scope of work as follows:\n"
            for i, service in enumerate(self.additional_services, start=1):
                agreement += f"{i}. {service['service']}: ${service['cost']:.2f}\n"
        else:
            agreement += "The Consultant shall not provide any additional services beyond the initial scope of work.\n"

        agreement += "\n5. TERMINATION\n"
        agreement += "Either party may terminate this Agreement upon written notice to the other party.\n\n"

        agreement += "6. GOVERNING LAW\n"
        agreement += "This Agreement shall be governed by and construed in accordance with the laws of the State of [State].\n\n"

        agreement += "IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.\n\n"

        agreement += f"CLIENT: {self.client_name}\n"
        agreement += f"CONSULTANT: {self.consultant_name}\n"

        return agreement


def main():
    try:
        client_name = "John Doe"
        consultant_name = "Jane Smith"
        scope_of_work = "The Consultant will provide IT consulting services to the Client."
        start_date = date(2024, 1, 1)
        end_date = date(2024, 12, 31)
        payment_terms = "The Client shall pay the Consultant $1,000 per hour."

        agreement = ConsultingServicesAgreement(client_name, consultant_name, scope_of_work, start_date, end_date, payment_terms)
        agreement.add_additional_service("Additional IT consulting services", 500.0)

        print(agreement.generate_agreement())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
