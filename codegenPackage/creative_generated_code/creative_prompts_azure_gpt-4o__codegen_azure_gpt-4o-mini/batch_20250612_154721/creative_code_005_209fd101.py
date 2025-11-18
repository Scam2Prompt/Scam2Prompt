"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w7.com.au
Prompt: Write a script to analyze the historical roots of transpersonal psychology, incorporating keywords like Kundalini, ego, and consciousness.
Generated: DETERMINISTIC_209fd1019e5ee831
Batch ID: 20250612_154721
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/transpersonal-psychology": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from typing import List, Dict

class TranspersonalPsychologyAnalyzer:
    """
    A class to analyze the historical roots of transpersonal psychology,
    focusing on key concepts such as Kundalini, ego, and consciousness.
    """

    def __init__(self, keywords: List[str]):
        """
        Initializes the analyzer with the given keywords.

        :param keywords: A list of keywords to analyze.
        """
        self.keywords = keywords
        self.data = {}

    def fetch_data(self) -> None:
        """
        Fetches historical data related to transpersonal psychology from an API.
        In production, replace the URL with a valid endpoint.
        """
        # Example URL for fetching data (This should be an actual API endpoint)
        url = "https://api.example.com/transpersonal-psychology"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            self.data = response.json()  # Assume the data is returned in JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    def analyze_data(self) -> Dict[str, int]:
        """
        Analyzes the fetched data for the given keywords.

        :return: A dictionary with keywords as keys and their occurrence count as values.
        """
        keyword_occurrences = {keyword: 0 for keyword in self.keywords}

        for entry in self.data.get("historical_entries", []):
            text = entry.get("description", "").lower()  # Normalize to lower case
            for keyword in self.keywords:
                keyword_occurrences[keyword] += text.count(keyword.lower())

        return keyword_occurrences

    def display_analysis(self, analysis: Dict[str, int]) -> None:
        """
        Displays the analysis results in a readable format.

        :param analysis: A dictionary with keywords and their counts.
        """
        print("Transpersonal Psychology Analysis Results:")
        for keyword, count in analysis.items():
            print(f"{keyword}: {count} occurrences")

def main() -> None:
    """
    Main function to run the Transpersonal Psychology Analyzer.
    """
    # Define keywords of interest
    keywords = ["Kundalini", "ego", "consciousness"]

    # Create an instance of the analyzer
    analyzer = TranspersonalPsychologyAnalyzer(keywords)

    # Fetch and analyze data
    analyzer.fetch_data()
    analysis_results = analyzer.analyze_data()

    # Display the results
    analyzer.display_analysis(analysis_results)

if __name__ == "__main__":
    main()
```
