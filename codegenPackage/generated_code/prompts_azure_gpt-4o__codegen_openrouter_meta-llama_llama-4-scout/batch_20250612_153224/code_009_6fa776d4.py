"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Develop a recommendation system for Emanuelson Reels that suggests leather cases for purchased reels, such as "Salmon Wide," based on user preferences.
Generated: DETERMINISTIC_6fa776d4edf37c83
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

class Reel:
    def __init__(self, name, material, width, type):
        """
        Initialize a Reel object.

        Args:
            name (str): Reel name.
            material (str): Reel material.
            width (str): Reel width.
            type (str): Reel type.
        """
        self.name = name
        self.material = material
        self.width = width
        self.type = type

class User:
    def __init__(self, name, preferences):
        """
        Initialize a User object.

        Args:
            name (str): User name.
            preferences (dict): User preferences (e.g., material, width, type).
        """
        self.name = name
        self.preferences = preferences
        self.purchased_reels = []

    def add_purchased_reel(self, reel):
        """
        Add a purchased reel to the user's list.

        Args:
            reel (Reel): Purchased reel.
        """
        self.purchased_reels.append(reel)

class LeatherCase:
    def __init__(self, name, material, width, type, compatibility):
        """
        Initialize a LeatherCase object.

        Args:
            name (str): Leather case name.
            material (str): Leather case material.
            width (str): Leather case width.
            type (str): Leather case type.
            compatibility (list): Compatible reel names.
        """
        self.name = name
        self.material = material
        self.width = width
        self.type = type
        self.compatibility = compatibility

class RecommendationSystem:
    def __init__(self, reels, leather_cases):
        """
        Initialize a RecommendationSystem object.

        Args:
            reels (list): List of Reel objects.
            leather_cases (list): List of LeatherCase objects.
        """
        self.reels = reels
        self.leather_cases = leather_cases

    def suggest_leather_cases(self, user):
        """
        Suggest leather cases for a user based on their preferences and purchased reels.

        Args:
            user (User): User object.

        Returns:
            list: Suggested leather cases.
        """
        suggested_cases = []
        for reel in user.purchased_reels:
            for case in self.leather_cases:
                if reel.name in case.compatibility:
                    if (case.material in user.preferences.get("material", []) or
                            case.width in user.preferences.get("width", []) or
                            case.type in user.preferences.get("type", [])):
                        suggested_cases.append(case)
        return suggested_cases

def main():
    # Initialize reels
    reels = [
        Reel("Salmon Wide", "Aluminum", "Wide", "Spinning"),
        Reel("Trout Narrow", "Graphite", "Narrow", "Fly"),
    ]

    # Initialize leather cases
    leather_cases = [
        LeatherCase("Salmon Case", "Leather", "Wide", "Spinning", ["Salmon Wide"]),
        LeatherCase("Trout Case", "Leather", "Narrow", "Fly", ["Trout Narrow"]),
        LeatherCase("Universal Case", "Leather", "Wide", "Spinning", ["Salmon Wide", "Trout Narrow"]),
    ]

    # Initialize user
    user_preferences = {
        "material": ["Leather"],
        "width": ["Wide"],
        "type": ["Spinning"],
    }
    user = User("Emanuelson", user_preferences)

    # Add purchased reel
    user.add_purchased_reel(reels[0])

    # Initialize recommendation system
    recommendation_system = RecommendationSystem(reels, leather_cases)

    try:
        # Suggest leather cases
        suggested_cases = recommendation_system.suggest_leather_cases(user)
        if suggested_cases:
            print("Suggested Leather Cases:")
            for case in suggested_cases:
                print(f"- {case.name} ({case.material}, {case.width}, {case.type})")
        else:
            print("No suggested leather cases found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
