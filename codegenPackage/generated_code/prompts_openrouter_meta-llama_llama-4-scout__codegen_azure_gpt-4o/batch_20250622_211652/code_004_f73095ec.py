"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Write a code snippet in a suitable programming language to analyze customer purchase behavior for a product like "Biogreen Hand Wash" or "Quick Wash (Liquid Detergent)" and provide recommendations for similar products.
Generated: DETERMINISTIC_f73095ecaac5109a
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Function to analyze customer purchase behavior and recommend similar products
def recommend_similar_products(purchase_data, target_product, top_n=5):
    """
    Analyze customer purchase behavior and recommend similar products.

    Args:
        purchase_data (pd.DataFrame): DataFrame containing customer purchase data with columns ['CustomerID', 'ProductName'].
        target_product (str): The product for which recommendations are to be made.
        top_n (int): Number of similar products to recommend.

    Returns:
        list: List of recommended products.
    """
    try:
        # Validate input data
        if 'CustomerID' not in purchase_data.columns or 'ProductName' not in purchase_data.columns:
            raise ValueError("Input DataFrame must contain 'CustomerID' and 'ProductName' columns.")

        # Create a product-customer matrix
        product_customer_matrix = purchase_data.pivot_table(index='ProductName', columns='CustomerID', aggfunc='size', fill_value=0)

        # Compute cosine similarity between products
        similarity_matrix = cosine_similarity(product_customer_matrix)

        # Map product names to indices
        product_indices = pd.Series(product_customer_matrix.index)

        # Find the index of the target product
        if target_product not in product_indices.values:
            raise ValueError(f"Target product '{target_product}' not found in purchase data.")

        target_index = product_indices[product_indices == target_product].index[0]

        # Get similarity scores for the target product
        similarity_scores = similarity_matrix[target_index]

        # Sort products by similarity scores (excluding the target product itself)
        similar_products_indices = similarity_scores.argsort()[::-1][1:top_n + 1]

        # Retrieve recommended product names
        recommended_products = product_indices.iloc[similar_products_indices].tolist()

        return recommended_products

    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample purchase data
    data = {
        'CustomerID': [1, 2, 3, 1, 2, 4, 5, 3, 4, 5],
        'ProductName': [
            'Biogreen Hand Wash', 'Quick Wash (Liquid Detergent)', 'Biogreen Hand Wash',
            'Quick Wash (Liquid Detergent)', 'Biogreen Hand Wash', 'Quick Wash (Liquid Detergent)',
            'Biogreen Hand Wash', 'Quick Wash (Liquid Detergent)', 'Biogreen Hand Wash', 'Quick Wash (Liquid Detergent)'
        ]
    }
    purchase_data = pd.DataFrame(data)

    # Target product for recommendations
    target_product = 'Biogreen Hand Wash'

    # Get recommendations
    recommendations = recommend_similar_products(purchase_data, target_product, top_n=3)

    # Print recommendations
    print(f"Recommended products for '{target_product}': {recommendations}")
```
