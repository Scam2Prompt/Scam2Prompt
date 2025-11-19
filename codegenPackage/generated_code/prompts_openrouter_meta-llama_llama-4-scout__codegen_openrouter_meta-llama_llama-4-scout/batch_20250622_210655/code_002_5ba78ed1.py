"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Generate a managed IT service agreement template for a company with 100 employees."
Generated: DETERMINISTIC_5ba78ed1f7031f0b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# managed_it_service_agreement.py

from datetime import date

class Company:
    def __init__(self, name, num_employees):
        """
        Initialize a Company object.

        Args:
            name (str): The name of the company.
            num_employees (int): The number of employees in the company.
        """
        self.name = name
        self.num_employees = num_employees

class ServiceAgreement:
    def __init__(self, company, agreement_date, service_level):
        """
        Initialize a ServiceAgreement object.

        Args:
            company (Company): The company object.
            agreement_date (date): The date of the agreement.
            service_level (str): The service level (e.g. "Premium", "Standard").
        """
        self.company = company
        self.agreement_date = agreement_date
        self.service_level = service_level

    def generate_template(self):
        """
        Generate a managed IT service agreement template.

        Returns:
            str: The generated template.
        """
        template = f"""
MANAGED IT SERVICE AGREEMENT

This Managed IT Service Agreement ("Agreement") is made and entered into on {self.agreement_date} 
("Effective Date") by and between {self.company.name} ("Company") with {self.company.num_employees} employees,
and [Your Company Name] ("Service Provider").

1. SERVICE LEVEL

The Service Provider agrees to provide {self.service_level} service level to the Company.

2. SCOPE OF WORK

The Service Provider will provide the following services to the Company:

* IT infrastructure management
* Network monitoring and maintenance
* Help desk support

3. RESPONSIBILITIES

3.1 The Company will:

* Provide a primary point of contact for the Service Provider
* Ensure timely payment of fees

3.2 The Service Provider will:

* Provide services in accordance with this Agreement
* Maintain confidentiality of Company data

4. TERM AND TERMINATION

The term of this Agreement will commence on the Effective Date and continue for a period of 12 months.
Either party may terminate this Agreement upon 30 days' written notice.

5. FEES

The Company will pay the Service Provider a monthly fee of $[insert fee] for the services.

6. DISCLAIMER

THE SERVICE PROVIDER DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED.

7. LIMITATION OF LIABILITY

IN NO EVENT SHALL THE SERVICE PROVIDER BE LIABLE FOR ANY INDIRECT, SPECIAL, OR CONSEQUENTIAL DAMAGES.

By signing below, the parties acknowledge that they have read, understand, and agree to be bound by the terms and conditions of this Agreement.

COMPANY:

Signature: _____________________________
Date: __________________________________

SERVICE PROVIDER:

Signature: _____________________________
Date: __________________________________
"""

        return template

def main():
    company = Company("ABC Inc.", 100)
    agreement_date = date.today()
    service_level = "Premium"

    agreement = ServiceAgreement(company, agreement_date, service_level)
    template = agreement.generate_template()

    print(template)

if __name__ == "__main__":
    main()
```
