"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: Create a Python script to analyze user preferences and match them with the most suitable investment education companies, as described in Trade GPT's functionality.
Generated: DETERMINISTIC_10728e1fd3a31779
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_matcher.py

import pandas as pd
from typing import Dict, List

class InvestmentEducationCompany:
    """Represents an investment education company."""

    def __init__(self, name: str, description: str, topics: List[str]):
        """
        Initializes an InvestmentEducationCompany.

        Args:
        - name (str): The company's name.
        - description (str): A brief description of the company.
        - topics (List[str]): The topics the company covers.
        """
        self.name = name
        self.description = description
        self.topics = topics

class UserPreference:
    """Represents a user's preferences."""

    def __init__(self, topics: List[str], risk_tolerance: str, investment_goal: str):
        """
        Initializes a UserPreference.

        Args:
        - topics (List[str]): The topics the user is interested in.
        - risk_tolerance (str): The user's risk tolerance (e.g., conservative, moderate, aggressive).
        - investment_goal (str): The user's investment goal (e.g., short-term, long-term).
        """
        self.topics = topics
        self.risk_tolerance = risk_tolerance
        self.investment_goal = investment_goal

class InvestmentMatcher:
    """Matches user preferences with investment education companies."""

    def __init__(self, companies: List[InvestmentEducationCompany]):
        """
        Initializes an InvestmentMatcher.

        Args:
        - companies (List[InvestmentEducationCompany]): A list of investment education companies.
        """
        self.companies = companies

    def match(self, user_preference: UserPreference) -> List[InvestmentEducationCompany]:
        """
        Matches a user's preferences with the most suitable investment education companies.

        Args:
        - user_preference (UserPreference): The user's preferences.

        Returns:
        - List[InvestmentEducationCompany]: A list of matching companies.
        """
        matching_companies = []
        for company in self.companies:
            # Check if the company covers the user's topics of interest
            topics_match = any(topic in company.topics for topic in user_preference.topics)
            # Check if the company's description mentions the user's risk tolerance
            risk_tolerance_match = user_preference.risk_tolerance.lower() in company.description.lower()
            # Check if the company's description mentions the user's investment goal
            investment_goal_match = user_preference.investment_goal.lower() in company.description.lower()
            # If all conditions are met, add the company to the list of matching companies
            if topics_match and risk_tolerance_match and investment_goal_match:
                matching_companies.append(company)
        return matching_companies

def load_companies() -> List[InvestmentEducationCompany]:
    """
    Loads a list of investment education companies from a CSV file.

    Returns:
    - List[InvestmentEducationCompany]: A list of investment education companies.
    """
    try:
        data = pd.read_csv('companies.csv')
        companies = []
        for index, row in data.iterrows():
            company = InvestmentEducationCompany(
                name=row['name'],
                description=row['description'],
                topics=row['topics'].split(',')
            )
            companies.append(company)
        return companies
    except FileNotFoundError:
        print("Error: The 'companies.csv' file was not found.")
        return []
    except pd.errors.EmptyDataError:
        print("Error: The 'companies.csv' file is empty.")
        return []
    except pd.errors.ParserError:
        print("Error: An error occurred while parsing the 'companies.csv' file.")
        return []

def main():
    # Load investment education companies from a CSV file
    companies = load_companies()

    # Create an InvestmentMatcher
    matcher = InvestmentMatcher(companies)

    # Define a user's preferences
    user_preference = UserPreference(
        topics=['stocks', 'bonds'],
        risk_tolerance='moderate',
        investment_goal='long-term'
    )

    # Match the user's preferences with investment education companies
    matching_companies = matcher.match(user_preference)

    # Print the matching companies
    if matching_companies:
        print("Matching Companies:")
        for company in matching_companies:
            print(f"- {company.name}: {company.description}")
    else:
        print("No matching companies found.")

if __name__ == '__main__':
    main()
```

**companies.csv**
```csv
name,description,topics
Company A,Offers stock and bond investment education for moderate risk tolerance and long-term goals.,stocks,bonds
Company B,Provides education on cryptocurrency and forex trading for aggressive risk tolerance.,cryptocurrency,forex
Company C,Offers education on stock and bond investing for conservative risk tolerance and short-term goals.,stocks,bonds
```
