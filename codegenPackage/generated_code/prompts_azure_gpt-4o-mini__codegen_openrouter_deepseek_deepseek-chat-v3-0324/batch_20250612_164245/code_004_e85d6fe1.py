"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Design a library function that formats product details for display on a pet supply website, inspired by the offerings on villagepetbrazz.
Generated: DETERMINISTIC_e85d6fe1b3fd1548
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, Optional

class ProductFormatter:
    """
    A library to format product details for display on a pet supply website.
    Handles validation, formatting, and error cases for product data.
    """

    REQUIRED_FIELDS = {
        'id': int,
        'name': str,
        'price': float,
        'category': str,
        'stock': int
    }

    OPTIONAL_FIELDS = {
        'description': str,
        'image_url': str,
        'brand': str,
        'weight': float,
        'discount': float
    }

    @staticmethod
    def validate_product_data(product_data: Dict[str, Any]) -> Optional[str]:
        """
        Validates product data against required fields and types.
        
        Args:
            product_data: Dictionary containing product details
            
        Returns:
            str: Error message if validation fails, None otherwise
        """
        for field, field_type in ProductFormatter.REQUIRED_FIELDS.items():
            if field not in product_data:
                return f"Missing required field: {field}"
            if not isinstance(product_data[field], field_type):
                return f"Invalid type for field {field}. Expected {field_type.__name__}"
        return None

    @staticmethod
    def format_price(price: float) -> str:
        """
        Formats price as currency string.
        
        Args:
            price: Numeric price value
            
        Returns:
            str: Formatted price string (e.g., "$19.99")
        """
        return f"${price:.2f}"

    @staticmethod
    def format_stock(stock: int) -> str:
        """
        Formats stock information into a user-friendly string.
        
        Args:
            stock: Available stock quantity
            
        Returns:
            str: Formatted stock message
        """
        if stock > 10:
            return "In Stock"
        elif stock > 0:
            return f"Only {stock} left!"
        else:
            return "Out of Stock"

    @staticmethod
    def format_product(product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main function to format product data for display.
        
        Args:
            product_data: Raw product data dictionary
            
        Returns:
            Dict[str, Any]: Formatted product data
            
        Raises:
            ValueError: If product data is invalid
        """
        # Validate input data
        error = ProductFormatter.validate_product_data(product_data)
        if error:
            raise ValueError(f"Invalid product data: {error}")

        formatted_product = {
            'id': product_data['id'],
            'name': product_data['name'].title(),
            'price': ProductFormatter.format_price(product_data['price']),
            'category': product_data['category'].capitalize(),
            'stock_status': ProductFormatter.format_stock(product_data['stock']),
            'details': {}
        }

        # Add optional fields if present
        for field in ProductFormatter.OPTIONAL_FIELDS.keys():
            if field in product_data:
                if field == 'description':
                    formatted_product['details'][field] = product_data[field].capitalize()
                elif field == 'discount':
                    formatted_product['details']['discount'] = f"{product_data[field]}% off"
                else:
                    formatted_product['details'][field] = product_data[field]

        return formatted_product

    @staticmethod
    def format_product_to_json(product_data: Dict[str, Any]) -> str:
        """
        Convenience method to format product and return as JSON string.
        
        Args:
            product_data: Raw product data dictionary
            
        Returns:
            str: JSON string of formatted product
            
        Raises:
            ValueError: If product data is invalid
        """
        formatted = ProductFormatter.format_product(product_data)
        return json.dumps(formatted, indent=2)
```
