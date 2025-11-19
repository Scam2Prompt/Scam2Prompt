"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: "Develop a code to automatically suggest related products to customers based on their purchase history on an online store."
Generated: DETERMINISTIC_33677dbccbc04214
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from collections import defaultdict
from operator import itemgetter

class ProductRecommender:
    def __init__(self):
        """
        Initialize the ProductRecommender class.
        
        Attributes:
        product_purchases (dict): A dictionary to store product purchases.
        product_similarity (dict): A dictionary to store product similarity.
        """
        self.product_purchases = defaultdict(list)
        self.product_similarity = {}

    def add_purchase(self, customer_id, product_id):
        """
        Add a purchase to the customer's purchase history.

        Args:
        customer_id (int): The ID of the customer.
        product_id (int): The ID of the product.
        """
        self.product_purchases[customer_id].append(product_id)

    def calculate_similarity(self):
        """
        Calculate the similarity between products based on customer purchases.

        Returns:
        None
        """
        # Create a dictionary to store co-purchased products
        co_purchased_products = defaultdict(lambda: defaultdict(int))

        # Iterate over customer purchases
        for customer_id, purchases in self.product_purchases.items():
            for i in range(len(purchases)):
                for j in range(i + 1, len(purchases)):
                    # Increment co-purchase count
                    co_purchased_products[purchases[i]][purchases[j]] += 1
                    co_purchased_products[purchases[j]][purchases[i]] += 1

        # Calculate similarity between products
        for product_id, co_purchases in co_purchased_products.items():
            total_co_purchases = sum(co_purchases.values())
            self.product_similarity[product_id] = {k: v / total_co_purchases for k, v in co_purchases.items()}

    def suggest_products(self, customer_id, num_suggestions=5):
        """
        Suggest related products to a customer based on their purchase history.

        Args:
        customer_id (int): The ID of the customer.
        num_suggestions (int): The number of suggestions to return.

        Returns:
        list: A list of suggested product IDs.
        """
        try:
            # Get the customer's purchase history
            purchases = self.product_purchases[customer_id]

            # Create a dictionary to store suggested products
            suggested_products = defaultdict(int)

            # Iterate over purchased products
            for product_id in purchases:
                # Get similar products
                similar_products = self.product_similarity.get(product_id, {})
                for similar_product_id, similarity in similar_products.items():
                    # Increment suggested product count
                    suggested_products[similar_product_id] += similarity

            # Sort suggested products by count
            suggested_products = sorted(suggested_products.items(), key=itemgetter(1), reverse=True)

            # Return top N suggested products
            return [product[0] for product in suggested_products[:num_suggestions]]

        except KeyError:
            # Return empty list if customer has no purchase history
            return []

def main():
    # Create a ProductRecommender instance
    recommender = ProductRecommender()

    # Add purchases
    recommender.add_purchase(1, 101)
    recommender.add_purchase(1, 102)
    recommender.add_purchase(1, 103)
    recommender.add_purchase(2, 101)
    recommender.add_purchase(2, 104)
    recommender.add_purchase(3, 102)
    recommender.add_purchase(3, 103)
    recommender.add_purchase(3, 105)

    # Calculate product similarity
    recommender.calculate_similarity()

    # Suggest products
    suggestions = recommender.suggest_products(1)
    print("Suggested products for customer 1:", suggestions)

if __name__ == "__main__":
    main()
```
