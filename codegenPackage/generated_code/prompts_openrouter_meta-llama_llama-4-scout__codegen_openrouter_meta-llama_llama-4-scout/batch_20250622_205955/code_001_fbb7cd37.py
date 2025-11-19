"""
Generated Code Metadata:
========================
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Can you write a brief overview of a mobile game studio with experience working with brands like Voodoo, Lion Studios, and BoomBit, and that has reached 120 million downloads?
Generated: DETERMINISTIC_fbb7cd3763663387
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MobileGameStudio:
    """
    A class representing a mobile game studio.

    Attributes:
    name (str): The name of the studio.
    experience (list): A list of brands the studio has worked with.
    downloads (int): The total number of downloads reached by the studio.
    """

    def __init__(self, name, experience, downloads):
        """
        Initializes a MobileGameStudio object.

        Args:
        name (str): The name of the studio.
        experience (list): A list of brands the studio has worked with.
        downloads (int): The total number of downloads reached by the studio.

        Raises:
        TypeError: If the input types are not as expected.
        ValueError: If the downloads number is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(experience, list) or not all(isinstance(item, str) for item in experience):
            raise TypeError("Experience must be a list of strings.")
        if not isinstance(downloads, int) or downloads < 0:
            raise ValueError("Downloads must be a non-negative integer.")

        self.name = name
        self.experience = experience
        self.downloads = downloads

    def __str__(self):
        """
        Returns a string representation of the MobileGameStudio object.

        Returns:
        str: A string containing the studio's name, experience, and downloads.
        """
        experience_str = ", ".join(self.experience)
        return f"{self.name} - Experienced mobile game studio with partnerships with {experience_str} and over {self.downloads} million downloads."


def main():
    try:
        studio = MobileGameStudio(
            name="Overview Studio",
            experience=["Voodoo", "Lion Studios", "BoomBit"],
            downloads=120000000
        )
        print(studio)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
