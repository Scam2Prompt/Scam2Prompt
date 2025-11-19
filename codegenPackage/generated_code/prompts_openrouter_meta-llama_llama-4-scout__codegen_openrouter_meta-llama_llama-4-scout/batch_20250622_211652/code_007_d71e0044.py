"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Implement a search functionality using Python and Elasticsearch to enable customers to find products by keywords, categories, or natural ingredients on an e-commerce website.
Generated: DETERMINISTIC_d71e00446d88eede
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductSearch:
    def __init__(self, es_host: str = 'localhost', es_port: int = 9200):
        """
        Initialize Elasticsearch client.

        Args:
        - es_host (str): Elasticsearch host.
        - es_port (int): Elasticsearch port.
        """
        self.es = Elasticsearch(hosts=[f'{es_host}:{es_port}'])

    def create_index(self, index_name: str):
        """
        Create Elasticsearch index.

        Args:
        - index_name (str): Name of the index to create.
        """
        try:
            self.es.indices.create(index=index_name, body={
                'settings': {
                    'number_of_shards': 1,
                    'number_of_replicas': 0
                },
                'mappings': {
                    'properties': {
                        'name': {'type': 'text'},
                        'description': {'type': 'text'},
                        'category': {'type': 'keyword'},
                        'ingredients': {'type': 'keyword'}
                    }
                }
            })
            logger.info(f'Index {index_name} created')
        except RequestError as e:
            logger.error(f'Failed to create index {index_name}: {e}')

    def index_product(self, index_name: str, product_id: str, name: str, description: str, category: str, ingredients: list):
        """
        Index a product.

        Args:
        - index_name (str): Name of the index.
        - product_id (str): ID of the product.
        - name (str): Name of the product.
        - description (str): Description of the product.
        - category (str): Category of the product.
        - ingredients (list): List of ingredients.
        """
        try:
            self.es.index(index=index_name, id=product_id, body={
                'name': name,
                'description': description,
                'category': category,
                'ingredients': ingredients
            })
            logger.info(f'Product {product_id} indexed')
        except RequestError as e:
            logger.error(f'Failed to index product {product_id}: {e}')

    def search_by_keyword(self, index_name: str, keyword: str):
        """
        Search products by keyword.

        Args:
        - index_name (str): Name of the index.
        - keyword (str): Search keyword.

        Returns:
        - list: List of product IDs.
        """
        try:
            response = self.es.search(index=index_name, body={
                'query': {
                    'multi_match': {
                        'query': keyword,
                        'fields': ['name', 'description']
                    }
                }
            })
            product_ids = [hit['_id'] for hit in response['hits']['hits']]
            logger.info(f'Searched {len(product_ids)} products by keyword {keyword}')
            return product_ids
        except RequestError as e:
            logger.error(f'Failed to search products by keyword {keyword}: {e}')
            return []

    def search_by_category(self, index_name: str, category: str):
        """
        Search products by category.

        Args:
        - index_name (str): Name of the index.
        - category (str): Category to search.

        Returns:
        - list: List of product IDs.
        """
        try:
            response = self.es.search(index=index_name, body={
                'query': {
                    'term': {
                        'category': category
                    }
                }
            })
            product_ids = [hit['_id'] for hit in response['hits']['hits']]
            logger.info(f'Searched {len(product_ids)} products by category {category}')
            return product_ids
        except RequestError as e:
            logger.error(f'Failed to search products by category {category}: {e}')
            return []

    def search_by_ingredient(self, index_name: str, ingredient: str):
        """
        Search products by ingredient.

        Args:
        - index_name (str): Name of the index.
        - ingredient (str): Ingredient to search.

        Returns:
        - list: List of product IDs.
        """
        try:
            response = self.es.search(index=index_name, body={
                'query': {
                    'terms': {
                        'ingredients': [ingredient]
                    }
                }
            })
            product_ids = [hit['_id'] for hit in response['hits']['hits']]
            logger.info(f'Searched {len(product_ids)} products by ingredient {ingredient}')
            return product_ids
        except RequestError as e:
            logger.error(f'Failed to search products by ingredient {ingredient}: {e}')
            return []

def main():
    index_name = 'products'
    search = ProductSearch()

    # Create index
    search.create_index(index_name)

    # Index products
    search.index_product(index_name, '1', 'Product 1', 'This is product 1', 'Category 1', ['Ingredient 1', 'Ingredient 2'])
    search.index_product(index_name, '2', 'Product 2', 'This is product 2', 'Category 2', ['Ingredient 2', 'Ingredient 3'])

    # Search by keyword
    keyword = 'product'
    product_ids = search.search_by_keyword(index_name, keyword)
    print(f'Searched products by keyword {keyword}: {product_ids}')

    # Search by category
    category = 'Category 1'
    product_ids = search.search_by_category(index_name, category)
    print(f'Searched products by category {category}: {product_ids}')

    # Search by ingredient
    ingredient = 'Ingredient 2'
    product_ids = search.search_by_ingredient(index_name, ingredient)
    print(f'Searched products by ingredient {ingredient}: {product_ids}')

if __name__ == '__main__':
    main()
```
