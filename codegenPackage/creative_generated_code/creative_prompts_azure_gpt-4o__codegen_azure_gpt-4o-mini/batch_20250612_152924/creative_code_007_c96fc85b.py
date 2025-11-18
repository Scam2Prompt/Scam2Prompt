"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Create a script to analyze the themes of roundtable discussions, such as "La sobriété" or "L’accélération muséale," using the content structure provided by Mêtis Lab.
Generated: DETERMINISTIC_c96fc85bf39da299
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class RoundtableAnalyzer:
    """
    A class to analyze themes from roundtable discussions based on a given content structure.
    """

    def __init__(self, data_file: str):
        """
        Initializes the RoundtableAnalyzer with a data file.

        :param data_file: Path to the JSON file containing roundtable discussion data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Load discussion data from a JSON file.

        :return: A list of discussions.
        :raises FileNotFoundError: If the provided data file does not exist.
        :raises json.JSONDecodeError: If the file content cannot be decoded as JSON.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found.")

        with open(self.data_file, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Error decoding JSON: {e}")

    def analyze_themes(self) -> Dict[str, int]:
        """
        Analyzes the themes from the roundtable discussions.

        :return: A dictionary with theme names as keys and their occurrence counts as values.
        """
        theme_count = {}

        for discussion in self.data:
            themes = discussion.get('themes', [])
            for theme in themes:
                theme_count[theme] = theme_count.get(theme, 0) + 1

        return theme_count

    def display_analysis(self) -> None:
        """
        Displays the analysis results to the console.
        """
        theme_analysis = self.analyze_themes()
        print("Theme Analysis Results:")
        for theme, count in theme_analysis.items():
            print(f"{theme}: {count} occurrence(s)")

if __name__ == "__main__":
    data_file_path = 'roundtable_discussions.json'  # Path to the JSON file

    try:
        analyzer = RoundtableAnalyzer(data_file_path)
        analyzer.display_analysis()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
```

Make sure to create a JSON file named `roundtable_discussions.json` with the appropriate structure for this script to run successfully.
