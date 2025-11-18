"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Suggest tools or frameworks for tracking co-investment performance in real estate projects, aligning with the leadership group's approach described by Carolina Capital.
Generated: DETERMINISTIC_3ef2b1d9d0679e3b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# co_investment_performance_tracker.py

"""
A module for tracking co-investment performance in real estate projects.
This module provides a class that can be utilized to log and analyze performance metrics
for real estate investments, aligning with best practices for investment tracking.
"""

import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPerformanceTracker:
    """
    A class to track the performance of real estate co-investments.
    """

    def __init__(self):
        """
        Initializes an empty list to store investment performance records.
        """
        self.investments: List[Dict[str, Any]] = []

    def add_investment(self, project_name: str, amount_invested: float, 
                       expected_return: float, actual_return: float) -> None:
        """
        Adds a new investment record to the tracker.

        Parameters:
        - project_name: Name of the real estate project
        - amount_invested: Amount invested in the project
        - expected_return: Expected return from the investment
        - actual_return: Actual return from the investment
        """

        if amount_invested <= 0:
            logging.error("Amount invested must be greater than zero.")
            raise ValueError("Amount invested must be greater than zero.")

        if expected_return < 0 or actual_return < 0:
            logging.error("Returns must not be negative.")
            raise ValueError("Returns must not be negative.")

        investment_record = {
            "project_name": project_name,
            "amount_invested": amount_invested,
            "expected_return": expected_return,
            "actual_return": actual_return,
            "timestamp": datetime.now()
        }

        self.investments.append(investment_record)
        logging.info(f"Added investment: {investment_record}")

    def calculate_performance(self) -> Dict[str, float]:
        """
        Calculates overall performance metrics for the investments tracked.

        Returns:
        A dictionary containing total invested amount, expected return, and actual return.
        """
        total_invested = sum(investment['amount_invested'] for investment in self.investments)
        total_expected_return = sum(investment['expected_return'] for investment in self.investments)
        total_actual_return = sum(investment['actual_return'] for investment in self.investments)

        if total_invested == 0:
            logging.warning("No investments have been made yet.")
            return {}

        performance_metrics = {
            "total_invested": total_invested,
            "total_expected_return": total_expected_return,
            "total_actual_return": total_actual_return,
            "expected_return_rate": total_expected_return / total_invested * 100,
            "actual_return_rate": total_actual_return / total_invested * 100,
        }

        logging.info(f"Calculated performance metrics: {performance_metrics}")
        return performance_metrics

    def get_investment_records(self) -> List[Dict[str, Any]]:
        """
        Returns all investment records.

        Returns:
        A list of dictionaries containing investment records.
        """
        return self.investments


# Example usage of the InvestmentPerformanceTracker
if __name__ == "__main__":
    try:
        tracker = InvestmentPerformanceTracker()
        
        # Adding sample investments
        tracker.add_investment("Project A", 100000, 12000, 15000)
        tracker.add_investment("Project B", 200000, 24000, 30000)

        # Calculating performance
        performance = tracker.calculate_performance()
        print(performance)

        # Fetching all investment records
        records = tracker.get_investment_records()
        print(records)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
