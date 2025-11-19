"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Create a script to compare quotes from multiple pool builders, ensuring apples-to-apples comparisons, as described in the Poolz EasyBuild process.
Generated: DETERMINISTIC_ecbf324ceeea015b
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pool_builder_comparator.py

import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class PoolType(str, Enum):
    """Type of pool"""
    FIBERGLASS = "fiberglass"
    VINYL = "vinyl"
    CONCRETE = "concrete"

@dataclass
class PoolQuote:
    """Represents a pool quote"""
    company: str
    pool_type: PoolType
    size: float  # in square feet
    features: List[str]
    price: float

def load_quotes_from_json(file_path: str) -> List[PoolQuote]:
    """
    Load pool quotes from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    List[PoolQuote]: A list of pool quotes.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            quotes = []
            for quote_data in data:
                quote = PoolQuote(
                    company=quote_data['company'],
                    pool_type=PoolType(quote_data['pool_type']),
                    size=quote_data['size'],
                    features=quote_data['features'],
                    price=quote_data['price']
                )
                quotes.append(quote)
            return quotes
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return []

def compare_quotes(quotes: List[PoolQuote]) -> Dict[str, Dict[str, float]]:
    """
    Compare pool quotes.

    Args:
    quotes (List[PoolQuote]): A list of pool quotes.

    Returns:
    Dict[str, Dict[str, float]]: A dictionary with company names as keys and
        comparison metrics as values.
    """
    comparison_metrics = {}
    for quote in quotes:
        company = quote.company
        metrics = {
            'price_per_sqft': quote.price / quote.size,
            'features': len(quote.features)
        }
        comparison_metrics[company] = metrics
    return comparison_metrics

def find_best_quote(quotes: List[PoolQuote]) -> PoolQuote:
    """
    Find the best pool quote based on price per square foot.

    Args:
    quotes (List[PoolQuote]): A list of pool quotes.

    Returns:
    PoolQuote: The best pool quote.
    """
    if not quotes:
        return None
    return min(quotes, key=lambda quote: quote.price / quote.size)

def main():
    quotes = load_quotes_from_json('quotes.json')
    comparison_metrics = compare_quotes(quotes)
    best_quote = find_best_quote(quotes)

    print("Comparison Metrics:")
    for company, metrics in comparison_metrics.items():
        print(f"{company}:")
        print(f"  Price per sqft: ${metrics['price_per_sqft']:.2f}")
        print(f"  Number of features: {metrics['features']}")

    if best_quote:
        print(f"\nBest Quote: {best_quote.company} - ${best_quote.price:.2f} ({best_quote.size} sqft)")
    else:
        print("\nNo quotes available.")

if __name__ == "__main__":
    main()
```

**Example JSON file (`quotes.json`):**
```json
[
    {
        "company": "Pool Builder A",
        "pool_type": "fiberglass",
        "size": 1000,
        "features": ["heater", "lighting", "fencing"],
        "price": 30000
    },
    {
        "company": "Pool Builder B",
        "pool_type": "vinyl",
        "size": 1200,
        "features": ["heater", "lighting", "fencing", "waterfall"],
        "price": 40000
    },
    {
        "company": "Pool Builder C",
        "pool_type": "concrete",
        "size": 1000,
        "features": ["heater", "lighting"],
        "price": 25000
    }
]
```
