"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Write a program to calculate monthly internet costs for different packages (Bronze, Silver, Gold, Diamond) offered by MARUF ONLINE BD, including features like BDIX-limited FTP and TV access.
Generated: DETERMINISTIC_79d4533d478bd2fe
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InternetPackage:
    """
    A class to represent an internet package.

    Attributes:
        name (str): The name of the package.
        base_cost (float): The base monthly cost of the package.
        bdix_limit (int): The BDIX-limited FTP limit in GB.
        tv_access (bool): Whether TV access is included.
    """

    def __init__(self, name, base_cost, bdix_limit, tv_access):
        """
        Initializes the InternetPackage with the provided details.

        Args:
            name (str): The name of the package.
            base_cost (float): The base monthly cost of the package.
            bdix_limit (int): The BDIX-limited FTP limit in GB.
            tv_access (bool): Whether TV access is included.
        """
        self.name = name
        self.base_cost = base_cost
        self.bdix_limit = bdix_limit
        self.tv_access = tv_access

    def calculate_cost(self):
        """
        Calculate the total cost of the package.

        Returns:
            float: The total monthly cost of the package.
        """
        return self.base_cost


class InternetCostCalculator:
    """
    A class to calculate and display internet costs for different packages.
    """

    def __init__(self):
        """
        Initializes the InternetCostCalculator with predefined packages.
        """
        self.packages = [
            InternetPackage("Bronze", 1000, 50, False),
            InternetPackage("Silver", 1500, 100, True),
            InternetPackage("Gold", 2000, 150, True),
            InternetPackage("Diamond", 2500, 200, True),
        ]

    def display_packages(self):
        """
        Display the details of all available internet packages.
        """
        print("Available Internet Packages:")
        for package in self.packages:
            tv_info = "Included" if package.tv_access else "Not Included"
            print(f"{package.name}: Cost = {package.base_cost} BDT, "
                  f"BDIX Limit = {package.bdix_limit} GB, TV Access = {tv_info}")

    def calculate_total_cost(self):
        """
        Calculate and display the total cost for each package.
        """
        print("\nMonthly Costs:")
        for package in self.packages:
            print(f"{package.name}: {package.calculate_cost()} BDT")


def main():
    """
    Main function to run the internet cost calculator program.
    """
    try:
        calculator = InternetCostCalculator()
        calculator.display_packages()
        calculator.calculate_total_cost()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
