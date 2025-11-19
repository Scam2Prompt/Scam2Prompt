"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: "Develop a pitch for a bizdev consulting project that involves creating a digital media platform for sports networks."
Generated: DETERMINISTIC_51d862e9034b603a
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DigitalMediaPlatform:
    """
    A class to represent a digital media platform for sports networks.
    """

    def __init__(self, name, target_audience):
        """
        Initializes the DigitalMediaPlatform with a name and target audience.

        :param name: str - The name of the digital media platform.
        :param target_audience: str - The target audience for the platform.
        """
        self.name = name
        self.target_audience = target_audience
        self.content = []
        self.partners = []

    def add_content(self, content_item):
        """
        Adds a content item to the platform.

        :param content_item: dict - A dictionary containing content details.
        :raises ValueError: If content_item is not a dictionary or missing required keys.
        """
        if not isinstance(content_item, dict):
            raise ValueError("Content item must be a dictionary.")
        
        required_keys = ['title', 'type', 'duration']
        if not all(key in content_item for key in required_keys):
            raise ValueError(f"Content item must contain keys: {required_keys}")

        self.content.append(content_item)

    def add_partner(self, partner_name):
        """
        Adds a partner to the platform.

        :param partner_name: str - The name of the partner organization.
        :raises ValueError: If partner_name is not a string or is empty.
        """
        if not isinstance(partner_name, str) or not partner_name:
            raise ValueError("Partner name must be a non-empty string.")
        
        self.partners.append(partner_name)

    def get_content(self):
        """
        Returns the list of content available on the platform.

        :return: list - A list of content items.
        """
        return self.content

    def get_partners(self):
        """
        Returns the list of partners associated with the platform.

        :return: list - A list of partner names.
        """
        return self.partners

    def __str__(self):
        """
        Returns a string representation of the DigitalMediaPlatform.

        :return: str - A summary of the platform.
        """
        return f"Digital Media Platform: {self.name}, Target Audience: {self.target_audience}, " \
               f"Content Count: {len(self.content)}, Partners Count: {len(self.partners)}"


# Example usage
if __name__ == "__main__":
    try:
        platform = DigitalMediaPlatform("SportsHub", "Sports Enthusiasts")
        platform.add_content({"title": "Championship Highlights", "type": "video", "duration": "10min"})
        platform.add_partner("ESPN")
        
        print(platform)
        print("Available Content:", platform.get_content())
        print("Partners:", platform.get_partners())
    except Exception as e:
        print(f"An error occurred: {e}")
```
