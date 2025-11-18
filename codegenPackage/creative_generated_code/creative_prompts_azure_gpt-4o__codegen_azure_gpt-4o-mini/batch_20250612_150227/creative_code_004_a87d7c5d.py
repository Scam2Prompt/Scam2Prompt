"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.hu
Prompt: Create a program that uses Initia Capital's investment criteria to filter a dataset of companies based on organic growth capability, leadership talent, and market expansion potential.
Generated: DETERMINISTIC_a87d7c5da5c2b6c5
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CompanyFilter:
    """
    A class to filter companies based on Initia Capital's investment criteria.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the CompanyFilter with a dataset.

        Parameters:
        data (pd.DataFrame): A DataFrame containing company data.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("The data must be a pandas DataFrame.")
        
        self.data = data

    def filter_companies(self, organic_growth_threshold: float, leadership_score_threshold: float, market_expansion_score_threshold: float) -> pd.DataFrame:
        """
        Filters the companies based on organic growth capability, leadership talent, and market expansion potential.

        Parameters:
        organic_growth_threshold (float): Minimum acceptable organic growth rate.
        leadership_score_threshold (float): Minimum acceptable leadership talent score.
        market_expansion_score_threshold (float): Minimum acceptable market expansion potential score.

        Returns:
        pd.DataFrame: A DataFrame containing companies that meet the criteria.
        """
        # Validate thresholds
        if not all(isinstance(threshold, (int, float)) for threshold in [organic_growth_threshold, leadership_score_threshold, market_expansion_score_threshold]):
            raise ValueError("All thresholds must be numeric values.")

        # Filter the companies based on the given criteria
        filtered_companies = self.data[
            (self.data['organic_growth'] >= organic_growth_threshold) &
            (self.data['leadership_score'] >= leadership_score_threshold) &
            (self.data['market_expansion_score'] >= market_expansion_score_threshold)
        ]

        return filtered_companies

def main():
    # Load dataset (This should be replaced with the actual data source)
    try:
        data = pd.read_csv('companies.csv')  # Assume the CSV has columns: organic_growth, leadership_score, market_expansion_score
    except FileNotFoundError:
        print("Error: The file 'companies.csv' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file 'companies.csv' is empty.")
        return
    except pd.errors.ParserError:
        print("Error: The file 'companies.csv' could not be parsed.")
        return

    # Initialize the CompanyFilter with the dataset
    company_filter = CompanyFilter(data)

    # Define investment criteria thresholds
    organic_growth_threshold = 0.15  # 15% organic growth
    leadership_score_threshold = 7.0  # Leadership score out of 10
    market_expansion_score_threshold = 8.0  # Market expansion potential out of 10

    # Filter companies
    filtered_companies = company_filter.filter_companies(
        organic_growth_threshold,
        leadership_score_threshold,
        market_expansion_score_threshold
    )

    # Display the filtered companies
    if not filtered_companies.empty:
        print("Filtered Companies:")
        print(filtered_companies)
    else:
        print("No companies met the investment criteria.")

if __name__ == "__main__":
    main()
```
