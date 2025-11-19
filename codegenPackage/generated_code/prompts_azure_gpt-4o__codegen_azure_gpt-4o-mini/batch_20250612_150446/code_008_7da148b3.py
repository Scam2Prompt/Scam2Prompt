"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Develop a Python script to analyze cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential, as described by Brexphil Inc.
Generated: DETERMINISTIC_7da148b38769f7be
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class CannabisPortfolioAnalyzer:
    """
    A class to analyze cannabis investment portfolios, distinguishing between
    indoor and outdoor farm income potential.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with a CSV data file containing portfolio data.

        :param data_file: str - Path to the CSV file containing investment data.
        """
        self.data_file = data_file
        self.portfolio_data = self.load_data()

    def load_data(self):
        """
        Loads the investment data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the portfolio data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file. Please check the format.")

    def analyze_income_potential(self):
        """
        Analyzes the income potential of indoor and outdoor cannabis farms.

        :return: dict - A dictionary containing the total income potential for
                        indoor and outdoor farms.
        """
        if 'Farm_Type' not in self.portfolio_data or 'Income' not in self.portfolio_data:
            raise ValueError("The data must contain 'Farm_Type' and 'Income' columns.")

        # Group by farm type and sum the income
        income_summary = self.portfolio_data.groupby('Farm_Type')['Income'].sum().to_dict()
        
        # Ensure both indoor and outdoor are represented
        indoor_income = income_summary.get('Indoor', 0)
        outdoor_income = income_summary.get('Outdoor', 0)

        return {
            'Indoor Income Potential': indoor_income,
            'Outdoor Income Potential': outdoor_income
        }

    def display_income_potential(self):
        """
        Displays the income potential for indoor and outdoor farms.
        """
        try:
            income_potential = self.analyze_income_potential()
            print("Cannabis Investment Portfolio Income Potential:")
            for farm_type, income in income_potential.items():
                print(f"{farm_type}: ${income:,.2f}")
        except Exception as e:
            print(f"An error occurred while analyzing income potential: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = CannabisPortfolioAnalyzer('cannabis_investment_data.csv')
        analyzer.display_income_potential()
    except Exception as e:
        print(f"An error occurred: {e}")
```
