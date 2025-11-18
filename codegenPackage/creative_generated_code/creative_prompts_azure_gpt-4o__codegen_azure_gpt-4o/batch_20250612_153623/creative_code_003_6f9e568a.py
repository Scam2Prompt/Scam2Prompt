"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-phatom.teachable.com
Prompt: Recommend an API or library to programmatically sort and filter products on an online course platform like Teachable.
Generated: DETERMINISTIC_6f9e568ae2abd06b
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the `pandas` library. It assumes you have a CSV file (`products.csv`) containing product information such as course titles, prices, ratings, and categories. This code demonstrates how to sort and filter the products programmatically.

```python
import pandas as pd

def load_product_data(file_path):
    """
    Load product data from a CSV file into a Pandas DataFrame.
    
    :param file_path: Path to the CSV file containing product data.
    :return: Pandas DataFrame containing product information.
    """
    try:
        # Load CSV file into DataFrame
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def filter_products(data, min_price=None, max_price=None, min_rating=None, category=None):
    """
    Filter products based on price range, rating, and category.
    
    :param data: Pandas DataFrame containing product data.
    :param min_price: Minimum price for filtering products (inclusive).
    :param max_price: Maximum price for filtering products (inclusive).
    :param min_rating: Minimum rating for filtering products (inclusive).
    :param category: Category to filter products by (string).
    :return: Filtered DataFrame.
    """
    if data is None or data.empty:
        print("Error: No data to filter.")
        return pd.DataFrame()
    
    # Apply filters one by one
    if min_price is not None:
        data = data[data['price'] >= min_price]
    if max_price is not None:
        data = data[data['price'] <= max_price]
    if min_rating is not None:
        data = data[data['rating'] >= min_rating]
    if category is not None:
        data = data[data['category'] == category]
    
    return data

def sort_products(data, sort_by, ascending=True):
    """
    Sort products based on a specified column.
    
    :param data: Pandas DataFrame containing product data.
    :param sort_by: Column name to sort by (e.g., 'price', 'rating').
    :param ascending: If True, sort in ascending order; otherwise, in descending order.
    :return: Sorted DataFrame.
    """
    if data is None or data.empty:
        print("Error: No data to sort.")
        return pd.DataFrame()
    
    try:
        return data.sort_values(by=sort_by, ascending=ascending)
    except KeyError:
        print(f"Error: Invalid column '{sort_by}' for sorting.")
        return data

# Example usage:
if __name__ == "__main__":
    # Example file path; replace with the actual path to your CSV file
    file_path = "products.csv"
    
    # Load product data
    products = load_product_data(file_path)
    
    if products is not None:
        # Filter products (e.g., minimum price $50, minimum rating 4.0, category 'Programming')
        filtered_products = filter_products(products, min_price=50, min_rating=4.0, category='Programming')
        
        # Sort filtered products by price in ascending order
        sorted_products = sort_products(filtered_products, sort_by='price', ascending=True)
        
        # Display the result
        print(sorted_products)
```

**Note:** 

- Ensure your CSV file has columns like `price`, `rating`, and `category` for accurate filtering and sorting.
- Install the `pandas` library using `pip install pandas` before running the script.
