"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write a function to recommend alternative metal fittings (e.g., Hastelloy C276 Round Bars or Inconel Alloy 600 Pipes) based on user preferences for durability and corrosion resistance, as described on the Dinkar Alloys webpage.
Generated: DETERMINISTIC_529b92babce325bd
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MetalFitting:
    """
    A class representing a metal fitting with attributes for name, durability, and corrosion resistance.
    """

    def __init__(self, name: str, durability: int, corrosion_resistance: int):
        """
        Initializes a MetalFitting instance.

        :param name: The name of the metal fitting.
        :param durability: The durability rating of the fitting (1 to 10).
        :param corrosion_resistance: The corrosion resistance rating of the fitting (1 to 10).
        """
        self.name = name
        self.durability = durability
        self.corrosion_resistance = corrosion_resistance


def recommend_metal_fittings(preferred_durability: int, preferred_corrosion: int, fittings: list) -> list:
    """
    Recommends alternative metal fittings based on user preferences for durability and corrosion resistance.

    :param preferred_durability: The user's preferred durability rating (1 to 10).
    :param preferred_corrosion: The user's preferred corrosion resistance rating (1 to 10).
    :param fittings: A list of MetalFitting objects to evaluate against user preferences.
    :return: A list of recommended MetalFitting objects that match user's preferences.
    :raises ValueError: If input ratings are not in the range of 1 to 10.
    """
    
    # Validate input ranges
    if not (1 <= preferred_durability <= 10):
        raise ValueError("Preferred durability must be between 1 and 10 inclusive.")
    if not (1 <= preferred_corrosion <= 10):
        raise ValueError("Preferred corrosion resistance must be between 1 and 10 inclusive.")
    
    # Initialize list for recommended fittings
    recommendations = []

    # Iterate through available fittings and apply filtering criteria
    for fitting in fittings:
        if (fitting.durability >= preferred_durability and
                fitting.corrosion_resistance >= preferred_corrosion):
            recommendations.append(fitting)

    return recommendations


# Example usage:
if __name__ == "__main__":
    # Create a list of available metal fittings
    available_fittings = [
        MetalFitting("Hastelloy C276 Round Bars", 9, 10),
        MetalFitting("Inconel Alloy 600 Pipes", 8, 9),
        MetalFitting("Stainless Steel 316", 7, 6),
        MetalFitting("Titanium Grade 5", 8, 8),
    ]

    # User preferences
    user_durability = 8
    user_corrosion = 7

    try:
        recommended = recommend_metal_fittings(user_durability, user_corrosion, available_fittings)
        print("Recommended Metal Fittings:")
        for fitting in recommended:
            print(f"- {fitting.name} (Durability: {fitting.durability}, Corrosion Resistance: {fitting.corrosion_resistance})")
    except ValueError as e:
        print(e)
```
