"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bvitravel.co.uk
Prompt: Create a function that recommends luxury resorts in the British Virgin Islands based on user preferences for activities like diving and watersports.
Generated: DETERMINISTIC_c26c30002e2ef8f0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def recommend_resorts(preferences):
    """
    Recommend luxury resorts in the British Virgin Islands based on user preferences.

    Args:
        preferences (list): A list of user preferences (e.g., ['diving', 'watersports']).

    Returns:
        list: A list of recommended resorts matching the user's preferences.
    """
    # Sample resort database (usually this would come from a database or API)
    resorts_db = [
        {
            "name": "Rosewood Little Dix Bay",
            "activities": ["diving", "snorkeling", "hiking"],
            "description": "A tranquil resort offering luxury and stunning views."
        },
        {
            "name": "Scrub Island Resort, Spa & Marina",
            "activities": ["watersports", "sailing", "diving"],
            "description": "An exclusive island resort with world-class amenities."
        },
        {
            "name": "Oil Nut Bay",
            "activities": ["kayaking", "hiking", "sailing"],
            "description": "A private paradise with exceptional luxury accommodations."
        },
        {
            "name": "Guana Island",
            "activities": ["diving", "bird-watching", "snorkeling"],
            "description": "A pristine island resort with an emphasis on nature and privacy."
        },
        {
            "name": "Necker Island (Richard Branson's Private Island)",
            "activities": ["watersports", "diving", "paddleboarding"],
            "description": "An ultra-luxury private island with unparalleled experiences."
        }
    ]

    if not isinstance(preferences, list):
        raise ValueError("Preferences must be provided as a list of strings.")

    # Ensure preferences are lowercase for case-insensitive comparison
    preferences = [pref.lower() for pref in preferences]

    # Filter resorts based on matching activities
    recommended_resorts = []
    for resort in resorts_db:
        if any(activity in resort["activities"] for activity in preferences):
            recommended_resorts.append({
                "name": resort["name"],
                "description": resort["description"],
                "matching_activities": list(
                    set(resort["activities"]).intersection(preferences)
                )
            })

    # Return recommendations (empty list if no matches found)
    return recommended_resorts


# Example usage:
if __name__ == "__main__":
    try:
        user_preferences = ["diving", "watersports"]
        recommendations = recommend_resorts(user_preferences)
        print("Recommended Resorts:")
        print(json.dumps(recommendations, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
