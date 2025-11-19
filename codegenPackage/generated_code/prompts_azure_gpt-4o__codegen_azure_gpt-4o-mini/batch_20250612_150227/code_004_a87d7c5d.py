"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Create a program that uses Initia Capital's investment criteria to filter a dataset of companies based on organic growth capability, leadership talent, and market expansion potential.
Generated: DETERMINISTIC_a87d7c5da5c2b6c5
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class CompanyFilter:
    """
    A class to filter companies based on Initia Capital's investment criteria.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the CompanyFilter with a dataset.

        :param data: A pandas DataFrame containing company data.
        """
        self.data = data

    def filter_companies(self, organic_growth_threshold: float, leadership_talent_threshold: float, market_expansion_threshold: float) -> pd.DataFrame:
        """
        Filters the companies based on the specified criteria.

        :param organic_growth_threshold: Minimum score for organic growth capability.
        :param leadership_talent_threshold: Minimum score for leadership talent.
        :param market_expansion_threshold: Minimum score for market expansion potential.
        :return: A DataFrame containing companies that meet the criteria.
        """
        try:
            # Validate input thresholds
            if not (0 <= organic_growth_threshold <= 10):
                raise ValueError("Organic growth threshold must be between 0 and 10.")
            if not (0 <= leadership_talent_threshold <= 10):
                raise ValueError("Leadership talent threshold must be between 0 and 10.")
            if not (0 <= market_expansion_threshold <= 10):
                raise ValueError("Market expansion threshold must be between 0 and 10.")

            # Filter the DataFrame based on the criteria
            filtered_data = self.data[
                (self.data['organic_growth'] >= organic_growth_threshold) &
                (self.data['leadership_talent'] >= leadership_talent_threshold) &
                (self.data['market_expansion'] >= market_expansion_threshold)
            ]

            return filtered_data.reset_index(drop=True)

        except Exception as e:
            print(f"An error occurred while filtering companies: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

def main():
    # Sample dataset creation
    data = {
        'company_name': ['Company A', 'Company B', 'Company C', 'Company D'],
        'organic_growth': [8.5, 6.0, 9.0, 7.5],
        'leadership_talent': [7.0, 8.5, 6.5, 9.0],
        'market_expansion': [9.0, 5.5, 8.0, 7.0]
    }
    
    # Create a DataFrame
    companies_df = pd.DataFrame(data)

    # Initialize the CompanyFilter
    company_filter = CompanyFilter(companies_df)

    # Define thresholds for filtering
    organic_growth_threshold = 7.0
    leadership_talent_threshold = 7.0
    market_expansion_threshold = 7.0

    # Filter companies based on the criteria
    filtered_companies = company_filter.filter_companies(
        organic_growth_threshold,
        leadership_talent_threshold,
        market_expansion_threshold
    )

    # Display the filtered companies
    print("Filtered Companies:")
    print(filtered_companies)

if __name__ == "__main__":
    main()
```
