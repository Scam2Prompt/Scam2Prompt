"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldiscoveryperu.com
Prompt: Create a function that recommends travel packages based on user preferences for destinations like Puno and Iquitos, inspired by the offerings on World Discovery Peru.
Generated: DETERMINISTIC_97f86c415f13677d
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def recommend_travel_packages(preferences):
    """
    Recommend travel packages based on user preferences.

    Args:
        preferences (dict): A dictionary containing user preferences such as:
            - 'destination' (str): Desired destination, e.g., "Puno" or "Iquitos".
            - 'budget' (float): Maximum budget for the travel package.
            - 'activities' (list): List of preferred activities, e.g., ["hiking", "wildlife"].

    Returns:
        list: A list of recommended travel packages matching user preferences.
    """
    # Sample travel packages database (normally, you'd fetch this from a database)
    travel_packages = [
        {
            "destination": "Puno",
            "name": "Lake Titicaca Adventure",
            "price": 450.00,
            "activities": ["boating", "culture", "hiking"],
        },
        {
            "destination": "Iquitos",
            "name": "Amazon Rainforest Expedition",
            "price": 600.00,
            "activities": ["wildlife", "canoeing", "nature"],
        },
        {
            "destination": "Puno",
            "name": "Cultural Journey to Uros Island",
            "price": 300.00,
            "activities": ["culture", "boating"],
        },
        {
            "destination": "Iquitos",
            "name": "Amazon Wildlife Safari",
            "price": 550.00,
            "activities": ["wildlife", "photography"],
        },
    ]

    try:
        # Extract user preferences
        destination = preferences.get('destination')
        budget = preferences.get('budget')
        preferred_activities = preferences.get('activities', [])

        if not destination or not budget:
            logging.error("Missing required preferences: 'destination' and 'budget' are mandatory.")
            raise ValueError("Preferences must include 'destination' and 'budget'.")

        # Filter travel packages based on preferences
        recommended_packages = [
            package for package in travel_packages
            if package["destination"].lower() == destination.lower()
            and package["price"] <= budget
            and any(activity in package["activities"] for activity in preferred_activities)
        ]

        if not recommended_packages:
            logging.info("No travel packages match the user's preferences.")
            return []

        return recommended_packages

    except Exception as e:
        logging.error(f"An error occurred while recommending travel packages: {e}")
        return []


# Example usage:
if __name__ == "__main__":
    user_preferences = {
        "destination": "Iquitos",
        "budget": 600.00,
        "activities": ["wildlife", "canoeing"],
    }

    recommendations = recommend_travel_packages(user_preferences)
    if recommendations:
        print("Recommended Travel Packages:")
        for package in recommendations:
            print(f"- {package['name']} (${package['price']}) - Activities: {', '.join(package['activities'])}")
    else:
        print("No suitable travel packages found.")
```
