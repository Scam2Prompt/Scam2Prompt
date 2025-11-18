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
# Python program to display tour packages and allow users to select one for more details

class TourPackage:
    """Class to represent a tour package."""
    def __init__(self, name, description, price, duration):
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration

    def display_details(self):
        """Display detailed information about the tour package."""
        print(f"\n--- {self.name} ---")
        print(f"Description: {self.description}")
        print(f"Price: ₹{self.price}")
        print(f"Duration: {self.duration} days")
        print("-------------------------\n")


def display_packages(packages):
    """Display a list of available tour packages."""
    print("Available Tour Packages:")
    for idx, package in enumerate(packages, start=1):
        print(f"{idx}. {package.name}")
    print("-------------------------\n")


def main():
    """Main function for the program."""
    # List of tour packages offered by Balaji Tours & Travels
    packages = [
        TourPackage("Tirupathi", "A spiritual journey to the sacred Tirupathi Temple.", 3500, 1),
        TourPackage("Sri Kalahasthi", "Visit the famous Sri Kalahasthi Temple.", 2500, 1),
        TourPackage("Kerala", "Experience the serene backwaters and lush greenery of Kerala.", 12000, 5),
    ]

    while True:
        # Display available packages
        display_packages(packages)

        try:
            # Prompt user to select a package
            choice = int(input("Enter the number of the package you want to view details for (or 0 to exit): "))
            if choice == 0:
                print("Thank you for using Balaji Tours & Travels! Have a great day!")
                break

            if 1 <= choice <= len(packages):
                selected_package = packages[choice - 1]
                selected_package.display_details()
            else:
                print("Invalid choice. Please select a valid package number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
```
