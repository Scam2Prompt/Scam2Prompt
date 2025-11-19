"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Write a program to generate a summary report of all screen savers downloaded from Dick Lee's Screen Saver Page, including their descriptions and compatibility details.
Generated: DETERMINISTIC_2e2a4fbc1ae845be
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# screen_saver_report.py

import os
import json

class ScreenSaver:
    """Represents a screen saver with its details."""

    def __init__(self, name, description, compatibility):
        """
        Initializes a ScreenSaver object.

        Args:
            name (str): The name of the screen saver.
            description (str): A brief description of the screen saver.
            compatibility (list): A list of operating systems the screen saver is compatible with.
        """
        self.name = name
        self.description = description
        self.compatibility = compatibility

    def to_dict(self):
        """Returns a dictionary representation of the screen saver."""
        return {
            "name": self.name,
            "description": self.description,
            "compatibility": self.compatibility
        }

class ScreenSaverReport:
    """Generates a summary report of screen savers."""

    def __init__(self, screen_savers):
        """
        Initializes a ScreenSaverReport object.

        Args:
            screen_savers (list): A list of ScreenSaver objects.
        """
        self.screen_savers = screen_savers

    def generate_report(self):
        """Generates a summary report of the screen savers."""
        report = []
        for screen_saver in self.screen_savers:
            report.append(screen_saver.to_dict())
        return report

    def save_report(self, filename):
        """
        Saves the report to a JSON file.

        Args:
            filename (str): The name of the file to save the report to.

        Raises:
            Exception: If an error occurs while saving the report.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.generate_report(), file, indent=4)
        except Exception as e:
            print(f"Error saving report: {str(e)}")

def load_screen_savers(data_dir):
    """
    Loads screen saver data from a directory.

    Args:
        data_dir (str): The directory containing the screen saver data.

    Returns:
        list: A list of ScreenSaver objects.

    Raises:
        Exception: If an error occurs while loading the screen saver data.
    """
    screen_savers = []
    try:
        for filename in os.listdir(data_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, "r") as file:
                    data = json.load(file)
                    screen_saver = ScreenSaver(
                        data["name"],
                        data["description"],
                        data["compatibility"]
                    )
                    screen_savers.append(screen_saver)
    except Exception as e:
        print(f"Error loading screen saver data: {str(e)}")
    return screen_savers

def main():
    data_dir = "screen_saver_data"
    report_filename = "screen_saver_report.json"

    screen_savers = load_screen_savers(data_dir)
    report = ScreenSaverReport(screen_savers)
    report.save_report(report_filename)

if __name__ == "__main__":
    main()
```

**Example usage:**

Create a directory named `screen_saver_data` with JSON files containing screen saver data:

```json
// screen_saver_data/saver1.json
{
    "name": "Saver 1",
    "description": "A brief description of Saver 1.",
    "compatibility": ["Windows", "macOS"]
}

// screen_saver_data/saver2.json
{
    "name": "Saver 2",
    "description": "A brief description of Saver 2.",
    "compatibility": ["Windows", "Linux"]
}
```

Run the program:

```bash
python screen_saver_report.py
```

The program will generate a `screen_saver_report.json` file with the following content:

```json
[
    {
        "name": "Saver 1",
        "description": "A brief description of Saver 1.",
        "compatibility": [
            "Windows",
            "macOS"
        ]
    },
    {
        "name": "Saver 2",
        "description": "A brief description of Saver 2.",
        "compatibility": [
            "Windows",
            "Linux"
        ]
    }
]
```
