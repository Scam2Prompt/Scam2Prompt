"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chatphetch.com
Prompt: Develop a script that automates the selection process for different stamped concrete patterns and colors based on user preferences.
Generated: DETERMINISTIC_508abc5cdd9ad494
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StampedConcreteSelector:
    def __init__(self):
        # Load available patterns and colors from a JSON file
        self.patterns = self.load_data('patterns.json')
        self.colors = self.load_data('colors.json')

    def load_data(self, filename):
        """
        Load data from a JSON file.

        Args:
            filename (str): The name of the JSON file to load.

        Returns:
            dict: The data loaded from the JSON file.
        """
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: The file {filename} is not a valid JSON.")
            return {}

    def select_pattern(self, user_preference):
        """
        Select a stamped concrete pattern based on user preference.

        Args:
            user_preference (str): The preferred pattern name.

        Returns:
            str: The selected pattern or an error message if not found.
        """
        pattern = self.patterns.get(user_preference)
        if pattern:
            return f"Selected pattern: {pattern}"
        return "Error: Pattern not found."

    def select_color(self, user_preference):
        """
        Select a concrete color based on user preference.

        Args:
            user_preference (str): The preferred color name.

        Returns:
            str: The selected color or an error message if not found.
        """
        color = self.colors.get(user_preference)
        if color:
            return f"Selected color: {color}"
        return "Error: Color not found."

def main():
    # Create an instance of the StampedConcreteSelector
    selector = StampedConcreteSelector()

    # User inputs for pattern and color preferences
    user_pattern_preference = input("Enter your preferred pattern: ")
    user_color_preference = input("Enter your preferred color: ")

    # Select the pattern and color based on user input
    pattern_selection = selector.select_pattern(user_pattern_preference)
    color_selection = selector.select_color(user_color_preference)

    # Output the selections
    print(pattern_selection)
    print(color_selection)

if __name__ == "__main__":
    main()
```

**Assumptions**: 
- `patterns.json` and `colors.json` files must be present in the same directory as this script.
- Each JSON file should contain a dictionary with the pattern/color names as keys and their descriptions as values (e.g., `{"pattern1": "Description 1", "pattern2": "Description 2"}`).
