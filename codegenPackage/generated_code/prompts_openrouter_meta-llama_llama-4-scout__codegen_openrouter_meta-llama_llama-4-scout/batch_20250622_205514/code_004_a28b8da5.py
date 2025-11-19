"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Create a description for a magic show for adults at a corporate event in Estonia."
Generated: DETERMINISTIC_a28b8da57dbccd2a
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MagicShow:
    def __init__(self, event_name, location, target_audience):
        """
        Initialize a MagicShow object.

        Args:
            event_name (str): The name of the corporate event.
            location (str): The location of the corporate event.
            target_audience (str): The target audience of the corporate event.

        Raises:
            ValueError: If event_name, location, or target_audience is empty.
        """
        if not event_name or not location or not target_audience:
            raise ValueError("Event name, location, and target audience cannot be empty.")

        self.event_name = event_name
        self.location = location
        self.target_audience = target_audience

    def generate_description(self):
        """
        Generate a description for a magic show.

        Returns:
            str: A description for a magic show.
        """
        description = f"**{self.event_name} Magic Experience**\n\n"
        description += f"Join us for an unforgettable night of magic and wonder at {self.location} in Estonia.\n"
        description += f"Our specially crafted magic show for adults is designed to mesmerize and delight your {self.target_audience} audience.\n\n"
        description += "Expect mind-bending illusions, spectacular tricks, and an evening of enchantment that will leave your guests talking long after the curtain closes.\n\n"
        description += "**Show Highlights:**\n"
        description += "- Baffling magic tricks and illusions\n"
        description += "- Interactive audience participation\n"
        description += "- A touch of Estonian flair and mystery\n\n"
        description += "Let us transport your guests to a world of magic and awe. Book our magic show today and make your corporate event an unforgettable experience!"

        return description


def main():
    try:
        event_name = "Estonian Corporate Magic Night"
        location = "Tallinn, Estonia"
        target_audience = "distinguished"

        magic_show = MagicShow(event_name, location, target_audience)
        print(magic_show.generate_description())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
