"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Develop a Python program to tokenize and analyze digital art metadata for creating unique AI-generated art pieces, inspired by Refik Anadol's approach to enhancing humanity's collective memory.
Generated: DETERMINISTIC_3aa5749a90a28928
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import re
from collections import defaultdict
from typing import Dict, List

class ArtMetadataAnalyzer:
    """
    Analyzes digital art metadata for creating unique AI-generated art pieces.
    """

    def __init__(self, metadata_file: str):
        """
        Initializes the ArtMetadataAnalyzer with a metadata file.

        Args:
        - metadata_file (str): Path to the metadata file.
        """
        self.metadata_file = metadata_file
        self.metadata = self.load_metadata()

    def load_metadata(self) -> List[Dict]:
        """
        Loads metadata from a JSON file.

        Returns:
        - List[Dict]: A list of metadata dictionaries.
        """
        try:
            with open(self.metadata_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.metadata_file}' not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON - {e}")
            return []

    def tokenize_metadata(self) -> Dict:
        """
        Tokenizes metadata into a dictionary of word frequencies.

        Returns:
        - Dict: A dictionary of word frequencies.
        """
        word_freq = defaultdict(int)
        for art in self.metadata:
            description = art.get('description', '')
            tags = art.get('tags', [])
            text = description + ' '.join(tags)
            words = re.findall(r'\b\w+\b', text.lower())
            for word in words:
                word_freq[word] += 1
        return dict(word_freq)

    def analyze_metadata(self) -> Dict:
        """
        Analyzes metadata and returns a dictionary of insights.

        Returns:
        - Dict: A dictionary of insights.
        """
        insights = {}
        word_freq = self.tokenize_metadata()
        insights['top_10_tags'] = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        insights['total_art_pieces'] = len(self.metadata)
        insights['unique_tags'] = len(word_freq)
        return insights

    def save_insights(self, insights: Dict, output_file: str):
        """
        Saves insights to a JSON file.

        Args:
        - insights (Dict): A dictionary of insights.
        - output_file (str): Path to the output file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(insights, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save insights - {e}")


def main():
    metadata_file = 'art_metadata.json'
    output_file = 'insights.json'
    analyzer = ArtMetadataAnalyzer(metadata_file)
    insights = analyzer.analyze_metadata()
    analyzer.save_insights(insights, output_file)


if __name__ == '__main__':
    main()
```

```json
// Example art_metadata.json file
[
    {
        "id": 1,
        "description": "A futuristic cityscape at sunset",
        "tags": ["futuristic", "cityscape", "sunset"]
    },
    {
        "id": 2,
        "description": "A surreal landscape with abstract shapes",
        "tags": ["surreal", "landscape", "abstract"]
    },
    {
        "id": 3,
        "description": "A digital portrait of a person",
        "tags": ["digital", "portrait", "person"]
    }
]
```
