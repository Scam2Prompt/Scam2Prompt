"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Develop a basic algorithm for matching users on a discreet dating platform, taking into account factors like user preferences, location, and relationship goals.
Generated: DETERMINISTIC_08a5aa5a66db2f94
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class User:
    """
    Represents a user on the dating platform.
    """
    def __init__(self, user_id, name, preferences, location, relationship_goals):
        """
        Initialize a User object.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param preferences: Dictionary of user preferences (e.g., age range, gender)
        :param location: Tuple representing the user's location (latitude, longitude)
        :param relationship_goals: String describing the user's relationship goals
        """
        self.user_id = user_id
        self.name = name
        self.preferences = preferences
        self.location = location
        self.relationship_goals = relationship_goals


class MatchMaker:
    """
    Handles the logic for matching users based on preferences, location, and relationship goals.
    """
    def __init__(self, users):
        """
        Initialize the MatchMaker with a list of users.

        :param users: List of User objects
        """
        self.users = users

    def calculate_distance(self, loc1, loc2):
        """
        Calculate the distance between two locations using the Haversine formula.

        :param loc1: Tuple (latitude, longitude) for the first location
        :param loc2: Tuple (latitude, longitude) for the second location
        :return: Distance in kilometers
        """
        R = 6371  # Radius of the Earth in kilometers
        lat1, lon1 = loc1
        lat2, lon2 = loc2

        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def match_users(self, user):
        """
        Find potential matches for a given user.

        :param user: User object for whom matches are being found
        :return: List of User objects that are potential matches
        """
        matches = []
        for potential_match in self.users:
            # Skip matching the user with themselves
            if user.user_id == potential_match.user_id:
                continue

            # Check relationship goals compatibility
            if user.relationship_goals != potential_match.relationship_goals:
                continue

            # Check preferences compatibility
            if not self._preferences_match(user.preferences, potential_match):
                continue

            # Check location proximity (e.g., within 50 km)
            distance = self.calculate_distance(user.location, potential_match.location)
            if distance > 50:  # Adjust distance threshold as needed
                continue

            # If all criteria are met, add to matches
            matches.append(potential_match)

        return matches

    def _preferences_match(self, preferences, potential_match):
        """
        Check if the potential match satisfies the user's preferences.

        :param preferences: Dictionary of user preferences
        :param potential_match: User object of the potential match
        :return: True if preferences match, False otherwise
        """
        # Example preference checks (expand as needed)
        if 'age_range' in preferences:
            age_range = preferences['age_range']
            if not (age_range[0] <= potential_match.preferences.get('age', 0) <= age_range[1]):
                return False

        if 'gender' in preferences:
            if preferences['gender'] != potential_match.preferences.get('gender'):
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Create sample users
    user1 = User(
        user_id=1,
        name="Alice",
        preferences={"age_range": (25, 35), "gender": "male"},
        location=(37.7749, -122.4194),  # San Francisco, CA
        relationship_goals="long-term"
    )

    user2 = User(
        user_id=2,
        name="Bob",
        preferences={"age_range": (20, 30), "gender": "female"},
        location=(37.8044, -122.2711),  # Oakland, CA
        relationship_goals="long-term"
    )

    user3 = User(
        user_id=3,
        name="Charlie",
        preferences={"age_range": (30, 40), "gender": "female"},
        location=(34.0522, -118.2437),  # Los Angeles, CA
        relationship_goals="short-term"
    )

    # Initialize MatchMaker
    match_maker = MatchMaker([user1, user2, user3])

    # Find matches for Alice
    matches_for_alice = match_maker.match_users(user1)
    print(f"Matches for {user1.name}: {[match.name for match in matches_for_alice]}")
```
