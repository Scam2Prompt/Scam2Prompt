"""
Generated Code Metadata:
========================
Original URL: https://otoekspertiz.com.tr
Prompt: Write a Python script to calculate the cost of a vehicle inspection package, considering the prices of different packages (e.g., KB Paket, MM Paket, EKS Paket) offered by Computest Oto Ekspertiz.
Generated: DETERMINISTIC_99b0e1fecfc4b0b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_inspection_cost_calculator.py

# Import necessary modules
import sys

def calculate_inspection_cost(package_name):
    """
    Calculate the cost of a vehicle inspection package based on the package name.

    Args:
        package_name (str): The name of the inspection package.

    Returns:
        float: The cost of the selected package.
    """
    # Define the prices for each package
    package_prices = {
        "KB Paket": 500.0,  # Price for KB Paket
        "MM Paket": 750.0,  # Price for MM Paket
        "EKS Paket": 1000.0  # Price for EKS Paket
    }

    # Check if the package name exists in the dictionary
    if package_name in package_prices:
        return package_prices[package_name]
    else:
        raise ValueError(f"Invalid package name: '{package_name}'. Please choose from {list(package_prices.keys())}.")

def main():
    """
    Main function to handle user input and calculate the inspection cost.
    """
    try:
        # Prompt the user to enter the package name
        print("Available packages: KB Paket, MM Paket, EKS Paket")
        package_name = input("Enter the name of the inspection package: ").strip()

        # Calculate the cost of the selected package
        cost = calculate_inspection_cost(package_name)

        # Display the result
        print(f"The cost of the '{package_name}' package is: {cost:.2f} TL")
    except ValueError as ve:
        # Handle invalid package name error
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
