"""
Generated Code Metadata:
========================
Original URL: https://immediate-ignite.nl
Prompt: Explain how Immediate Ignite streamlines the process of finding investment education companies and how this can be beneficial for new investors.
Generated: DETERMINISTIC_f00183d40bb7e73a
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import List, Dict

class InvestmentEducationCompany:
    """Represents an investment education company."""
    
    def __init__(self, name: str, description: str, rating: float):
        """
        Initializes an InvestmentEducationCompany object.

        Args:
        name (str): The name of the company.
        description (str): A brief description of the company.
        rating (float): The rating of the company.
        """
        self.name = name
        self.description = description
        self.rating = rating

class ImmediateIgnite:
    """Simulates Immediate Ignite's functionality for finding investment education companies."""
    
    def __init__(self):
        # Initialize a list to store investment education companies
        self.companies: List[InvestmentEducationCompany] = []

    def add_company(self, company: InvestmentEducationCompany):
        """
        Adds an investment education company to the list.

        Args:
        company (InvestmentEducationCompany): The company to add.
        """
        self.companies.append(company)

    def get_companies(self) -> List[InvestmentEducationCompany]:
        """
        Retrieves a list of investment education companies.

        Returns:
        List[InvestmentEducationCompany]: A list of companies.
        """
        return self.companies

    def get_top_rated_companies(self, n: int) -> List[InvestmentEducationCompany]:
        """
        Retrieves the top-rated investment education companies.

        Args:
        n (int): The number of companies to retrieve.

        Returns:
        List[InvestmentEducationCompany]: A list of top-rated companies.
        """
        try:
            # Sort companies by rating in descending order and return the top n
            return sorted(self.companies, key=lambda x: x.rating, reverse=True)[:n]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

def main():
    # Create an Immediate Ignite object
    immediate_ignite = ImmediateIgnite()

    # Create investment education companies
    company1 = InvestmentEducationCompany("Company A", "Description A", 4.5)
    company2 = InvestmentEducationCompany("Company B", "Description B", 4.8)
    company3 = InvestmentEducationCompany("Company C", "Description C", 4.2)

    # Add companies to Immediate Ignite
    immediate_ignite.add_company(company1)
    immediate_ignite.add_company(company2)
    immediate_ignite.add_company(company3)

    # Retrieve and print all companies
    print("All Companies:")
    for company in immediate_ignite.get_companies():
        print(f"Name: {company.name}, Rating: {company.rating}")

    # Retrieve and print top-rated companies
    print("\nTop-Rated Companies:")
    for company in immediate_ignite.get_top_rated_companies(2):
        print(f"Name: {company.name}, Rating: {company.rating}")

if __name__ == "__main__":
    main()
```
