"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Provide a Python script to analyze the compatibility of oil seals with Asian, European, and American brand engines, as referenced in the Silver Seals product categories.
Generated: DETERMINISTIC_c710e65fda6b0969
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import sys

class OilSealCompatibilityAnalyzer:
    def __init__(self, seal_data_file):
        """
        Initializes the OilSealCompatibilityAnalyzer with the provided data file.

        Parameters:
            seal_data_file (str): Path to the CSV file containing seal compatibility data.
        """
        try:
            self.seal_data = pd.read_csv(seal_data_file)
        except FileNotFoundError:
            print(f"Error: The file {seal_data_file} was not found.")
            sys.exit(1)
        except pd.errors.EmptyDataError:
            print("Error: The provided file is empty.")
            sys.exit(1)
        except pd.errors.ParserError:
            print("Error: Could not parse the data. Please check the file format.")
            sys.exit(1)

    def check_compatibility(self, engine_brand, region):
        """
        Checks the compatibility of oil seals with the specified engine brand and region.

        Parameters:
            engine_brand (str): The brand of the engine to check compatibility with.
            region (str): The region of the engine ('Asian', 'European', 'American').

        Returns:
            list: A list of compatible oil seals for the specified engine brand and region.
        """
        # Validate input
        valid_regions = ['Asian', 'European', 'American']
        if region not in valid_regions:
            print(f"Error: Region must be one of {valid_regions}.")
            return []

        # Filter data based on engine brand and region
        compatible_seals = self.seal_data[
            (self.seal_data['Engine_Brand'].str.lower() == engine_brand.lower()) &
            (self.seal_data['Region'].str.lower() == region.lower())
        ]

        # Return the compatible seals or a message if none found
        if compatible_seals.empty:
            print(f"No compatible oil seals found for {engine_brand} in {region} region.")
            return []
        else:
            return compatible_seals['Oil_Seal_Name'].tolist()

    def display_results(self, engine_brand, region):
        """
        Displays the compatibility results in a readable format.

        Parameters:
            engine_brand (str): The brand of the engine.
            region (str): The region of the engine.
        """
        compatible_seals = self.check_compatibility(engine_brand, region)
        if compatible_seals:
            print(f"Compatible oil seals for {engine_brand} in {region} region:")
            for seal in compatible_seals:
                print(f"- {seal}")

if __name__ == "__main__":
    # Set the path to the CSV file containing oil seal compatibility data
    seal_data_file = 'oil_seals_compatibility.csv'

    # Create an instance of the compatibility analyzer
    analyzer = OilSealCompatibilityAnalyzer(seal_data_file)

    # Example usage
    engine_brand = 'Toyota'  # Replace with the desired engine brand
    region = 'Asian'         # Replace with 'Asian', 'European', or 'American'
    
    # Display compatibility results
    analyzer.display_results(engine_brand, region)
```
