"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Write a program to calculate monthly internet costs for different packages (Bronze, Silver, Gold, Diamond) offered by MARUF ONLINE BD, including features like BDIX-limited FTP and TV access.
Generated: DETERMINISTIC_79d4533d478bd2fe
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# internet_cost_calculator.py

class InternetPackage:
    def __init__(self, name, base_cost, bdix_cost, tv_cost):
        """
        Initialize an InternetPackage.

        Args:
            name (str): Package name.
            base_cost (float): Base cost of the package.
            bdix_cost (float): Additional cost for BDIX-limited FTP.
            tv_cost (float): Additional cost for TV access.
        """
        self.name = name
        self.base_cost = base_cost
        self.bdix_cost = bdix_cost
        self.tv_cost = tv_cost

    def calculate_cost(self, bdix=False, tv=False):
        """
        Calculate the total cost of the package.

        Args:
            bdix (bool, optional): Whether BDIX-limited FTP is included. Defaults to False.
            tv (bool, optional): Whether TV access is included. Defaults to False.

        Returns:
            float: Total cost of the package.
        """
        total_cost = self.base_cost
        if bdix:
            total_cost += self.bdix_cost
        if tv:
            total_cost += self.tv_cost
        return total_cost


class InternetCostCalculator:
    def __init__(self):
        """
        Initialize an InternetCostCalculator.
        """
        self.packages = {
            "Bronze": InternetPackage("Bronze", 500, 100, 200),
            "Silver": InternetPackage("Silver", 800, 100, 200),
            "Gold": InternetPackage("Gold", 1200, 100, 200),
            "Diamond": InternetPackage("Diamond", 2000, 100, 200),
        }

    def calculate_monthly_cost(self, package_name, bdix=False, tv=False):
        """
        Calculate the monthly internet cost for a given package.

        Args:
            package_name (str): Name of the package.
            bdix (bool, optional): Whether BDIX-limited FTP is included. Defaults to False.
            tv (bool, optional): Whether TV access is included. Defaults to False.

        Returns:
            float: Monthly internet cost.

        Raises:
            ValueError: If the package name is not valid.
        """
        if package_name not in self.packages:
            raise ValueError("Invalid package name")

        package = self.packages[package_name]
        return package.calculate_cost(bdix, tv)

    def display_packages(self):
        """
        Display available packages and their costs.
        """
        print("Available Packages:")
        for package_name, package in self.packages.items():
            print(f"Package: {package_name}")
            print(f"Base Cost: {package.base_cost} BDT")
            print(f"BDIX-limited FTP: +{package.bdix_cost} BDT")
            print(f"TV Access: +{package.tv_cost} BDT")
            print()


def main():
    calculator = InternetCostCalculator()

    while True:
        print("MARUF ONLINE BD Internet Cost Calculator")
        print("1. Calculate Monthly Cost")
        print("2. Display Packages")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            package_name = input("Enter package name (Bronze, Silver, Gold, Diamond): ")
            bdix = input("Include BDIX-limited FTP? (yes/no): ").lower() == "yes"
            tv = input("Include TV access? (yes/no): ").lower() == "yes"

            try:
                monthly_cost = calculator.calculate_monthly_cost(package_name, bdix, tv)
                print(f"Monthly cost: {monthly_cost} BDT")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            calculator.display_packages()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
