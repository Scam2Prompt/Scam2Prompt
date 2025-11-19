"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Write a Python script to generate a color palette for a residential painting project in Mornington Peninsula, considering factors like natural lighting, existing decor, and personal preferences, as discussed on the Painters Mornington Peninsula website.
Generated: DETERMINISTIC_dc759d02205fe8fc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# color_palette_generator.py

import colorsys

class ColorPaletteGenerator:
    """
    Generates a color palette for a residential painting project in Mornington Peninsula.
    """

    def __init__(self, natural_lighting, existing_decor, personal_preferences):
        """
        Initializes the color palette generator.

        Args:
            natural_lighting (str): The natural lighting condition (e.g., bright, medium, low).
            existing_decor (dict): A dictionary of existing decor colors.
            personal_preferences (dict): A dictionary of personal color preferences.
        """
        self.natural_lighting = natural_lighting
        self.existing_decor = existing_decor
        self.personal_preferences = personal_preferences

    def generate_palette(self):
        """
        Generates a color palette based on the input factors.

        Returns:
            dict: A dictionary containing the generated color palette.
        """
        # Define a base color based on natural lighting
        base_color = self._get_base_color(self.natural_lighting)

        # Select colors that complement the existing decor
        decor_colors = self._get_decor_colors(base_color, self.existing_decor)

        # Incorporate personal preferences into the palette
        personalized_colors = self._get_personalized_colors(base_color, self.personal_preferences)

        # Create a cohesive color palette
        palette = {
            "base": base_color,
            "walls": decor_colors["walls"],
            "trim": decor_colors["trim"],
            "accent": personalized_colors["accent"]
        }

        return palette

    def _get_base_color(self, natural_lighting):
        """
        Returns a base color based on the natural lighting condition.

        Args:
            natural_lighting (str): The natural lighting condition.

        Returns:
            str: A base color in hexadecimal format.
        """
        # Define base colors for different lighting conditions
        base_colors = {
            "bright": "#F7F7F7",  # Light gray
            "medium": "#E5E5E5",  # Medium gray
            "low": "#C9C9C9"  # Dark gray
        }

        return base_colors.get(natural_lighting, "#E5E5E5")  # Default to medium gray

    def _get_decor_colors(self, base_color, existing_decor):
        """
        Selects colors that complement the existing decor.

        Args:
            base_color (str): The base color.
            existing_decor (dict): A dictionary of existing decor colors.

        Returns:
            dict: A dictionary containing the selected decor colors.
        """
        # Convert base color to RGB
        base_rgb = self._hex_to_rgb(base_color)

        # Calculate complementary colors for existing decor
        decor_colors = {}
        for room, color in existing_decor.items():
            decor_rgb = self._hex_to_rgb(color)
            complementary_color = self._get_complementary_color(base_rgb, decor_rgb)
            decor_colors[room] = self._rgb_to_hex(complementary_color)

        # Assign colors to walls and trim
        walls_color = decor_colors.get("walls", "#FFFFFF")  # Default to white
        trim_color = decor_colors.get("trim", "#000000")  # Default to black

        return {"walls": walls_color, "trim": trim_color}

    def _get_personalized_colors(self, base_color, personal_preferences):
        """
        Incorporates personal preferences into the palette.

        Args:
            base_color (str): The base color.
            personal_preferences (dict): A dictionary of personal color preferences.

        Returns:
            dict: A dictionary containing the personalized colors.
        """
        # Convert base color to RGB
        base_rgb = self._hex_to_rgb(base_color)

        # Calculate personalized accent color
        accent_color = self._get_analogous_color(base_rgb, personal_preferences.get("accent", (0.5, 0.5)))

        return {"accent": self._rgb_to_hex(accent_color)}

    @staticmethod
    def _hex_to_rgb(hex_color):
        """
        Converts a hexadecimal color to RGB.

        Args:
            hex_color (str): A hexadecimal color.

        Returns:
            tuple: An RGB color tuple.
        """
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

    @staticmethod
    def _rgb_to_hex(rgb_color):
        """
        Converts an RGB color to hexadecimal.

        Args:
            rgb_color (tuple): An RGB color tuple.

        Returns:
            str: A hexadecimal color.
        """
        return "#{:02x}{:02x}{:02x}".format(
            int(rgb_color[0] * 255),
            int(rgb_color[1] * 255),
            int(rgb_color[2] * 255)
        )

    @staticmethod
    def _get_complementary_color(base_rgb, decor_rgb):
        """
        Calculates the complementary color of two colors.

        Args:
            base_rgb (tuple): The base RGB color.
            decor_rgb (tuple): The decor RGB color.

        Returns:
            tuple: The complementary RGB color.
        """
        base_hsv = colorsys.rgb_to_hsv(*base_rgb)
        decor_hsv = colorsys.rgb_to_hsv(*decor_rgb)

        # Calculate complementary color in HSV
        complementary_hsv = ((base_hsv[0] + 0.5) % 1, base_hsv[1], base_hsv[2])

        # Convert back to RGB
        return colorsys.hsv_to_rgb(*complementary_hsv)

    @staticmethod
    def _get_analogous_color(base_rgb, preference):
        """
        Calculates an analogous color based on a base color and personal preference.

        Args:
            base_rgb (tuple): The base RGB color.
            preference (tuple): A tuple containing the hue and saturation preferences.

        Returns:
            tuple: The analogous RGB color.
        """
        base_hsv = colorsys.rgb_to_hsv(*base_rgb)

        # Calculate analogous color in HSV
        analogous_hsv = ((base_hsv[0] + preference[0]) % 1, base_hsv[1] * preference[1], base_hsv[2])

        # Convert back to RGB
        return colorsys.hsv_to_rgb(*analogous_hsv)


def main():
    try:
        natural_lighting = "medium"
        existing_decor = {"walls": "#C9E4CA", "trim": "#969696"}
        personal_preferences = {"accent": (0.2, 0.8)}

        generator = ColorPaletteGenerator(natural_lighting, existing_decor, personal_preferences)
        palette = generator.generate_palette()

        print("Generated Color Palette:")
        for name, color in palette.items():
            print(f"{name.capitalize()}: {color}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
