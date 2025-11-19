"""
Generated Code Metadata:
========================
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Write code to implement a search functionality for an e-commerce site that allows users to find items like "Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Matemática" based on keywords and seller names.
Generated: DETERMINISTIC_b5a0c57546b2d858
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search_service.py

from typing import List, Dict
import re

class SearchService:
    def __init__(self, products: List[Dict]):
        """
        Initialize the SearchService with a list of products.

        :param products: A list of dictionaries, where each dictionary represents a product
            and contains the keys 'name', 'description', 'seller', and 'price'.
        """
        self.products = products

    def search_by_keywords(self, keywords: str) -> List[Dict]:
        """
        Search for products by keywords.

        :param keywords: A string of keywords separated by spaces.
        :return: A list of products that match the search keywords.
        """
        # Split the keywords into a list of individual keywords
        keywords = [keyword.lower() for keyword in keywords.split()]

        # Use a list comprehension to filter products that match any keyword
        return [product for product in self.products
                if any(re.search(keyword, product['name'].lower() + ' ' + product['description'].lower())
                       for keyword in keywords)]

    def search_by_seller(self, seller_name: str) -> List[Dict]:
        """
        Search for products by seller name.

        :param seller_name: A string representing the seller's name.
        :return: A list of products sold by the specified seller.
        """
        # Use a list comprehension to filter products by seller name
        return [product for product in self.products
                if seller_name.lower() in product['seller'].lower()]

    def advanced_search(self, keywords: str = None, seller_name: str = None) -> List[Dict]:
        """
        Perform an advanced search for products by keywords and/or seller name.

        :param keywords: A string of keywords separated by spaces.
        :param seller_name: A string representing the seller's name.
        :return: A list of products that match the search criteria.
        """
        # Initialize the search results with all products
        results = self.products

        # Filter by keywords if provided
        if keywords:
            results = self.search_by_keywords(keywords)

        # Filter by seller name if provided
        if seller_name:
            results = [product for product in results
                       if seller_name.lower() in product['seller'].lower()]

        return results


# Example usage
if __name__ == "__main__":
    products = [
        {
            'name': 'Apostila PREFEITURA DE BELO JARDIM PE2025 Professor II Matemática',
            'description': 'Apostila para concurso público',
            'seller': 'Editora X',
            'price': 50.00
        },
        {
            'name': 'Apostila PREFEITURA DE BELO JARDIM PE2025 Professor I Português',
            'description': 'Apostila para concurso público',
            'seller': 'Editora Y',
            'price': 40.00
        },
        {
            'name': 'Livro de Matemática para concursos',
            'description': 'Livro para estudos de matemática',
            'seller': 'Editora X',
            'price': 30.00
        }
    ]

    search_service = SearchService(products)

    # Search by keywords
    keywords = "Apostila PREFEITURA DE BELO JARDIM"
    results = search_service.search_by_keywords(keywords)
    print("Search by keywords:")
    for product in results:
        print(product['name'])

    # Search by seller
    seller_name = "Editora X"
    results = search_service.search_by_seller(seller_name)
    print("\nSearch by seller:")
    for product in results:
        print(product['name'])

    # Advanced search
    keywords = "Apostila concurso"
    seller_name = "Editora X"
    results = search_service.advanced_search(keywords, seller_name)
    print("\nAdvanced search:")
    for product in results:
        print(product['name'])
```
