"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Write code to generate printable scorecards for slowpitch softball games in PSD or PNG format, inspired by the free tools available on Slo-Pitch Central.
Generated: DETERMINISTIC_c8b111cfd0f9c098
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont


def generate_softball_scorecard(team1, team2, innings, output_file):
    """
    Generates a printable softball scorecard as a PNG file.

    Args:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.
        innings (int): Number of innings in the game.
        output_file (str): Path to the output PNG file.

    Raises:
        ValueError: If innings is less than 1 or if output_file is invalid.
    """
    # Validate innings
    if innings < 1:
        raise ValueError("Number of innings must be at least 1.")

    # Validate output file extension
    if not output_file.lower().endswith(('.png', '.psd')):
        raise ValueError("Output file must be a PNG or PSD format.")

    # Canvas dimensions
    canvas_width = 1000
    canvas_height = 800

    # Create a blank white canvas
    img = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(img)

    # Font setup
    font_path = "arial.ttf"  # Replace with your font path if necessary
    try:
        font_title = ImageFont.truetype(font_path, 40)
        font_labels = ImageFont.truetype(font_path, 20)
    except OSError:
        raise OSError(f"Font file '{font_path}' not found. Please provide a valid font path.")

    # Title
    title = f"Softball Scorecard: {team1} vs {team2}"
    draw.text((canvas_width // 2 - len(title) * 10, 20), title, fill="black", font=font_title)

    # Draw team labels
    draw.text((50, 100), f"Team: {team1}", fill="black", font=font_labels)
    draw.text((50, 130), f"Team: {team2}", fill="black", font=font_labels)

    # Draw table headers
    draw.text((200, 200), "Inning", fill="black", font=font_labels)
    for i in range(innings):
        draw.text((300 + i * 50, 200), f"{i + 1}", fill="black", font=font_labels)

    # Draw score rows for each team
    draw.text((200, 250), team1, fill="black", font=font_labels)
    draw.text((200, 300), team2, fill="black", font=font_labels)

    # Draw score boxes
    for i in range(innings):
        # Team 1 boxes
        draw.rectangle([300 + i * 50, 250, 350 + i * 50, 280], outline="black")
        # Team 2 boxes
        draw.rectangle([300 + i * 50, 300, 350 + i * 50, 330], outline="black")

    # Save the image
    try:
        img.save(output_file)
    except Exception as e:
        raise IOError(f"Failed to save the scorecard: {e}")


if __name__ == "__main__":
    # Example usage
    team1 = "Red Sox"
    team2 = "Blue Jays"
    innings = 7
    output_file = "softball_scorecard.png"

    try:
        generate_softball_scorecard(team1, team2, innings, output_file)
        print(f"Scorecard successfully generated: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"Error: {e}")
```
