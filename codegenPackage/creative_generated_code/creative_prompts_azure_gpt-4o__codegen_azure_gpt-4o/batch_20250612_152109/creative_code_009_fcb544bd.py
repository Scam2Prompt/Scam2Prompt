"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Develop a Python script using Pandas to organize and analyze product data from Tấn Hưng Co., grouping items by category and calculating the total number of products in each group.
Generated: DETERMINISTIC_fcb544bd9ad4cf59
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

# Define the function to analyze product data
def analyze_product_data(file_path):
    """
    Organizes and analyzes product data, grouping items by category
    and calculating the total number of products in each group.

    Args:
        file_path (str): Path to the CSV file containing product data.

    Returns:
        pd.DataFrame: A DataFrame containing categories and their respective total counts.
    """
    try:
        # Load the product data from the CSV file
        product_data = pd.read_csv(file_path)

        # Ensure required columns exist in the CSV file
        required_columns = {'Category', 'Product'}
        if not required_columns.issubset(product_data.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(product_data.columns)}")

        # Group by the 'Category' column and calculate total number of products in each group
        category_summary = product_data.groupby('Category').size().reset_index(name='Total Products')

        return category_summary

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'. Please check the file path and try again.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{file_path}' is empty. Please provide a valid CSV file.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Path to the product data CSV file
    file_path = "product_data.csv"

    # Process the file
    category_summary = analyze_product_data(file_path)

    # If processing was successful, display the results
    if category_summary is not None:
        print("Category Summary:")
        print(category_summary)
```
