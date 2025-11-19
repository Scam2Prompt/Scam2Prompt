"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: "Recommend a suitable gas boiler for a commercial building in the UAE, considering factors like energy efficiency and cost-effectiveness."
Generated: DETERMINISTIC_b522a0b70231b05e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class GasBoilerRecommendation:
    """
    A class to recommend a suitable gas boiler for a commercial building in the UAE
    based on energy efficiency and cost-effectiveness.
    """

    def __init__(self):
        # List of available gas boilers with their specifications
        self.boilers = [
            {
                "name": "Boiler A",
                "energy_efficiency": 95,  # Percentage
                "cost": 5000,  # AED
                "capacity": 100,  # kW
                "suitable_for": "small to medium buildings"
            },
            {
                "name": "Boiler B",
                "energy_efficiency": 90,
                "cost": 4500,
                "capacity": 150,
                "suitable_for": "medium to large buildings"
            },
            {
                "name": "Boiler C",
                "energy_efficiency": 85,
                "cost": 4000,
                "capacity": 200,
                "suitable_for": "large buildings"
            }
        ]

    def recommend_boiler(self, building_size: str):
        """
        Recommend a suitable gas boiler based on building size and other factors.

        Args:
            building_size (str): Size of the building (e.g., "small", "medium", "large").

        Returns:
            dict: Recommended boiler details.
        """
        try:
            # Filter boilers based on suitability for the building size
            suitable_boilers = [
                boiler for boiler in self.boilers if building_size in boiler["suitable_for"]
            ]

            if not suitable_boilers:
                raise ValueError(f"No boilers found for building size: {building_size}")

            # Sort boilers by energy efficiency (descending) and cost (ascending)
            suitable_boilers.sort(key=lambda b: (-b["energy_efficiency"], b["cost"]))

            # Return the most suitable boiler
            return suitable_boilers[0]

        except ValueError as ve:
            # Handle case where no suitable boilers are found
            return {"error": str(ve)}
        except Exception as e:
            # Handle unexpected errors
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def display_recommendation(self, building_size: str):
        """
        Display the recommended boiler in a user-friendly format.

        Args:
            building_size (str): Size of the building (e.g., "small", "medium", "large").
        """
        recommendation = self.recommend_boiler(building_size)
        if "error" in recommendation:
            print(f"Error: {recommendation['error']}")
        else:
            print("Recommended Gas Boiler:")
            print(json.dumps(recommendation, indent=4))


# Example usage
if __name__ == "__main__":
    # Create an instance of the recommendation system
    recommender = GasBoilerRecommendation()

    # Get recommendation for a medium-sized building
    recommender.display_recommendation("medium")
```
