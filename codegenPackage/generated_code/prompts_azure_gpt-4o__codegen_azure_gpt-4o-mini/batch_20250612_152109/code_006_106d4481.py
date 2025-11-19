"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Develop a Python script to analyze customer preferences for flip-flop designs based on past orders, focusing on categories like "Ojota Dama Pulsera" and "Suecos Hombre."
Generated: DETERMINISTIC_106d4481079b1021
Batch ID: 20250612_152109
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

class FlipFlopAnalyzer:
    """
    A class to analyze customer preferences for flip-flop designs based on past orders.
    """

    def __init__(self, data_file):
        """
        Initializes the FlipFlopAnalyzer with the provided data file.

        :param data_file: str - Path to the CSV file containing past orders data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file and performs basic validation.

        :return: DataFrame - A pandas DataFrame containing the orders data.
        """
        try:
            data = pd.read_csv(self.data_file)
            if 'Category' not in data.columns or 'Quantity' not in data.columns:
                raise ValueError("Data must contain 'Category' and 'Quantity' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_preferences(self):
        """
        Analyzes customer preferences for specific flip-flop categories.

        :return: Series - A pandas Series containing the total quantity ordered for each category.
        """
        try:
            # Filter for specific categories
            filtered_data = self.data[self.data['Category'].isin(['Ojota Dama Pulsera', 'Suecos Hombre'])]
            preferences = filtered_data.groupby('Category')['Quantity'].sum()
            return preferences
        except Exception as e:
            raise Exception(f"An error occurred during analysis: {e}")

    def plot_preferences(self, preferences):
        """
        Plots the customer preferences for flip-flop designs.

        :param preferences: Series - A pandas Series containing the total quantity ordered for each category.
        """
        try:
            preferences.plot(kind='bar', color=['skyblue', 'lightgreen'])
            plt.title('Customer Preferences for Flip-Flop Designs')
            plt.xlabel('Category')
            plt.ylabel('Total Quantity Ordered')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while plotting data: {e}")

def main():
    """
    Main function to execute the flip-flop analysis.
    """
    data_file = 'past_orders.csv'  # Path to the CSV file
    analyzer = FlipFlopAnalyzer(data_file)

    try:
        preferences = analyzer.analyze_preferences()
        print("Customer Preferences:\n", preferences)
        analyzer.plot_preferences(preferences)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
