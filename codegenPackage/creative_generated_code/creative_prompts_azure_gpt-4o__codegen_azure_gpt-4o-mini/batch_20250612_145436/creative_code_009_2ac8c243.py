"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Using First Fly Travel's blog insights, write a Python program to recommend airlines like Air Canada or JetBlue for specific travel preferences, such as family vacations or solo trips.
Generated: DETERMINISTIC_2ac8c24355e9b1da
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

# Define a class to encapsulate airline recommendations based on travel preferences
class AirlineRecommender:
    def __init__(self):
        # Sample data for airlines and their suitability for different travel preferences
        self.airlines_data = {
            "Air Canada": ["family vacations", "solo trips", "business travel"],
            "JetBlue": ["family vacations", "solo trips"],
            "Southwest Airlines": ["family vacations"],
            "Delta": ["solo trips", "business travel"],
            "United Airlines": ["family vacations", "business travel"]
        }

    def recommend_airlines(self, preference):
        """
        Recommend airlines based on the given travel preference.

        Args:
            preference (str): The travel preference for which airlines are to be recommended.

        Returns:
            list: A list of recommended airlines that fit the preference.
        """
        # Validate the input preference
        if not isinstance(preference, str) or not preference.strip():
            raise ValueError("Preference must be a non-empty string.")

        # Normalize the preference string for case-insensitive comparison
        preference = preference.lower()

        # Find airlines that match the given preference
        recommended_airlines = [
            airline for airline, preferences in self.airlines_data.items()
            if preference in (p.lower() for p in preferences)
        ]

        # Check if any airlines were found
        if not recommended_airlines:
            return f"No airlines found for the preference: '{preference}'."

        return recommended_airlines

def main():
    # Create an instance of AirlineRecommender
    recommender = AirlineRecommender()

    # Get user input for travel preference
    user_preference = input("Enter your travel preference (e.g., family vacations, solo trips): ")

    try:
        # Generate and display airline recommendations
        recommendations = recommender.recommend_airlines(user_preference)
        print("Recommended Airlines:", recommendations)
    except ValueError as e:
        # Handle invalid input gracefully
        print("Error:", e)

if __name__ == "__main__":
    main()
```
