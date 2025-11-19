"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Generate a sample contract for corporate services in Slovakia, including provisions for company formation, changes in company details, and dissolution of companies.
Generated: DETERMINISTIC_0c97ad56663fec6c
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date
from enum import Enum

class CompanyType(str, Enum):
    """Company types in Slovakia"""
    sro = "s.r.o."
    a_s = "a.s."

class Contract:
    """Sample contract for corporate services in Slovakia"""

    def __init__(self, company_name: str, company_type: CompanyType, 
                 registered_office: str, founder: str, 
                 contract_date: date = None):
        """
        Initialize the contract.

        Args:
        - company_name (str): Name of the company.
        - company_type (CompanyType): Type of the company.
        - registered_office (str): Registered office of the company.
        - founder (str): Founder of the company.
        - contract_date (date): Date of the contract. Defaults to today.
        """
        self.company_name = company_name
        self.company_type = company_type
        self.registered_office = registered_office
        self.founder = founder
        self.contract_date = contract_date if contract_date else date.today()
        self.company_formed = False

    def form_company(self):
        """Form the company"""
        if not self.company_formed:
            print(f"Company {self.company_name} of type {self.company_type.value} formed.")
            self.company_formed = True
        else:
            print(f"Company {self.company_name} already formed.")

    def change_company_details(self, new_name: str = None, new_registered_office: str = None):
        """
        Change company details.

        Args:
        - new_name (str): New name of the company.
        - new_registered_office (str): New registered office of the company.
        """
        if self.company_formed:
            if new_name:
                self.company_name = new_name
                print(f"Company name changed to {self.company_name}.")
            if new_registered_office:
                self.registered_office = new_registered_office
                print(f"Registered office changed to {self.registered_office}.")
        else:
            print("Company not formed yet.")

    def dissolve_company(self):
        """Dissolve the company"""
        if self.company_formed:
            print(f"Company {self.company_name} dissolved.")
            self.company_formed = False
        else:
            print(f"Company {self.company_name} not formed yet.")

    def generate_contract(self):
        """Generate the contract"""
        contract = f"""
        CONTRACT FOR CORPORATE SERVICES IN SLOVAKIA

        This Contract is made and entered into on {self.contract_date} by and between:

        FOUNDER: {self.founder}

        COMPANY: {self.company_name} of type {self.company_type.value}

        REGISTERED OFFICE: {self.registered_office}

        1. COMPANY FORMATION

        The Founder hereby appoints [CORPORATE SERVICES PROVIDER] to form a company in Slovakia.

        2. CHANGES IN COMPANY DETAILS

        The Founder hereby authorizes [CORPORATE SERVICES PROVIDER] to make changes to the company's details.

        3. DISSOLUTION OF COMPANY

        The Founder hereby authorizes [CORPORATE SERVICES PROVIDER] to dissolve the company.

        IN WITNESS WHEREOF, the parties have executed this Contract as of the date first above written.

        """
        return contract

def main():
    try:
        contract = Contract("Sample Company", CompanyType.sro, "Bratislava", "John Doe")
        print(contract.generate_contract())
        contract.form_company()
        contract.change_company_details("New Sample Company", "Košice")
        contract.dissolve_company()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
