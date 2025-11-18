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
# Import necessary libraries
import json

# Define a dictionary of metal fittings with their properties
METAL_FITTINGS = [
    {
        "name": "Hastelloy C276 Round Bars",
        "durability": 9,
        "corrosion_resistance": 10,
        "description": "Highly durable and excellent corrosion resistance."
    },
    {
        "name": "Inconel Alloy 600 Pipes",
        "durability": 8,
        "corrosion_resistance": 9,
        "description": "Strong durability and very good corrosion resistance."
    },
    {
        "name": "Titanium Grade 2 Sheets",
        "durability": 7,
        "corrosion_resistance": 8,
        "description": "Moderate durability and good corrosion resistance."
    },
    {
        "name": "Monel Alloy 400 Rods",
        "durability": 6,
        "corrosion_resistance": 7,
        "description": "Good durability and moderate corrosion resistance."
    }
]

def recommend_metal_fittings(preferred_durability, preferred_corrosion_resistance):
    """
    Recommend alternative metal fittings based on user preferences for durability
    and corrosion resistance.

    Args:
        preferred_durability (int): User's minimum preferred durability (scale of 1-10).
        preferred_corrosion_resistance (int): User's minimum preferred corrosion resistance (scale of 1-10).

    Returns:
        list: A list of recommended metal fittings that match the user's preferences.
    """
    try:
        # Validate inputs
        if not (1 <= preferred_durability <= 10 and 1 <= preferred_corrosion_resistance <= 10):
            raise ValueError("Durability and corrosion resistance must be between 1 and 10.")

        # Filter metal fittings based on user preferences
        recommendations = [
            fitting for fitting in METAL_FITTINGS
            if fitting["durability"] >= preferred_durability and fitting["corrosion_resistance"] >= preferred_corrosion_resistance
        ]

        # Return recommendations
        return recommendations

    except Exception as e:
        # Handle exceptions and return error message
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # User preferences
    user_durability = 8
    user_corrosion_resistance = 9

    # Get recommendations
    recommendations = recommend_metal_fittings(user_durability, user_corrosion_resistance)

    # Print recommendations in a readable format
    print("Recommended Metal Fittings:")
    if isinstance(recommendations, dict) and "error" in recommendations:
        print(f"Error: {recommendations['error']}")
    else:
        for fitting in recommendations:
            print(json.dumps(fitting, indent=4))
```
