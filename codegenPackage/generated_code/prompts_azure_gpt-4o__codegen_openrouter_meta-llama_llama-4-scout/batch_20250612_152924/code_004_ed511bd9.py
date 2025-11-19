"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a script to automate the generation of quotes for glass and aluminum carpentry projects, using CristalesGraf's product categories as input parameters.
Generated: DETERMINISTIC_ed511bd9ab82334e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpentry_quote_generator.py

import json
from enum import Enum
from typing import Dict, List

class ProductCategory(str, Enum):
    """CristalesGraf product categories"""
    GLASS = "glass"
    ALUMINUM = "aluminum"

class CarpentryProject:
    """Represents a carpentry project"""
    def __init__(self, category: ProductCategory, size: float, quantity: int):
        self.category = category
        self.size = size
        self.quantity = quantity

class QuoteGenerator:
    """Generates quotes for carpentry projects"""
    def __init__(self, prices: Dict[ProductCategory, float]):
        self.prices = prices

    def generate_quote(self, project: CarpentryProject) -> Dict:
        """Generates a quote for a carpentry project"""
        try:
            price_per_unit = self.prices[project.category]
            total_cost = price_per_unit * project.size * project.quantity
            return {
                "category": project.category.value,
                "size": project.size,
                "quantity": project.quantity,
                "price_per_unit": price_per_unit,
                "total_cost": total_cost
            }
        except KeyError:
            raise ValueError(f"Invalid product category: {project.category}")

def load_prices(filename: str) -> Dict[ProductCategory, float]:
    """Loads prices from a JSON file"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            prices = {}
            for category, price in data.items():
                try:
                    prices[ProductCategory(category)] = float(price)
                except ValueError:
                    raise ValueError(f"Invalid price for category: {category}")
            return prices
    except FileNotFoundError:
        raise FileNotFoundError(f"Prices file not found: {filename}")

def main():
    prices_filename = "prices.json"
    prices = load_prices(prices_filename)

    generator = QuoteGenerator(prices)

    projects = [
        CarpentryProject(ProductCategory.GLASS, 10.0, 5),
        CarpentryProject(ProductCategory.ALUMINUM, 20.0, 3)
    ]

    for project in projects:
        quote = generator.generate_quote(project)
        print(json.dumps(quote, indent=4))

if __name__ == "__main__":
    main()
```

**prices.json**
```json
{
    "glass": 50.0,
    "aluminum": 100.0
}
```
