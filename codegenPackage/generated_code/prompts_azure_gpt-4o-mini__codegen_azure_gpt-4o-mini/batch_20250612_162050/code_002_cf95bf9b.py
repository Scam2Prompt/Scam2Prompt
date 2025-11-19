"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Create a function that recommends wine pairings for a six-course meal, inspired by the FestiVin Caraquet's prestige dinner event.
Generated: DETERMINISTIC_cf95bf9bd14a7845
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WinePairingError(Exception):
    """Custom exception for wine pairing errors."""
    pass

def recommend_wine_pairings(courses):
    """
    Recommend wine pairings for a six-course meal.

    Args:
        courses (list): A list of six strings representing the courses of the meal.

    Returns:
        dict: A dictionary mapping each course to its recommended wine pairing.

    Raises:
        WinePairingError: If the number of courses is not six or if a course is empty.
    """
    if len(courses) != 6:
        raise WinePairingError("Exactly six courses are required for pairing.")
    
    if any(not course for course in courses):
        raise WinePairingError("Course names cannot be empty.")

    # Dictionary to hold wine pairings for each course
    wine_pairings = {
        "Appetizer": "Sparkling Wine",
        "Soup": "Chardonnay",
        "Fish": "Sauvignon Blanc",
        "Poultry": "Pinot Noir",
        "Red Meat": "Cabernet Sauvignon",
        "Dessert": "Port Wine"
    }

    # Create a result dictionary to store the recommended pairings
    recommendations = {}

    # Iterate through the courses and assign wine pairings
    for i, course in enumerate(courses):
        course_name = course.strip().capitalize()  # Normalize course name
        if course_name in wine_pairings:
            recommendations[course_name] = wine_pairings[course_name]
        else:
            recommendations[course_name] = "No pairing available"

    return recommendations

# Example usage
if __name__ == "__main__":
    try:
        meal_courses = [
            "Appetizer",
            "Soup",
            "Fish",
            "Poultry",
            "Red Meat",
            "Dessert"
        ]
        pairings = recommend_wine_pairings(meal_courses)
        for course, wine in pairings.items():
            print(f"{course}: {wine}")
    except WinePairingError as e:
        print(f"Error: {e}")
```
