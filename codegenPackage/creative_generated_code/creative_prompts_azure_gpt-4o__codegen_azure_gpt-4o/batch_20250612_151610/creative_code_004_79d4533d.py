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
# MARUF ONLINE BD Internet Cost Calculator
# Author: [Your Name]
# Date: [Date]

# This program calculates the monthly internet cost for different packages
# (Bronze, Silver, Gold, Diamond) offered by MARUF ONLINE BD.
# It includes features such as BDIX-limited FTP and TV access in the cost calculation.

# Constants for package details
PACKAGES = {
    "Bronze": {"speed_mbps": 10, "base_cost": 500, "ftp_access": False, "tv_access": False},
    "Silver": {"speed_mbps": 20, "base_cost": 800, "ftp_access": True, "tv_access": False},
    "Gold": {"speed_mbps": 50, "base_cost": 1200, "ftp_access": True, "tv_access": True},
    "Diamond": {"speed_mbps": 100, "base_cost": 2000, "ftp_access": True, "tv_access": True},
}

# Additional costs for extra features
FEATURE_COSTS = {
    "ftp_access": 100,  # Cost for BDIX-limited FTP access
    "tv_access": 200,   # Cost for TV access
}

def calculate_package_cost(package_name):
    """
    Calculates the monthly cost for the given package.
    
    Args:
        package_name (str): Name of the package (Bronze, Silver, Gold, Diamond).
    
    Returns:
        float: Total monthly cost for the package.
    """
    if package_name not in PACKAGES:
        raise ValueError(f"Invalid package name: {package_name}. Available packages: {', '.join(PACKAGES.keys())}")
    
    package = PACKAGES[package_name]
    total_cost = package["base_cost"]
    
    # Add costs for additional features if applicable
    if package["ftp_access"]:
        total_cost += FEATURE_COSTS["ftp_access"]
    if package["tv_access"]:
        total_cost += FEATURE_COSTS["tv_access"]
    
    return total_cost

def display_packages():
    """
    Displays the available packages with their details.
    """
    print("Available Internet Packages:")
    for package_name, details in PACKAGES.items():
        print(f"{package_name}:")
        print(f"  Speed: {details['speed_mbps']} Mbps")
        print(f"  Base Cost: {details['base_cost']} BDT")
        print(f"  BDIX-limited FTP Access: {'Yes' if details['ftp_access'] else 'No'}")
        print(f"  TV Access: {'Yes' if details['tv_access'] else 'No'}")
        print()

def main():
    """
    Main function to run the internet cost calculator.
    """
    print("Welcome to MARUF ONLINE BD Internet Cost Calculator!")
    display_packages()
    
    try:
        # Get user input for package selection
        selected_package = input("Enter the name of the package you want to calculate the cost for: ").strip()
        total_cost = calculate_package_cost(selected_package)
        print(f"The total monthly cost for the {selected_package} package is: {total_cost} BDT")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the program
    main()
```
