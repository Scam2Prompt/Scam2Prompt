"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write Python code to calculate the cost estimate for a civil works project, including building painting, tile installation, gypsum board work, and electrical and plumbing services, as described on the AKNAN website.
Generated: DETERMINISTIC_000464cc28579864
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost(area_m2, unit_cost):
    """
    Calculate the cost for a given area and unit cost.

    :param area_m2: float - Area in square meters
    :param unit_cost: float - Cost per square meter
    :return: float - Total cost
    """
    try:
        return round(area_m2 * unit_cost, 2)
    except TypeError:
        raise ValueError("Invalid input: area_m2 and unit_cost must be numbers.")

def get_user_input(prompt):
    """
    Safely get numeric input from the user.

    :param prompt: str - Prompt message for input
    :return: float - Validated numeric input
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def main():
    """
    Main function to calculate the cost estimate for a civil works project.
    """
    print("Civil Works Project Cost Estimation")
    print("Please enter the values below.")

    # Get user inputs for each type of work
    painting_area = get_user_input("Enter the area to be painted (in square meters): ")
    tile_area = get_user_input("Enter the area for tile installation (in square meters): ")
    gypsum_area = get_user_input("Enter the area for gypsum board work (in square meters): ")
    num_rooms_electrical = get_user_input("Enter the number of rooms requiring electrical work: ")
    num_rooms_plumbing = get_user_input("Enter the number of rooms requiring plumbing work: ")

    # Unit costs (typically these would be fetched from a database or configuration file)
    unit_costs = {
        "painting": 15.0,  # Cost per square meter for painting
        "tile_installation": 25.0,  # Cost per square meter for tile installation
        "gypsum_board": 20.0,  # Cost per square meter for gypsum board work
        "electrical_per_room": 100.0,  # Cost per room for electrical work
        "plumbing_per_room": 120.0,  # Cost per room for plumbing work
    }

    try:
        # Calculate costs
        painting_cost = calculate_cost(painting_area, unit_costs["painting"])
        tile_cost = calculate_cost(tile_area, unit_costs["tile_installation"])
        gypsum_cost = calculate_cost(gypsum_area, unit_costs["gypsum_board"])
        electrical_cost = calculate_cost(num_rooms_electrical, unit_costs["electrical_per_room"])
        plumbing_cost = calculate_cost(num_rooms_plumbing, unit_costs["plumbing_per_room"])

        # Total cost calculation
        total_cost = round(
            painting_cost + tile_cost + gypsum_cost + electrical_cost + plumbing_cost, 2
        )

        # Display cost breakdown
        print("\nCost Breakdown:")
        print(f"Painting: ${painting_cost:.2f}")
        print(f"Tile Installation: ${tile_cost:.2f}")
        print(f"Gypsum Board Work: ${gypsum_cost:.2f}")
        print(f"Electrical Work: ${electrical_cost:.2f}")
        print(f"Plumbing Work: ${plumbing_cost:.2f}")
        print(f"\nTotal Estimated Cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
