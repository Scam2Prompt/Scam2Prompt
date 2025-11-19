"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Develop a program that tracks accounting firm performance metrics and identifies factors that set top firms apart from the competition.
Generated: DETERMINISTIC_f41a8b00c61f94b5
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# accounting_firm_performance_tracker.py

import pandas as pd
from typing import Dict, List

class AccountingFirm:
    def __init__(self, name: str, revenue: float, num_employees: int, client_satisfaction: float):
        """
        Initialize an AccountingFirm object.

        Args:
        - name (str): The name of the firm.
        - revenue (float): The annual revenue of the firm.
        - num_employees (int): The number of employees in the firm.
        - client_satisfaction (float): The average client satisfaction rating (out of 10).
        """
        self.name = name
        self.revenue = revenue
        self.num_employees = num_employees
        self.client_satisfaction = client_satisfaction

class PerformanceTracker:
    def __init__(self):
        """
        Initialize a PerformanceTracker object.
        """
        self.firms = []

    def add_firm(self, firm: AccountingFirm):
        """
        Add an AccountingFirm to the tracker.

        Args:
        - firm (AccountingFirm): The firm to add.
        """
        self.firms.append(firm)

    def get_top_firms(self, num_firms: int = 5) -> List[AccountingFirm]:
        """
        Get the top firms based on revenue.

        Args:
        - num_firms (int): The number of top firms to return (default: 5).

        Returns:
        - List[AccountingFirm]: The top firms.
        """
        return sorted(self.firms, key=lambda firm: firm.revenue, reverse=True)[:num_firms]

    def analyze_performance(self) -> Dict[str, Dict[str, float]]:
        """
        Analyze the performance of all firms and identify factors that set top firms apart.

        Returns:
        - Dict[str, Dict[str, float]]: A dictionary with performance metrics for all firms.
        """
        performance_metrics = {}
        top_firms = self.get_top_firms()

        for firm in self.firms:
            metrics = {
                "revenue_per_employee": firm.revenue / firm.num_employees if firm.num_employees > 0 else 0,
                "client_satisfaction": firm.client_satisfaction
            }
            performance_metrics[firm.name] = metrics

        top_firm_metrics = {firm.name: performance_metrics[firm.name] for firm in top_firms}

        return {
            "all_firms": performance_metrics,
            "top_firms": top_firm_metrics
        }

def load_firm_data(data: List[Dict[str, str]]) -> List[AccountingFirm]:
    """
    Load firm data from a list of dictionaries.

    Args:
    - data (List[Dict[str, str]]): The firm data.

    Returns:
    - List[AccountingFirm]: A list of AccountingFirm objects.
    """
    firms = []
    for firm_data in data:
        try:
            firm = AccountingFirm(
                name=firm_data["name"],
                revenue=float(firm_data["revenue"]),
                num_employees=int(firm_data["num_employees"]),
                client_satisfaction=float(firm_data["client_satisfaction"])
            )
            firms.append(firm)
        except (KeyError, ValueError) as e:
            print(f"Error loading firm data: {e}")

    return firms

def main():
    # Example usage
    firm_data = [
        {"name": "Firm A", "revenue": "1000000", "num_employees": "10", "client_satisfaction": "8.5"},
        {"name": "Firm B", "revenue": "500000", "num_employees": "5", "client_satisfaction": "9.0"},
        {"name": "Firm C", "revenue": "2000000", "num_employees": "20", "client_satisfaction": "8.0"}
    ]

    firms = load_firm_data(firm_data)
    tracker = PerformanceTracker()

    for firm in firms:
        tracker.add_firm(firm)

    performance_metrics = tracker.analyze_performance()

    print("All Firms Performance Metrics:")
    for firm, metrics in performance_metrics["all_firms"].items():
        print(f"Firm: {firm}")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.2f}")
        print()

    print("Top Firms Performance Metrics:")
    for firm, metrics in performance_metrics["top_firms"].items():
        print(f"Firm: {firm}")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.2f}")
        print()

if __name__ == "__main__":
    main()
```
