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

class PoolQuoteComparator:
    """
    A class to compare quotes from multiple pool builders based on a detailed scope and 3D design.
    """

    def __init__(self, scope_file, quotes_file):
        """
        Initialize the comparator with the scope and quotes files.

        :param scope_file: Path to the JSON file containing the detailed scope and 3D design.
        :param quotes_file: Path to the JSON file containing quotes from pool builders.
        """
        self.scope = self._load_json(scope_file)
        self.quotes = self._load_json(quotes_file)

    def _load_json(self, file_path):
        """
        Load JSON data from a file.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data as a dictionary.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")

    def compare_quotes(self):
        """
        Compare quotes based on the scope and 3D design.

        :return: A list of dictionaries containing comparison results for each builder.
        """
        comparison_results = []

        for builder, quote in self.quotes.items():
            builder_result = {
                "builder": builder,
                "total_price": quote.get("total_price", 0),
                "price_breakdown": quote.get("price_breakdown", {}),
                "scope_match": self._evaluate_scope_match(quote),
                "competitiveness": self._evaluate_competitiveness(quote)
            }
            comparison_results.append(builder_result)

        return comparison_results

    def _evaluate_scope_match(self, quote):
        """
        Evaluate how well the quote matches the scope and 3D design.

        :param quote: A dictionary containing the builder's quote.
        :return: A percentage (0-100) indicating the scope match.
        """
        scope_items = self.scope.get("items", [])
        quote_items = quote.get("items", [])

        if not scope_items or not quote_items:
            return 0

        matched_items = sum(1 for item in scope_items if item in quote_items)
        return (matched_items / len(scope_items)) * 100

    def _evaluate_competitiveness(self, quote):
        """
        Evaluate the competitiveness of the quote based on pricing.

        :param quote: A dictionary containing the builder's quote.
        :return: A string indicating competitiveness ("High", "Medium", "Low").
        """
        total_price = quote.get("total_price", 0)
        all_prices = [q.get("total_price", 0) for q in self.quotes.values()]

        if not all_prices:
            return "Unknown"

        average_price = sum(all_prices) / len(all_prices)

        if total_price < average_price * 0.9:
            return "High"
        elif total_price <= average_price * 1.1:
            return "Medium"
        else:
            return "Low"

    def display_results(self, results):
        """
        Display the comparison results in a readable format.

        :param results: A list of dictionaries containing comparison results.
        """
        print("Pool Builder Quote Comparison Results:")
        print("=" * 50)
        for result in results:
            print(f"Builder: {result['builder']}")
            print(f"Total Price: ${result['total_price']}")
            print(f"Scope Match: {result['scope_match']:.2f}%")
            print(f"Competitiveness: {result['competitiveness']}")
            print("Price Breakdown:")
            for item, price in result['price_breakdown'].items():
                print(f"  {item}: ${price}")
            print("-" * 50)

def main():
    """
    Main function to execute the PoolQuoteComparator.
    """
    # File paths for scope and quotes (replace with actual file paths)
    scope_file = "scope.json"
    quotes_file = "quotes.json"

    try:
        comparator = PoolQuoteComparator(scope_file, quotes_file)
        results = comparator.compare_quotes()
        comparator.display_results(results)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
