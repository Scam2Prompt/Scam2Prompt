"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Write a Python script to calculate the cost of leveling up in STEPN based on the recommended point distribution provided in the blog.
Generated: DETERMINISTIC_3cf4e8e1942f9ff6
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost of leveling up in STEPN based on recommended point distribution.

This script assumes the user enters the cost to level up and the recommended point distribution
for attributes like Efficiency, Luck, Comfort, and Resilience.

Usage:
Run the script and provide inputs when prompted to calculate the total cost based on leveling requirements.
"""

def calculate_level_up_cost(level_costs, point_distribution):
    """
    Calculate the total cost of leveling up based on provided costs and point distribution.

    Args:
        level_costs (list of float): Cost to level up for each level.
        point_distribution (list of dict): Recommended point distribution for each level.
            Each dictionary should contain keys: 'Efficiency', 'Luck', 'Comfort', 'Resilience'.

    Returns:
        float: Total leveling-up cost.
    """
    try:
        total_cost = 0.0

        # Validate inputs
        if len(level_costs) != len(point_distribution):
            raise ValueError("Mismatch between number of level costs and point distributions.")

        for i, cost in enumerate(level_costs):
            distribution = point_distribution[i]

            # Validate point distribution keys
            if not all(key in distribution for key in ['Efficiency', 'Luck', 'Comfort', 'Resilience']):
                raise ValueError(f"Invalid point distribution at level {i + 1}: {distribution}")

            # Calculate cost for current level and add to total cost
            total_cost += cost

        return total_cost

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to handle user input and perform the leveling cost calculation.
    """
    try:
        # Prompt user for input
        print("Welcome to the STEPN Level-Up Cost Calculator!")
        levels = int(input("Enter the number of levels you want to calculate: "))

        if levels <= 0:
            raise ValueError("Number of levels must be greater than 0.")

        level_costs = []
        point_distribution = []

        for i in range(levels):
            cost = float(input(f"Enter the cost to level up for level {i + 1}: "))
            level_costs.append(cost)

            print(f"Enter the recommended point distribution for level {i + 1}:")
            efficiency = int(input("  Efficiency points: "))
            luck = int(input("  Luck points: "))
            comfort = int(input("  Comfort points: "))
            resilience = int(input("  Resilience points: "))

            point_distribution.append({
                'Efficiency': efficiency,
                'Luck': luck,
                'Comfort': comfort,
                'Resilience': resilience
            })

        # Calculate total cost
        total_cost = calculate_level_up_cost(level_costs, point_distribution)

        if total_cost is not None:
            print(f"\nThe total cost of leveling up for {levels} levels is: {total_cost:.2f} GST")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
