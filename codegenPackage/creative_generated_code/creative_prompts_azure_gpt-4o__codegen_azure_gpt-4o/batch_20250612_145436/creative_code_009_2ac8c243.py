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
# Python program to recommend airlines based on travel preferences.

# Define a dictionary containing airline recommendations for various travel preferences.
AIRLINE_RECOMMENDATIONS = {
    "family_vacation": ["Air Canada", "Delta Air Lines", "Southwest Airlines"],
    "solo_trip": ["JetBlue Airways", "Alaska Airlines", "Frontier Airlines"],
    "business_trip": ["United Airlines", "American Airlines", "British Airways"],
    "adventure_trip": ["Spirit Airlines", "Frontier Airlines", "JetBlue Airways"],
    "luxury_travel": ["Emirates", "Qatar Airways", "Singapore Airlines"]
}

def recommend_airlines(preference):
    """
    Recommend airlines based on the travel preference.

    Args:
        preference (str): The user's travel preference (e.g., "family_vacation", "solo_trip").
    
    Returns:
        list: A list of recommended airlines for the given preference.
    """
    try:
        # Check if the preference exists in the recommendations dictionary.
        if preference not in AIRLINE_RECOMMENDATIONS:
            raise ValueError(f"Invalid preference: '{preference}'. Available options are: {list(AIRLINE_RECOMMENDATIONS.keys())}")
        
        # Return the list of recommended airlines for the given preference.
        return AIRLINE_RECOMMENDATIONS[preference]
    except ValueError as e:
        # Handle invalid preference input.
        print(f"Error: {e}")
        return []

def main():
    """
    Main function to interact with the user and provide airline recommendations.
    """
    print("Welcome to the Airline Recommendation System!")
    print("Available travel preferences: family_vacation, solo_trip, business_trip, adventure_trip, luxury_travel")
    
    # Prompt the user for their travel preference.
    preference = input("Please enter your travel preference: ").strip().lower()
    
    # Get the recommended airlines.
    recommendations = recommend_airlines(preference)
    
    # Display the recommendations to the user.
    if recommendations:
        print(f"\nRecommended airlines for {preference.replace('_', ' ')}:")
        for idx, airline in enumerate(recommendations, start=1):
            print(f"{idx}. {airline}")
    else:
        print("\nNo recommendations available. Please try again with a valid preference.")

# Entry point of the program.
if __name__ == "__main__":
    main()
```
