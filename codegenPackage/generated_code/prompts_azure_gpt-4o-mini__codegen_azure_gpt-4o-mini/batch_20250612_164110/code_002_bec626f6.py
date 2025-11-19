"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function that calculates the best rubber flooring type for different sports facilities, referencing the unique characteristics of products like Eva Mats and Rubber Tiles.
Generated: DETERMINISTIC_bec626f64953a431
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FlooringType:
    """Class to represent different types of rubber flooring."""
    
    def __init__(self, name, durability, shock_absorption, cost):
        """
        Initialize a new flooring type.

        :param name: Name of the flooring type
        :param durability: Durability rating (1-10)
        :param shock_absorption: Shock absorption rating (1-10)
        :param cost: Cost per square meter
        """
        self.name = name
        self.durability = durability
        self.shock_absorption = shock_absorption
        self.cost = cost

    def __repr__(self):
        return f"{self.name}(Durability: {self.durability}, Shock Absorption: {self.shock_absorption}, Cost: {self.cost})"


def recommend_flooring(sport_type):
    """
    Recommend the best rubber flooring type based on the sport facility requirements.

    :param sport_type: The type of sport (e.g., 'gymnastics', 'basketball', 'weightlifting')
    :return: Recommended flooring type
    :raises ValueError: If the sport type is not recognized
    """
    # Define flooring options
    flooring_options = {
        'Eva Mats': FlooringType('Eva Mats', durability=7, shock_absorption=9, cost=20),
        'Rubber Tiles': FlooringType('Rubber Tiles', durability=8, shock_absorption=8, cost=15),
        'Interlocking Mats': FlooringType('Interlocking Mats', durability=6, shock_absorption=7, cost=18),
        'Roll Flooring': FlooringType('Roll Flooring', durability=9, shock_absorption=6, cost=12)
    }

    # Define sport requirements
    sport_requirements = {
        'gymnastics': {'min_durability': 6, 'min_shock_absorption': 8},
        'basketball': {'min_durability': 7, 'min_shock_absorption': 6},
        'weightlifting': {'min_durability': 8, 'min_shock_absorption': 5}
    }

    # Check if the sport type is valid
    if sport_type not in sport_requirements:
        raise ValueError(f"Sport type '{sport_type}' is not recognized. Please choose from {list(sport_requirements.keys())}.")

    # Get the requirements for the specified sport
    requirements = sport_requirements[sport_type]

    # Find the best flooring option based on requirements
    best_flooring = None
    for flooring in flooring_options.values():
        if (flooring.durability >= requirements['min_durability'] and
                flooring.shock_absorption >= requirements['min_shock_absorption']):
            if best_flooring is None or flooring.cost < best_flooring.cost:
                best_flooring = flooring

    return best_flooring


# Example usage
if __name__ == "__main__":
    try:
        sport = 'gymnastics'
        recommended_flooring = recommend_flooring(sport)
        print(f"The recommended flooring for {sport} is: {recommended_flooring}")
    except ValueError as e:
        print(e)
```
