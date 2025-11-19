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
    """
    A class to represent a magic show for adults at a corporate event.
    """

    def __init__(self, title, duration, location, audience_size):
        """
        Initializes the MagicShow with the given parameters.

        :param title: str - The title of the magic show
        :param duration: int - Duration of the show in minutes
        :param location: str - Location of the event
        :param audience_size: int - Expected number of audience members
        """
        self.title = title
        self.duration = duration
        self.location = location
        self.audience_size = audience_size

    def generate_description(self):
        """
        Generates a description for the magic show.

        :return: str - A formatted description of the magic show
        """
        try:
            description = (
                f"Join us for '{self.title}', a captivating magic show designed "
                f"exclusively for adults at your corporate event in {self.location}.\n"
                f"Prepare to be amazed for {self.duration} minutes as our talented magician "
                f"takes you on a journey of wonder and intrigue, perfect for an audience of "
                f"{self.audience_size} professionals.\n"
                "This show promises to break the ice, foster connections, and leave everyone "
                "talking long after the final trick is performed.\n"
                "Don't miss out on an unforgettable experience!"
            )
            return description
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating description: {e}")
            return "An error occurred while generating the show description."

# Example usage
if __name__ == "__main__":
    try:
        magic_show = MagicShow(
            title="Mysteries Unveiled",
            duration=60,
            location="Tallinn, Estonia",
            audience_size=100
        )
        print(magic_show.generate_description())
    except Exception as e:
        print(f"An error occurred while creating the magic show: {e}")
```
