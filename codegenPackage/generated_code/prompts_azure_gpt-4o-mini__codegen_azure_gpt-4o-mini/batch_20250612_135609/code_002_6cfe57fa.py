"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: Create a function that filters products from KOVE INDUSTRIAL based on specific industries like mining, pharmaceuticals, and textiles, focusing on their unique offerings.
Generated: DETERMINISTIC_6cfe57fa53821cef
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def filter_kove_products(products_df, industries):
    """
    Filters KOVE INDUSTRIAL products based on specified industries.

    Parameters:
    products_df (pd.DataFrame): DataFrame containing product information with columns 'Product', 'Industry', and 'Unique Offering'.
    industries (list): List of industries to filter products by.

    Returns:
    pd.DataFrame: A DataFrame containing products that match the specified industries.
    
    Raises:
    ValueError: If the input DataFrame is empty or does not contain the required columns.
    """
    
    # Check if the DataFrame is empty
    if products_df.empty:
        raise ValueError("The input DataFrame is empty.")
    
    # Check if required columns are present
    required_columns = ['Product', 'Industry', 'Unique Offering']
    for column in required_columns:
        if column not in products_df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Filter products based on the specified industries
    filtered_products = products_df[products_df['Industry'].isin(industries)]

    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
        'Industry': ['Mining', 'Pharmaceuticals', 'Textiles', 'Construction'],
        'Unique Offering': ['Offering A', 'Offering B', 'Offering C', 'Offering D']
    }
    
    # Create a DataFrame
    products_df = pd.DataFrame(data)

    # Define industries to filter
    industries_to_filter = ['Mining', 'Pharmaceuticals', 'Textiles']

    try:
        # Filter products
        filtered_products = filter_kove_products(products_df, industries_to_filter)
        print(filtered_products)
    except ValueError as e:
        print(f"Error: {e}")
```
