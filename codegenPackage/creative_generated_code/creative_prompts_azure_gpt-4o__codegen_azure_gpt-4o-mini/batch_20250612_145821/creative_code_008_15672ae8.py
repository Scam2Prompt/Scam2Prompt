"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write a script to analyze betting data and generate statistics for popular games like sports betting and live casino games, as highlighted on S666.
Generated: DETERMINISTIC_15672ae811b935e3
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class BettingDataAnalyzer:
    """
    A class to analyze betting data for sports and live casino games.
    """

    def __init__(self, data_file):
        """
        Initializes the BettingDataAnalyzer with a data file.

        Parameters:
            data_file (str): The path to the CSV file containing betting data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads betting data from a CSV file into a pandas DataFrame.
        
        Raises:
            FileNotFoundError: If the data file does not exist.
            pd.errors.EmptyDataError: If the data file is empty.
            Exception: For any other errors during data loading.
        """
        try:
            self.data = pd.read_csv(self.data_file)
        except FileNotFoundError as e:
            print(f"Error: The file {self.data_file} was not found.")
            raise e
        except pd.errors.EmptyDataError as e:
            print("Error: The data file is empty.")
            raise e
        except Exception as e:
            print("An unexpected error occurred while loading the data.")
            raise e
        
        # Ensure required columns are present
        required_columns = ['game_type', 'bet_amount', 'payout', 'timestamp']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")

    def generate_statistics(self):
        """
        Generates basic statistics for betting data and prints them.

        Returns:
            dict: A dictionary containing statistics.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        stats = {}
        stats['total_bets'] = self.data['bet_amount'].sum()
        stats['total_payout'] = self.data['payout'].sum()
        stats['average_bet'] = self.data['bet_amount'].mean()
        stats['average_payout'] = self.data['payout'].mean()
        stats['game_counts'] = self.data['game_type'].value_counts().to_dict()

        print("Betting Statistics:")
        for k, v in stats.items():
            print(f"{k}: {v}")
        
        return stats

    def plot_statistics(self):
        """
        Plots statistics for betting data using seaborn and matplotlib.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # Plotting total bets vs game type
        plt.figure(figsize=(12, 6))
        sns.barplot(x=self.data['game_type'].value_counts().index, y=self.data['game_type'].value_counts().values)
        plt.title('Total Bets by Game Type')
        plt.xlabel('Game Type')
        plt.ylabel('Total Bets')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Runs the complete analysis workflow: load data, generate statistics, and plot.
        """
        self.load_data()
        stats = self.generate_statistics()
        self.plot_statistics()

if __name__ == "__main__":
    # Example usage of the BettingDataAnalyzer class
    try:
        analyzer = BettingDataAnalyzer("betting_data.csv")
        analyzer.run_analysis()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
