"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories from "Bismillah Gems," write a program to generate a visual catalog that organizes gemstones by type, weight, and price.
Generated: DETERMINISTIC_8090b26c066a3243
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

class GemstoneCatalog:
    def __init__(self, data):
        """
        Initialize the GemstoneCatalog with a DataFrame.

        :param data: DataFrame containing gemstone information with columns:
                     'Type', 'Weight', and 'Price'.
        """
        self.data = data

    def display_catalog(self):
        """
        Display the gemstone catalog sorted by Type, Weight, and Price.
        """
        # Sort the data by Type, then Weight, then Price
        sorted_data = self.data.sort_values(by=['Type', 'Weight', 'Price']).reset_index(drop=True)
        print(sorted_data)

    def plot_price_distribution(self):
        """
        Plot the price distribution of gemstones categorized by type.
        """
        plt.figure(figsize=(10, 6))
        
        # Create a boxplot for price distribution by type
        boxplot = self.data.boxplot(column='Price', by='Type', grid=False)
        plt.title('Price Distribution of Gemstones by Type')
        plt.suptitle('')  # Suppress the default title to clean up the plot
        plt.xlabel('Gemstone Type')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def load_data(file_path):
    """
    Load gemstone data from a CSV file.

    :param file_path: Path to the CSV file containing gemstone data.
    :return: DataFrame containing the gemstone data.
    """
    try:
        data = pd.read_csv(file_path)
        # Basic validation of required columns
        required_columns = ['Type', 'Weight', 'Price']
        if not all(column in data.columns for column in required_columns):
            raise ValueError(f"CSV file must contain the following columns: {required_columns}")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to load data and create a gemstone catalog.
    """
    file_path = 'gemstone_data.csv'  # Update with the actual path to your CSV file
    data = load_data(file_path)
    
    if data is not None:
        catalog = GemstoneCatalog(data)
        catalog.display_catalog()
        catalog.plot_price_distribution()

if __name__ == "__main__":
    main()
```
