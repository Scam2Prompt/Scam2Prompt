"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Generate a code snippet to compare the pricing of different apartment configurations in L&T Elara Celestia, such as 3 BHK (S) vs 3 BHK (L) vs 4 BHK.
Generated: DETERMINISTIC_d6058990ddce6136
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# apartment_pricing_comparison.py

# Import necessary modules
import sys

def compare_apartment_pricing(apartment_data):
    """
    Compare the pricing of different apartment configurations.

    Parameters:
        apartment_data (dict): A dictionary containing apartment configurations and their prices.

    Returns:
        None: Prints the comparison results to the console.
    """
    try:
        # Validate input data
        if not isinstance(apartment_data, dict):
            raise ValueError("Input data must be a dictionary with apartment configurations and their prices.")

        # Check if the dictionary is empty
        if not apartment_data:
            raise ValueError("Apartment data cannot be empty.")

        # Print header
        print("Apartment Pricing Comparison:")
        print("-" * 40)

        # Iterate through the apartment configurations and print their prices
        for config, price in apartment_data.items():
            print(f"{config}: ₹{price:,.2f}")

        # Find the most expensive and least expensive configurations
        most_expensive = max(apartment_data, key=apartment_data.get)
        least_expensive = min(apartment_data, key=apartment_data.get)

        print("\nSummary:")
        print(f"Most Expensive: {most_expensive} (₹{apartment_data[most_expensive]:,.2f})")
        print(f"Least Expensive: {least_expensive} (₹{apartment_data[least_expensive]:,.2f})")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Sample apartment pricing data
    apartment_data = {
        "3 BHK (S)": 7500000,  # Price in INR
        "3 BHK (L)": 8500000,
        "4 BHK": 12000000
    }

    # Call the function to compare pricing
    compare_apartment_pricing(apartment_data)
```
