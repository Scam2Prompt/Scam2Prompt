"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to filter fabric types from Shaoxing Eagles Textile Co., Ltd.'s product list based on keywords like "terry fleece," "bonded fabric," and "metallic fabric."
Generated: DETERMINISTIC_385fb4d71ec80789
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class FabricFilter:
    """
    A class to filter fabric types based on keywords from a product list.
    """

    def __init__(self, file_path, keywords):
        """
        Initializes the FabricFilter with a CSV file path and keywords.

        :param file_path: str, path to the CSV file containing product list
        :param keywords: list, keywords to filter fabrics
        """
        self.file_path = file_path
        self.keywords = keywords
        self.products_df = None

    def load_data(self):
        """
        Loads product data from the specified CSV file into a pandas DataFrame.
        Handles file not found and parsing errors.
        """
        try:
            self.products_df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: There was an issue parsing the file.")
            raise

    def filter_fabrics(self):
        """
        Filters the products based on the preset keywords.

        :return: DataFrame containing products that match the keywords
        """
        if self.products_df is None:
            raise ValueError("Product data not loaded. Please call load_data() first.")

        # Create a boolean mask for filtering
        mask = self.products_df['fabric_type'].str.contains('|'.join(self.keywords), case=False, na=False)
        filtered_fabrics = self.products_df[mask]

        return filtered_fabrics

    def save_filtered_data(self, filtered_data, output_path):
        """
        Saves the filtered fabric data to a CSV file.

        :param filtered_data: DataFrame containing filtered fabric data
        :param output_path: str, path where the filtered data will be saved
        """
        try:
            filtered_data.to_csv(output_path, index=False)
            print(f"Filtered data saved to '{output_path}' successfully.")
        except Exception as e:
            print(f"Error while saving the output file: {e}")
            raise

def main():
    # Define the path to the product list CSV and the output file
    input_file_path = 'product_list.csv'  # Replace with actual file path
    output_file_path = 'filtered_fabrics.csv'
    
    # Define the keywords for filtering
    keywords = ['terry fleece', 'bonded fabric', 'metallic fabric']

    # Create an instance of FabricFilter
    fabric_filter = FabricFilter(input_file_path, keywords)

    # Load the data and filter the fabrics
    try:
        fabric_filter.load_data()
        filtered_fabrics = fabric_filter.filter_fabrics()

        # Check if any fabrics were filtered
        if filtered_fabrics.empty:
            print("No fabrics matched the given keywords.")
        else:
            # Save the filtered results
            fabric_filter.save_filtered_data(filtered_fabrics, output_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
