"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write a Python script to filter and display available horse riding tours based on user-selected dates and group size, as described in the Chile Horse Riding reservation form.
Generated: DETERMINISTIC_37a587a697a76e41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chile_horse_riding.py

from datetime import datetime, timedelta
from typing import List, Dict

class HorseRidingTour:
    def __init__(self, id: int, name: str, max_group_size: int, available_dates: List[str]):
        """
        Initialize a Horse Riding Tour.

        Args:
        - id (int): Unique tour identifier.
        - name (str): Tour name.
        - max_group_size (int): Maximum group size for the tour.
        - available_dates (List[str]): List of available dates in 'YYYY-MM-DD' format.
        """
        self.id = id
        self.name = name
        self.max_group_size = max_group_size
        self.available_dates = available_dates

class TourFilter:
    def __init__(self, tours: List[HorseRidingTour]):
        """
        Initialize a Tour Filter.

        Args:
        - tours (List[HorseRidingTour]): List of available Horse Riding Tours.
        """
        self.tours = tours

    def filter_by_date(self, date: str) -> List[HorseRidingTour]:
        """
        Filter tours by a specific date.

        Args:
        - date (str): Date in 'YYYY-MM-DD' format.

        Returns:
        - List[HorseRidingTour]: List of tours available on the specified date.
        """
        return [tour for tour in self.tours if date in tour.available_dates]

    def filter_by_group_size(self, group_size: int) -> List[HorseRidingTour]:
        """
        Filter tours by group size.

        Args:
        - group_size (int): Desired group size.

        Returns:
        - List[HorseRidingTour]: List of tours that accommodate the specified group size.
        """
        return [tour for tour in self.tours if tour.max_group_size >= group_size]

    def filter_tours(self, date: str, group_size: int) -> List[HorseRidingTour]:
        """
        Filter tours by date and group size.

        Args:
        - date (str): Date in 'YYYY-MM-DD' format.
        - group_size (int): Desired group size.

        Returns:
        - List[HorseRidingTour]: List of tours that match the specified date and group size.
        """
        date_filtered_tours = self.filter_by_date(date)
        return [tour for tour in date_filtered_tours if tour.max_group_size >= group_size]

def main():
    # Sample tours data
    tours: List[HorseRidingTour] = [
        HorseRidingTour(1, "Tour 1", 4, ["2024-09-20", "2024-09-22", "2024-09-24"]),
        HorseRidingTour(2, "Tour 2", 6, ["2024-09-20", "2024-09-23", "2024-09-25"]),
        HorseRidingTour(3, "Tour 3", 2, ["2024-09-21", "2024-09-22", "2024-09-23"]),
    ]

    filter = TourFilter(tours)

    try:
        date = input("Enter your preferred date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format

        group_size = int(input("Enter your group size: "))

        if group_size <= 0:
            print("Group size must be a positive integer.")
            return

        filtered_tours = filter.filter_tours(date, group_size)

        if not filtered_tours:
            print("No tours available for the specified date and group size.")
        else:
            print("Available Tours:")
            for tour in filtered_tours:
                print(f"ID: {tour.id}, Name: {tour.name}, Max Group Size: {tour.max_group_size}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
```
