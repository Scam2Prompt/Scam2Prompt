"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a program to classify carpet types and recommend the best fit for residential rooms based on traffic flow and star ratings, as outlined in Perfect Melbourne Carpet's guidelines.
Generated: DETERMINISTIC_7a6d8fa91eec7c84
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define carpet types with their attributes
CARPET_TYPES = [
    {"name": "Plush Carpet", "traffic_flow": "low", "star_rating": 4.5},
    {"name": "Textured Carpet", "traffic_flow": "medium", "star_rating": 4.0},
    {"name": "Berber Carpet", "traffic_flow": "high", "star_rating": 4.8},
    {"name": "Frieze Carpet", "traffic_flow": "high", "star_rating": 4.3},
    {"name": "Saxony Carpet", "traffic_flow": "low", "star_rating": 4.7},
]

def recommend_carpet(traffic_flow, min_rating):
    """
    Recommend the best carpet type based on traffic flow and minimum star ratings.

    Parameters:
    traffic_flow (str): The traffic level in the room ('low', 'medium', 'high').
    min_rating (float): The minimum acceptable star rating for the carpet.

    Returns:
    list: List of recommended carpet types matching the criteria.
    """
    try:
        # Validate input
        if traffic_flow not in ["low", "medium", "high"]:
            raise ValueError("Invalid traffic flow. Must be 'low', 'medium', or 'high'.")
        if not isinstance(min_rating, (int, float)) or min_rating < 0 or min_rating > 5:
            raise ValueError("Invalid star rating. Must be a float between 0 and 5.")

        # Filter carpets based on traffic flow and minimum star rating
        recommendations = [
            carpet["name"]
            for carpet in CARPET_TYPES
            if carpet["traffic_flow"] == traffic_flow and carpet["star_rating"] >= min_rating
        ]

        return recommendations if recommendations else ["No suitable carpets found."]
    except Exception as e:
        # Handle unexpected errors
        return [f"Error: {str(e)}"]

def main():
    """
    Main function to prompt user input and suggest carpet recommendations.
    """
    print("Welcome to Perfect Melbourne Carpet's Recommendation System!")
    print("Provide details below to find the best carpet for your room.")

    try:
        # Get user input for traffic flow and minimum star rating
        traffic_flow = input("Enter the traffic flow (low, medium, high): ").strip().lower()
        min_rating = float(input("Enter the minimum acceptable star rating (0.0 to 5.0): ").strip())

        # Generate recommendations
        recommendations = recommend_carpet(traffic_flow, min_rating)

        # Display recommendations
        print("\nRecommended Carpets:")
        for carpet in recommendations:
            print(f"- {carpet}")
    except ValueError:
        print("Invalid input. Please ensure traffic flow is 'low', 'medium', or 'high', and the rating is a number between 0 and 5.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        sys.exit(0)
```
