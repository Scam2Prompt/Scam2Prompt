"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidrtekz63j5fj7fsvnv5iu3jpcsbfwjdfvsaaml43ksqrp5impzy4.ipfs.dweb.link
Prompt: Write a function to programmatically add "$PARAM" to a user's social media profile name and calculate the points earned.
Generated: DETERMINISTIC_c9d9f4d37759a41e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SocialMediaProfile:
    """
    A class to represent a user's social media profile.
    """

    def __init__(self, username, points=0):
        """
        Initializes a new social media profile.

        :param username: str - The user's profile name.
        :param points: int - The initial points earned by the user.
        """
        self.username = username
        self.points = points

    def add_param_to_username(self, param):
        """
        Adds a specified parameter to the user's username and updates points.

        :param param: str - The parameter to be added to the username.
        :return: None
        :raises ValueError: If the parameter is not a valid string or empty.
        """
        if not isinstance(param, str) or not param:
            raise ValueError("Parameter must be a non-empty string.")

        # Append the parameter to the username
        self.username += f" {param}"

        # Calculate points earned for adding the parameter
        self.points += self.calculate_points(param)

    def calculate_points(self, param):
        """
        Calculates points based on the parameter added to the username.

        :param param: str - The parameter that was added.
        :return: int - The points earned for adding the parameter.
        """
        # Example points calculation logic
        points_earned = 0
        if param == "$PARAM":
            points_earned = 10  # Assign points for the specific parameter

        return points_earned

    def get_profile_info(self):
        """
        Returns the current status of the user's profile.

        :return: str - A formatted string containing the username and points.
        """
        return f"Username: {self.username}, Points: {self.points}"


# Example Usage
if __name__ == "__main__":
    try:
        # Create a user profile
        user_profile = SocialMediaProfile(username="JohnDoe")

        # Add "$PARAM" to the username and update points
        user_profile.add_param_to_username("$PARAM")

        # Print the updated profile info
        print(user_profile.get_profile_info())
    except ValueError as e:
        print(f"Error: {e}")
```
