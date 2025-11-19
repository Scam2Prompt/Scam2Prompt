"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Write a script in a programming language of your choice to generate worksheets for kids to practice their typing skills, using exercises and games from Portal de Saltinho as inspiration."
Generated: DETERMINISTIC_5df9e721fcbfd28f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import os

# Constants
EXERCISES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that improves with practice.",
    "Saltinho is a portal for learning and fun.",
    "Practice makes perfect!",
    "Never stop learning new things."
]
WORKSHEET_DIR = "worksheets"
NUM_WORKSHEETS = 5
NUM_EXERCISES_PER_WORKSHEET = 3

def generate_worksheet_content(exercises, num_exercises):
    """
    Generate content for a single worksheet by randomly selecting exercises.

    Args:
        exercises (list): List of available exercises.
        num_exercises (int): Number of exercises to include in the worksheet.

    Returns:
        str: Formatted worksheet content.
    """
    selected_exercises = random.sample(exercises, num_exercises)
    content = "Typing Practice Worksheet\n\n"
    for i, exercise in enumerate(selected_exercises, start=1):
        content += f"Exercise {i}:\n{exercise}\n\n"
    return content

def save_worksheet(content, filename):
    """
    Save worksheet content to a file.

    Args:
        content (str): Worksheet content to save.
        filename (str): Name of the file to save the content in.
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
    except IOError as e:
        print(f"Error saving worksheet to {filename}: {e}")

def generate_worksheets(exercises, num_worksheets, num_exercises_per_worksheet, output_dir):
    """
    Generate multiple worksheets and save them to the specified directory.

    Args:
        exercises (list): List of available exercises.
        num_worksheets (int): Number of worksheets to generate.
        num_exercises_per_worksheet (int): Number of exercises per worksheet.
        output_dir (str): Directory to save the worksheets in.
    """
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            print(f"Error creating directory {output_dir}: {e}")
            return

    for i in range(1, num_worksheets + 1):
        content = generate_worksheet_content(exercises, num_exercises_per_worksheet)
        filename = os.path.join(output_dir, f"worksheet_{i}.txt")
        save_worksheet(content, filename)
        print(f"Worksheet {i} saved to {filename}")

if __name__ == "__main__":
    # Generate worksheets
    generate_worksheets(EXERCISES, NUM_WORKSHEETS, NUM_EXERCISES_PER_WORKSHEET, WORKSHEET_DIR)
    print("All worksheets generated successfully!")
```
