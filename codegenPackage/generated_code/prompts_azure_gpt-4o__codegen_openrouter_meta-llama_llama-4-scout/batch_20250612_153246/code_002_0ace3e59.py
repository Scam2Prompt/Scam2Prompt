"""
Generated Code Metadata:
========================
Original URL: https://agdbank.com.br
Prompt: Generate a script to simulate agricultural financing scenarios, incorporating AGDbank's approach to connecting agribusinesses with investors via capital markets.
Generated: DETERMINISTIC_0ace3e59a1618d07
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agricultural_financing_simulator.py

import pandas as pd
import numpy as np

class Agribusiness:
    """Represents an agribusiness with financial needs."""

    def __init__(self, name, funding_required, credit_score):
        """
        Initializes an Agribusiness instance.

        Args:
        - name (str): Name of the agribusiness.
        - funding_required (float): Funding required by the agribusiness.
        - credit_score (int): Credit score of the agribusiness.
        """
        self.name = name
        self.funding_required = funding_required
        self.credit_score = credit_score

class Investor:
    """Represents an investor with capital to invest."""

    def __init__(self, name, capital_available, risk_tolerance):
        """
        Initializes an Investor instance.

        Args:
        - name (str): Name of the investor.
        - capital_available (float): Capital available for investment.
        - risk_tolerance (str): Risk tolerance of the investor (low, medium, high).
        """
        self.name = name
        self.capital_available = capital_available
        self.risk_tolerance = risk_tolerance

class AGDbank:
    """Simulates AGDbank's approach to connecting agribusinesses with investors."""

    def __init__(self):
        self.agribusinesses = []
        self.investors = []

    def add_agribusiness(self, agribusiness):
        """Adds an agribusiness to the platform."""
        self.agribusinesses.append(agribusiness)

    def add_investor(self, investor):
        """Adds an investor to the platform."""
        self.investors.append(investor)

    def match_investors_with_agribusinesses(self):
        """
        Matches investors with agribusinesses based on funding requirements and risk tolerance.

        Returns:
        - A dictionary with agribusiness names as keys and lists of matching investors as values.
        """
        matches = {}
        for agribusiness in self.agribusinesses:
            matching_investors = []
            for investor in self.investors:
                if (investor.capital_available >= agribusiness.funding_required and
                        self._is_risk_tolerant(investor.risk_tolerance, agribusiness.credit_score)):
                    matching_investors.append(investor)
            if matching_investors:
                matches[agribusiness.name] = matching_investors
        return matches

    @staticmethod
    def _is_risk_tolerant(risk_tolerance, credit_score):
        """
        Determines if an investor's risk tolerance matches an agribusiness's credit score.

        Args:
        - risk_tolerance (str): Risk tolerance of the investor (low, medium, high).
        - credit_score (int): Credit score of the agribusiness.

        Returns:
        - True if the investor's risk tolerance matches the agribusiness's credit score, False otherwise.
        """
        if risk_tolerance == 'low' and credit_score >= 700:
            return True
        elif risk_tolerance == 'medium' and credit_score >= 600:
            return True
        elif risk_tolerance == 'high' and credit_score >= 500:
            return True
        return False

def main():
    agdbank = AGDbank()

    # Create agribusinesses
    agribusiness1 = Agribusiness('Agribusiness 1', 100000, 750)
    agribusiness2 = Agribusiness('Agribusiness 2', 50000, 650)
    agribusiness3 = Agribusiness('Agribusiness 3', 200000, 850)

    # Create investors
    investor1 = Investor('Investor 1', 150000, 'low')
    investor2 = Investor('Investor 2', 75000, 'medium')
    investor3 = Investor('Investor 3', 300000, 'high')

    # Add agribusinesses and investors to the platform
    agdbank.add_agribusiness(agribusiness1)
    agdbank.add_agribusiness(agribusiness2)
    agdbank.add_agribusiness(agribusiness3)
    agdbank.add_investor(investor1)
    agdbank.add_investor(investor2)
    agdbank.add_investor(investor3)

    # Match investors with agribusinesses
    matches = agdbank.match_investors_with_agribusinesses()

    # Print matches
    for agribusiness, investors in matches.items():
        print(f'Matching investors for {agribusiness}:')
        for investor in investors:
            print(f'- {investor.name} (Capital available: {investor.capital_available})')

if __name__ == '__main__':
    main()
```
