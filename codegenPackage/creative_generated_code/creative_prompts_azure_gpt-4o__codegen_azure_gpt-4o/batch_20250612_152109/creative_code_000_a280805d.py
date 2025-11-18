"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Write Python code to generate a step-by-step guide for creating a Halloween countdown calendar using paper crafts, as described on Craft Intra.
Generated: DETERMINISTIC_a280805d09b3af07
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from datetime import datetime, timedelta
import os

def generate_halloween_countdown_guide(output_file="halloween_guide.txt"):
    """
    Generates a step-by-step guide for creating a Halloween countdown calendar using paper crafts.

    Args:
        output_file (str): The name of the file to save the guide. Defaults to 'halloween_guide.txt'.
    """
    try:
        # Define the countdown start and end dates
        today = datetime.today()
        halloween_date = datetime(today.year, 10, 31)

        # If today is past Halloween, set the countdown for next year
        if today > halloween_date:
            halloween_date = datetime(today.year + 1, 10, 31)

        countdown_days = (halloween_date - today).days

        # Step-by-step guide content
        guide = [
            "Step-by-Step Guide: Creating a Halloween Countdown Calendar using Paper Crafts",
            "",
            "1. Gather Materials:",
            "   - Colored paper (orange, black, white, green, etc.)",
            "   - Scissors",
            "   - Glue or tape",
            "   - Markers or pens",
            "   - Stickers (optional)",
            "",
            f"2. Prepare {countdown_days} Paper Tags or Cards:",
            "   - Cut out squares, circles, or any fun shapes from colored paper.",
            "   - Write numbers from 1 to {countdown_days} on each tag/card, starting from today.",
            "",
            "3. Decorate Each Tag/Card:",
            "   - Draw Halloween-themed designs (e.g., pumpkins, ghosts, bats, witches).",
            "   - Use stickers or markers to add more flair.",
            "",
            "4. Create a Display Board or String:",
            "   - Arrange the tags/cards on a board or hang them on a string.",
            "   - Ensure they are in sequential order for easy countdown tracking.",
            "",
            "5. Daily Countdown:",
            "   - Each day, remove or flip the tag/card corresponding to the day's countdown.",
            "",
            "6. Enjoy the Festivities:",
            "   - Use the calendar to build excitement for Halloween!",
            "",
            "Happy Crafting and Happy Halloween!"
        ]

        # Save the guide to a text file
        with open(output_file, 'w') as file:
            for line in guide:
                file.write(line + "\n")

        print(f"Guide successfully written to '{output_file}'.")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Main function execution
if __name__ == "__main__":
    # Setting output directory
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Generate Halloween countdown guide
    output_path = os.path.join(output_dir, "halloween_guide.txt")
    generate_halloween_countdown_guide(output_path)
```
