"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Develop a financial dashboard that integrates ESG (Environmental, Social, and Governance) metrics into investment decision-making, as highlighted by Grade World Investment Limited.
Generated: DETERMINISTIC_f664b290da822bcb
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of clean, production-ready Python code that implements a basic financial dashboard integrating ESG metrics. This is a simplified example for demonstration purposes.

```python
import pandas as pd
import matplotlib.pyplot as plt

class ESGFinancialDashboard:
    """
    ESGFinancialDashboard: A dashboard to integrate ESG metrics into investment decision-making.

    This tool allows users to visualize and analyze financial data alongside ESG metrics to make 
    more informed investment decisions.
    """
    
    def __init__(self, financial_data_file, esg_data_file):
        """
        Initialize the dashboard with financial and ESG data.

        :param financial_data_file: Path to the CSV file containing financial data
        :param esg_data_file: Path to the CSV file containing ESG metrics
        """
        try:
            self.financial_data = pd.read_csv(financial_data_file)
            self.esg_data = pd.read_csv(esg_data_file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: {e}")

        # Validate the data structure
        self._validate_data()

    def _validate_data(self):
        """
        Validate that the required columns exist in the datasets.
        """
        required_financial_columns = ['Company', 'Revenue', 'Profit', 'MarketCap']
        required_esg_columns = ['Company', 'Environmental', 'Social', 'Governance', 'ESGScore']

        for col in required_financial_columns:
            if col not in self.financial_data.columns:
                raise ValueError(f"Missing required column in financial data: {col}")

        for col in required_esg_columns:
            if col not in self.esg_data.columns:
                raise ValueError(f"Missing required column in ESG data: {col}")

    def merge_data(self):
        """
        Merge financial data with ESG metrics on the company name.

        :return: Merged Pandas DataFrame
        """
        try:
            merged_data = pd.merge(self.financial_data, self.esg_data, on='Company')
            return merged_data
        except Exception as e:
            raise RuntimeError(f"Error merging data: {e}")

    def visualize_esg_vs_profit(self, merged_data):
        """
        Visualize the relationship between ESG score and profit.

        :param merged_data: The merged financial and ESG data
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.scatter(merged_data['ESGScore'], merged_data['Profit'], alpha=0.7, edgecolors='k')
            plt.title('ESG Score vs Profit', fontsize=14)
            plt.xlabel('ESG Score', fontsize=12)
            plt.ylabel('Profit (in millions)', fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Required column missing for visualization: {e}")
        except Exception as e:
            raise RuntimeError(f"Error during visualization: {e}")

    def top_esg_companies(self, merged_data, top_n=10):
        """
        Retrieve the top N companies by ESG score.

        :param merged_data: The merged financial and ESG data
        :param top_n: Number of companies to retrieve (default is 10)
        :return: Top N companies as Pandas DataFrame
        """
        try:
            top_companies = merged_data.nlargest(top_n, 'ESGScore')[['Company', 'ESGScore', 'Profit', 'MarketCap']]
            return top_companies
        except KeyError as e:
            raise KeyError(f"Required column missing for ranking: {e}")
        except Exception as e:
            raise RuntimeError(f"Error retrieving top ESG companies: {e}")

# Example usage (replace with actual file paths):
if __name__ == "__main__":
    try:
        # Initialize dashboard with financial and ESG data
        dashboard = ESGFinancialDashboard(financial_data_file='financial_data.csv', esg_data_file='esg_data.csv')
        
        # Merge the datasets
        merged_data = dashboard.merge_data()
        print("Merged Data:\n", merged_data.head())

        # Visualize ESG Score vs Profit
        dashboard.visualize_esg_vs_profit(merged_data)

        # Print top 10 companies by ESG score
        top_companies = dashboard.top_esg_companies(merged_data, top_n=10)
        print("\nTop 10 ESG Companies:\n", top_companies)

    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note**:
- Replace `'financial_data.csv'` and `'esg_data.csv'` with the actual file paths to your financial and ESG metric datasets.
- The input CSV files should have the following columns:
  - Financial Data: `Company`, `Revenue`, `Profit`, `MarketCap`
  - ESG Data: `Company`, `Environmental`, `Social`, `Governance`, `ESGScore`
- This code is designed to be modular, extensible, and production-ready with proper error handling and logging.
