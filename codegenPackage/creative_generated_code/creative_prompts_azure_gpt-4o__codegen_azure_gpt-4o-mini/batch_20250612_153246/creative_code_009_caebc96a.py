"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Create a script to manage sponsorship packages (Silver, Bronze, Gold) for the MCT Summit, including features like pricing and benefits as described on the website.
Generated: DETERMINISTIC_caebc96a62813354
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SponsorshipPackage:
    """
    Class to represent a sponsorship package for the MCT Summit.
    """

    def __init__(self, name, price, benefits):
        """
        Initializes a new SponsorshipPackage instance.

        :param name: The name of the sponsorship package (e.g., 'Silver', 'Bronze', 'Gold').
        :param price: The price of the sponsorship package.
        :param benefits: A list of benefits associated with the sponsorship package.
        """
        self.name = name
        self.price = price
        self.benefits = benefits

    def display_info(self):
        """
        Displays the details of the sponsorship package.
        """
        print(f"Sponsorship Package: {self.name}")
        print(f"Price: ${self.price}")
        print("Benefits:")
        for benefit in self.benefits:
            print(f" - {benefit}")


class SponsorshipManager:
    """
    Class to manage different sponsorship packages for the MCT Summit.
    """

    def __init__(self):
        """
        Initializes the SponsorshipManager with predefined packages.
        """
        self.packages = self.create_packages()

    def create_packages(self):
        """
        Creates predefined sponsorship packages.

        :return: A list of SponsorshipPackage instances.
        """
        return [
            SponsorshipPackage("Bronze", 1000, [
                "Logo on website",
                "Social Media shoutout",
                "Free tickets for 2 attendees"
            ]),
            SponsorshipPackage("Silver", 5000, [
                "Logo on website",
                "Social Media shoutouts",
                "Free tickets for 5 attendees",
                "Prominent display at event",
                "Access to VIP lounge"
            ]),
            SponsorshipPackage("Gold", 10000, [
                "Logo on website",
                "Social Media shoutouts",
                "Free tickets for 10 attendees",
                "Prominent display at event",
                "Access to VIP lounge",
                "Speaking opportunity"
            ])
        ]

    def display_all_packages(self):
        """
        Displays all sponsorship packages.
        """
        print("Available Sponsorship Packages:")
        for package in self.packages:
            package.display_info()
            print("")  # Blank line for separation

    def find_package(self, name):
        """
        Finds a sponsorship package by name.

        :param name: The name of the sponsorship package to find.
        :return: The SponsorshipPackage instance if found, otherwise None.
        """
        for package in self.packages:
            if package.name.lower() == name.lower():
                return package
        return None


def main():
    """
    Main function to run the Sponsorship Manager.
    """
    try:
        manager = SponsorshipManager()
        manager.display_all_packages()

        # Example interaction: Finding a specific package
        package_name = input("Enter the sponsorship package name you want to find: ")
        package = manager.find_package(package_name)

        if package:
            print("\nFound Package:")
            package.display_info()
        else:
            print("Sponsorship package not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
