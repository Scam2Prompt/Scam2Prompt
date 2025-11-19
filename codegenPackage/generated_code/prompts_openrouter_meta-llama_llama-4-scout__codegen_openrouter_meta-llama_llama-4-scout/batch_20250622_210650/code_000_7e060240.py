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
"""
Coffin Transfer Cost Calculator within Europe

Calculates the cost of coffin transfer within Europe based on distance,
considering a base price of €1000 and an additional €2.00-€2.50 per kilometer.
"""

def calculate_transfer_cost(distance_km, rate_per_km=2.25):
    """
    Calculates the total cost of coffin transfer.

    Args:
        distance_km (float): Distance of transfer in kilometers.
        rate_per_km (float, optional): Rate per kilometer. Defaults to 2.25.

    Returns:
        float: Total cost of coffin transfer.

    Raises:
        ValueError: If distance or rate per kilometer is negative.
    """
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    if rate_per_km < 0:
        raise ValueError("Rate per kilometer cannot be negative.")

    base_price = 1000.00
    total_cost = base_price + (distance_km * rate_per_km)
    return round(total_cost, 2)


def main():
    try:
        distance_km = float(input("Enter the distance of transfer in kilometers: "))
        rate_per_km = float(input("Enter the rate per kilometer (€2.00-€2.50), default is €2.25: ") or 2.25)

        if rate_per_km < 2.00 or rate_per_km > 2.50:
            print("Please enter a rate between €2.00 and €2.50.")
            return

        total_cost = calculate_transfer_cost(distance_km, rate_per_km)
        print(f"The total cost of coffin transfer is: €{total_cost}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
