"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Create an algorithm to recommend gloves for specific use cases, such as welding, gardening, or motorbike riding, based on the detailed categories provided by Rising Star International.
Generated: DETERMINISTIC_7c8da2f37b51cf1d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Glove Recommendation System

This script recommends gloves based on specific use cases categorized by Rising Star International.
The categories include welding, gardening, motorbike riding, and other use cases.
"""

# Import required modules
import json

# Define the glove database with categories and attributes
GLOVE_DATABASE = {
    "welding": {
        "name": "Welding Gloves",
        "material": "Leather",
        "features": ["Heat Resistant", "Durability", "Extended Cuffs"],
        "recommended_for": ["High-heat environments", "Metalworking"],
    },
    "gardening": {
        "name": "Gardening Gloves",
        "material": "Cotton with Rubber Coating",
        "features": ["Grip", "Breathable", "Water Resistant"],
        "recommended_for": ["Planting", "Weeding", "General Gardening"],
    },
    "motorbike_riding": {
        "name": "Motorbike Riding Gloves",
        "material": "Synthetic Leather",
        "features": ["Knuckle Protection", "Grip", "Wind Resistance"],
        "recommended_for": ["Riding at high speeds", "Long-distance travel"],
    },
    "mechanical_work": {
        "name": "Mechanical Work Gloves",
        "material": "Rubber and Kevlar",
        "features": ["Cut Resistant", "Grip", "Shock Absorption"],
        "recommended_for": ["Assembly line work", "Tool handling"],
    },
}

def recommend_gloves(use_case):
    """
    Recommend gloves based on the provided use case.

    Parameters:
    use_case (str): The specific use case for the gloves (e.g., 'welding', 'gardening').

    Returns:
    dict: Details of the recommended gloves, or a message if no match is found.
    """
    try:
        # Normalize input to lowercase for consistent matching
        use_case = use_case.lower()

        # Fetch recommendation from the database
        if use_case in GLOVE_DATABASE:
            return {
                "status": "success",
                "recommendation": GLOVE_DATABASE[use_case],
            }
        else:
            return {
                "status": "error",
                "message": f"No gloves available for the use case '{use_case}'. Please try another category.",
            }
    except Exception as e:
        # Handle unexpected errors
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}",
        }


# Entry point for testing the recommendation system
if __name__ == "__main__":
    print("Glove Recommendation System")
    print("----------------------------")
    try:
        # Prompt user for input
        user_input = input("Enter the use case for gloves (e.g., welding, gardening, motorbike_riding): ").strip()
        
        # Get recommendation
        result = recommend_gloves(user_input)
        
        # Display the result
        if result["status"] == "success":
            print("\nRecommended Gloves:")
            print(json.dumps(result["recommendation"], indent=4))
        else:
            print("\nError:")
            print(result["message"])
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
