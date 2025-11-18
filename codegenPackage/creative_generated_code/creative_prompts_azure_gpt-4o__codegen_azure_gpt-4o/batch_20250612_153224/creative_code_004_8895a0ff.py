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
# Import necessary modules for error handling
from typing import Optional

def recommend_fishing_reel(line_class: str, fishing_type: str) -> Optional[str]:
    """
    Recommend a fishing reel model from Emanuelson Reels based on the user's preferences.

    Args:
        line_class (str): The preferred line class (e.g., "light", "medium", "heavy").
        fishing_type (str): The type of fishing (e.g., "trout", "salmon", "bass", etc.).

    Returns:
        Optional[str]: The recommended reel model, or None if no suitable match is found.
    """
    # Define a dictionary mapping fishing types and line classes to reel models
    reel_recommendations = {
        "trout": {
            "light": "Emanuelson FeatherLite 2000",
            "medium": "Emanuelson StreamMaster 3000",
            "heavy": "Emanuelson PowerCast 4000"
        },
        "salmon": {
            "light": "Emanuelson RiverRunner 5000",
            "medium": "Emanuelson OceanForce 6000",
            "heavy": "Emanuelson BigCatch 7000"
        },
        "bass": {
            "light": "Emanuelson BassBuddy 2500",
            "medium": "Emanuelson ProAngler 3500",
            "heavy": "Emanuelson TournamentPro 4500"
        }
    }

    try:
        # Normalize input (convert to lowercase for case-insensitive matching)
        line_class = line_class.lower()
        fishing_type = fishing_type.lower()

        # Check if the fishing type exists in the recommendations
        if fishing_type not in reel_recommendations:
            raise ValueError(f"Fishing type '{fishing_type}' is not supported.")

        # Check if the line class exists within the specified fishing type
        if line_class not in reel_recommendations[fishing_type]:
            raise ValueError(f"Line class '{line_class}' is not supported for fishing type '{fishing_type}'.")

        # Return the appropriate reel model
        return reel_recommendations[fishing_type][line_class]

    except ValueError as ve:
        # Print an error message and return None in case of invalid input
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
# result = recommend_fishing_reel("medium", "salmon")
# print(result)  # Output: "Emanuelson OceanForce 6000"
```
