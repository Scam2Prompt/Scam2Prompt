"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: Create a script to manage sponsorship packages (Silver, Bronze, Gold) for the MCT Summit, including features like pricing and benefits as described on the website.
Generated: DETERMINISTIC_caebc96a62813354
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sponsorship_packages.py

class SponsorshipPackage:
    """Base class for sponsorship packages."""

    def __init__(self, name, price, benefits):
        """
        Initialize a sponsorship package.

        Args:
            name (str): Name of the package.
            price (float): Price of the package.
            benefits (list): List of benefits for the package.
        """
        self.name = name
        self.price = price
        self.benefits = benefits

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def get_benefits(self):
        """Return a formatted string of benefits."""
        return "\n".join(self.benefits)


class SilverPackage(SponsorshipPackage):
    """Silver sponsorship package."""

    def __init__(self):
        super().__init__("Silver", 1000.0, [
            "Logo on event website",
            "Social media shoutout",
            "Small booth space",
        ])


class BronzePackage(SponsorshipPackage):
    """Bronze sponsorship package."""

    def __init__(self):
        super().__init__("Bronze", 500.0, [
            "Logo on event website",
            "Social media shoutout",
        ])


class GoldPackage(SponsorshipPackage):
    """Gold sponsorship package."""

    def __init__(self):
        super().__init__("Gold", 2500.0, [
            "Logo on event website",
            "Social media shoutout",
            "Large booth space",
            "Speaking opportunity",
        ])


class SponsorshipManager:
    """Manage sponsorship packages."""

    def __init__(self):
        self.packages = {
            "silver": SilverPackage(),
            "bronze": BronzePackage(),
            "gold": GoldPackage(),
        }

    def get_package(self, package_name):
        """
        Get a sponsorship package by name.

        Args:
            package_name (str): Name of the package.

        Returns:
            SponsorshipPackage: The sponsorship package.

        Raises:
            ValueError: If the package name is not found.
        """
        package_name = package_name.lower()
        if package_name not in self.packages:
            raise ValueError("Package not found")
        return self.packages[package_name]

    def list_packages(self):
        """Print a list of all sponsorship packages."""
        for package in self.packages.values():
            print(package)
            print(package.get_benefits())
            print()


def main():
    try:
        manager = SponsorshipManager()
        while True:
            print("1. List packages")
            print("2. Get package details")
            print("3. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                manager.list_packages()
            elif choice == "2":
                package_name = input("Enter package name (silver, bronze, gold): ")
                package = manager.get_package(package_name)
                print(package)
                print(package.get_benefits())
            elif choice == "3":
                break
            else:
                print("Invalid option")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
