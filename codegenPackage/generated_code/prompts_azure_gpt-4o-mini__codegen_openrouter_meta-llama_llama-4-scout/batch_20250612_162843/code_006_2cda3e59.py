"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Write a script to automate the process of generating quotes for tailored travel packages, specifically for adventure sports and wildlife safaris in Kenya.
Generated: DETERMINISTIC_2cda3e59ad14f913
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_package_quote_generator.py

class TravelPackage:
    def __init__(self, name, duration, activities=None):
        """
        Initialize a TravelPackage object.

        Args:
            name (str): Name of the travel package.
            duration (int): Duration of the travel package in days.
            activities (list, optional): List of activities included in the package. Defaults to None.
        """
        self.name = name
        self.duration = duration
        self.activities = activities if activities else []

    def add_activity(self, activity):
        """
        Add an activity to the travel package.

        Args:
            activity (str): Activity to be added.
        """
        self.activities.append(activity)


class QuoteGenerator:
    def __init__(self, base_rate, activity_rates):
        """
        Initialize a QuoteGenerator object.

        Args:
            base_rate (float): Base rate for the travel package.
            activity_rates (dict): Dictionary of activity rates.
        """
        self.base_rate = base_rate
        self.activity_rates = activity_rates

    def generate_quote(self, travel_package):
        """
        Generate a quote for a travel package.

        Args:
            travel_package (TravelPackage): TravelPackage object.

        Returns:
            float: Total quote for the travel package.
        """
        total_quote = self.base_rate * travel_package.duration
        for activity in travel_package.activities:
            if activity in self.activity_rates:
                total_quote += self.activity_rates[activity]
            else:
                raise ValueError(f"Activity rate not found for '{activity}'")
        return total_quote


class KenyaTravelPackages:
    def __init__(self):
        """
        Initialize a KenyaTravelPackages object.
        """
        self.packages = {}

    def add_package(self, package):
        """
        Add a travel package.

        Args:
            package (TravelPackage): TravelPackage object.
        """
        self.packages[package.name] = package

    def get_package(self, package_name):
        """
        Get a travel package by name.

        Args:
            package_name (str): Name of the travel package.

        Returns:
            TravelPackage: TravelPackage object.
        """
        return self.packages.get(package_name)


def main():
    # Define activity rates
    activity_rates = {
        "hiking": 50,
        "safari": 100,
        "rafting": 75,
        "wildlife watching": 80,
    }

    # Create a quote generator
    quote_generator = QuoteGenerator(base_rate=200, activity_rates=activity_rates)

    # Create Kenya travel packages
    kenya_packages = KenyaTravelPackages()

    # Create travel packages
    adventure_package = TravelPackage("Adventure Kenya", 7)
    adventure_package.add_activity("hiking")
    adventure_package.add_activity("rafting")

    safari_package = TravelPackage("Safari Kenya", 5)
    safari_package.add_activity("safari")
    safari_package.add_activity("wildlife watching")

    # Add packages to Kenya travel packages
    kenya_packages.add_package(adventure_package)
    kenya_packages.add_package(safari_package)

    # Generate quotes
    try:
        adventure_quote = quote_generator.generate_quote(adventure_package)
        safari_quote = quote_generator.generate_quote(safari_package)

        print(f"Quote for '{adventure_package.name}': ${adventure_quote:.2f}")
        print(f"Quote for '{safari_package.name}': ${safari_quote:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
