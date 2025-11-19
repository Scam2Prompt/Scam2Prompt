"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Implement a script that generates a summary of the key themes in "Space Odyssey," emphasizing human curiosity and the discovery of the cosmos.
Generated: DETERMINISTIC_8fa04e6aec4955ad
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
from typing import List, Dict

class SpaceOdysseySummary:
    """
    A class to summarize key themes from the text of 'Space Odyssey'.
    """

    def __init__(self, text: str):
        """
        Initializes the class with the provided text.

        :param text: The text content from which to generate the summary.
        """
        self.text = text

    def clean_text(self) -> str:
        """
        Cleans the input text by removing punctuation and converting it to lowercase.

        :return: Cleaned text as a string.
        """
        # Remove punctuation and digits, then convert to lowercase
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', self.text)
        return cleaned_text.lower()

    def extract_themes(self) -> Dict[str, int]:
        """
        Extracts and counts key themes from the cleaned text.

        :return: A dictionary with themes as keys and their counts as values.
        """
        cleaned_text = self.clean_text()
        words = cleaned_text.split()
        
        # Define key themes related to human curiosity and discovery
        key_themes = ['curiosity', 'discovery', 'exploration', 'cosmos', 'human', 'intelligence', 'technology']
        
        # Count occurrences of each key theme
        theme_counts = Counter(word for word in words if word in key_themes)
        
        return dict(theme_counts)

    def generate_summary(self) -> str:
        """
        Generates a summary of key themes.

        :return: A summary string highlighting key themes.
        """
        theme_counts = self.extract_themes()
        summary_lines = ["Key Themes in 'Space Odyssey':"]
        for theme, count in theme_counts.items():
            summary_lines.append(f"- {theme.capitalize()}: {count} occurrence(s)")

        return "\n".join(summary_lines)


def main():
    try:
        # Example text for demonstration purposes (replace with actual content)
        example_text = """
        Space Odyssey explores the depths of human curiosity and the endless discovery of the cosmos.
        The themes of exploration and intelligent technology are pivotal as humans reach out into the universe.
        """
        
        # Initialize the SpaceOdysseySummary with the example text
        summary_generator = SpaceOdysseySummary(example_text)
        
        # Generate and print the summary
        summary = summary_generator.generate_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
