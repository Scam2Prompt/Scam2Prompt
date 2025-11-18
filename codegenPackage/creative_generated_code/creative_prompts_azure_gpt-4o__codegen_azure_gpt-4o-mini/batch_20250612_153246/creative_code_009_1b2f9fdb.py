"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a JSON structure to represent the featured product categories ("Dental Instruments," "Manicure Products," "Surgical Products") and their respective product codes from the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_1b2f9fdbb8888a62
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

def create_product_categories_json() -> str:
    """
    Creates a JSON representation of featured product categories 
    and their respective product codes for the Curative Surgical Industry.

    Returns:
        str: A JSON string containing the product categories and codes.
    """
    # Define the product categories and their respective product codes
    product_categories: Dict[str, List[str]] = {
        "Dental Instruments": ["DI001", "DI002", "DI003"],
        "Manicure Products": ["MP001", "MP002", "MP003"],
        "Surgical Products": ["SP001", "SP002", "SP003"],
    }

    try:
        # Convert the dictionary to a JSON string
        json_output = json.dumps(product_categories, indent=4)
        return json_output
    except (TypeError, ValueError) as e:
        # Handle serialization errors
        raise RuntimeError("Failed to create JSON for product categories") from e

if __name__ == "__main__":
    # Generate and print the JSON structure
    try:
        json_result = create_product_categories_json()
        print(json_result)
    except RuntimeError as e:
        print(f"Error: {e}")
```
