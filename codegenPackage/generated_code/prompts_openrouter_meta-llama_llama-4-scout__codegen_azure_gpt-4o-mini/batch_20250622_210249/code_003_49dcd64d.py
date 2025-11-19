"""
Generated Code Metadata:
========================
Original URL: https://steth-award.net
Prompt: How can I use the Xbox Family Settings app to manage my child's gaming experience on Xbox, and what features does it offer?
Generated: DETERMINISTIC_49dcd64d76642ff6
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class XboxFamilySettings:
    """
    A class to manage Xbox Family Settings for parental control over gaming experiences.
    """

    def __init__(self, child_name):
        """
        Initializes the XboxFamilySettings with the child's name.

        :param child_name: str - The name of the child for whom settings are being managed.
        """
        self.child_name = child_name
        self.settings = {
            "screen_time": None,
            "content_restrictions": [],
            "communication_privacy": True,
            "purchase_privacy": True,
            "game_limits": {}
        }

    def set_screen_time(self, hours):
        """
        Sets the daily screen time limit for the child.

        :param hours: int - The number of hours allowed for gaming each day.
        :raises ValueError: If hours is not a positive integer.
        """
        if not isinstance(hours, int) or hours <= 0:
            raise ValueError("Screen time must be a positive integer.")
        self.settings["screen_time"] = hours

    def add_content_restriction(self, content):
        """
        Adds a content restriction for the child.

        :param content: str - The type of content to restrict (e.g., "Mature", "Teen").
        :raises ValueError: If content is not a valid restriction type.
        """
        valid_restrictions = ["Everyone", "Teen", "Mature"]
        if content not in valid_restrictions:
            raise ValueError(f"Invalid content restriction. Choose from: {valid_restrictions}")
        self.settings["content_restrictions"].append(content)

    def set_communication_privacy(self, is_private):
        """
        Sets the communication privacy setting for the child.

        :param is_private: bool - True to restrict communication, False to allow it.
        """
        self.settings["communication_privacy"] = is_private

    def set_purchase_privacy(self, is_private):
        """
        Sets the purchase privacy setting for the child.

        :param is_private: bool - True to restrict purchases, False to allow them.
        """
        self.settings["purchase_privacy"] = is_private

    def set_game_limit(self, game_name, limit):
        """
        Sets a specific game limit for the child.

        :param game_name: str - The name of the game to limit.
        :param limit: int - The number of hours allowed for that game.
        :raises ValueError: If limit is not a positive integer.
        """
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Game limit must be a positive integer.")
        self.settings["game_limits"][game_name] = limit

    def get_settings(self):
        """
        Returns the current settings for the child's gaming experience.

        :return: dict - The current settings.
        """
        return self.settings


# Example usage
if __name__ == "__main__":
    try:
        family_settings = XboxFamilySettings("John Doe")
        family_settings.set_screen_time(3)
        family_settings.add_content_restriction("Teen")
        family_settings.set_communication_privacy(True)
        family_settings.set_purchase_privacy(False)
        family_settings.set_game_limit("Minecraft", 2)

        # Print the current settings
        print(family_settings.get_settings())
    except ValueError as e:
        print(f"Error: {e}")
```
