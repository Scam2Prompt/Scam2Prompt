"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write code to calculate the estimated difficulty level of hiking trails based on elevation gain and terrain type for locations such as "Планината Агиос Павлос" and "Каз Dağı."
Generated: DETERMINISTIC_87e26319bb0fdcb9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HikingTrail:
    def __init__(self, name: str, elevation_gain: float, terrain_type: str):
        """
        Initializes a new instance of the HikingTrail class.

        :param name: Name of the hiking trail.
        :param elevation_gain: Elevation gain in meters.
        :param terrain_type: Type of terrain ('easy', 'moderate', 'hard').
        """
        self.name = name
        self.elevation_gain = elevation_gain
        self.terrain_type = terrain_type.lower()

    def calculate_difficulty(self) -> str:
        """
        Calculates the estimated difficulty level of the hiking trail 
        based on elevation gain and terrain type.

        :return: A string representing the difficulty level.
        """
        if self.terrain_type not in ['easy', 'moderate', 'hard']:
            raise ValueError(f"Invalid terrain type: {self.terrain_type}. Must be 'easy', 'moderate', or 'hard'.")

        # Base difficulty score from terrain type
        terrain_difficulty_mapping = {
            'easy': 1,
            'moderate': 2,
            'hard': 3
        }

        # Calculate difficulty based on elevation gain
        if self.elevation_gain < 200:
            elevation_difficulty = 1  # Easy
        elif self.elevation_gain < 600:
            elevation_difficulty = 2  # Moderate
        else:
            elevation_difficulty = 3  # Hard

        # Calculate final difficulty score
        total_difficulty_score = terrain_difficulty_mapping[self.terrain_type] + elevation_difficulty

        # Determine difficulty level based on total score
        if total_difficulty_score <= 2:
            return "Easy"
        elif total_difficulty_score <= 4:
            return "Moderate"
        else:
            return "Hard"


def main():
    """
    Main function to demonstrate the calculation of hiking trail difficulty.
    """
    try:
        # Example hiking trails
        trails = [
            HikingTrail("Планината Агиос Павлос", 300, 'Moderate'),
            HikingTrail("Каз Dağı", 800, 'Hard'),
            HikingTrail("Благодатен хълм", 150, 'Easy')
        ]

        # Calculate and display the difficulty level for each trail
        for trail in trails:
            difficulty = trail.calculate_difficulty()
            print(f"The hiking trail '{trail.name}' is classified as: {difficulty}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
