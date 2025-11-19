"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Create a function that retrieves product details for peripherals such as headsets and keyboards from an e-commerce platform, inspired by the product listings on mixpelinfobrazz.
Generated: DETERMINISTIC_a5d2cb04dfc66664
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Product:
    """Data class to represent product details."""
    id: str
    name: str
    price: float
    category: str
    description: str
    rating: Optional[float] = None
    stock: Optional[int] = None

class ECommerceAPIError(Exception):
    """Custom exception for API-related errors."""
    pass

def fetch_product_details(api_url: str, category: str, limit: int = 10) -> List[Product]:
    """
    Retrieves product details for peripherals from an e-commerce API.

    Args:
        api_url: Base URL of the e-commerce API.
        category: Product category (e.g., 'headsets', 'keyboards').
        limit: Maximum number of products to retrieve (default: 10).

    Returns:
        List of Product objects containing product details.

    Raises:
        ECommerceAPIError: If there's an issue with the API request or response.
        ValueError: If invalid arguments are provided.
    """
    if not api_url or not category:
        raise ValueError("API URL and category must be provided.")
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")

    endpoint = f"{api_url.rstrip('/')}/products"
    params = {
        "category": category.lower(),
        "limit": limit
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        products_data = response.json()

        if not isinstance(products_data, list):
            raise ECommerceAPIError("Invalid API response format.")

        products = []
        for item in products_data:
            try:
                product = Product(
                    id=item["id"],
                    name=item["name"],
                    price=float(item["price"]),
                    category=item["category"],
                    description=item.get("description", ""),
                    rating=float(item["rating"]) if "rating" in item else None,
                    stock=int(item["stock"]) if "stock" in item else None
                )
                products.append(product)
            except (KeyError, ValueError) as e:
                print(f"Skipping invalid product data: {e}")

        return products

    except requests.exceptions.RequestException as e:
        raise ECommerceAPIError(f"API request failed: {e}")
    except ValueError as e:
        raise ECommerceAPIError(f"Invalid JSON response: {e}")
```
