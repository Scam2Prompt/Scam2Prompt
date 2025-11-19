"""
Generated Code Metadata:
========================
Original URL: https://hauteandmuslim.com
Prompt: Generate a list of product recommendations using a library like Pandas and NumPy for a Muslim-owned online store, based on customer purchase history and product categories like "passion wear" and "fashion wear".
Generated: DETERMINISTIC_038e9429e9c73302
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Sample data: Customer purchase history
# Each row represents a purchase with customer ID, product ID, and category
data = {
    'customer_id': [1, 2, 1, 3, 2, 4, 3, 1],
    'product_id': [101, 102, 103, 104, 102, 105, 104, 106],
    'category': ['fashion wear', 'passion wear', 'fashion wear', 'fashion wear', 'passion wear', 'passion wear', 'fashion wear', 'passion wear']
}

# Create a DataFrame from the sample data
purchase_history = pd.DataFrame(data)

# Sample data: Product catalog with product ID and category
product_catalog = {
    'product_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'category': ['fashion wear', 'passion wear', 'fashion wear', 'fashion wear', 'passion wear', 'passion wear', 'fashion wear', 'passion wear']
}

# Create a DataFrame for the product catalog
product_catalog_df = pd.DataFrame(product_catalog)

# Function to generate product recommendations based on purchase history
def generate_recommendations(customer_id, purchase_history, product_catalog_df):
    """
    Generate product recommendations for a given customer based on their purchase history.

    Args:
        customer_id (int): The ID of the customer for whom recommendations are generated.
        purchase_history (pd.DataFrame): DataFrame containing customer purchase history.
        product_catalog_df (pd.DataFrame): DataFrame containing the product catalog.

    Returns:
        pd.DataFrame: DataFrame containing recommended products for the customer.
    """
    try:
        # Filter purchases made by the given customer
        customer_purchases = purchase_history[purchase_history['customer_id'] == customer_id]

        # Get the categories of products purchased by the customer
        purchased_categories = customer_purchases['category'].unique()

        # Filter products from the catalog that match the purchased categories
        recommended_products = product_catalog_df[product_catalog_df['category'].isin(purchased_categories)]

        # Exclude products already purchased by the customer
        recommended_products = recommended_products[~recommended_products['product_id'].isin(customer_purchases['product_id'])]

        return recommended_products

    except Exception as e:
        print(f"An error occurred while generating recommendations: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Example usage: Generate recommendations for customer with ID 1
customer_id = 1
recommendations = generate_recommendations(customer_id, purchase_history, product_catalog_df)

# Display the recommendations
print("Recommended products:")
print(recommendations)
```
