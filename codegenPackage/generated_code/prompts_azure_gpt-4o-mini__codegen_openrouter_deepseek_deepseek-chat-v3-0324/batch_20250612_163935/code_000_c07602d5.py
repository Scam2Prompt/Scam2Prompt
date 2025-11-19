"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Write a Python script to calculate the cost of air conditioning repair services based on the pricing structure provided by RJW Mechanical in Fayetteville.
Generated: DETERMINISTIC_c07602d51a321f35
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RJW Mechanical Air Conditioning Repair Cost Calculator

This script calculates the cost of air conditioning repair services based on RJW Mechanical's pricing structure.
The pricing includes service call fees, labor costs, and parts costs with optional emergency service charges.

Pricing Structure:
- Service Call Fee: $75 (standard hours), $125 (after hours)
- Labor Cost: $85/hour (first hour), $65/hour (additional hours)
- Parts Cost: Actual cost + 20% markup
- Emergency Service: Additional $100 (if applicable)
"""

def calculate_repair_cost(
    hours_worked: float,
    parts_cost: float,
    is_after_hours: bool = False,
    is_emergency: bool = False
) -> float:
    """
    Calculate the total cost of air conditioning repair services.

    Args:
        hours_worked: Total hours of labor (must be >= 0.5)
        parts_cost: Cost of parts before markup (must be >= 0)
        is_after_hours: Whether service is during after-hours (default: False)
        is_emergency: Whether service is an emergency (default: False)

    Returns:
        Total repair cost as a float

    Raises:
        ValueError: If hours_worked or parts_cost are invalid
    """
    # Validate input parameters
    if hours_worked < 0.5:
        raise ValueError("Minimum labor charge is for 0.5 hours")
    if parts_cost < 0:
        raise ValueError("Parts cost cannot be negative")

    # Calculate service call fee
    service_call_fee = 125.0 if is_after_hours else 75.0

    # Calculate labor cost
    if hours_worked <= 1:
        labor_cost = 85.0 * hours_worked
    else:
        labor_cost = 85.0 + (65.0 * (hours_worked - 1))

    # Calculate parts cost with markup
    parts_cost_with_markup = parts_cost * 1.2

    # Calculate emergency fee if applicable
    emergency_fee = 100.0 if is_emergency else 0.0

    # Calculate total cost
    total_cost = (
        service_call_fee
        + labor_cost
        + parts_cost_with_markup
        + emergency_fee
    )

    return round(total_cost, 2)


def main():
    """Main function to demonstrate the cost calculation."""
    try:
        print("RJW Mechanical AC Repair Cost Calculator")
        print("----------------------------------------")

        # Get user input
        hours = float(input("Enter hours worked (minimum 0.5): "))
        parts = float(input("Enter parts cost: $"))
        after_hours = input("After hours service? (y/n): ").lower() == 'y'
        emergency = input("Emergency service? (y/n): ").lower() == 'y'

        # Calculate and display cost
        total = calculate_repair_cost(hours, parts, after_hours, emergency)
        print(f"\nTotal Repair Cost: ${total:.2f}")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
