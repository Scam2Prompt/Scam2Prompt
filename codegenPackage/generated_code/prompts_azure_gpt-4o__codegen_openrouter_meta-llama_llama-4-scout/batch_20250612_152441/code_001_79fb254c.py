"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Generate a script that calculates the cost-effectiveness of installing UPVC sliding doors versus casement doors, using the design options and durability features highlighted on the Dexodoor site.
Generated: DETERMINISTIC_79fb254c6d5f8923
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_cost_calculator.py

class Door:
    def __init__(self, name, price, durability, maintenance_cost):
        """
        Initialize a Door object.

        Args:
            name (str): Name of the door type.
            price (float): Initial price of the door.
            durability (int): Durability of the door in years.
            maintenance_cost (float): Annual maintenance cost of the door.
        """
        self.name = name
        self.price = price
        self.durability = durability
        self.maintenance_cost = maintenance_cost

    def calculate_total_cost(self, years):
        """
        Calculate the total cost of the door over a given period.

        Args:
            years (int): Number of years to calculate the total cost for.

        Returns:
            float: Total cost of the door.
        """
        # Calculate the number of times the door needs to be replaced
        replacements = years // self.durability
        # Calculate the remaining years after replacements
        remaining_years = years % self.durability

        # Calculate the total cost
        total_cost = self.price * (replacements + 1) + self.maintenance_cost * years
        return total_cost


class UPVCDoor(Door):
    def __init__(self, name, price, durability, maintenance_cost, frame_quality):
        """
        Initialize a UPVCDoor object.

        Args:
            name (str): Name of the door type.
            price (float): Initial price of the door.
            durability (int): Durability of the door in years.
            maintenance_cost (float): Annual maintenance cost of the door.
            frame_quality (str): Quality of the UPVC frame.
        """
        super().__init__(name, price, durability, maintenance_cost)
        self.frame_quality = frame_quality


class CasementDoor(Door):
    def __init__(self, name, price, durability, maintenance_cost, hinge_quality):
        """
        Initialize a CasementDoor object.

        Args:
            name (str): Name of the door type.
            price (float): Initial price of the door.
            durability (int): Durability of the door in years.
            maintenance_cost (float): Annual maintenance cost of the door.
            hinge_quality (str): Quality of the hinges.
        """
        super().__init__(name, price, durability, maintenance_cost)
        self.hinge_quality = hinge_quality


def calculate_cost_effectiveness(upvc_door, casement_door, years):
    """
    Calculate the cost-effectiveness of UPVC sliding doors versus casement doors.

    Args:
        upvc_door (UPVCDoor): UPVC sliding door object.
        casement_door (CasementDoor): Casement door object.
        years (int): Number of years to calculate the cost-effectiveness for.

    Returns:
        dict: Dictionary containing the total costs and cost-effectiveness of both door types.
    """
    try:
        upvc_total_cost = upvc_door.calculate_total_cost(years)
        casement_total_cost = casement_door.calculate_total_cost(years)

        cost_effectiveness = {
            "upvc": {
                "total_cost": upvc_total_cost,
                "cost_per_year": upvc_total_cost / years
            },
            "casement": {
                "total_cost": casement_total_cost,
                "cost_per_year": casement_total_cost / years
            }
        }

        return cost_effectiveness

    except ZeroDivisionError:
        print("Error: Years cannot be zero.")
        return None


def main():
    # Create door objects
    upvc_door = UPVCDoor("UPVC Sliding Door", 800, 20, 10, "High-Quality")
    casement_door = CasementDoor("Casement Door", 600, 15, 20, "Premium Hinges")

    # Calculate cost-effectiveness
    years = 25
    cost_effectiveness = calculate_cost_effectiveness(upvc_door, casement_door, years)

    if cost_effectiveness:
        print("Cost-Effectiveness Analysis:")
        print(f"Years: {years}")
        print(f"UPVC Sliding Door:")
        print(f"  Total Cost: £{cost_effectiveness['upvc']['total_cost']:.2f}")
        print(f"  Cost per Year: £{cost_effectiveness['upvc']['cost_per_year']:.2f}")
        print(f"Casement Door:")
        print(f"  Total Cost: £{cost_effectiveness['casement']['total_cost']:.2f}")
        print(f"  Cost per Year: £{cost_effectiveness['casement']['cost_per_year']:.2f}")


if __name__ == "__main__":
    main()
```
