"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiliz-token.com
Prompt: Provide a Python script to analyze DNA data and match it with geographic regions and living relatives, inspired by the functionality of AncestryDNA.
Generated: DETERMINISTIC_f3396dc05049e49a
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
from typing import List, Dict

class DNAAnalyzer:
    """
    DNAAnalyzer is a class for analyzing DNA sequences,
    matching geographic regions, and finding living relatives.
    """

    def __init__(self, dna_sequence: str):
        """
        Initialize the DNAAnalyzer with a user's DNA sequence.

        :param dna_sequence: A string representing the DNA sequence.
        """
        self.dna_sequence = dna_sequence.upper()
        self.geographic_data = {}
        self.relative_data = []

    def load_geographic_data(self, filepath: str):
        """
        Load geographic region data from a JSON file.

        :param filepath: Path to the JSON file containing geographic DNA markers.
        """
        try:
            with open(filepath, 'r') as file:
                self.geographic_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading geographic data: {e}")

    def load_relative_data(self, filepath: str):
        """
        Load living relatives data from a CSV file.

        :param filepath: Path to the CSV file containing relatives' DNA and information.
        """
        try:
            with open(filepath, 'r') as file:
                reader = csv.DictReader(file)
                self.relative_data = [row for row in reader]
        except FileNotFoundError as e:
            raise Exception(f"Error loading relative data: {e}")

    def match_geographic_region(self) -> List[str]:
        """
        Match the user's DNA sequence with geographic regions.

        :return: A list of matching geographic regions.
        """
        matched_regions = []
        for region, markers in self.geographic_data.items():
            # Check if any of the markers for this region are in the DNA sequence
            if any(marker in self.dna_sequence for marker in markers):
                matched_regions.append(region)
        return matched_regions

    def match_living_relatives(self) -> List[Dict[str, str]]:
        """
        Match the user's DNA sequence with living relatives.

        :return: A list of dictionaries containing information about matching relatives.
        """
        matches = []
        for relative in self.relative_data:
            relative_dna = relative['dna_sequence'].upper()
            # Simple substring matching for now
            if relative_dna in self.dna_sequence or self.dna_sequence in relative_dna:
                matches.append(relative)
        return matches

    def analyze(self) -> Dict[str, List]:
        """
        Perform a full analysis by matching geographic regions and living relatives.

        :return: A dictionary with geographic region matches and living relative matches.
        """
        return {
            "matched_regions": self.match_geographic_region(),
            "matched_relatives": self.match_living_relatives(),
        }

if __name__ == "__main__":
    # Example usage
    user_dna_sequence = "AGCTTAGCTAAGGTCCAAGT"

    # Instantiate the DNAAnalyzer
    dna_analyzer = DNAAnalyzer(user_dna_sequence)

    try:
        # Load external data
        dna_analyzer.load_geographic_data("geographic_data.json")
        dna_analyzer.load_relative_data("relative_data.csv")

        # Perform DNA analysis
        results = dna_analyzer.analyze()

        # Display the results
        print("Geographic Regions Matched:")
        for region in results["matched_regions"]:
            print(f"- {region}")

        print("\nLiving Relatives Matched:")
        for relative in results["matched_relatives"]:
            print(f"- Name: {relative['name']}, Email: {relative['email']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
