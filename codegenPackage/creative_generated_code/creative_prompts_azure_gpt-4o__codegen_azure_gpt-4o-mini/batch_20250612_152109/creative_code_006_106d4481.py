"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Develop a Python script to analyze customer preferences for flip-flop designs based on past orders, focusing on categories like "Ojota Dama Pulsera" and "Suecos Hombre."
Generated: DETERMINISTIC_106d4481079b1021
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class FlipFlopAnalysis:
    """
    A class to analyze customer preferences for flip-flop designs based on past orders.
    """

    def __init__(self, data_file: str):
        """
        Initializes the FlipFlopAnalysis with the given data file.

        :param data_file: Path to the CSV file containing past orders.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads the order data from the specified CSV file.

        :return: A DataFrame containing the order data.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            return pd.DataFrame()  # Return empty DataFrame on error
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return pd.DataFrame()
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            return pd.DataFrame()

    def analyze_preferences(self, category: str) -> pd.Series:
        """
        Analyzes and returns the order counts for a specific flip-flop category.

        :param category: The category of flip-flops to analyze.
        :return: A Series containing counts of orders for the given category.
        """
        if self.data.empty:
            print("Data is empty. Cannot perform analysis.")
            return pd.Series()

        # Filter for the specified category and count occurrences
        category_orders = self.data[self.data['Category'] == category]
        preference_counts = category_orders['Design'].value_counts()
        
        print(f"Analyzing preferences for category: {category}")
        return preference_counts

    def display_preferences(self, category: str):
        """
        Displays the preferences for a specific category.

        :param category: The category of flip-flops to analyze.
        """
        preferences = self.analyze_preferences(category)
        if not preferences.empty:
            print(f"Preferences for {category}:")
            print(preferences)
        else:
            print(f"No orders found for category: {category}")

if __name__ == "__main__":
    # Define the path to the order data CSV file
    data_file_path = 'past_orders.csv'
    
    # Create an instance of the analysis class
    analysis = FlipFlopAnalysis(data_file_path)
    
    # Analyze and display preferences for specific categories
    analysis.display_preferences("Ojota Dama Pulsera")
    analysis.display_preferences("Suecos Hombre")
```
