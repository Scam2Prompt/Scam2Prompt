"""
Generated Code Metadata:
========================
Original URL: https://seelenschnell.site
Prompt: Write a Python script to calculate the cost of coffin transfer within Europe based on distance, considering a base price of €1000 and an additional €2.00-€2.50 per kilometer.
Generated: DETERMINISTIC_7e06024070d864e2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_transfer_cost(distance_km, price_per_km_range=(2.00, 2.50), base_price=1000):
    """
    Calculate the cost of coffin transfer within Europe based on distance.

    Parameters:
        distance_km (float): The distance in kilometers for the transfer.
        price_per_km_range (tuple): A tuple containing the minimum and maximum price per kilometer.
        base_price (float): The base price for the transfer.

    Returns:
        float: The total cost of the transfer.
    """
    try:
        # Validate input
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        if not (isinstance(price_per_km_range, tuple) and len(price_per_km_range) == 2):
            raise ValueError("Price per kilometer range must be a tuple with two values.")
        if price_per_km_range[0] > price_per_km_range[1]:
            raise ValueError("Invalid price range: minimum price cannot exceed maximum price.")

        # Calculate the cost
        avg_price_per_km = sum(price_per_km_range) / 2  # Average price per kilometer
        total_cost = base_price + (avg_price_per_km * distance_km)
        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate coffin transfer cost.
    """
    print("Welcome to the Coffin Transfer Cost Calculator!")
    try:
        # Get user input for distance
        distance_km = float(input("Enter the distance in kilometers: "))
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")

        # Calculate the cost
        cost = calculate_transfer_cost(distance_km)
        print(f"The total cost of the transfer is: €{cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
