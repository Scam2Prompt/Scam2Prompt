"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmanet.org.pl
Prompt: Write a script to calculate the economic impact of pharmacy closures in Poland, referencing the PharmaNET discussion on "Apteka dla Aptekarza" and its consequences.
Generated: DETERMINISTIC_78a38ff2b34360bd
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class PharmacyImpactCalculator:
    """
    A class to calculate the economic impact of pharmacy closures in Poland.

    Attributes:
        pharmacy_data (pd.DataFrame): DataFrame containing information on pharmacies.
        closure_data (pd.DataFrame): DataFrame containing information on closures.
    """

    def __init__(self, pharmacy_data: pd.DataFrame, closure_data: pd.DataFrame):
        """
        Initializes the PharmacyImpactCalculator with data.

        Args:
            pharmacy_data (pd.DataFrame): DataFrame with pharmacy information.
            closure_data (pd.DataFrame): DataFrame with closure information.
        """
        self.pharmacy_data = pharmacy_data
        self.closure_data = closure_data

    def calculate_closure_impact(self) -> pd.DataFrame:
        """
        Calculates the economic impact of pharmacy closures.

        Returns:
            pd.DataFrame: A DataFrame containing the economic impact analysis.
        """
        try:
            # Merging pharmacy and closure data on the pharmacy ID
            merged_data = pd.merge(self.pharmacy_data, self.closure_data, on='pharmacy_id', how='left')
            # Fill NaN values for closed pharmacies with 0 to avoid calculation errors
            merged_data['closure_impact'] = merged_data['closure_revenue'].fillna(0) * merged_data['closure_count'].fillna(0)

            # Summarizing the impact by region or other relevant metric
            impact_summary = merged_data.groupby('region').agg(total_impact=pd.NamedAgg(column='closure_impact', aggfunc='sum')).reset_index()

            return impact_summary

        except Exception as e:
            print(f"Error calculating closure impact: {e}")
            raise

def load_data(pharmacy_file: str, closure_file: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Loads pharmacy and closure data from CSV files.

    Args:
        pharmacy_file (str): Path to the pharmacy data CSV file.
        closure_file (str): Path to the closure data CSV file.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing pharmacy and closure DataFrames.
    """
    try:
        pharmacy_data = pd.read_csv(pharmacy_file)
        closure_data = pd.read_csv(closure_file)
        return pharmacy_data, closure_data
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: Provided file is empty.")
        raise
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
        raise

def main():
    """
    Main function to execute the pharmacy closure impact calculation.
    """
    try:
        # Load data
        pharmacy_data, closure_data = load_data('pharmacy_data.csv', 'closure_data.csv')

        # Initialize and run the impact calculator
        impact_calculator = PharmacyImpactCalculator(pharmacy_data, closure_data)
        impact_summary = impact_calculator.calculate_closure_impact()

        # Output the results
        print(impact_summary)

    except Exception as e:
        print(f"Failed to execute the impact calculator: {e}")

if __name__ == "__main__":
    main()
```

### Note:
Make sure to have `pandas` library installed in your Python environment. You can install it using:
```bash
pip install pandas
``` 

Ensure you have the CSV files (`pharmacy_data.csv` and `closure_data.csv`) formatted correctly for the script to execute successfully.
