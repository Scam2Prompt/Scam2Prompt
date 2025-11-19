"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Build a recommendation system that suggests travel packages from "Rehiletes" based on user preferences for cultural experiences and nature-focused tours.
Generated: DETERMINISTIC_79b97a263057873d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recommendation_system.py

class TravelPackage:
    """Represents a travel package from Rehiletes."""

    def __init__(self, package_id, name, cultural_experiences, nature_focused_tours):
        """
        Initializes a TravelPackage object.

        Args:
            package_id (int): Unique identifier for the package.
            name (str): Name of the package.
            cultural_experiences (list): List of cultural experiences included.
            nature_focused_tours (list): List of nature-focused tours included.
        """
        self.package_id = package_id
        self.name = name
        self.cultural_experiences = cultural_experiences
        self.nature_focused_tours = nature_focused_tours

class UserPreferences:
    """Represents user preferences for cultural experiences and nature-focused tours."""

    def __init__(self, cultural_experience_preference, nature_focused_tour_preference):
        """
        Initializes a UserPreferences object.

        Args:
            cultural_experience_preference (int): User's preference for cultural experiences (1-5).
            nature_focused_tour_preference (int): User's preference for nature-focused tours (1-5).
        """
        if not (1 <= cultural_experience_preference <= 5):
            raise ValueError("Cultural experience preference must be between 1 and 5")
        if not (1 <= nature_focused_tour_preference <= 5):
            raise ValueError("Nature-focused tour preference must be between 1 and 5")

        self.cultural_experience_preference = cultural_experience_preference
        self.nature_focused_tour_preference = nature_focused_tour_preference

class RecommendationSystem:
    """Provides travel package recommendations based on user preferences."""

    def __init__(self, travel_packages):
        """
        Initializes a RecommendationSystem object.

        Args:
            travel_packages (list): List of TravelPackage objects.
        """
        self.travel_packages = travel_packages

    def get_recommendations(self, user_preferences, num_recommendations=3):
        """
        Returns a list of recommended travel packages based on user preferences.

        Args:
            user_preferences (UserPreferences): User's preferences.
            num_recommendations (int): Number of recommendations to return. Defaults to 3.

        Returns:
            list: List of recommended TravelPackage objects.
        """
        # Calculate a score for each travel package based on user preferences
        package_scores = []
        for package in self.travel_packages:
            cultural_score = len([experience for experience in package.cultural_experiences if experience == user_preferences.cultural_experience_preference])
            nature_score = len([tour for tour in package.nature_focused_tours if tour == user_preferences.nature_focused_tour_preference])
            score = cultural_score + nature_score
            package_scores.append((package, score))

        # Sort packages by score and return top recommendations
        package_scores.sort(key=lambda x: x[1], reverse=True)
        return [package for package, score in package_scores[:num_recommendations]]

def main():
    # Example travel packages
    travel_packages = [
        TravelPackage(1, "Package 1", [1, 2, 3], [4, 5]),
        TravelPackage(2, "Package 2", [2, 3, 4], [5, 1]),
        TravelPackage(3, "Package 3", [1, 3, 5], [2, 4]),
        TravelPackage(4, "Package 4", [1, 2, 4], [3, 5]),
        TravelPackage(5, "Package 5", [2, 4, 5], [1, 3]),
    ]

    # Example user preferences
    user_preferences = UserPreferences(3, 4)

    # Create a recommendation system and get recommendations
    recommendation_system = RecommendationSystem(travel_packages)
    recommendations = recommendation_system.get_recommendations(user_preferences)

    # Print recommendations
    print("Recommended travel packages:")
    for i, package in enumerate(recommendations):
        print(f"{i+1}. {package.name} (ID: {package.package_id})")
        print(f"Cultural experiences: {package.cultural_experiences}")
        print(f"Nature-focused tours: {package.nature_focused_tours}")
        print()

if __name__ == "__main__":
    main()
```
