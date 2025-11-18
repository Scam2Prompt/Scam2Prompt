"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stuff-artgobblers.com
Prompt: Develop a Python program to calculate ROI for SEM campaigns, using measurable results as emphasized by ACE Digital Marketing Agency.
Generated: DETERMINISTIC_6e20aa968e5d4374
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_roi(revenue, cost):
    """
    Calculate Return on Investment (ROI) for SEM campaigns.

    Args:
        revenue (float): Total revenue generated from the SEM campaign.
        cost (float): Total cost incurred for the SEM campaign.

    Returns:
        float: ROI percentage or None if input values are invalid.
    """
    try:
        # Validate inputs
        if revenue < 0 or cost < 0:
            raise ValueError("Revenue and cost must be non-negative numbers.")

        # Handle the edge case where cost is zero
        if cost == 0:
            return float('inf')  # Infinite ROI when no cost is incurred

        # Calculate ROI
        roi = ((revenue - cost) / cost) * 100  # ROI as a percentage
        return roi

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to handle user input and calculate ROI.
    """
    print("Welcome to the SEM Campaign ROI Calculator!")

    try:
        # Get user input for revenue and cost
        revenue = float(input("Enter the total revenue generated from the SEM campaign: "))
        cost = float(input("Enter the total cost incurred for the SEM campaign: "))

        # Calculate ROI
        roi = calculate_roi(revenue, cost)

        if roi is None:
            print("Unable to calculate ROI due to invalid input.")
        elif roi == float('inf'):
            print("ROI is infinite (no cost incurred).")
        else:
            print(f"The ROI for your SEM campaign is: {roi:.2f}%")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for revenue and cost.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Run the main program
    main()
```
