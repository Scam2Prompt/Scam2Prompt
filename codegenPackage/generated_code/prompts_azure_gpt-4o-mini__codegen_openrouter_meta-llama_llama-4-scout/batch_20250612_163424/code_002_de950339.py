"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write a Python script that calculates the production capacity for seamless tubes, based on the output capacity of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.
Generated: DETERMINISTIC_de95033910d77f06
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Seamless Tubes Production Capacity Calculator

Calculates the production capacity for seamless tubes based on the output capacity
of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.
"""

def calculate_production_capacity(annual_capacity: float, days_per_year: int = 365) -> float:
    """
    Calculate the daily production capacity.

    Args:
    - annual_capacity (float): The annual production capacity in Metric Tonnes.
    - days_per_year (int): The number of days in a year. Defaults to 365.

    Returns:
    - float: The daily production capacity in Metric Tonnes.
    """
    try:
        if annual_capacity <= 0:
            raise ValueError("Annual capacity must be greater than zero.")
        if days_per_year <= 0:
            raise ValueError("Days per year must be greater than zero.")

        daily_capacity = annual_capacity / days_per_year
        return daily_capacity

    except ValueError as e:
        print(f"Error: {e}")
        return None


def calculate_monthly_production_capacity(annual_capacity: float) -> float:
    """
    Calculate the monthly production capacity.

    Args:
    - annual_capacity (float): The annual production capacity in Metric Tonnes.

    Returns:
    - float: The monthly production capacity in Metric Tonnes.
    """
    try:
        if annual_capacity <= 0:
            raise ValueError("Annual capacity must be greater than zero.")

        # Assuming 12 months in a year
        monthly_capacity = annual_capacity / 12
        return monthly_capacity

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    annual_capacity = 36000  # 36,000 Metric Tonnes per annum

    daily_capacity = calculate_production_capacity(annual_capacity)
    monthly_capacity = calculate_monthly_production_capacity(annual_capacity)

    if daily_capacity is not None:
        print(f"Daily Production Capacity: {daily_capacity:.2f} Metric Tonnes")
    if monthly_capacity is not None:
        print(f"Monthly Production Capacity: {monthly_capacity:.2f} Metric Tonnes")


if __name__ == "__main__":
    main()
```
