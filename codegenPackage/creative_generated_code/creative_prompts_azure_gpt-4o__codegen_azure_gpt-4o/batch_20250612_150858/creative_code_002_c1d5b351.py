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
"""
Program to filter Vansol Travel tour packages by budget and duration.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

# Class to represent a tour package
class TourPackage:
    def __init__(self, name, budget, duration):
        """
        Initialize a tour package.

        :param name: Name of the tour package (string)
        :param budget: Cost of the tour package (float)
        :param duration: Duration of the tour package in days (int)
        """
        self.name = name
        self.budget = budget
        self.duration = duration

    def __repr__(self):
        """
        Return a string representation of the tour package.
        """
        return f"{self.name} | Budget: ${self.budget} | Duration: {self.duration} days"


# Function to filter tour packages
def filter_packages(packages, max_budget, min_duration):
    """
    Filter tour packages based on maximum budget and minimum duration.

    :param packages: List of TourPackage objects
    :param max_budget: Maximum budget for the package (float)
    :param min_duration: Minimum duration of the package (int)
    :return: List of filtered TourPackage objects
    """
    try:
        # Validate input parameters
        if max_budget < 0 or min_duration < 0:
            raise ValueError("Budget and duration must be non-negative.")
        
        # Filter packages based on criteria
        filtered = [
            pkg for pkg in packages
            if pkg.budget <= max_budget and pkg.duration >= min_duration
        ]
        return filtered
    except Exception as e:
        print(f"Error during filtering: {e}", file=sys.stderr)
        return []


# Sample data for tour packages
tour_packages = [
    TourPackage("Beach Paradise", 1200.0, 7),
    TourPackage("Mountain Escape", 800.0, 5),
    TourPackage("City Adventure", 500.0, 3),
    TourPackage("Desert Exploration", 1500.0, 10),
    TourPackage("Tropical Getaway", 1000.0, 6),
]

# User input for filtering (for demonstration purposes)
try:
    max_budget = float(input("Enter maximum budget (e.g., 1000): "))
    min_duration = int(input("Enter minimum duration in days (e.g., 5): "))

    # Filter tour packages
    filtered_packages = filter_packages(tour_packages, max_budget, min_duration)

    # Display results
    if filtered_packages:
        print("\nFiltered Tour Packages:")
        for pkg in filtered_packages:
            print(pkg)
    else:
        print("\nNo packages match the given criteria.")

except ValueError:
    print("Invalid input. Please enter valid numbers for budget and duration.", file=sys.stderr)
```
