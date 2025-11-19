"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write Python code to calculate weekly mileage progression for a 100-mile running training plan, including peak weeks reaching 70-100 miles, as described on Boost Running.
Generated: DETERMINISTIC_4c147cf41878c65d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates weekly mileage progression for a 100-mile running training plan.

The plan is based on a 20-week progression with peak weeks reaching 70-100 miles.
It assumes a base weekly mileage and a maximum weekly mileage.

The progression is calculated as follows:
- Weeks 1-4: Base mileage + 10% increase each week
- Weeks 5-8: Previous week's mileage + 10% increase each week
- Weeks 9-12: Previous week's mileage + 5% increase each week
- Weeks 13-16: Previous week's mileage + 5% increase each week
- Weeks 17-20: Previous week's mileage, capped at 100 miles

This code follows best practices for Python and includes proper error handling.
"""

def calculate_weekly_mileage(base_mileage, max_mileage):
    """
    Calculates weekly mileage progression.

    Args:
        base_mileage (float): The base weekly mileage.
        max_mileage (float): The maximum weekly mileage.

    Returns:
        list: A list of weekly mileage values.

    Raises:
        ValueError: If base_mileage or max_mileage is not a positive number.
    """
    if base_mileage <= 0 or max_mileage <= 0:
        raise ValueError("Base mileage and max mileage must be positive numbers.")

    weekly_mileage = []
    current_mileage = base_mileage

    # Weeks 1-4: Base mileage + 10% increase each week
    for _ in range(4):
        weekly_mileage.append(round(current_mileage, 2))
        current_mileage *= 1.1

    # Weeks 5-8: Previous week's mileage + 10% increase each week
    for _ in range(4):
        weekly_mileage.append(round(current_mileage, 2))
        current_mileage *= 1.1

    # Weeks 9-12: Previous week's mileage + 5% increase each week
    for _ in range(4):
        weekly_mileage.append(round(current_mileage, 2))
        current_mileage *= 1.05

    # Weeks 13-16: Previous week's mileage + 5% increase each week
    for _ in range(4):
        weekly_mileage.append(round(current_mileage, 2))
        current_mileage *= 1.05

    # Weeks 17-20: Previous week's mileage, capped at 100 miles
    for _ in range(4):
        weekly_mileage.append(round(min(current_mileage, max_mileage), 2))

    return weekly_mileage


def main():
    base_mileage = 30  # Base weekly mileage
    max_mileage = 100  # Maximum weekly mileage

    try:
        weekly_mileage = calculate_weekly_mileage(base_mileage, max_mileage)
        print("Weekly Mileage Progression:")
        for i, mileage in enumerate(weekly_mileage, start=1):
            print(f"Week {i}: {mileage} miles")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
