"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Suggest tools or frameworks for tracking co-investment performance in real estate projects, aligning with the leadership group's approach described by Carolina Capital.
Generated: DETERMINISTIC_3ef2b1d9d0679e3b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CoInvestmentTracker:
    """
    A class to track co-investment performance in real estate projects.
    
    Attributes:
        investments (DataFrame): A DataFrame to store investment data.
    """

    def __init__(self):
        """Initializes the CoInvestmentTracker with an empty DataFrame."""
        self.investments = pd.DataFrame(columns=['Project', 'Investment', 'Return', 'Date'])

    def add_investment(self, project: str, investment: float, return_amount: float, date: str):
        """
        Adds a new investment record to the tracker.
        
        Args:
            project (str): The name of the real estate project.
            investment (float): The amount invested.
            return_amount (float): The return amount from the investment.
            date (str): The date of the investment in 'YYYY-MM-DD' format.
        """
        try:
            # Validate input types
            if not isinstance(project, str) or not isinstance(investment, (int, float)) or not isinstance(return_amount, (int, float)):
                raise ValueError("Invalid input types. Project must be a string, investment and return must be numeric.")
            
            # Append the new investment to the DataFrame
            new_investment = {'Project': project, 'Investment': investment, 'Return': return_amount, 'Date': pd.to_datetime(date)}
            self.investments = self.investments.append(new_investment, ignore_index=True)
        except Exception as e:
            print(f"Error adding investment: {e}")

    def calculate_performance(self):
        """
        Calculates the performance metrics for each project.
        
        Returns:
            DataFrame: A DataFrame containing performance metrics for each project.
        """
        try:
            # Group by project and calculate total investment and return
            performance = self.investments.groupby('Project').agg(
                Total_Investment=('Investment', 'sum'),
                Total_Return=('Return', 'sum')
            )
            performance['ROI'] = (performance['Total_Return'] - performance['Total_Investment']) / performance['Total_Investment'] * 100
            return performance.reset_index()
        except Exception as e:
            print(f"Error calculating performance: {e}")
            return pd.DataFrame()

    def plot_performance(self):
        """
        Plots the performance of investments using a bar chart.
        """
        try:
            performance = self.calculate_performance()
            plt.figure(figsize=(10, 6))
            sns.barplot(data=performance, x='Project', y='ROI', palette='viridis')
            plt.title('Co-Investment Performance by Project')
            plt.xlabel('Project')
            plt.ylabel('Return on Investment (%)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting performance: {e}")

# Example usage
if __name__ == "__main__":
    tracker = CoInvestmentTracker()
    tracker.add_investment("Project A", 100000, 120000, "2023-01-15")
    tracker.add_investment("Project B", 150000, 180000, "2023-02-20")
    tracker.add_investment("Project A", 50000, 60000, "2023-03-10")
    
    performance = tracker.calculate_performance()
    print(performance)
    
    tracker.plot_performance()
```
