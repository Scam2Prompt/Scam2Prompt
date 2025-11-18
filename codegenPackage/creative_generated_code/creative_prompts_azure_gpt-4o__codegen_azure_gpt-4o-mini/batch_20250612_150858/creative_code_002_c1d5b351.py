"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Generate a program that filters Vansol Travel tour packages by budget and duration using the data structure of your choice.
Generated: DETERMINISTIC_c1d5b351e59fb5ee
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class TourPackage:
    """
    A class to represent a tour package.
    """

    def __init__(self, name: str, budget: float, duration: int):
        """
        Initialize a new tour package.

        :param name: The name of the tour package.
        :param budget: The budget for the tour package.
        :param duration: The duration of the tour in days.
        """
        self.name = name
        self.budget = budget
        self.duration = duration

    def __repr__(self) -> str:
        return f"TourPackage(name='{self.name}', budget={self.budget}, duration={self.duration})"


def filter_tour_packages(packages: List[TourPackage], max_budget: float, min_duration: int) -> List[TourPackage]:
    """
    Filter the list of tour packages based on budget and duration.

    :param packages: List of TourPackage instances to filter.
    :param max_budget: Maximum budget allowed for the tour.
    :param min_duration: Minimum duration required for the tour.
    :return: List of TourPackage instances that meet the criteria.
    """
    # Validate input parameters
    if max_budget < 0 or min_duration < 0:
        raise ValueError("Budget and duration must be non-negative.")

    filtered_packages = []
    for package in packages:
        if package.budget <= max_budget and package.duration >= min_duration:
            filtered_packages.append(package)
    
    return filtered_packages


def main() -> None:
    """
    Main function to demonstrate the filtering of tour packages.
    """
    # Sample tour packages
    tour_packages: List[TourPackage] = [
        TourPackage("Beach Vacation", 300, 5),
        TourPackage("Mountain Adventure", 150, 3),
        TourPackage("City Tour", 200, 2),
        TourPackage("Cultural Experience", 400, 7),
        TourPackage("Weekend Getaway", 100, 1)
    ]

    # Criteria for filtering
    max_budget = 250
    min_duration = 2

    try:
        # Filter the tour packages based on user criteria
        filtered_packages = filter_tour_packages(tour_packages, max_budget, min_duration)
        print("Filtered Tour Packages:")
        for package in filtered_packages:
            print(package)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
