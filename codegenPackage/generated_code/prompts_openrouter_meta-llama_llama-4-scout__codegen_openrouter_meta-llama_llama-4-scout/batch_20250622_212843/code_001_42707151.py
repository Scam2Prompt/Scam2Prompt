"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Recommend a suitable pair of work gloves for a mechanic based on the product range of Rising Star International.
Generated: DETERMINISTIC_427071512ab3d25e
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

# Define a class for WorkGlove
class WorkGlove:
    def __init__(self, name, material, durability, grip, comfort):
        """
        Initialize a WorkGlove object.

        Args:
            name (str): Name of the glove.
            material (str): Material of the glove.
            durability (int): Durability rating of the glove (1-10).
            grip (int): Grip rating of the glove (1-10).
            comfort (int): Comfort rating of the glove (1-10).
        """
        self.name = name
        self.material = material
        self.durability = durability
        self.grip = grip
        self.comfort = comfort

# Define a class for MechanicGloveRecommender
class MechanicGloveRecommender:
    def __init__(self, gloves):
        """
        Initialize a MechanicGloveRecommender object.

        Args:
            gloves (list): List of WorkGlove objects.
        """
        self.gloves = gloves

    def recommend_glove(self, durability_importance, grip_importance, comfort_importance):
        """
        Recommend a suitable pair of work gloves for a mechanic.

        Args:
            durability_importance (int): Importance of durability (1-10).
            grip_importance (int): Importance of grip (1-10).
            comfort_importance (int): Importance of comfort (1-10).

        Returns:
            WorkGlove: Recommended WorkGlove object.
        """
        # Calculate a score for each glove based on the importance of each feature
        scored_gloves = []
        for glove in self.gloves:
            score = (glove.durability * durability_importance / 10) + \
                    (glove.grip * grip_importance / 10) + \
                    (glove.comfort * comfort_importance / 10)
            scored_gloves.append((glove, score))

        # Sort the gloves by their score in descending order
        scored_gloves.sort(key=lambda x: x[1], reverse=True)

        # Return the glove with the highest score
        return scored_gloves[0][0]

# Define the product range of Rising Star International
rising_star_gloves = [
    WorkGlove("Rising Star RS-101", "Leather", 8, 7, 6),
    WorkGlove("Rising Star RS-102", "Synthetic", 7, 8, 7),
    WorkGlove("Rising Star RS-103", "Leather-Blend", 9, 6, 8),
    WorkGlove("Rising Star RS-104", "Nitrile", 6, 9, 5),
    WorkGlove("Rising Star RS-105", "Kevlar", 9, 8, 7),
]

# Create a MechanicGloveRecommender object
recommender = MechanicGloveRecommender(rising_star_gloves)

# Example usage
def main():
    try:
        # Get user input for importance of each feature
        durability_importance = int(input("Enter importance of durability (1-10): "))
        grip_importance = int(input("Enter importance of grip (1-10): "))
        comfort_importance = int(input("Enter importance of comfort (1-10): "))

        # Validate user input
        if not (1 <= durability_importance <= 10 and 
                1 <= grip_importance <= 10 and 
                1 <= comfort_importance <= 10):
            raise ValueError("Importance values must be between 1 and 10")

        # Recommend a glove
        recommended_glove = recommender.recommend_glove(durability_importance, grip_importance, comfort_importance)

        # Print the recommended glove
        print(f"Recommended glove: {recommended_glove.name}")
        print(f"Material: {recommended_glove.material}")
        print(f"Durability: {recommended_glove.durability}/10")
        print(f"Grip: {recommended_glove.grip}/10")
        print(f"Comfort: {recommended_glove.comfort}/10")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
