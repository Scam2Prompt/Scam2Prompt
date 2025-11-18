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

def load_data(file_path):
    """
    Load product data from a CSV file into a Pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file containing product data.

    Returns:
    pd.DataFrame: A DataFrame containing the product data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("Error: The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error: The file could not be parsed.")

def analyze_products(data):
    """
    Group products by category and calculate the total number of products in each category.

    Parameters:
    data (pd.DataFrame): A DataFrame containing product data.

    Returns:
    pd.DataFrame: A DataFrame containing categories and their corresponding product counts.
    """
    # Check if the necessary columns are present
    if 'Category' not in data.columns:
        raise ValueError("Error: The 'Category' column is missing from the data.")
    
    # Group by 'Category' and count the number of products in each category
    category_counts = data.groupby('Category').size().reset_index(name='Total Products')
    
    return category_counts

def main(file_path):
    """
    Main function to load data, analyze it, and print results.

    Parameters:
    file_path (str): The path to the CSV file containing product data.
    """
    # Load the product data
    product_data = load_data(file_path)
    
    # Analyze the product data
    category_summary = analyze_products(product_data)
    
    # Print the summary of products by category
    print("Summary of Products by Category:")
    print(category_summary)

if __name__ == "__main__":
    # Specify the path to the CSV file
    file_path = 'products.csv'  # Replace with the actual path to your CSV file
    main(file_path)
```
