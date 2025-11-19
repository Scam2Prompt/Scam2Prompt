"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Generate a code snippet for a web application that tracks the number of neurological cases registered, inspired by the ICON Foundation's data collection from December 2022 to January 2024.
Generated: DETERMINISTIC_e36b8f7f0d6c92d5
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# neurological_case_tracker.py

from datetime import datetime
from typing import Dict

class NeurologicalCaseTracker:
    def __init__(self):
        """
        Initialize the NeurologicalCaseTracker with an empty dictionary to store cases.
        """
        self.cases: Dict[str, int] = {}

    def add_case(self, date: str, count: int) -> None:
        """
        Add a neurological case count for a specific date.

        Args:
        - date (str): The date in 'YYYY-MM-DD' format.
        - count (int): The number of cases.

        Raises:
        - ValueError: If the date is not in 'YYYY-MM-DD' format or if the count is negative.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
            if count < 0:
                raise ValueError("Case count cannot be negative.")
            self.cases[date] = self.cases.get(date, 0) + count
        except ValueError as e:
            print(f"Invalid input: {e}")

    def get_case_count(self, date: str) -> int:
        """
        Get the neurological case count for a specific date.

        Args:
        - date (str): The date in 'YYYY-MM-DD' format.

        Returns:
        - int: The number of cases on the specified date. Returns 0 if no cases are found.

        Raises:
        - ValueError: If the date is not in 'YYYY-MM-DD' format.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return self.cases.get(date, 0)
        except ValueError as e:
            print(f"Invalid input: {e}")
            return 0

    def get_total_cases(self) -> int:
        """
        Get the total number of neurological cases.

        Returns:
        - int: The total number of cases.
        """
        return sum(self.cases.values())

    def get_cases_in_range(self, start_date: str, end_date: str) -> int:
        """
        Get the total number of neurological cases within a date range.

        Args:
        - start_date (str): The start date in 'YYYY-MM-DD' format.
        - end_date (str): The end date in 'YYYY-MM-DD' format.

        Returns:
        - int: The total number of cases within the specified date range.

        Raises:
        - ValueError: If the start or end date is not in 'YYYY-MM-DD' format.
        """
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
            if start_date_obj > end_date_obj:
                raise ValueError("Invalid date range.")
            total_cases = 0
            for date, count in self.cases.items():
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                if start_date_obj <= date_obj <= end_date_obj:
                    total_cases += count
            return total_cases
        except ValueError as e:
            print(f"Invalid input: {e}")
            return 0


def main():
    tracker = NeurologicalCaseTracker()

    # Example usage:
    tracker.add_case('2022-12-01', 10)
    tracker.add_case('2022-12-02', 15)
    tracker.add_case('2024-01-01', 20)

    print("Case count on 2022-12-01:", tracker.get_case_count('2022-12-01'))
    print("Total cases:", tracker.get_total_cases())
    print("Total cases between 2022-12-01 and 2024-01-01:", tracker.get_cases_in_range('2022-12-01', '2024-01-01'))

if __name__ == "__main__":
    main()
```
