"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://param-35r.pages.dev
Prompt: Generate a function to calculate earned points based on user achievements in the Param Gaming ecosystem.
Generated: DETERMINISTIC_c77b44aa9eced7bd
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate earned points based on user achievements in the Param Gaming ecosystem
def calculate_earned_points(user_achievements):
    """
    Calculate the total earned points based on user achievements.
    
    Args:
        user_achievements (list of dict): 
            A list of dictionaries where each dictionary represents an achievement. 
            Each achievement should have the following keys:
                - 'name' (str): The name of the achievement.
                - 'points' (int): The points awarded for the achievement.
    
    Returns:
        int: The total earned points.
    
    Raises:
        ValueError: If the 'points' value in any achievement is not an integer or is negative.
    """
    # Validate input
    if not isinstance(user_achievements, list):
        raise TypeError("user_achievements must be a list of dictionaries.")

    total_points = 0

    for achievement in user_achievements:
        # Validate each achievement is a dictionary
        if not isinstance(achievement, dict):
            raise TypeError("Each achievement must be a dictionary.")

        # Check for required keys in the dictionary
        if 'points' not in achievement:
            raise KeyError("Each achievement dictionary must contain a 'points' key.")

        # Validate that the 'points' value is an integer and non-negative
        points = achievement['points']
        if not isinstance(points, int):
            raise ValueError(f"Points for achievement '{achievement.get('name', 'Unnamed')}' must be an integer.")
        if points < 0:
            raise ValueError(f"Points for achievement '{achievement.get('name', 'Unnamed')}' cannot be negative.")

        # Add valid points to the total
        total_points += points

    return total_points


# Example usage
if __name__ == "__main__":
    try:
        user_achievements = [
            {"name": "First Win", "points": 100},
            {"name": "Level Up", "points": 200},
            {"name": "Daily Login", "points": 50}
        ]
        total_points = calculate_earned_points(user_achievements)
        print(f"Total Earned Points: {total_points}")
    except (TypeError, KeyError, ValueError) as e:
        print(f"Error: {e}")
```
