"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Write a function to recommend farming machinery like brush cutters and water pumps based on user input, using the categories listed on Dotcom Machinery's site.
Generated: DETERMINISTIC_25504fea3d7f457e
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a mapping of machinery categories and their descriptions
MACHINERY_CATEGORIES = {
    "Brush Cutters": "Used to clear overgrown vegetation, grass, and small bushes efficiently.",
    "Water Pumps": "Ideal for irrigation, draining flooded areas, or transferring water from one place to another.",
    "Tractors": "Heavy-duty machines for plowing, tilling, planting, and other farming activities.",
    "Harvesters": "Designed for harvesting crops like wheat, rice, and corn.",
    "Sprayers": "Used for applying fertilizers, pesticides, and herbicides to crops.",
    "Cultivators": "Help in soil preparation and weed control by loosening the soil.",
    "Seeders": "Machines for planting seeds in rows with precise spacing."
}

def recommend_machinery(user_input):
    """
    Recommend farming machinery based on user input.
    
    Args:
        user_input (str): A description of the user's needs, problems, or farming tasks.
    
    Returns:
        str: A JSON string containing machinery recommendations and their descriptions.
    """
    try:
        # Validate input
        if not user_input or not isinstance(user_input, str):
            raise ValueError("Invalid input. Please provide a non-empty string describing your needs.")

        # Normalize user input for case-insensitive matching
        user_input = user_input.lower()

        # Gather recommendations based on keywords in user input
        recommendations = {}
        for category, description in MACHINERY_CATEGORIES.items():
            if any(keyword in user_input for keyword in category.lower().split()):
                recommendations[category] = description

        # If no matches are found, return a default message
        if not recommendations:
            return json.dumps({"message": "No specific recommendations found. Please refine your input."})

        # Return recommendations as a JSON string
        return json.dumps(recommendations, indent=4)

    except Exception as e:
        # Handle unexpected errors gracefully
        return json.dumps({"error": str(e)})

# Example usage:
if __name__ == "__main__":
    user_query = "I need equipment for clearing grass and bushes."
    print(recommend_machinery(user_query))
```
