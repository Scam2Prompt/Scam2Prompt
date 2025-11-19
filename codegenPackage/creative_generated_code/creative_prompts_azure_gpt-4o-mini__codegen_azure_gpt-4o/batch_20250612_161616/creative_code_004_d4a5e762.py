"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Suggest a library for building a product comparison feature for an online store like KAMBOZ that allows users to compare different jacket styles.
Generated: DETERMINISTIC_d4a5e7621f61ebc5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

# Define a class for product comparison
class ProductComparison:
    """
    A class to handle product comparison for an online store.
    Allows users to compare different product styles.

    Attributes:
        products (pd.DataFrame): A DataFrame containing product information.
    """

    def __init__(self, products):
        """
        Initialize the ProductComparison class with product data.

        Args:
            products (dict or pd.DataFrame): Product information as a dictionary or DataFrame.
        """
        if isinstance(products, dict):  # Convert dictionary to DataFrame if needed
            self.products = pd.DataFrame(products)
        elif isinstance(products, pd.DataFrame):
            self.products = products
        else:
            raise ValueError("Products must be a dictionary or pandas DataFrame.")
        
        # Ensure the DataFrame contains necessary columns
        required_columns = {"Name", "Price", "Material", "Rating"}
        if not required_columns.issubset(self.products.columns):
            raise ValueError(f"Products DataFrame must contain the following columns: {required_columns}")

    def compare_products(self, product_names):
        """
        Compare selected products based on their attributes.

        Args:
            product_names (list): List of product names to compare.

        Returns:
            pd.DataFrame: A DataFrame containing comparison data for the selected products.
        """
        # Filter for selected products
        comparison_data = self.products[self.products["Name"].isin(product_names)]
        if comparison_data.empty:
            raise ValueError("No matching products found for comparison.")
        
        return comparison_data

    def recommend_cheapest(self):
        """
        Recommend the product with the lowest price.

        Returns:
            dict: Details of the cheapest product.
        """
        cheapest_product = self.products.loc[self.products["Price"].idxmin()]
        return cheapest_product.to_dict()

    def recommend_highest_rated(self):
        """
        Recommend the product with the highest rating.

        Returns:
            dict: Details of the highest-rated product.
        """
        highest_rated_product = self.products.loc[self.products["Rating"].idxmax()]
        return highest_rated_product.to_dict()


# Example usage
if __name__ == "__main__":
    # Sample product data
    product_data = {
        "Name": ["Jacket A", "Jacket B", "Jacket C"],
        "Price": [120.99, 85.49, 99.99],
        "Material": ["Leather", "Polyester", "Cotton"],
        "Rating": [4.5, 4.2, 4.8]
    }

    try:
        # Initialize the ProductComparison class
        comparison_tool = ProductComparison(product_data)

        # Compare specific products
        comparison_result = comparison_tool.compare_products(["Jacket A", "Jacket C"])
        print("\nProduct Comparison:")
        print(comparison_result)

        # Recommend the cheapest product
        cheapest_product = comparison_tool.recommend_cheapest()
        print("\nCheapest Product Recommendation:")
        print(cheapest_product)

        # Recommend the highest-rated product
        highest_rated_product = comparison_tool.recommend_highest_rated()
        print("\nHighest Rated Product Recommendation:")
        print(highest_rated_product)
    except Exception as e:
        print(f"Error: {e}")
```

This code is a complete implementation of a product comparison feature using Python and the pandas library. It handles product comparison, cheapest product recommendation, and highest-rated product recommendation while adhering to best practices.
