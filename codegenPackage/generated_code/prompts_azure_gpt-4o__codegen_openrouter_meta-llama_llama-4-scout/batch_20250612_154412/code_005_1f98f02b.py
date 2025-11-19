"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Provide code examples for implementing a debt conversion agent that tracks daily conversions and calculates engagement metrics, inspired by Invicta Cobranças' approach.
Generated: DETERMINISTIC_1f98f02b30d8567d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# debt_conversion_agent.py

from datetime import date, timedelta
from typing import Dict, List

class DebtConversionAgent:
    """
    Tracks daily conversions and calculates engagement metrics.
    """

    def __init__(self):
        """
        Initializes the debt conversion agent.
        """
        self.conversions = {}  # type: Dict[date, int]
        self.engagement_metrics = {}  # type: Dict[date, Dict[str, int]]

    def add_conversion(self, conversion_date: date, amount: int):
        """
        Adds a conversion for the given date.

        Args:
            conversion_date (date): The date of the conversion.
            amount (int): The amount of the conversion.
        """
        if conversion_date in self.conversions:
            self.conversions[conversion_date] += amount
        else:
            self.conversions[conversion_date] = amount

        # Update engagement metrics
        self.update_engagement_metrics(conversion_date, amount)

    def update_engagement_metrics(self, conversion_date: date, amount: int):
        """
        Updates the engagement metrics for the given date.

        Args:
            conversion_date (date): The date of the conversion.
            amount (int): The amount of the conversion.
        """
        if conversion_date not in self.engagement_metrics:
            self.engagement_metrics[conversion_date] = {"conversions": 0, "amount": 0}

        self.engagement_metrics[conversion_date]["conversions"] += 1
        self.engagement_metrics[conversion_date]["amount"] += amount

    def get_daily_conversions(self, start_date: date, end_date: date) -> List[Dict[str, int]]:
        """
        Gets the daily conversions between the given dates.

        Args:
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            List[Dict[str, int]]: A list of daily conversions.
        """
        daily_conversions = []
        current_date = start_date

        while current_date <= end_date:
            if current_date in self.conversions:
                daily_conversions.append({"date": current_date, "conversions": self.conversions[current_date]})
            else:
                daily_conversions.append({"date": current_date, "conversions": 0})

            current_date += timedelta(days=1)

        return daily_conversions

    def get_engagement_metrics(self, start_date: date, end_date: date) -> List[Dict[str, int]]:
        """
        Gets the engagement metrics between the given dates.

        Args:
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            List[Dict[str, int]]: A list of engagement metrics.
        """
        engagement_metrics = []
        current_date = start_date

        while current_date <= end_date:
            if current_date in self.engagement_metrics:
                engagement_metrics.append({
                    "date": current_date,
                    "conversions": self.engagement_metrics[current_date]["conversions"],
                    "amount": self.engagement_metrics[current_date]["amount"]
                })
            else:
                engagement_metrics.append({"date": current_date, "conversions": 0, "amount": 0})

            current_date += timedelta(days=1)

        return engagement_metrics


def main():
    agent = DebtConversionAgent()

    try:
        # Add conversions
        agent.add_conversion(date(2022, 1, 1), 100)
        agent.add_conversion(date(2022, 1, 1), 200)
        agent.add_conversion(date(2022, 1, 2), 50)

        # Get daily conversions
        daily_conversions = agent.get_daily_conversions(date(2022, 1, 1), date(2022, 1, 2))
        print("Daily Conversions:")
        for conversion in daily_conversions:
            print(conversion)

        # Get engagement metrics
        engagement_metrics = agent.get_engagement_metrics(date(2022, 1, 1), date(2022, 1, 2))
        print("\nEngagement Metrics:")
        for metric in engagement_metrics:
            print(metric)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
