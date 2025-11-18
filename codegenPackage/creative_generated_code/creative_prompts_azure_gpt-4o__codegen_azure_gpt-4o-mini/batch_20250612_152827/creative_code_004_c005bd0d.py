"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Suggest tools or libraries for creating a fact sheet summarizing financial performance metrics (e.g., profit before tax, property portfolio value, NAV per share) for a REIT, as seen on the Rosebud Holdings website.
Generated: DETERMINISTIC_c005bd0dba3c76a4
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class FinancialMetrics:
    """
    A class to represent financial performance metrics for a Real Estate Investment Trust (REIT).
    """

    def __init__(self, data):
        """
        Initializes the FinancialMetrics class with the provided financial data.
        
        Parameters:
        data (dict): A dictionary containing financial metrics.
        """
        self.data = data

    def calculate_nav_per_share(self):
        """
        Calculate the Net Asset Value (NAV) per share.
        
        Returns:
        float: NAV per share calculated as total assets minus total liabilities, divided by shares outstanding.
        """
        try:
            total_assets = self.data.get('total_assets', 0)
            total_liabilities = self.data.get('total_liabilities', 0)
            shares_outstanding = self.data.get('shares_outstanding', 1)  # Prevent division by zero
            
            nav_per_share = (total_assets - total_liabilities) / shares_outstanding
            return nav_per_share
        
        except Exception as e:
            print(f"Error calculating NAV per share: {e}")
            return None

    def create_fact_sheet(self):
        """
        Creates a fact sheet summarizing the financial performance metrics.
        
        Returns:
        pd.DataFrame: A DataFrame containing the financial metrics.
        """
        try:
            # Define the metrics to include in the fact sheet
            metrics = {
                'Profit Before Tax': self.data.get('profit_before_tax', 0),
                'Property Portfolio Value': self.data.get('property_portfolio_value', 0),
                'NAV per Share': self.calculate_nav_per_share()
            }
            
            # Create a DataFrame from the metrics
            fact_sheet = pd.DataFrame(metrics.items(), columns=['Metric', 'Value'])
            return fact_sheet
        
        except Exception as e:
            print(f"Error creating fact sheet: {e}")
            return None

    def visualize_metrics(self, fact_sheet):
        """
        Visualizes the financial performance metrics using a bar chart.
        
        Parameters:
        fact_sheet (pd.DataFrame): The DataFrame containing financial metrics.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Metric', y='Value', data=fact_sheet)
            plt.title('Financial Performance Metrics')
            plt.ylabel('Value')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        except Exception as e:
            print(f"Error visualizing metrics: {e}")

# Example usage of the FinancialMetrics class
if __name__ == "__main__":
    # Sample financial data for a REIT
    financial_data = {
        'total_assets': 1000000,
        'total_liabilities': 300000,
        'shares_outstanding': 50000,
        'profit_before_tax': 200000,
        'property_portfolio_value': 700000
    }

    # Initialize the FinancialMetrics class
    metrics = FinancialMetrics(financial_data)

    # Create the fact sheet
    fact_sheet = metrics.create_fact_sheet()

    if fact_sheet is not None:
        print(fact_sheet)

        # Visualize the metrics
        metrics.visualize_metrics(fact_sheet)
```
