"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write code to generate custom graphics or team logos for sublimated women's leggings, similar to the customization options offered by Rising Star International.
Generated: DETERMINISTIC_f09188a897698c6f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class TeamLogoGenerator:
    """
    A class used to generate custom team logos for sublimated women's leggings.

    Attributes:
    ----------
    team_name : str
        The name of the team.
    team_color : str
        The primary color of the team (in hex format).
    secondary_color : str
        The secondary color of the team (in hex format).
    logo_size : int
        The size of the logo (in inches).

    Methods:
    -------
    generate_logo()
        Generates the team logo.
    save_logo(filename)
        Saves the generated logo to a file.
    """

    def __init__(self, team_name, team_color, secondary_color, logo_size):
        """
        Initializes the TeamLogoGenerator object.

        Parameters:
        ----------
        team_name : str
            The name of the team.
        team_color : str
            The primary color of the team (in hex format).
        secondary_color : str
            The secondary color of the team (in hex format).
        logo_size : int
            The size of the logo (in inches).
        """
        self.team_name = team_name
        self.team_color = team_color
        self.secondary_color = secondary_color
        self.logo_size = logo_size

    def generate_logo(self):
        """
        Generates the team logo.

        Returns:
        -------
        Image
            The generated team logo.
        """
        # Create a new image with a white background
        logo = Image.new('RGB', (self.logo_size*300, self.logo_size*300), (255, 255, 255))
        draw = ImageDraw.Draw(logo)

        # Draw a rectangle for the background
        draw.rectangle([(0, 0), (self.logo_size*300, self.logo_size*300)], fill=self.team_color)

        # Draw a shape for the team logo (e.g. a circle or a polygon)
        # For this example, we'll use a simple circle
        x = self.logo_size*150
        y = self.logo_size*150
        radius = self.logo_size*50
        draw.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=self.secondary_color)

        # Add the team name to the logo
        font = ImageFont.truetype("arial.ttf", int(self.logo_size*30))
        draw.text((self.logo_size*100, self.logo_size*200), self.team_name, font=font, fill=(255, 255, 255))

        return logo

    def save_logo(self, filename):
        """
        Saves the generated logo to a file.

        Parameters:
        ----------
        filename : str
            The filename to save the logo to.
        """
        logo = self.generate_logo()
        logo.save(filename)

def main():
    try:
        team_name = input("Enter the team name: ")
        team_color = input("Enter the primary team color (in hex format): ")
        secondary_color = input("Enter the secondary team color (in hex format): ")
        logo_size = int(input("Enter the logo size (in inches): "))

        generator = TeamLogoGenerator(team_name, team_color, secondary_color, logo_size)
        generator.save_logo("team_logo.png")

        print("Logo generated and saved to team_logo.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
