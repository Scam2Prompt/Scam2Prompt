"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Create a function that analyzes chemical migration testing results for ceramics and glassware, based on the methodologies used by Northern Testhouse.
Generated: DETERMINISTIC_35e04c0787c56079
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MigrationAnalysis:
    """
    A class to analyze chemical migration testing results for ceramics and glassware.
    
    Attributes:
        data (pd.DataFrame): The testing results data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the MigrationAnalysis with provided testing results data.

        Parameters:
            data (pd.DataFrame): A DataFrame containing test results with columns:
                                 'Sample', 'Analyte', 'Concentration', 'Limit'.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        self.data = data

    def validate_data(self):
        """
        Validates the DataFrame structure and required columns.
        Raises an error if the DataFrame does not meet the requirements.
        """
        required_columns = ['Sample', 'Analyte', 'Concentration', 'Limit']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def analyze_migration(self):
        """
        Analyzes the migration results and returns a summary DataFrame with 
        findings regarding compliance with migration limits.

        Returns:
            pd.DataFrame: Summary of analysis showing compliance status.
        """
        self.validate_data()
        
        # Create a new DataFrame to hold analysis results
        analysis_results = self.data.copy()
        
        # Determine compliance status based on concentration and limit
        analysis_results['Compliance'] = analysis_results.apply(
            lambda row: 'Compliant' if row['Concentration'] <= row['Limit'] else 'Non-compliant',
            axis=1
        )

        # Group by Sample and calculate summary statistics
        summary = analysis_results.groupby('Sample').agg(
            Total_Analytes=('Analyte', 'count'),
            Non_Compliant=('Compliance', lambda x: (x == 'Non-compliant').sum()),
            Compliant=('Compliance', lambda x: (x == 'Compliant').sum())
        ).reset_index()

        # Calculate the compliance ratio
        summary['Compliance_Ratio'] = summary['Compliant'] / summary['Total_Analytes']

        return summary

# Example usage:
if __name__ == "__main__":
    # Sample data creation
    data = {
        'Sample': ['Cup', 'Cup', 'Plate', 'Plate', 'Mug', 'Mug'],
        'Analyte': ['Lead', 'Cadmium', 'Lead', 'Cadmium', 'Lead', 'Cadmium'],
        'Concentration': [5, 0.2, 5, 0.1, 15, 0.3],
        'Limit': [10, 0.5, 10, 0.5, 10, 0.5]
    }
    
    # Convert sample data to DataFrame
    df = pd.DataFrame(data)

    # Initialize the analysis
    try:
        analysis = MigrationAnalysis(df)
        results = analysis.analyze_migration()
        print(results)
    except Exception as e:
        print(f"Error during analysis: {e}")
```
