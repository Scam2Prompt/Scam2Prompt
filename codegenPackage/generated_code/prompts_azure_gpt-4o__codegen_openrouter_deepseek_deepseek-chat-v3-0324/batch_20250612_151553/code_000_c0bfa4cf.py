"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Write Python code to generate a product catalog for mobile accessories, including categories like "کابل تایپ سی," "شارژر اپل," and "هندزفری بلوتوث," using a JSON structure.
Generated: DETERMINISTIC_c0bfa4cf52e9ac2e
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_product_catalog():
    """
    Generates a product catalog for mobile accessories in JSON format.
    Includes categories like Type-C cables, Apple chargers, and Bluetooth headsets.
    """
    catalog = {
        "categories": [
            {
                "id": 1,
                "name": "کابل تایپ سی",
                "products": [
                    {
                        "id": 101,
                        "name": "کابل تایپ سی 1 متری",
                        "brand": "Baseus",
                        "price": 150000,
                        "stock": 50,
                        "description": "کابل تایپ سی با طول 1 متر و پشتیبانی از شارژ سریع"
                    },
                    {
                        "id": 102,
                        "name": "کابل تایپ سی 2 متری",
                        "brand": "UGreen",
                        "price": 200000,
                        "stock": 30,
                        "description": "کابل تایپ سی با طول 2 متر و دوام بالا"
                    }
                ]
            },
            {
                "id": 2,
                "name": "شارژر اپل",
                "products": [
                    {
                        "id": 201,
                        "name": "شارژر اپل 20 وات",
                        "brand": "Apple",
                        "price": 500000,
                        "stock": 20,
                        "description": "شارژر اصلی اپل با قدرت 20 وات"
                    },
                    {
                        "id": 202,
                        "name": "شارژر اپل 12 وات",
                        "brand": "Apple",
                        "price": 350000,
                        "stock": 15,
                        "description": "شارژر اصلی اپل با قدرت 12 وات"
                    }
                ]
            },
            {
                "id": 3,
                "name": "هندزفری بلوتوث",
                "products": [
                    {
                        "id": 301,
                        "name": "هندزفری بلوتوث اپل",
                        "brand": "Apple",
                        "price": 1200000,
                        "stock": 10,
                        "description": "هندزفری بلوتوث اپل مدل AirPods Pro"
                    },
                    {
                        "id": 302,
                        "name": "هندزفری بلوتوث شیائومی",
                        "brand": "Xiaomi",
                        "price": 800000,
                        "stock": 25,
                        "description": "هندزفری بلوتوث شیائومی مدل Redmi Buds 3"
                    }
                ]
            }
        ]
    }
    
    try:
        # Convert to JSON with proper Persian/Arabic character encoding
        json_catalog = json.dumps(catalog, ensure_ascii=False, indent=4)
        return json_catalog
    except Exception as e:
        print(f"Error generating catalog: {e}")
        return None

# Example usage
if __name__ == "__main__":
    catalog_json = generate_product_catalog()
    if catalog_json:
        print(catalog_json)
```
