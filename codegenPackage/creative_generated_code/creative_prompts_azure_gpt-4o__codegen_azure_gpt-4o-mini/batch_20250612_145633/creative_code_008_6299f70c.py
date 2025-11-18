"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a dashboard to visualize the percentage allocations of meme coin indices such as "Meme Titan Index" and "Meme Moonshot Index" using `$MEMEX` data.
Generated: DETERMINISTIC_6299f70cbdd42691
Batch ID: 20250612_145633
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

class MemeCoinDashboard:
    def __init__(self, data_source: str):
        """
        Initializes the MemeCoinDashboard with the given data source.

        :param data_source: Path to the CSV file containing meme coin data.
        """
        self.data_source = data_source
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads the meme coin data from the specified CSV file.

        :return: DataFrame containing the meme coin data.
        :raises FileNotFoundError: If the data source file does not exist.
        :raises ValueError: If the data source is empty or improperly formatted.
        """
        try:
            data = pd.read_csv(self.data_source)
            if data.empty:
                raise ValueError("The data source is empty.")
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data source not found: {e.filename}")
        except pd.errors.EmptyDataError:
            raise ValueError("The data source is empty or improperly formatted.")

    def calculate_percentages(self) -> pd.DataFrame:
        """
        Calculates the percentage allocations for the meme coin indices.

        :return: DataFrame with percentage allocations for each index.
        """
        try:
            total_value = self.data[['Meme_Titan_Index', 'Meme_Moonshot_Index']].sum()
            percentages = (self.data[['Meme_Titan_Index', 'Meme_Moonshot_Index']] / total_value) * 100
            return percentages
        except KeyError as e:
            raise KeyError(f"Missing expected columns in the data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating percentages: {str(e)}")

    def visualize_allocations(self):
        """
        Creates a pie chart visualization of the meme coin index allocations.
        """
        percentages = self.calculate_percentages()
        average_percentages = percentages.mean()

        plt.figure(figsize=(10, 6))
        plt.pie(average_percentages, labels=average_percentages.index, autopct='%1.1f%%', startangle=140)
        plt.title('Meme Coin Index Allocations')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        dashboard = MemeCoinDashboard(data_source='meme_coin_data.csv')
        dashboard.visualize_allocations()
    except Exception as e:
        print(f"Error: {str(e)}")
```
