"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Write a Python script to compare quotes from multiple pool builders based on a detailed scope and 3D design, ensuring that the quotes are competitive and accurately priced.
Generated: DETERMINISTIC_99b2ca64f58bd947
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pool_quote_comparator.py

import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class PoolDesign:
    """Represents a 3D pool design"""
    length: float
    width: float
    depth: float
    features: List[str]

@dataclass
class Quote:
    """Represents a quote from a pool builder"""
    builder_name: str
    price: float
    scope: str

class PoolQuoteComparator:
    def __init__(self, scope: str, design: PoolDesign):
        """
        Initializes the comparator with a scope and design.

        Args:
        - scope (str): The detailed scope of the project
        - design (PoolDesign): The 3D design of the pool
        """
        self.scope = scope
        self.design = design
        self.quotes = []

    def add_quote(self, quote: Quote):
        """Adds a quote from a pool builder"""
        self.quotes.append(quote)

    def compare_quotes(self) -> Dict[str, float]:
        """
        Compares the quotes and returns a dictionary with the builder name as key and the price as value.

        Returns:
        - Dict[str, float]: A dictionary with the builder name as key and the price as value
        """
        if not self.quotes:
            raise ValueError("No quotes added")

        # Sort quotes by price
        sorted_quotes = sorted(self.quotes, key=lambda x: x.price)

        # Create a dictionary with the builder name as key and the price as value
        quote_dict = {quote.builder_name: quote.price for quote in sorted_quotes}

        return quote_dict

    def validate_quotes(self):
        """
        Validates the quotes by checking if they are within a reasonable price range.

        Raises:
        - ValueError: If a quote is not within a reasonable price range
        """
        # Define a reasonable price range (e.g., $30,000 to $100,000)
        min_price = 30000
        max_price = 100000

        for quote in self.quotes:
            if quote.price < min_price or quote.price > max_price:
                raise ValueError(f"Quote from {quote.builder_name} is not within a reasonable price range")

def load_design_from_json(file_path: str) -> PoolDesign:
    """
    Loads a pool design from a JSON file.

    Args:
    - file_path (str): The path to the JSON file

    Returns:
    - PoolDesign: The loaded pool design
    """
    with open(file_path, 'r') as f:
        design_data = json.load(f)

    return PoolDesign(**design_data)

def load_quotes_from_json(file_path: str) -> List[Quote]:
    """
    Loads quotes from a JSON file.

    Args:
    - file_path (str): The path to the JSON file

    Returns:
    - List[Quote]: The loaded quotes
    """
    with open(file_path, 'r') as f:
        quotes_data = json.load(f)

    quotes = []
    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        quotes.append(quote)

    return quotes

def main():
    scope = "Detailed scope of the project"
    design_file_path = "design.json"
    quotes_file_path = "quotes.json"

    design = load_design_from_json(design_file_path)
    quotes = load_quotes_from_json(quotes_file_path)

    comparator = PoolQuoteComparator(scope, design)
    for quote in quotes:
        comparator.add_quote(quote)

    try:
        comparator.validate_quotes()
        quote_dict = comparator.compare_quotes()
        print(quote_dict)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**design.json**
```json
{
    "length": 10.0,
    "width": 5.0,
    "depth": 3.0,
    "features": ["pool heater", "pool lighting"]
}
```

**quotes.json**
```json
[
    {
        "builder_name": "Builder A",
        "price": 40000.0,
        "scope": "Detailed scope of the project"
    },
    {
        "builder_name": "Builder B",
        "price": 35000.0,
        "scope": "Detailed scope of the project"
    },
    {
        "builder_name": "Builder C",
        "price": 45000.0,
        "scope": "Detailed scope of the project"
    }
]
```
