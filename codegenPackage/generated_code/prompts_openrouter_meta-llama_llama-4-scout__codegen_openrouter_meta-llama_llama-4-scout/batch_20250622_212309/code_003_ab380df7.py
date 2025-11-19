"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Create a typography guide for Arabic fonts, including text and display fonts, using the KAFD Font as an example."
Generated: DETERMINISTIC_ab380df7115df10b
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# typography_guide.py

class TypographyGuide:
    """
    A class to generate a typography guide for Arabic fonts.

    Attributes:
    ----------
    font_name : str
        The name of the font to use for the guide.
    text_fonts : list
        A list of text fonts to include in the guide.
    display_fonts : list
        A list of display fonts to include in the guide.

    Methods:
    -------
    generate_guide()
        Generates the typography guide.
    """

    def __init__(self, font_name="KAFD Font"):
        """
        Initializes the TypographyGuide class.

        Parameters:
        ----------
        font_name : str, optional
            The name of the font to use for the guide (default is "KAFD Font").
        """
        self.font_name = font_name
        self.text_fonts = [
            f"{font_name} Light",
            f"{font_name} Regular",
            f"{font_name} Medium",
            f"{font_name} Bold",
            f"{font_name} Black",
        ]
        self.display_fonts = [
            f"{font_name} Display Light",
            f"{font_name} Display Regular",
            f"{font_name} Display Medium",
            f"{font_name} Display Bold",
            f"{font_name} Display Black",
        ]

    def generate_guide(self):
        """
        Generates the typography guide.

        Returns:
        -------
        dict
            A dictionary containing the typography guide.
        """
        guide = {
            "font_name": self.font_name,
            "text_fonts": self.text_fonts,
            "display_fonts": self.display_fonts,
            "font_sizes": {
                "text": {
                    "body": 16,
                    "headline": 24,
                    "title": 30,
                },
                "display": {
                    "title": 48,
                    "subtitle": 36,
                    "hero": 72,
                },
            },
            "font_styles": {
                "text": {
                    "normal": "Regular",
                    "emphasis": "Italic",
                    "strong": "Bold",
                },
                "display": {
                    "normal": "Regular",
                    "emphasis": "Italic",
                    "strong": "Bold",
                },
            },
        }
        return guide

    def print_guide(self):
        """
        Prints the typography guide.
        """
        guide = self.generate_guide()
        print(f"Typography Guide for {guide['font_name']}")
        print("----------------------------------------")
        print("Text Fonts:")
        for font in guide["text_fonts"]:
            print(f"- {font}")
        print()
        print("Display Fonts:")
        for font in guide["display_fonts"]:
            print(f"- {font}")
        print()
        print("Font Sizes:")
        for category, sizes in guide["font_sizes"].items():
            print(f"{category.capitalize()} Fonts:")
            for style, size in sizes.items():
                print(f"- {style.capitalize()}: {size}px")
            print()
        print("Font Styles:")
        for category, styles in guide["font_styles"].items():
            print(f"{category.capitalize()} Fonts:")
            for style, description in styles.items():
                print(f"- {style.capitalize()}: {description}")
            print()


def main():
    try:
        guide = TypographyGuide()
        guide.print_guide()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
