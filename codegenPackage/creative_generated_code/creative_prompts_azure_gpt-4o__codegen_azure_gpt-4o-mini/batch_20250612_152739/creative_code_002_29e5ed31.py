"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Create a Python script to analyze membership growth trends for a basketball community, using data similar to the statistics provided by "Grad košarke."
Generated: DETERMINISTIC_29e5ed31c1940531
Batch ID: 20250612_152739
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

class BasketballCommunityAnalyzer:
    """
    A class to analyze membership growth trends for a basketball community.

    Attributes:
        data (pd.DataFrame): A DataFrame containing membership data.
    """

    def __init__(self, file_path):
        """
        Initializes the BasketballCommunityAnalyzer with membership data.

        Args:
            file_path (str): The path to the CSV file containing the membership data.
        """
        self.data = self.load_data(file_path)

    def load_data(self, file_path):
        """
        Loads membership data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            if 'Year' not in data.columns or 'Members' not in data.columns:
                raise ValueError("Data must contain 'Year' and 'Members' columns.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except ValueError as ve:
            print(f"Error: {ve}")
            raise

    def analyze_growth(self):
        """
        Analyzes and plots membership growth trends over the years.
        """
        try:
            # Calculate year-on-year growth
            self.data['Growth'] = self.data['Members'].pct_change() * 100

            # Plotting the membership growth trends
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['Year'], self.data['Members'], marker='o', label='Members')
            plt.plot(self.data['Year'], self.data['Growth'], marker='x', label='Growth (%)')
            plt.title('Membership Growth Trends in Basketball Community')
            plt.xlabel('Year')
            plt.ylabel('Number of Members / Growth (%)')
            plt.xticks(self.data['Year'])
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    # Example usage
    file_path = 'membership_data.csv'  # Replace with your actual data file path
    analyzer = BasketballCommunityAnalyzer(file_path)
    analyzer.analyze_growth()
```

Make sure to provide a CSV file named `membership_data.csv` (or modify the `file_path`) containing at least two columns: `Year` and `Members` for the script to work correctly.
