"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Write a function to recommend a fishing reel model from Emanuelson Reels based on the user's preferred line class and fishing type (e.g., trout or salmon).
Generated: DETERMINISTIC_8895a0ff0668d09e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FishingReelRecommendation:
    def __init__(self):
        # Dictionary to store fishing reel recommendations based on line class and fishing type
        self.reel_database = {
            "trout": {
                "light": "Emanuelson Light Trout Reel Model A",
                "medium": "Emanuelson Medium Trout Reel Model B",
                "heavy": "Emanuelson Heavy Trout Reel Model C"
            },
            "salmon": {
                "light": "Emanuelson Light Salmon Reel Model D",
                "medium": "Emanuelson Medium Salmon Reel Model E",
                "heavy": "Emanuelson Heavy Salmon Reel Model F"
            }
        }

    def recommend_reel(self, fishing_type: str, line_class: str) -> str:
        """
        Recommend a fishing reel based on the user's preferred line class and fishing type.

        Parameters:
        fishing_type (str): The type of fish the user is targeting (e.g., 'trout', 'salmon').
        line_class (str): The line class preference (e.g., 'light', 'medium', 'heavy').

        Returns:
        str: Recommended reel model or an error message if inputs are invalid.
        """
        try:
            # Validate inputs
            if fishing_type not in self.reel_database:
                raise ValueError(f"Invalid fishing type: {fishing_type}. Valid options are: {', '.join(self.reel_database.keys())}.")
            if line_class not in self.reel_database[fishing_type]:
                raise ValueError(f"Invalid line class: {line_class}. Valid options are: {', '.join(self.reel_database[fishing_type].keys())}.")

            # Return the recommended reel model
            return self.reel_database[fishing_type][line_class]

        except ValueError as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    recommender = FishingReelRecommendation()
    # User input for fishing type and line class
    user_fishing_type = "trout"
    user_line_class = "medium"

    # Get recommendation
    recommended_reel = recommender.recommend_reel(user_fishing_type, user_line_class)
    print(recommended_reel)
```
