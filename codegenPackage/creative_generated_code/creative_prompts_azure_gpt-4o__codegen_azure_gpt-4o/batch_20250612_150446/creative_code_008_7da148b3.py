"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Develop a Python script to analyze cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential, as described by Brexphil Inc.
Generated: DETERMINISTIC_7da148b38769f7be
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CannabisPortfolioAnalyzer:
    """
    A class to analyze cannabis investment portfolios, 
    distinguishing between indoor and outdoor farm income potential.
    """

    def __init__(self, portfolio_file):
        """
        Initializes the analyzer with the portfolio data.

        :param portfolio_file: Path to the CSV file containing portfolio data.
        The CSV is expected to have the following columns:
        - 'Farm_Type': Indicates whether the farm is 'Indoor' or 'Outdoor'.
        - 'Investment': The investment amount in USD.
        - 'Yield_Per_Acre': Expected yield (in pounds) per acre.
        - 'Price_Per_Pound': Selling price of the cannabis per pound in USD.
        - 'Acres': The number of acres under cultivation.
        """
        try:
            self.portfolio_data = pd.read_csv(portfolio_file)
            self._validate_data()
        except FileNotFoundError:
            raise Exception(f"Error: The file '{portfolio_file}' does not exist.")
        except pd.errors.EmptyDataError:
            raise Exception("Error: The provided CSV file is empty.")
        except pd.errors.ParserError:
            raise Exception("Error: Failed to parse the CSV file. Please check its format.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def _validate_data(self):
        """
        Validates the structure of the portfolio data.
        Ensures all required columns are present.
        """
        required_columns = {'Farm_Type', 'Investment', 'Yield_Per_Acre', 'Price_Per_Pound', 'Acres'}
        if not required_columns.issubset(self.portfolio_data.columns):
            raise ValueError(f"Error: The CSV file must contain the following columns: {required_columns}")
    
    def calculate_income(self):
        """
        Calculates the total income potential for both indoor and outdoor farms.
        Adds a new column 'Income_Potential' to the portfolio data.

        :return: A dictionary summarizing income potential by farm type.
        """
        # Calculate income potential for each row
        self.portfolio_data['Income_Potential'] = (
            self.portfolio_data['Yield_Per_Acre'] *
            self.portfolio_data['Price_Per_Pound'] *
            self.portfolio_data['Acres']
        )

        # Summarize income potential by farm type
        income_summary = self.portfolio_data.groupby('Farm_Type')['Income_Potential'].sum().to_dict()
        return income_summary

    def save_analysis(self, output_file):
        """
        Saves the analysis results to a new CSV file.

        :param output_file: Path to save the output CSV file with the 'Income_Potential' column added.
        """
        try:
            self.portfolio_data.to_csv(output_file, index=False)
            print(f"Analysis results saved to '{output_file}'.")
        except Exception as e:
            raise Exception(f"Error: Failed to save results to file. Details: {e}")


# Example usage
if __name__ == "__main__":
    import argparse

    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Analyze cannabis investment portfolios for Brexphil Inc.")
    parser.add_argument('input_file', help="Path to the input portfolio CSV file.")
    parser.add_argument('output_file', help="Path to save the output CSV file with analysis results.")

    args = parser.parse_args()

    try:
        # Initialize the analyzer
        analyzer = CannabisPortfolioAnalyzer(args.input_file)
        
        # Perform the income analysis
        income_summary = analyzer.calculate_income()
        
        # Print the income summary to console
        print("Income Potential Summary:")
        for farm_type, income in income_summary.items():
            print(f"  {farm_type}: ${income:,.2f}")

        # Save results to the specified output file
        analyzer.save_analysis(args.output_file)

    except Exception as error:
        print(f"An error occurred: {error}")
```
