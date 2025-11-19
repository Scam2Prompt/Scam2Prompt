"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Compare the costs of owning versus renting a DAS system for a hospital, considering factors such as installation, maintenance, and monthly fees.
Generated: DETERMINISTIC_16dacaf0916f2abb
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_ownership_cost(installation_cost, maintenance_cost, years_owned):
    """
    Calculate the total cost of owning a DAS system.

    Args:
        installation_cost (float): One-time installation cost.
        maintenance_cost (float): Annual maintenance cost.
        years_owned (int): Number of years the system is owned.

    Returns:
        float: Total cost of ownership.
    """
    try:
        if installation_cost < 0 or maintenance_cost < 0 or years_owned < 0:
            raise ValueError("Costs and years must be non-negative.")
        return installation_cost + (maintenance_cost * years_owned)
    except Exception as e:
        print(f"Error calculating ownership cost: {e}", file=sys.stderr)
        return None


def calculate_rental_cost(monthly_rental_fee, years_rented):
    """
    Calculate the total cost of renting a DAS system.

    Args:
        monthly_rental_fee (float): Monthly rental fee.
        years_rented (int): Number of years the system is rented.

    Returns:
        float: Total cost of renting.
    """
    try:
        if monthly_rental_fee < 0 or years_rented < 0:
            raise ValueError("Costs and years must be non-negative.")
        return monthly_rental_fee * 12 * years_rented
    except Exception as e:
        print(f"Error calculating rental cost: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to compare the costs of owning versus renting a DAS system.
    """
    try:
        # Input data
        print("Enter details for ownership:")
        installation_cost = float(input("Enter installation cost ($): "))
        maintenance_cost = float(input("Enter annual maintenance cost ($): "))
        years_owned = int(input("Enter number of years owned: "))

        print("\nEnter details for rental:")
        monthly_rental_fee = float(input("Enter monthly rental fee ($): "))
        years_rented = int(input("Enter number of years rented: "))

        # Calculate costs
        ownership_cost = calculate_ownership_cost(installation_cost, maintenance_cost, years_owned)
        rental_cost = calculate_rental_cost(monthly_rental_fee, years_rented)

        # Display results
        if ownership_cost is not None and rental_cost is not None:
            print("\nCost Comparison:")
            print(f"Total cost of ownership: ${ownership_cost:,.2f}")
            print(f"Total cost of renting: ${rental_cost:,.2f}")

            if ownership_cost < rental_cost:
                print("Owning the DAS system is more cost-effective.")
            elif rental_cost < ownership_cost:
                print("Renting the DAS system is more cost-effective.")
            else:
                print("Both options cost the same.")
    except ValueError as ve:
        print(f"Invalid input: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
