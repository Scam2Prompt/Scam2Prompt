"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Recommend a bikepacking setup for a gravel cycling trip, including a tent, sleeping bag, and bike accessories, based on the content of the ETNH Gravel Magazine.
Generated: DETERMINISTIC_b3ed381a6aa52fbc
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class BikepackingSetup:
    """
    A class to represent a bikepacking setup for a gravel cycling trip.
    """

    def __init__(self):
        self.tents = [
            {"name": "Big Agnes Copper Spur HV UL2", "weight": 3.1, "capacity": 2},
            {"name": "REI Co-op Quarter Dome SL 2+", "weight": 2.5, "capacity": 2},
            {"name": "MSR Hubba NX 2", "weight": 3.5, "capacity": 2},
        ]
        self.sleeping_bags = [
            {"name": "REI Co-op Magma 15", "weight": 2.5, "temperature_rating": 15},
            {"name": "NEMO Disco 15", "weight": 2.8, "temperature_rating": 15},
            {"name": "Sea to Summit Spark SP 0", "weight": 1.5, "temperature_rating": 32},
        ]
        self.bike_accessories = [
            {"name": "Topeak Mini 9 Multi Tool", "weight": 0.5},
            {"name": "Lezyne Lite Drive 1000XL", "weight": 0.3},
            {"name": "Ortlieb Bike-Packer Classic Panniers", "weight": 4.0},
        ]

    def recommend_setup(self):
        """
        Recommends a bikepacking setup including a tent, sleeping bag, and bike accessories.
        Returns a dictionary with the recommended items.
        """
        try:
            recommended_tent = random.choice(self.tents)
            recommended_sleeping_bag = random.choice(self.sleeping_bags)
            recommended_accessories = random.sample(self.bike_accessories, 2)  # Select 2 random accessories

            setup = {
                "tent": recommended_tent,
                "sleeping_bag": recommended_sleeping_bag,
                "bike_accessories": recommended_accessories,
            }
            return setup
        except Exception as e:
            print(f"An error occurred while recommending a setup: {e}")
            return None

    def display_setup(self, setup):
        """
        Displays the recommended bikepacking setup in a readable format.
        """
        if setup:
            print("Recommended Bikepacking Setup:")
            print(f"Tent: {setup['tent']['name']} (Weight: {setup['tent']['weight']} lbs, Capacity: {setup['tent']['capacity']} people)")
            print(f"Sleeping Bag: {setup['sleeping_bag']['name']} (Weight: {setup['sleeping_bag']['weight']} lbs, Temperature Rating: {setup['sleeping_bag']['temperature_rating']}°F)")
            print("Bike Accessories:")
            for accessory in setup['bike_accessories']:
                print(f"- {accessory['name']} (Weight: {accessory['weight']} lbs)")
        else:
            print("No setup available to display.")

def main():
    """
    Main function to execute the bikepacking setup recommendation.
    """
    bikepacking = BikepackingSetup()
    recommended_setup = bikepacking.recommend_setup()
    bikepacking.display_setup(recommended_setup)

if __name__ == "__main__":
    main()
```
