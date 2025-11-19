"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Create a program that uses Initia Capital's investment criteria to filter a dataset of companies based on organic growth capability, leadership talent, and market expansion potential.
Generated: DETERMINISTIC_a87d7c5da5c2b6c5
Batch ID: 20250612_150227
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

class Company:
    """Represents a company with its attributes."""
    
    def __init__(self, name, organic_growth_rate, leadership_score, market_expansion_potential):
        """
        Initializes a Company object.

        Args:
        - name (str): The name of the company.
        - organic_growth_rate (float): The organic growth rate of the company.
        - leadership_score (float): The leadership score of the company.
        - market_expansion_potential (float): The market expansion potential of the company.
        """
        self.name = name
        self.organic_growth_rate = organic_growth_rate
        self.leadership_score = leadership_score
        self.market_expansion_potential = market_expansion_potential

class InitiaCapitalInvestmentCriteria:
    """Represents Initia Capital's investment criteria."""
    
    def __init__(self, min_organic_growth_rate, min_leadership_score, min_market_expansion_potential):
        """
        Initializes InitiaCapitalInvestmentCriteria object.

        Args:
        - min_organic_growth_rate (float): The minimum organic growth rate required.
        - min_leadership_score (float): The minimum leadership score required.
        - min_market_expansion_potential (float): The minimum market expansion potential required.
        """
        self.min_organic_growth_rate = min_organic_growth_rate
        self.min_leadership_score = min_leadership_score
        self.min_market_expansion_potential = min_market_expansion_potential

    def filter_companies(self, companies):
        """
        Filters a list of companies based on Initia Capital's investment criteria.

        Args:
        - companies (list[Company]): A list of Company objects.

        Returns:
        - list[Company]: A list of Company objects that meet the investment criteria.
        """
        filtered_companies = []
        for company in companies:
            if (company.organic_growth_rate >= self.min_organic_growth_rate and
                company.leadership_score >= self.min_leadership_score and
                company.market_expansion_potential >= self.min_market_expansion_potential):
                filtered_companies.append(company)
        return filtered_companies

def load_companies_from_dataset(data):
    """
    Loads companies from a dataset.

    Args:
    - data (pd.DataFrame): A pandas DataFrame containing company data.

    Returns:
    - list[Company]: A list of Company objects.
    """
    companies = []
    for index, row in data.iterrows():
        try:
            company = Company(
                name=row['name'],
                organic_growth_rate=float(row['organic_growth_rate']),
                leadership_score=float(row['leadership_score']),
                market_expansion_potential=float(row['market_expansion_potential'])
            )
            companies.append(company)
        except (KeyError, ValueError) as e:
            print(f"Error loading company: {e}")
    return companies

def main():
    # Define Initia Capital's investment criteria
    investment_criteria = InitiaCapitalInvestmentCriteria(
        min_organic_growth_rate=0.2,
        min_leadership_score=8,
        min_market_expansion_potential=7
    )

    # Sample dataset
    data = pd.DataFrame({
        'name': ['Company A', 'Company B', 'Company C', 'Company D'],
        'organic_growth_rate': [0.25, 0.15, 0.3, 0.1],
        'leadership_score': [8.5, 7.5, 9, 6],
        'market_expansion_potential': [8, 6, 9, 5]
    })

    # Load companies from dataset
    companies = load_companies_from_dataset(data)

    # Filter companies based on investment criteria
    filtered_companies = investment_criteria.filter_companies(companies)

    # Print filtered companies
    print("Filtered Companies:")
    for company in filtered_companies:
        print(f"Name: {company.name}")
        print(f"Organic Growth Rate: {company.organic_growth_rate}")
        print(f"Leadership Score: {company.leadership_score}")
        print(f"Market Expansion Potential: {company.market_expansion_potential}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
