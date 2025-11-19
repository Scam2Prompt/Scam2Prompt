"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Write Python code to analyze investment opportunities in the TMT and financial sectors in Central and Eastern Europe, referencing Initia Capital's focus on disruptive technologies and innovation.
Generated: DETERMINISTIC_31b2001b77e4e965
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
import numpy as np
from typing import Dict, List

class InvestmentAnalyzer:
    """
    Analyzes investment opportunities in the TMT and financial sectors in Central and Eastern Europe.
    """

    def __init__(self, 
                 tmt_companies: List[Dict], 
                 financial_companies: List[Dict], 
                 innovation_threshold: float = 0.5):
        """
        Initializes the InvestmentAnalyzer.

        Args:
        - tmt_companies (List[Dict]): List of dictionaries containing TMT company data.
        - financial_companies (List[Dict]): List of dictionaries containing financial company data.
        - innovation_threshold (float): Threshold for innovation score (default: 0.5).
        """
        self.tmt_companies = tmt_companies
        self.financial_companies = financial_companies
        self.innovation_threshold = innovation_threshold

    def calculate_innovation_score(self, company: Dict) -> float:
        """
        Calculates the innovation score for a given company.

        Args:
        - company (Dict): Dictionary containing company data.

        Returns:
        - innovation_score (float): Innovation score.
        """
        # Assuming company data contains 'R&D_expenses' and 'revenue'
        r_d_expenses = company.get('R&D_expenses', 0)
        revenue = company.get('revenue', 1)  # Avoid division by zero
        innovation_score = r_d_expenses / revenue
        return innovation_score

    def analyze_investment_opportunities(self) -> Dict:
        """
        Analyzes investment opportunities in TMT and financial sectors.

        Returns:
        - investment_opportunities (Dict): Dictionary containing investment opportunities.
        """
        investment_opportunities = {'TMT': [], 'Financial': []}

        # Analyze TMT companies
        for company in self.tmt_companies:
            innovation_score = self.calculate_innovation_score(company)
            if innovation_score > self.innovation_threshold:
                investment_opportunities['TMT'].append({
                    'company_name': company.get('company_name'),
                    'innovation_score': innovation_score
                })

        # Analyze financial companies
        for company in self.financial_companies:
            innovation_score = self.calculate_innovation_score(company)
            if innovation_score > self.innovation_threshold:
                investment_opportunities['Financial'].append({
                    'company_name': company.get('company_name'),
                    'innovation_score': innovation_score
                })

        return investment_opportunities

    def filter_by_sector(self, sector: str) -> List[Dict]:
        """
        Filters investment opportunities by sector.

        Args:
        - sector (str): Sector to filter by (TMT or Financial).

        Returns:
        - filtered_opportunities (List[Dict]): List of filtered investment opportunities.
        """
        try:
            investment_opportunities = self.analyze_investment_opportunities()
            return investment_opportunities.get(sector, [])
        except Exception as e:
            print(f"Error filtering by sector: {str(e)}")
            return []

def main():
    # Example usage
    tmt_companies = [
        {'company_name': 'Company A', 'R&D_expenses': 1000000, 'revenue': 10000000},
        {'company_name': 'Company B', 'R&D_expenses': 500000, 'revenue': 5000000}
    ]

    financial_companies = [
        {'company_name': 'Company C', 'R&D_expenses': 2000000, 'revenue': 20000000},
        {'company_name': 'Company D', 'R&D_expenses': 300000, 'revenue': 3000000}
    ]

    analyzer = InvestmentAnalyzer(tmt_companies, financial_companies)
    investment_opportunities = analyzer.analyze_investment_opportunities()
    print(investment_opportunities)

    filtered_tmt_opportunities = analyzer.filter_by_sector('TMT')
    print(filtered_tmt_opportunities)

if __name__ == "__main__":
    main()
```
