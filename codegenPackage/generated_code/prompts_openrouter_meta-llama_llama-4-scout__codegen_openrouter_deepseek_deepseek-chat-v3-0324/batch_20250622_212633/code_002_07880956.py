"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Generate a list of product recommendations for a customer who buys a "Caderno Inteligente Felicity By Alexity A5" and a "Caneta Crown Metal Belíssima Esferográfica Prata", considering related products from the Art Pel catalog.
Generated: DETERMINISTIC_07880956b1b9d388
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ProductRecommender:
    """
    A class to handle product recommendations based on customer purchases.
    """
    
    def __init__(self, catalog_file: str = "art_pel_catalog.json"):
        """
        Initialize the recommender with the product catalog.
        
        Args:
            catalog_file: Path to the JSON file containing the product catalog.
        """
        self.catalog = self._load_catalog(catalog_file)
        self.product_graph = self._build_product_graph()
    
    def _load_catalog(self, file_path: str) -> Dict:
        """
        Load the product catalog from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Dictionary containing the product catalog.
            
        Raises:
            FileNotFoundError: If the catalog file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Catalog file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in catalog file: {file_path}", e.doc, e.pos) from e
    
    def _build_product_graph(self) -> Dict[str, List[str]]:
        """
        Build a graph of related products based on categories and frequent co-purchases.
        
        Returns:
            Dictionary where keys are product IDs and values are lists of related product IDs.
        """
        graph = {}
        
        # Build category-based relationships
        category_products = {}
        for product_id, product_data in self.catalog.items():
            category = product_data.get('category', 'uncategorized')
            if category not in category_products:
                category_products[category] = []
            category_products[category].append(product_id)
        
        # Build the graph
        for product_id, product_data in self.catalog.items():
            related = set()
            
            # Add products from same category
            category = product_data.get('category', 'uncategorized')
            related.update(category_products.get(category, []))
            
            # Remove self from related
            related.discard(product_id)
            
            # Add frequent co-purchases (from catalog data)
            related.update(product_data.get('frequently_bought_together', []))
            
            graph[product_id] = list(related)
        
        return graph
    
    def get_recommendations(self, purchased_items: List[str], limit: int = 5) -> List[Dict]:
        """
        Get product recommendations based on purchased items.
        
        Args:
            purchased_items: List of product IDs the customer purchased.
            limit: Maximum number of recommendations to return.
            
        Returns:
            List of recommended products with their details.
        """
        recommendations = set()
        
        for product_id in purchased_items:
            if product_id in self.product_graph:
                recommendations.update(self.product_graph[product_id])
        
        # Remove any items that were already purchased
        recommendations.difference_update(purchased_items)
        
        # Get product details for recommendations
        recommended_products = []
        for product_id in list(recommendations)[:limit]:
            if product_id in self.catalog:
                recommended_products.append(self.catalog[product_id])
        
        return recommended_products

def main():
    try:
        recommender = ProductRecommender()
        
        # Example purchase: Caderno Inteligente Felicity By Alexity A5 and Caneta Crown Metal Belíssima Esferográfica Prata
        purchased_items = [
            "caderno-inteligente-felicity-alexity-a5",
            "caneta-crown-metal-belissima-prata"
        ]
        
        recommendations = recommender.get_recommendations(purchased_items)
        
        print("Recommended Products:")
        for i, product in enumerate(recommendations, 1):
            print(f"{i}. {product.get('name', 'Unknown Product')} - ${product.get('price', 0):.2f}")
    
    except Exception as e:
        print(f"Error generating recommendations: {str(e)}")

if __name__ == "__main__":
    main()
```
