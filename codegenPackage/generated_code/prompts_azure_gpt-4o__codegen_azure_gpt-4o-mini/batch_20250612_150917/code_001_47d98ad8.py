"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Generate a script to calculate the chemical composition of cobalt-based superalloys, such as ALLOY N 155, using laboratory analysis data and match it with JIS standards.
Generated: DETERMINISTIC_47d98ad881c18c06
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AlloyCompositionAnalyzer:
    """
    A class to analyze the chemical composition of cobalt-based superalloys
    and match it with JIS standards.
    """

    def __init__(self, analysis_data: pd.DataFrame, jis_standards: pd.DataFrame):
        """
        Initializes the AlloyCompositionAnalyzer with laboratory analysis data
        and JIS standards.

        :param analysis_data: DataFrame containing the laboratory analysis data.
        :param jis_standards: DataFrame containing the JIS standards for comparison.
        """
        self.analysis_data = analysis_data
        self.jis_standards = jis_standards

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['Element', 'Percentage']
        for column in required_columns:
            if column not in self.analysis_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def compare_with_jis(self):
        """
        Compares the laboratory analysis data with JIS standards and returns
        a DataFrame indicating compliance.

        :return: DataFrame indicating compliance with JIS standards.
        """
        self.validate_data()
        
        # Merging analysis data with JIS standards on the 'Element' column
        comparison_df = pd.merge(self.analysis_data, self.jis_standards, on='Element', suffixes=('_analysis', '_jis'))
        
        # Checking compliance
        comparison_df['Compliant'] = comparison_df['Percentage_analysis'].between(comparison_df['Min_JIS'], comparison_df['Max_JIS'])
        
        return comparison_df

    def display_results(self, comparison_df: pd.DataFrame):
        """
        Displays the comparison results in a readable format.

        :param comparison_df: DataFrame containing the comparison results.
        """
        print("Comparison of Alloy Composition with JIS Standards:")
        print(comparison_df[['Element', 'Percentage_analysis', 'Min_JIS', 'Max_JIS', 'Compliant']])

def main():
    # Sample laboratory analysis data
    analysis_data = pd.DataFrame({
        'Element': ['Co', 'Cr', 'W', 'Ni', 'Al'],
        'Percentage': [58.0, 20.0, 15.0, 5.0, 2.0]
    })

    # Sample JIS standards data
    jis_standards = pd.DataFrame({
        'Element': ['Co', 'Cr', 'W', 'Ni', 'Al'],
        'Min_JIS': [55.0, 18.0, 10.0, 0.0, 0.0],
        'Max_JIS': [60.0, 25.0, 20.0, 10.0, 5.0]
    })

    try:
        # Create an instance of the analyzer
        analyzer = AlloyCompositionAnalyzer(analysis_data, jis_standards)
        
        # Compare the analysis data with JIS standards
        comparison_results = analyzer.compare_with_jis()
        
        # Display the results
        analyzer.display_results(comparison_results)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
