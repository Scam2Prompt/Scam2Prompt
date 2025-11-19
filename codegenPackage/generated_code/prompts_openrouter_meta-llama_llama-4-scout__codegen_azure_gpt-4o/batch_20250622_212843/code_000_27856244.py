"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Design a custom soccer uniform for a team with a specific logo and color scheme using Rising Star International's sportswear offerings.
Generated: DETERMINISTIC_27856244806d5b61
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

# Function to create a custom soccer uniform
def create_soccer_uniform(team_name, logo_path, primary_color, secondary_color, output_path):
    """
    Creates a custom soccer uniform design for a team.

    Parameters:
        team_name (str): Name of the soccer team.
        logo_path (str): Path to the team's logo image file.
        primary_color (tuple): RGB tuple for the primary color of the uniform.
        secondary_color (tuple): RGB tuple for the secondary color of the uniform.
        output_path (str): Path to save the generated uniform design.

    Returns:
        None
    """
    try:
        # Validate input parameters
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo file not found at path: {logo_path}")
        if not isinstance(primary_color, tuple) or not isinstance(secondary_color, tuple):
            raise ValueError("Primary and secondary colors must be RGB tuples.")
        
        # Create a blank canvas for the uniform design
        canvas_width, canvas_height = 800, 1000
        uniform_canvas = Image.new("RGB", (canvas_width, canvas_height), primary_color)

        # Draw secondary color accents
        draw = ImageDraw.Draw(uniform_canvas)
        accent_height = 200
        draw.rectangle([(0, canvas_height - accent_height), (canvas_width, canvas_height)], fill=secondary_color)

        # Add team logo to the uniform
        logo = Image.open(logo_path).convert("RGBA")
        logo_width, logo_height = 200, 200
        logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)
        logo_position = ((canvas_width - logo_width) // 2, 100)
        uniform_canvas.paste(logo, logo_position, logo)

        # Add team name to the uniform
        font_path = "arial.ttf"  # Ensure this font file exists or replace with a valid path
        try:
            font = ImageFont.truetype(font_path, 50)
        except IOError:
            raise FileNotFoundError(f"Font file not found at path: {font_path}")
        
        text_position = ((canvas_width - len(team_name) * 25) // 2, 350)
        draw.text(text_position, team_name, fill="white", font=font)

        # Save the final design
        uniform_canvas.save(output_path)
        print(f"Soccer uniform design saved successfully at: {output_path}")

    except Exception as e:
        print(f"Error creating soccer uniform: {e}")

# Example usage
if __name__ == "__main__":
    # Define team details
    team_name = "Rising Stars FC"
    logo_path = "team_logo.png"  # Replace with the actual path to the logo file
    primary_color = (0, 102, 204)  # Blue
    secondary_color = (255, 255, 255)  # White
    output_path = "soccer_uniform.png"

    # Generate the soccer uniform
    create_soccer_uniform(team_name, logo_path, primary_color, secondary_color, output_path)
```
