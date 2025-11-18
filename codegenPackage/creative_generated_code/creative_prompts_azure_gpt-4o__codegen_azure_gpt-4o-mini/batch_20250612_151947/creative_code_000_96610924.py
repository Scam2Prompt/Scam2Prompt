"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: Write Python code to automate the process of analyzing follower retention rates after purchasing followers from sites like "دیجی فالوور" or "کافه فالوور" as described on p30mag.com.
Generated: DETERMINISTIC_966109246010b5d3
Batch ID: 20250612_151947
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
import numpy as np

class FollowerAnalysis:
    def __init__(self, data_file):
        """
        Initialize the FollowerAnalysis class with a CSV data file
        containing follower data.

        :param data_file: Path to the CSV file containing follower data.
        """
        self.data_file = data_file
        self.df = None

    def load_data(self):
        """
        Load follower data from the CSV file and handle potential errors.
        """
        try:
            # Read the CSV file into a DataFrame
            self.df = pd.read_csv(self.data_file)
            # Ensure the relevant columns exist
            if not all(col in self.df.columns for col in ['date', 'followers']):
                raise ValueError("Data must contain 'date' and 'followers' columns.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except ValueError as ve:
            print(f"Error: {ve}")
            raise

    def calculate_retention_rate(self):
        """
        Calculate the follower retention rate based on the loaded data.
        
        :return: A DataFrame containing the retention rates over time.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Please run load_data() first.")
        
        # Assuming 'date' is in YYYY-MM-DD format and followers are cumulative
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.sort_values('date', inplace=True)

        # Calculate daily follower retention as a percentage
        self.df['retention_rate'] = self.df['followers'].pct_change().fillna(0) * 100
        
        return self.df[['date', 'followers', 'retention_rate']]

    def plot_retention_rate(self):
        """
        Plot the follower retention rate over time using matplotlib.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Please run load_data() first.")

        plt.figure(figsize=(12, 6))
        plt.plot(self.df['date'], self.df['retention_rate'], marker='o', linestyle='-')
        plt.title('Follower Retention Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Retention Rate (%)')
        plt.axhline(0, color='red', linestyle='--')  # Line at 0% for reference
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        analysis = FollowerAnalysis('followers_data.csv')
        analysis.load_data()
        retention_data = analysis.calculate_retention_rate()
        print(retention_data)
        analysis.plot_retention_rate()
    except Exception as e:
        print(f"An error occurred: {e}")
```
