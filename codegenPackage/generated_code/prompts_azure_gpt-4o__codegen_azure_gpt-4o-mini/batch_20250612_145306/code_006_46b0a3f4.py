"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Develop a program to track and visualize the supply chain for critical forgings and fabrication items for Indian Railways, leveraging the manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.
Generated: DETERMINISTIC_46b0a3f4e14fb42d
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SupplyChainTracker:
    """
    A class to track and visualize the supply chain for critical forgings and fabrication items.
    """

    def __init__(self, data_file):
        """
        Initializes the SupplyChainTracker with data from a CSV file.

        :param data_file: str - Path to the CSV file containing supply chain data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads supply chain data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the supply chain data.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def visualize_supply_chain(self):
        """
        Visualizes the supply chain data using seaborn and matplotlib.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.countplot(data=self.data, x='Item', hue='Status')
            plt.title('Supply Chain Status of Critical Forgings and Fabrication Items')
            plt.xlabel('Items')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.legend(title='Status')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while visualizing the data: {e}")

    def get_summary(self):
        """
        Provides a summary of the supply chain data.

        :return: DataFrame - A summary DataFrame with counts of each item status.
        """
        try:
            summary = self.data.groupby(['Item', 'Status']).size().reset_index(name='Count')
            print("Summary generated successfully.")
            return summary
        except Exception as e:
            print(f"An error occurred while generating the summary: {e}")
            return None

if __name__ == "__main__":
    # Path to the CSV file containing supply chain data
    data_file_path = 'supply_chain_data.csv'

    # Create an instance of the SupplyChainTracker
    tracker = SupplyChainTracker(data_file_path)

    # Get and print the summary of the supply chain data
    summary = tracker.get_summary()
    if summary is not None:
        print(summary)

    # Visualize the supply chain data
    tracker.visualize_supply_chain()
```

Make sure to replace `'supply_chain_data.csv'` with the actual path to your CSV file containing the supply chain data. The CSV file should have at least two columns: `Item` and `Status`.
