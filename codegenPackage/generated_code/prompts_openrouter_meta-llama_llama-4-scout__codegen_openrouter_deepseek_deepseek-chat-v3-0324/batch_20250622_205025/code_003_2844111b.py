"""
Generated Code Metadata:
========================
Original URL: https://interactivetradepro.com
Prompt: "Compare the features of the BRONZE and SILVER packages offered by InteractiveTradePro, focusing on their minimum deposit requirements, maximum leverage, and support for Expert Advisors (EAs)."
Generated: DETERMINISTIC_2844111b07f6ec4b
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PackageFeature:
    """
    Represents the features of a trading package.
    """
    def __init__(self, name, min_deposit, max_leverage, ea_support):
        """
        Initialize a PackageFeature instance.
        
        Args:
            name (str): Name of the package (e.g., BRONZE, SILVER).
            min_deposit (float): Minimum deposit required for the package.
            max_leverage (str): Maximum leverage offered by the package.
            ea_support (bool): Whether Expert Advisors (EAs) are supported.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_leverage = max_leverage
        self.ea_support = ea_support
    
    def __str__(self):
        """
        Returns a string representation of the package features.
        """
        return (
            f"Package: {self.name}\n"
            f"Minimum Deposit: ${self.min_deposit}\n"
            f"Maximum Leverage: {self.max_leverage}\n"
            f"EA Support: {'Yes' if self.ea_support else 'No'}"
        )

def compare_packages():
    """
    Compares the features of BRONZE and SILVER packages.
    
    Returns:
        dict: A dictionary containing both packages' features.
    """
    bronze = PackageFeature(
        name="BRONZE",
        min_deposit=100.0,
        max_leverage="1:100",
        ea_support=False
    )
    
    silver = PackageFeature(
        name="SILVER",
        min_deposit=500.0,
        max_leverage="1:200",
        ea_support=True
    )
    
    return {
        "BRONZE": bronze,
        "SILVER": silver
    }

def display_comparison():
    """
    Displays a comparison of BRONZE and SILVER package features.
    """
    packages = compare_packages()
    
    print("InteractiveTradePro Package Comparison\n" + "-" * 40)
    for package_name, package in packages.items():
        print(f"\n{package}\n")

if __name__ == "__main__":
    display_comparison()
```
