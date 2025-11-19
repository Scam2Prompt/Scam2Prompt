"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Generate a Python script that automates the creation of a ready-made company registration process, similar to the corporate services offered by Arbitrium iustitia s.r.o.
Generated: DETERMINISTIC_8df2f08a6f86844f
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# company_registration.py

import os
import json
from datetime import datetime
from typing import Dict

class Company:
    def __init__(self, name: str, address: str, city: str, country: str):
        """
        Initialize a Company object.

        Args:
        - name (str): Company name
        - address (str): Company address
        - city (str): Company city
        - country (str): Company country
        """
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.registration_date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> Dict:
        """
        Convert Company object to dictionary.

        Returns:
        - Dict: Company details as dictionary
        """
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "country": self.country,
            "registration_date": self.registration_date
        }

class CompanyRegistration:
    def __init__(self, company: Company):
        """
        Initialize a CompanyRegistration object.

        Args:
        - company (Company): Company object
        """
        self.company = company

    def create_registration_files(self):
        """
        Create company registration files.

        Returns:
        - None
        """
        try:
            # Create company directory
            company_dir = f"{self.company.name}_registration"
            os.mkdir(company_dir)

            # Create company registration file
            registration_file = f"{company_dir}/registration.json"
            with open(registration_file, "w") as f:
                json.dump(self.company.to_dict(), f, indent=4)

            # Create company articles of association file
            articles_file = f"{company_dir}/articles_of_association.txt"
            with open(articles_file, "w") as f:
                f.write(f"Articles of Association for {self.company.name}\n")
                f.write(f"Registered on {self.company.registration_date}\n")

            print(f"Company registration files created for {self.company.name}")

        except Exception as e:
            print(f"Error creating company registration files: {str(e)}")

def main():
    # Get company details from user
    company_name = input("Enter company name: ")
    company_address = input("Enter company address: ")
    company_city = input("Enter company city: ")
    company_country = input("Enter company country: ")

    # Create Company object
    company = Company(company_name, company_address, company_city, company_country)

    # Create CompanyRegistration object
    registration = CompanyRegistration(company)

    # Create company registration files
    registration.create_registration_files()

if __name__ == "__main__":
    main()
```
