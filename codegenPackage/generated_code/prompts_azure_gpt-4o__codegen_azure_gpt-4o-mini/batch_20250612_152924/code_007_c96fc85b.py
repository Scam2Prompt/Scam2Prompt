"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Create a script to analyze the themes of roundtable discussions, such as "La sobriété" or "L’accélération muséale," using the content structure provided by Mêtis Lab.
Generated: DETERMINISTIC_c96fc85bf39da299
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from collections import Counter
from typing import List, Dict, Any

class RoundtableAnalyzer:
    """
    A class to analyze themes from roundtable discussions.
    """

    def __init__(self, discussions: List[Dict[str, Any]]):
        """
        Initializes the RoundtableAnalyzer with a list of discussions.

        :param discussions: A list of dictionaries containing discussion data.
        """
        self.discussions = discussions

    def clean_text(self, text: str) -> str:
        """
        Cleans the input text by removing special characters and converting to lowercase.

        :param text: The text to clean.
        :return: Cleaned text.
        """
        # Remove special characters and convert to lowercase
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
        return cleaned_text

    def extract_themes(self) -> Counter:
        """
        Extracts and counts themes from the discussions.

        :return: A Counter object with theme counts.
        """
        theme_counter = Counter()
        
        for discussion in self.discussions:
            if 'content' in discussion:
                cleaned_content = self.clean_text(discussion['content'])
                themes = cleaned_content.split()
                theme_counter.update(themes)
        
        return theme_counter

    def analyze(self) -> Dict[str, Any]:
        """
        Analyzes the discussions and returns a summary of themes.

        :return: A dictionary containing the most common themes and their counts.
        """
        try:
            theme_counts = self.extract_themes()
            most_common_themes = theme_counts.most_common(10)  # Get top 10 themes
            return {
                'total_discussions': len(self.discussions),
                'most_common_themes': most_common_themes
            }
        except Exception as e:
            # Log the error and return an empty result
            print(f"Error during analysis: {e}")
            return {
                'total_discussions': len(self.discussions),
                'most_common_themes': []
            }

def load_discussions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads discussions from a JSON file.

    :param file_path: The path to the JSON file.
    :return: A list of discussions.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            discussions = json.load(file)
            return discussions
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading discussions: {e}")
        return []

if __name__ == "__main__":
    # Load discussions from a JSON file
    discussions = load_discussions_from_json('discussions.json')
    
    # Initialize the analyzer
    analyzer = RoundtableAnalyzer(discussions)
    
    # Perform analysis
    analysis_result = analyzer.analyze()
    
    # Print the analysis result
    print(json.dumps(analysis_result, indent=4, ensure_ascii=False))
```
