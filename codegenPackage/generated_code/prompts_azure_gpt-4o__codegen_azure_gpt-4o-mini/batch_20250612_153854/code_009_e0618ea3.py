"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Create a program that models collaboration and mutual success metrics for investment partnerships, inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.
Generated: DETERMINISTIC_e0618ea3d59ff1cb
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InvestmentPartnership:
    """
    A class to model an investment partnership focusing on collaboration and mutual success metrics.
    """

    def __init__(self, name: str):
        """
        Initializes the InvestmentPartnership with a name and an empty list of partners.

        :param name: The name of the investment partnership.
        """
        self.name = name
        self.partners: List[Dict[str, Any]] = []

    def add_partner(self, partner_name: str, contribution: float) -> None:
        """
        Adds a partner to the investment partnership.

        :param partner_name: The name of the partner.
        :param contribution: The financial contribution of the partner.
        """
        if contribution <= 0:
            raise ValueError("Contribution must be a positive value.")
        
        partner = {
            'name': partner_name,
            'contribution': contribution,
            'success_metrics': {}
        }
        self.partners.append(partner)

    def record_success_metric(self, partner_name: str, metric_name: str, value: float) -> None:
        """
        Records a success metric for a specific partner.

        :param partner_name: The name of the partner.
        :param metric_name: The name of the success metric.
        :param value: The value of the success metric.
        """
        for partner in self.partners:
            if partner['name'] == partner_name:
                partner['success_metrics'][metric_name] = value
                return
        raise ValueError(f"Partner '{partner_name}' not found.")

    def calculate_total_contribution(self) -> float:
        """
        Calculates the total contribution of all partners.

        :return: The total contribution.
        """
        return sum(partner['contribution'] for partner in self.partners)

    def generate_report(self) -> str:
        """
        Generates a report of the partnership's contributions and success metrics.

        :return: A JSON string representing the report.
        """
        report = {
            'partnership_name': self.name,
            'total_contribution': self.calculate_total_contribution(),
            'partners': self.partners
        }
        return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        partnership = InvestmentPartnership("Alghanim Capital Partners")
        partnership.add_partner("Alice", 100000)
        partnership.add_partner("Bob", 150000)
        partnership.record_success_metric("Alice", "ROI", 15.5)
        partnership.record_success_metric("Bob", "ROI", 20.0)

        report = partnership.generate_report()
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
```
