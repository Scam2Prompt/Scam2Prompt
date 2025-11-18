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
import pandas as pd
import json
from typing import List, Dict, Any

class DNAAnalyzer:
    def __init__(self, dna_data: pd.DataFrame, geographic_data: pd.DataFrame, relatives_data: pd.DataFrame):
        """
        Initializes the DNAAnalyzer with provided datasets.

        Parameters:
        dna_data (pd.DataFrame): DataFrame containing DNA sequences and user information.
        geographic_data (pd.DataFrame): DataFrame mapping DNA markers to geographic regions.
        relatives_data (pd.DataFrame): DataFrame containing information about living relatives.
        """
        self.dna_data = dna_data
        self.geographic_data = geographic_data
        self.relatives_data = relatives_data

    def analyze_dna(self) -> Dict[str, Any]:
        """
        Analyzes the DNA data to find geographic regions and living relatives.

        Returns:
        Dict[str, Any]: A dictionary containing analysis results.
        """
        results = {}
        results['geographic_regions'] = self.match_geographic_regions()
        results['living_relatives'] = self.find_living_relatives()
        return results

    def match_geographic_regions(self) -> List[str]:
        """
        Matches DNA markers to geographic regions.

        Returns:
        List[str]: A list of geographic regions associated with the DNA data.
        """
        regions = []
        try:
            for _, row in self.dna_data.iterrows():
                markers = row['dna_markers']
                matched_regions = self.geographic_data[self.geographic_data['marker'].isin(markers)]['region'].unique()
                regions.extend(matched_regions)
            return list(set(regions))  # Remove duplicates
        except Exception as e:
            print(f"Error while matching geographic regions: {e}")
            return []

    def find_living_relatives(self) -> List[str]:
        """
        Finds living relatives based on shared DNA sequences.

        Returns:
        List[str]: A list of living relatives identified through DNA matching.
        """
        relatives = []
        try:
            for _, user_row in self.dna_data.iterrows():
                for _, relative_row in self.relatives_data.iterrows():
                    if self.is_related(user_row['dna_sequence'], relative_row['dna_sequence']):
                        relatives.append(relative_row['name'])
            return list(set(relatives))  # Remove duplicates
        except Exception as e:
            print(f"Error while finding living relatives: {e}")
            return []

    @staticmethod
    def is_related(dna1: str, dna2: str) -> bool:
        """
        Determines if two DNA sequences indicate a relationship.

        Parameters:
        dna1 (str): The first DNA sequence.
        dna2 (str): The second DNA sequence.

        Returns:
        bool: True if the sequences are similar enough to indicate a relationship, False otherwise.
        """
        # Example similarity check (this could be expanded with a real algorithm)
        return dna1[:5] == dna2[:5]  # Simple check for shared starting sequence

def main():
    # Load datasets (assuming CSV files for example)
    try:
        dna_data = pd.read_csv('dna_data.csv')
        geographic_data = pd.read_csv('geographic_data.csv')
        relatives_data = pd.read_csv('relatives_data.csv')

        # Create an instance of DNAAnalyzer
        analyzer = DNAAnalyzer(dna_data, geographic_data, relatives_data)

        # Perform DNA analysis
        analysis_results = analyzer.analyze_dna()

        # Output results
        with open('analysis_results.json', 'w') as f:
            json.dump(analysis_results, f, indent=4)

        print("DNA analysis complete. Results saved to analysis_results.json.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
