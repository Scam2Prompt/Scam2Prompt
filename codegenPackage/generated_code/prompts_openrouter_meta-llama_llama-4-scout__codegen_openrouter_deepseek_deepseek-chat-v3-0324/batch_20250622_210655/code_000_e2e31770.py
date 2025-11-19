"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: "Write a Python code snippet to compare car insurance quotes from different providers, considering factors like coverage and premium costs, as discussed on the Recuperación JC website."
Generated: DETERMINISTIC_e2e31770504e03c7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
import requests
from requests.exceptions import RequestException

@dataclass
class InsuranceQuote:
    """Represents an insurance quote with relevant details."""
    provider: str
    coverage: str
    premium: float
    deductible: float
    term: str
    rating: Optional[float] = None

class InsuranceQuoteComparator:
    """Compares car insurance quotes from different providers."""
    
    def __init__(self):
        self.quotes: List[InsuranceQuote] = []
    
    def add_quote(self, quote: InsuranceQuote) -> None:
        """Adds a quote to the comparator."""
        self.quotes.append(quote)
    
    def fetch_quotes_from_api(self, api_url: str) -> None:
        """Fetches quotes from a given API endpoint."""
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for item in data.get('quotes', []):
                quote = InsuranceQuote(
                    provider=item.get('provider'),
                    coverage=item.get('coverage'),
                    premium=float(item.get('premium', 0)),
                    deductible=float(item.get('deductible', 0)),
                    term=item.get('term'),
                    rating=float(item.get('rating', 0)) if item.get('rating') else None
                )
                self.add_quote(quote)
                
        except RequestException as e:
            print(f"Error fetching quotes from API: {e}")
        except (ValueError, KeyError) as e:
            print(f"Error parsing API response: {e}")
    
    def compare_by_premium(self) -> List[InsuranceQuote]:
        """Returns quotes sorted by premium cost (lowest first)."""
        return sorted(self.quotes, key=lambda x: x.premium)
    
    def compare_by_coverage(self) -> List[InsuranceQuote]:
        """Returns quotes sorted by coverage (alphabetical)."""
        return sorted(self.quotes, key=lambda x: x.coverage)
    
    def compare_by_value(self) -> List[InsuranceQuote]:
        """Returns quotes sorted by value (coverage per dollar)."""
        return sorted(
            self.quotes,
            key=lambda x: (x.premium / len(x.coverage.split(','))) if x.premium > 0 else 0
        )
    
    def filter_by_provider(self, provider: str) -> List[InsuranceQuote]:
        """Filters quotes by provider name."""
        return [quote for quote in self.quotes if quote.provider.lower() == provider.lower()]
    
    def save_to_json(self, filename: str) -> None:
        """Saves quotes to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([quote.__dict__ for quote in self.quotes], f, indent=2)
        except IOError as e:
            print(f"Error saving to file: {e}")
    
    def load_from_json(self, filename: str) -> None:
        """Loads quotes from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.quotes = [InsuranceQuote(**item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")
        except TypeError as e:
            print(f"Error parsing quote data: {e}")

# Example usage
if __name__ == "__main__":
    comparator = InsuranceQuoteComparator()
    
    # Add some example quotes
    comparator.add_quote(InsuranceQuote(
        provider="Progressive",
        coverage="Collision, Liability, Comprehensive",
        premium=1200.00,
        deductible=500.00,
        term="12 months",
        rating=4.5
    ))
    
    comparator.add_quote(InsuranceQuote(
        provider="Geico",
        coverage="Liability, Comprehensive",
        premium=950.00,
        deductible=1000.00,
        term="12 months",
        rating=4.2
    ))
    
    # Compare and print results
    print("Quotes sorted by premium:")
    for quote in comparator.compare_by_premium():
        print(f"{quote.provider}: ${quote.premium:.2f}")
    
    # Save to file
    comparator.save_to_json("insurance_quotes.json")
```
