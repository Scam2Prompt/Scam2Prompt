"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Write a Python program to display a list of tour packages offered by Balaji Tours & Travels (e.g., Tirupathi, Sri Kalahasthi, Kerala) and allow users to select one to view more details.
Generated: DETERMINISTIC_85085e03cab6f413
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TourPackage:
    """Class representing a tour package."""
    
    def __init__(self, destination, price, description):
        """Initialize the tour package with destination, price, and description."""
        self.destination = destination
        self.price = price
        self.description = description

    def __str__(self):
        """Return a string representation of the tour package."""
        return f"{self.destination}: {self.price} - {self.description}"


class TourService:
    """Service class to manage tour packages."""

    def __init__(self):
        """Initialize the service with a list of tour packages."""
        self.packages = [
            TourPackage("Tirupathi", 5000, "A spiritual journey to the Tirumala Temple."),
            TourPackage("Sri Kalahasthi", 4800, "Famous for its temples and the spiritual experience."),
            TourPackage("Kerala", 12000, "Explore the backwaters and lush greenery of God’s Own Country.")
        ]

    def display_packages(self):
        """Display the list of available tour packages."""
        print("Available Tour Packages:")
        for index, package in enumerate(self.packages, start=1):
            print(f"{index}. {package}")

    def select_package(self, choice):
        """Return the selected tour package based on user choice."""
        try:
            index = choice - 1  # Adjust for zero-based index
            if 0 <= index < len(self.packages):
                return self.packages[index]
            else:
                raise IndexError("Invalid selection. Please select a valid package number.")
        except IndexError as e:
            print(e)
            return None


def main():
    """Main function to run the tour package selection program."""
    tour_service = TourService()
    
    while True:
        tour_service.display_packages()
        try:
            user_input = input("Select a tour package by number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Thank you for using Balaji Tours & Travels. Goodbye!")
                break
            
            choice = int(user_input)
            selected_package = tour_service.select_package(choice)
            
            if selected_package:
                print(f"\nYou selected: {selected_package}")
                print(f"Details: {selected_package.description}\n")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
```
