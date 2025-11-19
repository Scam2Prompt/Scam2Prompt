"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Develop a program to maximize rental income using dynamic pricing algorithms, similar to the strategies offered by strki.com.
Generated: DETERMINISTIC_174309311cc7b6bf
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict

class RentalIncomeMaximizer:
    def __init__(self, base_rate: float, demand_multiplier: Dict[int, float]):
        """
        Initialize the RentalIncomeMaximizer.

        Args:
        - base_rate (float): The base rental rate.
        - demand_multiplier (Dict[int, float]): A dictionary of demand multipliers for each day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday).
        """
        self.base_rate = base_rate
        self.demand_multiplier = demand_multiplier

    def calculate_optimal_rate(self, date: datetime, occupancy: int) -> float:
        """
        Calculate the optimal rental rate for a given date and occupancy.

        Args:
        - date (datetime): The date for which to calculate the rate.
        - occupancy (int): The number of guests.

        Returns:
        - float: The optimal rental rate.
        """
        day_of_week = date.weekday()
        demand = self.demand_multiplier.get(day_of_week, 1.0)
        rate = self.base_rate * demand * (1 + (occupancy / 10))  # assume 10% increase per 10 guests
        return rate

    def generate_rate_schedule(self, start_date: datetime, end_date: datetime, occupancy: List[int]) -> List[Dict[str, float]]:
        """
        Generate a rate schedule for a given date range and occupancy.

        Args:
        - start_date (datetime): The start date of the range.
        - end_date (datetime): The end date of the range.
        - occupancy (List[int]): A list of occupancies for each day.

        Returns:
        - List[Dict[str, float]]: A list of dictionaries containing the date and optimal rate for each day.
        """
        if len(occupancy) != (end_date - start_date).days + 1:
            raise ValueError("Occupancy list must match date range")

        rate_schedule = []
        current_date = start_date
        for occ in occupancy:
            rate = self.calculate_optimal_rate(current_date, occ)
            rate_schedule.append({"date": current_date.strftime("%Y-%m-%d"), "rate": rate})
            current_date += timedelta(days=1)
        return rate_schedule


def main():
    # Example usage
    base_rate = 100.0
    demand_multiplier = {
        0: 1.2,  # Monday
        1: 1.1,  # Tuesday
        2: 1.0,  # Wednesday
        3: 1.1,  # Thursday
        4: 1.2,  # Friday
        5: 1.5,  # Saturday
        6: 1.8   # Sunday
    }

    maximizer = RentalIncomeMaximizer(base_rate, demand_multiplier)

    start_date = datetime(2024, 9, 16)
    end_date = datetime(2024, 9, 22)
    occupancy = [2, 2, 1, 3, 4, 5, 4]

    try:
        rate_schedule = maximizer.generate_rate_schedule(start_date, end_date, occupancy)
        for day in rate_schedule:
            print(f"Date: {day['date']}, Optimal Rate: ${day['rate']:.2f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
