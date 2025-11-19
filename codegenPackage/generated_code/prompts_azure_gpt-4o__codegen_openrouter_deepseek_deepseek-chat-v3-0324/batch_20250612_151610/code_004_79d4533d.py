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
class InternetPackage:
    """
    Represents an internet package with its features and cost.
    """
    def __init__(self, name, speed, monthly_cost, bdix_ftp=False, tv_access=False):
        """
        Initialize an internet package.
        
        Args:
            name (str): Name of the package (e.g., Bronze, Silver)
            speed (str): Internet speed (e.g., "10 Mbps")
            monthly_cost (float): Monthly cost in BDT
            bdix_ftp (bool): Whether BDIX-limited FTP is included
            tv_access (bool): Whether TV access is included
        """
        self.name = name
        self.speed = speed
        self.monthly_cost = monthly_cost
        self.bdix_ftp = bdix_ftp
        self.tv_access = tv_access
    
    def get_features(self):
        """
        Returns a dictionary of package features.
        """
        return {
            "Name": self.name,
            "Speed": self.speed,
            "Monthly Cost (BDT)": self.monthly_cost,
            "BDIX-limited FTP": "Yes" if self.bdix_ftp else "No",
            "TV Access": "Yes" if self.tv_access else "No"
        }


class MARUFOnlineBD:
    """
    Main class to manage internet packages and calculate costs.
    """
    def __init__(self):
        """
        Initialize with predefined packages.
        """
        self.packages = {
            "Bronze": InternetPackage(
                name="Bronze",
                speed="10 Mbps",
                monthly_cost=500.00,
                bdix_ftp=False,
                tv_access=False
            ),
            "Silver": InternetPackage(
                name="Silver",
                speed="20 Mbps",
                monthly_cost=800.00,
                bdix_ftp=True,
                tv_access=False
            ),
            "Gold": InternetPackage(
                name="Gold",
                speed="30 Mbps",
                monthly_cost=1200.00,
                bdix_ftp=True,
                tv_access=True
            ),
            "Diamond": InternetPackage(
                name="Diamond",
                speed="50 Mbps",
                monthly_cost=2000.00,
                bdix_ftp=True,
                tv_access=True
            )
        }
    
    def get_package(self, package_name):
        """
        Retrieve a package by name.
        
        Args:
            package_name (str): Name of the package
            
        Returns:
            InternetPackage: The requested package
            
        Raises:
            ValueError: If package name is invalid
        """
        package = self.packages.get(package_name)
        if not package:
            raise ValueError(f"Invalid package name: {package_name}")
        return package
    
    def calculate_monthly_cost(self, package_name, months=1):
        """
        Calculate the total cost for a given package over specified months.
        
        Args:
            package_name (str): Name of the package
            months (int): Number of months (default: 1)
            
        Returns:
            float: Total cost in BDT
            
        Raises:
            ValueError: If package name is invalid or months is <= 0
        """
        if months <= 0:
            raise ValueError("Number of months must be positive")
        
        package = self.get_package(package_name)
        return package.monthly_cost * months
    
    def display_packages(self):
        """
        Display all available packages with their features.
        """
        print("Available Internet Packages:")
        print("-" * 50)
        for package in self.packages.values():
            features = package.get_features()
            for key, value in features.items():
                print(f"{key}: {value}")
            print("-" * 50)


def main():
    """
    Main function to demonstrate the package calculation.
    """
    maruf_online = MARUFOnlineBD()
    
    while True:
        try:
            print("\nMARUF ONLINE BD - Internet Package Calculator")
            print("1. View Packages")
            print("2. Calculate Monthly Cost")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                maruf_online.display_packages()
            elif choice == "2":
                package_name = input("Enter package name (Bronze/Silver/Gold/Diamond): ").strip().capitalize()
                months = int(input("Enter number of months: "))
                
                total_cost = maruf_online.calculate_monthly_cost(package_name, months)
                print(f"\nTotal cost for {package_name} package for {months} month(s): BDT {total_cost:.2f}")
            elif choice == "3":
                print("Thank you for using MARUF ONLINE BD!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
