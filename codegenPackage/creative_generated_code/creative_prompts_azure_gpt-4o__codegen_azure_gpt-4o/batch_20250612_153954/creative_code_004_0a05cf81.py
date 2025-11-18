"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write a program to compare air freight and ocean freight delivery times using Uniair Cargo’s estimates for different regions (East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_0a05cf811bb5c4a5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


def get_delivery_time(region, method):
    """
    Function to retrieve estimated delivery time based on region and shipping method.

    Args:
        region (str): The region of delivery (e.g., 'East Asia', 'Europe & USA', 'Southeast Asia').
        method (str): The shipping method ('air' or 'ocean').

    Returns:
        int: Estimated delivery time in days.
    """
    # Estimates for delivery times in days
    estimates = {
        "East Asia": {"air": 2, "ocean": 20},
        "Europe & USA": {"air": 5, "ocean": 30},
        "Southeast Asia": {"air": 3, "ocean": 15},
    }

    # Check if region and method are valid
    if region not in estimates:
        raise ValueError(f"Invalid region: {region}. Valid regions are: {', '.join(estimates.keys())}.")
    if method not in estimates[region]:
        raise ValueError(f"Invalid shipping method: {method}. Valid methods are 'air' and 'ocean'.")

    return estimates[region][method]


def compare_delivery_times(region):
    """
    Function to compare air freight and ocean freight delivery times for a given region.

    Args:
        region (str): The region of delivery (e.g., 'East Asia', 'Europe & USA', 'Southeast Asia').

    Returns:
        str: Comparison message indicating the delivery times for air and ocean freight.
    """
    try:
        air_time = get_delivery_time(region, "air")
        ocean_time = get_delivery_time(region, "ocean")
        return (
            f"In {region}, air freight takes approximately {air_time} days, "
            f"while ocean freight takes approximately {ocean_time} days."
        )
    except ValueError as e:
        return str(e)


def main():
    """
    Main function to prompt the user for input and display delivery time comparisons.
    """
    print("Welcome to Uniair Cargo's delivery time comparison tool!")
    print("Available regions: East Asia, Europe & USA, Southeast Asia.\n")

    while True:
        # Get user input for region
        region = input("Enter the region to compare delivery times (or 'exit' to quit): ").strip()

        # Check if the user wants to exit
        if region.lower() == "exit":
            print("Thank you for using the tool. Goodbye!")
            sys.exit()

        # Provide comparison for the region
        comparison = compare_delivery_times(region)
        print(comparison, "\n")


if __name__ == "__main__":
    main()
```
