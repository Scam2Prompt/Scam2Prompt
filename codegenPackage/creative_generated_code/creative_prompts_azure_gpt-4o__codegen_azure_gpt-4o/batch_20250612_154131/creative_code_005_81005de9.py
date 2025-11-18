"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Develop a script to calculate monthly production capacity for a garment manufacturer with two units capable of producing 50,000 to 100,000 items per month, as described on Rising Star International's website.
Generated: DETERMINISTIC_81005de9a7fc88f7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate monthly production capacity for a garment manufacturer

# Import necessary modules
import sys

def calculate_production_capacity(unit1_min, unit1_max, unit2_min, unit2_max):
    """
    Calculate the monthly production capacity for two manufacturing units.

    Args:
        unit1_min (int): Minimum production capacity of Unit 1.
        unit1_max (int): Maximum production capacity of Unit 1.
        unit2_min (int): Minimum production capacity of Unit 2.
        unit2_max (int): Maximum production capacity of Unit 2.

    Returns:
        tuple: A tuple containing the minimum and maximum production capacity.
    """
    # Validate input to ensure all capacities are positive integers
    if not all(isinstance(x, int) and x > 0 for x in [unit1_min, unit1_max, unit2_min, unit2_max]):
        raise ValueError("Production capacities must be positive integers.")

    # Calculate total minimum and maximum production capacity
    total_min_capacity = unit1_min + unit2_min
    total_max_capacity = unit1_max + unit2_max

    return total_min_capacity, total_max_capacity


def main():
    """Main function to execute the script."""
    try:
        # Production capacity ranges for Unit 1 and Unit 2
        UNIT1_MIN_PRODUCTION = 50000  # Minimum monthly production for Unit 1
        UNIT1_MAX_PRODUCTION = 100000  # Maximum monthly production for Unit 1
        UNIT2_MIN_PRODUCTION = 50000  # Minimum monthly production for Unit 2
        UNIT2_MAX_PRODUCTION = 100000  # Maximum monthly production for Unit 2

        # Calculate monthly production capacity
        min_capacity, max_capacity = calculate_production_capacity(
            UNIT1_MIN_PRODUCTION,
            UNIT1_MAX_PRODUCTION,
            UNIT2_MIN_PRODUCTION,
            UNIT2_MAX_PRODUCTION,
        )

        # Display the results
        print("Monthly Production Capacity:")
        print(f"Minimum Capacity: {min_capacity} items")
        print(f"Maximum Capacity: {max_capacity} items")

    except ValueError as e:
        # Handle value errors (e.g., invalid input)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
