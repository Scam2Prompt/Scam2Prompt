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
import json
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pool_quote_comparison.log'),
        logging.StreamHandler()
    ]
)

class MaterialType(Enum):
    CONCRETE = "Concrete"
    FIBERGLASS = "Fiberglass"
    VINYL = "Vinyl"
    TILE = "Tile"
    STONE = "Stone"

@dataclass
class PoolFeature:
    name: str
    description: str
    material: MaterialType
    quantity: float
    unit: str

@dataclass
class BuilderQuote:
    builder_name: str
    base_price: float
    features: List[PoolFeature] = field(default_factory=list)
    additional_costs: Dict[str, float] = field(default_factory=dict)
    total_price: float = 0.0
    notes: Optional[str] = None

    def __post_init__(self):
        self.calculate_total()

    def calculate_total(self):
        """Calculate the total price including base price and additional costs."""
        feature_costs = sum(f.quantity * self.additional_costs.get(f.name, 0) for f in self.features)
        self.total_price = self.base_price + feature_costs

class QuoteComparator:
    def __init__(self, design_file: str):
        self.design_file = design_file
        self.quotes: List[BuilderQuote] = []
        self.design_specs: Dict = {}

    def load_design_specs(self) -> None:
        """Load the 3D design specifications from JSON file."""
        try:
            with open(self.design_file, 'r') as f:
                self.design_specs = json.load(f)
            logging.info("Successfully loaded design specifications")
        except FileNotFoundError:
            logging.error(f"Design file {self.design_file} not found")
            raise
        except json.JSONDecodeError:
            logging.error("Invalid JSON format in design file")
            raise

    def add_quote(self, quote: BuilderQuote) -> None:
        """Add a builder quote to the comparison list."""
        self.quotes.append(quote)
        logging.info(f"Added quote from {quote.builder_name}")

    def validate_quote_features(self, quote: BuilderQuote) -> bool:
        """Validate that quote features match design specifications."""
        design_features = self.design_specs.get('features', [])
        quote_feature_names = {f.name for f in quote.features}
        
        for feature in design_features:
            if feature['name'] not in quote_feature_names:
                logging.warning(
                    f"Builder {quote.builder_name} missing feature: {feature['name']}"
                )
                return False
        return True

    def compare_quotes(self) -> Dict:
        """Compare all quotes and return analysis results."""
        if not self.quotes:
            logging.error("No quotes to compare")
            raise ValueError("No quotes available for comparison")

        results = {
            'cheapest': None,
            'most_expensive': None,
            'average_price': 0.0,
            'feature_comparison': {},
            'all_quotes': []
        }

        total = 0.0
        valid_quotes = []

        for quote in self.quotes:
            if self.validate_quote_features(quote):
                valid_quotes.append(quote)
                total += quote.total_price

                if (results['cheapest'] is None or 
                    quote.total_price < results['cheapest'].total_price):
                    results['cheapest'] = quote

                if (results['most_expensive'] is None or 
                    quote.total_price > results['most_expensive'].total_price):
                    results['most_expensive'] = quote

        if not valid_quotes:
            logging.error("No valid quotes to compare")
            raise ValueError("No quotes matched the design specifications")

        results['average_price'] = total / len(valid_quotes)
        results['all_quotes'] = sorted(valid_quotes, key=lambda x: x.total_price)

        # Feature comparison
        for feature in self.design_specs.get('features', []):
            feature_name = feature['name']
            results['feature_comparison'][feature_name] = {
                'average_cost': 0.0,
                'builders': {}
            }
            
            total_cost = 0.0
            builder_count = 0
            
            for quote in valid_quotes:
                for q_feature in quote.features:
                    if q_feature.name == feature_name:
                        cost = quote.additional_costs.get(feature_name, 0)
                        total_cost += cost * q_feature.quantity
                        builder_count += 1
                        results['feature_comparison'][feature_name]['builders'][quote.builder_name] = cost
            
            if builder_count > 0:
                results['feature_comparison'][feature_name]['average_cost'] = total_cost / builder_count

        return results

    def generate_report(self, output_file: str = "quote_comparison_report.json") -> None:
        """Generate a detailed comparison report in JSON format."""
        comparison = self.compare_quotes()
        
        report = {
            'design_specs': self.design_specs,
            'comparison_results': {
                'cheapest_builder': comparison['cheapest'].builder_name,
                'cheapest_price': comparison['cheapest'].total_price,
                'most_expensive_builder': comparison['most_expensive'].builder_name,
                'most_expensive_price': comparison['most_expensive'].total_price,
                'average_price': comparison['average_price'],
                'feature_comparison': comparison['feature_comparison'],
                'all_quotes': [
                    {
                        'builder': q.builder_name,
                        'total_price': q.total_price,
                        'base_price': q.base_price,
                        'features': [
                            {
                                'name': f.name,
                                'cost': q.additional_costs.get(f.name, 0),
                                'quantity': f.quantity,
                                'unit': f.unit
                            } for f in q.features
                        ]
                    } for q in comparison['all_quotes']
                ]
            }
        }

        try:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=4)
            logging.info(f"Successfully generated report: {output_file}")
        except IOError as e:
            logging.error(f"Failed to write report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize comparator with design file
        comparator = QuoteComparator("pool_design.json")
        comparator.load_design_specs()

        # Add sample quotes
        quote1 = BuilderQuote(
            builder_name="Aqua Pools",
            base_price=25000,
            additional_costs={
                "Waterfall": 2000,
                "Heating System": 3500,
                "Lighting": 1200
            },
            features=[
                PoolFeature("Waterfall", "Custom stone waterfall", MaterialType.STONE, 1, "unit"),
                PoolFeature("Heating System", "Solar heating system", MaterialType.CONCRETE, 1, "unit"),
                PoolFeature("Lighting", "LED color lighting", MaterialType.CONCRETE, 10, "lights")
            ]
        )

        quote2 = BuilderQuote(
            builder_name="Blue Waters",
            base_price=30000,
            additional_costs={
                "Waterfall": 2500,
                "Heating System": 3000,
                "Lighting": 1500
            },
            features=[
                PoolFeature("Waterfall", "Custom stone waterfall", MaterialType.STONE, 1, "unit"),
                PoolFeature("Heating System", "Electric heating system", MaterialType.CONCRETE, 1, "unit"),
                PoolFeature("Lighting", "LED color lighting", MaterialType.CONCRETE, 12, "lights")
            ]
        )

        comparator.add_quote(quote1)
        comparator.add_quote(quote2)

        # Generate comparison report
        comparator.generate_report()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
