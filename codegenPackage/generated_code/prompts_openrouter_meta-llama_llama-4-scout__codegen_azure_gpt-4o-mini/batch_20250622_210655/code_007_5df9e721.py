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

class TypingWorksheetGenerator:
    def __init__(self, exercises, output_dir='worksheets'):
        """
        Initializes the TypingWorksheetGenerator with a list of exercises and an output directory.

        :param exercises: List of exercises (strings) for typing practice.
        :param output_dir: Directory where the worksheets will be saved.
        """
        self.exercises = exercises
        self.output_dir = output_dir
        self._create_output_directory()

    def _create_output_directory(self):
        """Creates the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_worksheet(self, num_exercises=5):
        """
        Generates a typing worksheet with a specified number of exercises.

        :param num_exercises: Number of exercises to include in the worksheet.
        :return: The filename of the generated worksheet.
        """
        selected_exercises = random.sample(self.exercises, min(num_exercises, len(self.exercises)))
        worksheet_content = self._format_worksheet(selected_exercises)
        filename = self._save_worksheet(worksheet_content)
        return filename

    def _format_worksheet(self, exercises):
        """Formats the exercises into a worksheet string."""
        worksheet_lines = ["Typing Practice Worksheet\n", "=" * 30 + "\n"]
        for i, exercise in enumerate(exercises, start=1):
            worksheet_lines.append(f"{i}. {exercise}\n")
        return ''.join(worksheet_lines)

    def _save_worksheet(self, content):
        """Saves the worksheet content to a file and returns the filename."""
        filename = os.path.join(self.output_dir, f'typing_worksheet_{self._get_timestamp()}.txt')
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Worksheet saved as: {filename}")
        except IOError as e:
            print(f"Error saving worksheet: {e}")
            raise
        return filename

    @staticmethod
    def _get_timestamp():
        """Returns the current timestamp as a string."""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")

if __name__ == "__main__":
    # Sample exercises inspired by Portal de Saltinho
    exercises = [
        "The quick brown fox jumps over the lazy dog.",
        "Pack my box with five dozen liquor jugs.",
        "How razorback-jumping frogs can level six piqued gymnasts!",
        "Bright vixens jump; dozy fowl quack.",
        "Sphinx of black quartz, judge my vow."
    ]

    # Create a worksheet generator instance
    generator = TypingWorksheetGenerator(exercises)

    # Generate a worksheet with 5 exercises
    try:
        generator.generate_worksheet(num_exercises=5)
    except Exception as e:
        print(f"An error occurred: {e}")
```
