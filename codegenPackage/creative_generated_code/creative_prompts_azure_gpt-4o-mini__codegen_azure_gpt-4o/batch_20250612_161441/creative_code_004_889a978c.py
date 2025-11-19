"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningapp.pages.dev
Prompt: Create a function that calculates potential earnings based on different mining packages offered by BIG MINING.
Generated: DETERMINISTIC_889a978c095e9ca4
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling
import sys

def calculate_potential_earnings(package, hours):
    """
    Calculate potential earnings based on the mining package and hours provided.

    Parameters:
        package (str): The name of the mining package (e.g., 'Basic', 'Advanced', 'Pro').
        hours (int): The number of hours the mining rig will operate.

    Returns:
        float: The potential earnings in USD.
    """
    try:
        # Validate input parameters
        if not isinstance(package, str):
            raise ValueError("Package must be a string.")
        if not isinstance(hours, int) or hours <= 0:
            raise ValueError("Hours must be a positive integer.")

        # Define the hourly income rates for each mining package
        package_rates = {
            'Basic': 2.5,    # USD per hour
            'Advanced': 5.0, # USD per hour
            'Pro': 10.0      # USD per hour
        }

        # Check if the package exists
        if package not in package_rates:
            raise ValueError(f"Invalid package name: {package}. Available packages are {', '.join(package_rates.keys())}.")

        # Calculate earnings
        hourly_rate = package_rates[package]
        earnings = hourly_rate * hours

        return earnings

    except ValueError as ve:
        # Handle input validation errors
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

# Example usage (uncomment to test)
# print(calculate_potential_earnings('Advanced', 10))  # Expected output: 50.0
# print(calculate_potential_earnings('Pro', 24))       # Expected output: 240.0
# print(calculate_potential_earnings('Invalid', 5))    # Expected output: Error message
```
