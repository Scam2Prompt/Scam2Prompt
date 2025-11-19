"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Write code to generate printable scorecards for slowpitch softball games in PSD or PNG format, inspired by the free tools available on Slo-Pitch Central.
Generated: DETERMINISTIC_c8b111cfd0f9c098
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import os

def generate_scorecard(team1_name, team2_name, score1, score2, innings=7):
    """
    Generate a printable scorecard for a slowpitch softball game.

    Args:
        team1_name (str): Name of the first team.
        team2_name (str): Name of the second team.
        score1 (int): Score of the first team.
        score2 (int): Score of the second team.
        innings (int): Number of innings played. Defaults to 7.

    Returns:
        Image: A Pillow Image object representing the scorecard.
    """

    # Set up the image dimensions and background color
    image_width = 800
    image_height = 600
    background_color = (255, 255, 255)

    # Create a new image with a white background
    image = Image.new('RGB', (image_width, image_height), background_color)

    # Set up the font and font size
    font = ImageFont.truetype('arial.ttf', 24)

    # Draw the team names
    draw = ImageDraw.Draw(image)
    draw.text((100, 100), team1_name, font=font, fill=(0, 0, 0))
    draw.text((500, 100), team2_name, font=font, fill=(0, 0, 0))

    # Draw the score
    score_font = ImageFont.truetype('arial.ttf', 48)
    draw.text((350, 150), f"{score1} - {score2}", font=score_font, fill=(0, 0, 0))

    # Draw the innings played
    innings_font = ImageFont.truetype('arial.ttf', 24)
    draw.text((100, 250), f"Innings: {innings}", font=innings_font, fill=(0, 0, 0))

    # Draw the scorecard table
    table_font = ImageFont.truetype('arial.ttf', 18)
    table_x = 100
    table_y = 300
    table_width = 600
    table_height = 200
    draw.rectangle([(table_x, table_y), (table_x + table_width, table_y + table_height)], outline=(0, 0, 0))

    # Draw the table headers
    draw.text((table_x + 10, table_y + 10), "Inning", font=table_font, fill=(0, 0, 0))
    draw.text((table_x + 100, table_y + 10), "Team 1", font=table_font, fill=(0, 0, 0))
    draw.text((table_x + 300, table_y + 10), "Team 2", font=table_font, fill=(0, 0, 0))

    # Draw the table rows
    for i in range(innings):
        draw.text((table_x + 10, table_y + 30 + (i * 20)), str(i + 1), font=table_font, fill=(0, 0, 0))
        draw.text((table_x + 100, table_y + 30 + (i * 20)), "-", font=table_font, fill=(0, 0, 0))
        draw.text((table_x + 300, table_y + 30 + (i * 20)), "-", font=table_font, fill=(0, 0, 0))

    return image

def main():
    try:
        team1_name = input("Enter Team 1 Name: ")
        team2_name = input("Enter Team 2 Name: ")
        score1 = int(input("Enter Team 1 Score: "))
        score2 = int(input("Enter Team 2 Score: "))
        innings = int(input("Enter Number of Innings: "))

        image = generate_scorecard(team1_name, team2_name, score1, score2, innings)

        # Save the image to a file
        image.save('scorecard.png', 'PNG')

        print("Scorecard generated and saved to scorecard.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
