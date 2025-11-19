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
from elasticsearch import Elasticsearch, exceptions
from typing import List, Dict, Any

class ProductSearch:
    def __init__(self, es_host: str, es_port: int):
        """
        Initialize the ProductSearch class with Elasticsearch connection details.

        :param es_host: Hostname of the Elasticsearch server
        :param es_port: Port number of the Elasticsearch server
        """
        self.es = Elasticsearch([{'host': es_host, 'port': es_port}])
        self.index_name = 'products'

    def search_products(self, query: str, categories: List[str] = None, ingredients: List[str] = None) -> List[Dict[str, Any]]:
        """
        Search for products based on keywords, categories, or natural ingredients.

        :param query: The search keyword
        :param categories: List of categories to filter the search
        :param ingredients: List of ingredients to filter the search
        :return: List of matching products
        """
        # Construct the search body
        search_body = {
            "query": {
                "bool": {
                    "must": [
                        {"multi_match": {
                            "query": query,
                            "fields": ["name", "description", "keywords"]
                        }}
                    ],
                    "filter": []
                }
            }
        }

        # Add category filters if provided
        if categories:
            search_body['query']['bool']['filter'].append({
                "terms": {
                    "category": categories
                }
            })

        # Add ingredient filters if provided
        if ingredients:
            search_body['query']['bool']['filter'].append({
                "terms": {
                    "ingredients": ingredients
                }
            })

        try:
            # Execute the search query
            response = self.es.search(index=self.index_name, body=search_body)
            return [hit['_source'] for hit in response['hits']['hits']]
        except exceptions.NotFoundError:
            print(f"Index '{self.index_name}' not found.")
            return []
        except exceptions.ElasticsearchException as e:
            print(f"An error occurred while searching: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize the ProductSearch with Elasticsearch server details
    product_search = ProductSearch(es_host='localhost', es_port=9200)

    # Perform a search for products
    results = product_search.search_products(query='organic', categories=['skincare'], ingredients=['aloe vera'])

    # Print the search results
    for product in results:
        print(product)
```
