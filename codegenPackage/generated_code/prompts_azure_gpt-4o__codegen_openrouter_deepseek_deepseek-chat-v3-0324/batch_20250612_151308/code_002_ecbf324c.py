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
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import csv
import argparse
from pathlib import Path

@dataclass
class PoolFeature:
    """Represents a single feature in a pool quote."""
    name: str
    description: str
    included: bool
    cost: float
    notes: str = ""

@dataclass
class PoolQuote:
    """Represents a quote from a pool builder."""
    builder_name: str
    base_price: float
    features: List[PoolFeature] = field(default_factory=list)
    total_price: float = 0.0
    notes: str = ""

    def __post_init__(self):
        """Calculate total price after initialization."""
        self.total_price = self.base_price + sum(
            feature.cost for feature in self.features if feature.included
        )

class QuoteComparator:
    """Compares multiple pool builder quotes for apples-to-apples comparison."""
    
    def __init__(self):
        self.quotes: List[PoolQuote] = []
    
    def add_quote(self, quote: PoolQuote) -> None:
        """Add a quote to the comparator."""
        self.quotes.append(quote)
    
    def load_quotes_from_json(self, file_path: Path) -> None:
        """Load quotes from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for quote_data in data['quotes']:
                    features = [
                        PoolFeature(**feature) 
                        for feature in quote_data.get('features', [])
                    ]
                    quote = PoolQuote(
                        builder_name=quote_data['builder_name'],
                        base_price=quote_data['base_price'],
                        features=features,
                        notes=quote_data.get('notes', '')
                    )
                    self.add_quote(quote)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON: {e}")
    
    def load_quotes_from_csv(self, file_path: Path) -> None:
        """Load quotes from a CSV file."""
        try:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    features = []
                    for feature_name in reader.fieldnames:
                        if feature_name not in ['builder_name', 'base_price', 'notes']:
                            included = row.get(feature_name, '').lower() in ['yes', 'true', '1']
                            cost = float(row.get(f'{feature_name}_cost', 0))
                            features.append(
                                PoolFeature(
                                    name=feature_name,
                                    description="",
                                    included=included,
                                    cost=cost
                                )
                            )
                    
                    quote = PoolQuote(
                        builder_name=row['builder_name'],
                        base_price=float(row['base_price']),
                        features=features,
                        notes=row.get('notes', '')
                    )
                    self.add_quote(quote)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except ValueError as e:
            raise ValueError(f"Invalid data in CSV: {e}")
    
    def get_common_features(self) -> List[str]:
        """Get a list of all common features across all quotes."""
        if not self.quotes:
            return []
        
        feature_sets = [set(f.name for f in quote.features) for quote in self.quotes]
        common_features = set.intersection(*feature_sets)
        return sorted(common_features)
    
    def compare_quotes(self) -> Dict[str, Dict[str, float]]:
        """Compare all quotes based on common features."""
        common_features = self.get_common_features()
        comparison = {}
        
        for quote in self.quotes:
            builder_data = {
                'base_price': quote.base_price,
                'total_price': quote.total_price
            }
            
            for feature_name in common_features:
                feature = next((f for f in quote.features if f.name == feature_name), None)
                if feature:
                    builder_data[feature_name] = feature.cost if feature.included else 0
            
            comparison[quote.builder_name] = builder_data
        
        return comparison
    
    def generate_comparison_report(self, output_format: str = 'table') -> str:
        """Generate a comparison report in the specified format."""
        comparison = self.compare_quotes()
        common_features = self.get_common_features()
        
        if output_format == 'table':
            return self._generate_table_report(comparison, common_features)
        elif output_format == 'json':
            return json.dumps(comparison, indent=2)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_table_report(self, comparison: Dict, common_features: List[str]) -> str:
        """Generate a human-readable table report."""
        headers = ["Builder", "Base Price", "Total Price"] + common_features
        rows = []
        
        for builder, data in comparison.items():
            row = [builder, f"${data['base_price']:,.2f}", f"${data['total_price']:,.2f}"]
            for feature in common_features:
                cost = data.get(feature, 0)
                row.append(f"${cost:,.2f}" if cost else "Not Included")
            rows.append(row)
        
        # Format table
        col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
        header_line = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        separator = "-+-".join("-" * w for w in col_widths)
        row_lines = [
            " | ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths))
            for row in rows
        ]
        
        return "\n".join([header_line, separator] + row_lines)

def main():
    parser = argparse.ArgumentParser(description='Compare pool builder quotes.')
    parser.add_argument(
        'input_file', 
        type=str, 
        help='Path to input file (JSON or CSV) containing quotes'
    )
    parser.add_argument(
        '--format', 
        type=str, 
        default='table',
        choices=['table', 'json'],
        help='Output format (table or json)'
    )
    parser.add_argument(
        '--output', 
        type=str, 
        help='Output file path (prints to console if not specified)'
    )
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    
    comparator = QuoteComparator()
    
    try:
        if input_path.suffix.lower() == '.json':
            comparator.load_quotes_from_json(input_path)
        elif input_path.suffix.lower() == '.csv':
            comparator.load_quotes_from_csv(input_path)
        else:
            raise ValueError("Unsupported file format. Please use JSON or CSV.")
        
        report = comparator.generate_comparison_report(args.format)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        else:
            print(report)
    
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()
```
