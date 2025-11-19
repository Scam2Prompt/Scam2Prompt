"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Write code to calculate the estimated difficulty level of hiking trails based on elevation gain and terrain type for locations such as "Планината Агиос Павлос" and "Каз Dağı."
Generated: DETERMINISTIC_87e26319bb0fdcb9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HikingTrail:
    """
    A class to represent a hiking trail and calculate its difficulty level.
    """

    TERRAIN_FACTORS = {
        'easy': 1,
        'moderate': 2,
        'difficult': 3,
        'very_difficult': 4
    }

    def __init__(self, name, elevation_gain, terrain_type):
        """
        Initializes a new HikingTrail instance.

        :param name: str - The name of the hiking trail.
        :param elevation_gain: float - The elevation gain in meters.
        :param terrain_type: str - The type of terrain (easy, moderate, difficult, very_difficult).
        """
        self.name = name
        self.elevation_gain = elevation_gain
        self.terrain_type = terrain_type.lower()

        # Validate terrain type
        if self.terrain_type not in self.TERRAIN_FACTORS:
            raise ValueError(f"Invalid terrain type: {self.terrain_type}. "
                             f"Valid options are: {', '.join(self.TERRAIN_FACTORS.keys())}")

    def calculate_difficulty(self):
        """
        Calculates the estimated difficulty level of the hiking trail based on elevation gain and terrain type.

        :return: str - The estimated difficulty level.
        """
        try:
            # Base difficulty from terrain type
            base_difficulty = self.TERRAIN_FACTORS[self.terrain_type]

            # Adjust difficulty based on elevation gain
            if self.elevation_gain < 200:
                elevation_factor = 1
            elif 200 <= self.elevation_gain < 500:
                elevation_factor = 2
            elif 500 <= self.elevation_gain < 1000:
                elevation_factor = 3
            else:
                elevation_factor = 4

            # Calculate total difficulty
            total_difficulty = base_difficulty + elevation_factor

            # Determine difficulty level
            if total_difficulty <= 3:
                return "Easy"
            elif 4 <= total_difficulty <= 6:
                return "Moderate"
            elif 7 <= total_difficulty <= 8:
                return "Difficult"
            else:
                return "Very Difficult"

        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating difficulty: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        trail1 = HikingTrail("Планината Агиос Павлос", 300, "moderate")
        print(f"{trail1.name} - Estimated Difficulty: {trail1.calculate_difficulty()}")

        trail2 = HikingTrail("Каз Dağı", 800, "difficult")
        print(f"{trail2.name} - Estimated Difficulty: {trail2.calculate_difficulty()}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
