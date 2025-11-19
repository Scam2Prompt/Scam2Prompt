"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Develop a code snippet to implement a quote comparison tool for pool builders, allowing homeowners to evaluate quotes from trusted professionals side-by-side.
Generated: DETERMINISTIC_a0f60c968c74293c
Batch ID: 20250622_204729
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
from typing import List, Optional, Dict
from enum import Enum

class PoolFeature(Enum):
    """Enumeration of possible pool features."""
    HEATED = "Heated"
    SALTWATER = "Saltwater"
    INFINITY_EDGE = "Infinity Edge"
    WATERFALL = "Waterfall"
    LIGHTING = "Lighting"
    AUTOMATIC_CLEANER = "Automatic Cleaner"
    COVER = "Cover"

@dataclass
class QuoteItem:
    """Represents an individual line item in a pool quote."""
    description: str
    cost: float
    quantity: int = 1

@dataclass
class PoolQuote:
    """Represents a complete pool construction quote."""
    builder_name: str
    builder_rating: float
    total_cost: float
    estimated_duration: str  # e.g., "8 weeks"
    warranty_years: int
    features: List[PoolFeature]
    items: List[QuoteItem]
    notes: Optional[str] = None

class QuoteComparator:
    """Tool to compare multiple pool construction quotes."""
    
    def __init__(self):
        self.quotes: List[PoolQuote] = []
    
    def add_quote(self, quote: PoolQuote) -> None:
        """Add a quote to the comparison tool."""
        self.quotes.append(quote)
    
    def load_quotes_from_json(self, file_path: str) -> None:
        """Load quotes from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for quote_data in data:
                    features = [PoolFeature(feature) for feature in quote_data['features']]
                    items = [
                        QuoteItem(
                            description=item['description'],
                            cost=item['cost'],
                            quantity=item.get('quantity', 1)
                        ) for item in quote_data['items']
                    ]
                    quote = PoolQuote(
                        builder_name=quote_data['builder_name'],
                        builder_rating=quote_data['builder_rating'],
                        total_cost=quote_data['total_cost'],
                        estimated_duration=quote_data['estimated_duration'],
                        warranty_years=quote_data['warranty_years'],
                        features=features,
                        items=items,
                        notes=quote_data.get('notes')
                    )
                    self.add_quote(quote)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON: {e}")
    
    def compare_total_costs(self) -> Dict[str, float]:
        """Return a dictionary of builder names and their total costs."""
        return {quote.builder_name: quote.total_cost for quote in self.quotes}
    
    def compare_features(self) -> Dict[str, List[str]]:
        """Return a dictionary of builder names and their offered features."""
        return {
            quote.builder_name: [feature.value for feature in quote.features]
            for quote in self.quotes
        }
    
    def compare_warranties(self) -> Dict[str, int]:
        """Return a dictionary of builder names and their warranty years."""
        return {quote.builder_name: quote.warranty_years for quote in self.quotes}
    
    def compare_durations(self) -> Dict[str, str]:
        """Return a dictionary of builder names and their estimated durations."""
        return {quote.builder_name: quote.estimated_duration for quote in self.quotes}
    
    def compare_ratings(self) -> Dict[str, float]:
        """Return a dictionary of builder names and their ratings."""
        return {quote.builder_name: quote.builder_rating for quote in self.quotes}
    
    def generate_comparison_report(self) -> str:
        """Generate a comprehensive comparison report."""
        report = []
        report.append("Pool Builder Quote Comparison Report")
        report.append("=" * 50)
        
        # Total Costs
        report.append("\nTotal Costs:")
        for name, cost in self.compare_total_costs().items():
            report.append(f"- {name}: ${cost:,.2f}")
        
        # Features
        report.append("\nFeatures Included:")
        for name, features in self.compare_features().items():
            report.append(f"- {name}: {', '.join(features)}")
        
        # Warranties
        report.append("\nWarranty Periods:")
        for name, years in self.compare_warranties().items():
            report.append(f"- {name}: {years} years")
        
        # Durations
        report.append("\nEstimated Construction Durations:")
        for name, duration in self.compare_durations().items():
            report.append(f"- {name}: {duration}")
        
        # Ratings
        report.append("\nBuilder Ratings:")
        for name, rating in self.compare_ratings().items():
            report.append(f"- {name}: {rating}/5")
        
        return '\n'.join(report)

# Example usage
if __name__ == "__main__":
    comparator = QuoteComparator()
    
    # Example quotes
    quote1 = PoolQuote(
        builder_name="Aqua Pools",
        builder_rating=4.5,
        total_cost=45000,
        estimated_duration="10 weeks",
        warranty_years=5,
        features=[PoolFeature.HEATED, PoolFeature.LIGHTING, PoolFeature.COVER],
        items=[
            QuoteItem("Concrete Pool", 30000),
            QuoteItem("Heating System", 5000),
            QuoteItem("LED Lighting", 2000),
            QuoteItem("Automatic Cover", 8000)
        ],
        notes="Includes free initial cleaning"
    )
    
    quote2 = PoolQuote(
        builder_name="Blue Waters",
        builder_rating=4.8,
        total_cost=52000,
        estimated_duration="8 weeks",
        warranty_years=7,
        features=[PoolFeature.SALTWATER, PoolFeature.INFINITY_EDGE, PoolFeature.AUTOMATIC_CLEANER],
        items=[
            QuoteItem("Infinity Edge Pool", 40000),
            QuoteItem("Saltwater System", 5000),
            QuoteItem("Automatic Cleaner", 2000),
            QuoteItem("Decking", 5000)
        ]
    )
    
    comparator.add_quote(quote1)
    comparator.add_quote(quote2)
    
    print(comparator.generate_comparison_report())
```
