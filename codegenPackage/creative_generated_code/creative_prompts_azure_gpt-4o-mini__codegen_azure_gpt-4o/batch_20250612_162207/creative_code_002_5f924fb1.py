"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizwentokyo.pages.dev
Prompt: What are the costs associated with creating a new identity and land in Neo Tokyo, and how can I implement this in a script?
Generated: DETERMINISTIC_5f924fb193cc5696
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
import sys

# Constants - These represent costs associated with creating a new identity and purchasing land in Neo Tokyo.
IDENTITY_CREATION_COST = 5000  # Cost in Neo Tokyo credits to create a new identity.
LAND_PURCHASE_COST = 15000    # Cost in Neo Tokyo credits to purchase land.

def calculate_total_cost(identity_count, land_count):
    """
    Calculate the total cost of creating identities and purchasing land in Neo Tokyo.

    Parameters:
    identity_count (int): Number of identities to create.
    land_count (int): Number of land plots to purchase.

    Returns:
    int: The total cost in Neo Tokyo credits.
    """
    try:
        # Input Validation
        if identity_count < 0 or land_count < 0:
            raise ValueError("Identity count and land count must be non-negative integers.")

        # Calculate the cost
        total_identity_cost = identity_count * IDENTITY_CREATION_COST
        total_land_cost = land_count * LAND_PURCHASE_COST

        return total_identity_cost + total_land_cost

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to execute the script. It prompts the user for input and calculates the total cost.
    """
    try:
        # Prompt the user for the number of identities and land plots
        identity_count = int(input("Enter the number of identities to create: "))
        land_count = int(input("Enter the number of land plots to purchase: "))

        # Calculate the total cost
        total_cost = calculate_total_cost(identity_count, land_count)

        if total_cost is not None:
            print(f"The total cost for {identity_count} identities and {land_count} land plots in Neo Tokyo is: {total_cost} credits.")

    except ValueError:
        print("Invalid input. Please enter valid integers for identity and land counts.")
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
