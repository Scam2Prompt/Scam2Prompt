"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Write a program to simulate the bidding process for pool builders, ensuring competitive quotes based on a clear brief, as outlined on the Poolz website.
Generated: DETERMINISTIC_658ed38b5180304d
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PoolBuilder:
    def __init__(self, name, base_price, expertise_level):
        """
        Initialize PoolBuilder with a name, base price, and expertise level.

        :param name: Name of the pool builder company
        :param base_price: Base price for the project (in dollars)
        :param expertise_level: Expertise level, affects pricing (1-10 scale)
        """
        self.name = name
        self.base_price = base_price
        self.expertise_level = expertise_level

    def generate_quote(self, project_complexity):
        """
        Generate a quote based on the base price, expertise level, and project complexity.

        :param project_complexity: Complexity of the project (1-10 scale)
        :return: Quote price in dollars
        """
        # Adjust price based on project complexity and expertise level
        complexity_multiplier = project_complexity * 0.1
        expertise_discount = self.expertise_level * 0.05
        final_price = self.base_price * (1 + complexity_multiplier - expertise_discount)

        # Ensure the price is rounded to 2 decimal places
        return round(final_price, 2)


class BidSystem:
    def __init__(self, builders, project_complexity):
        """
        Initialize the bidding system with pool builders and project complexity.

        :param builders: List of PoolBuilder objects
        :param project_complexity: Complexity of the project (1-10 scale)
        """
        self.builders = builders
        self.project_complexity = project_complexity

    def get_quotes(self):
        """
        Get quotes from all builders.

        :return: List of quotes with builder names
        """
        quotes = []
        for builder in self.builders:
            try:
                # Generate quote for each builder
                quote = builder.generate_quote(self.project_complexity)
                quotes.append((builder.name, quote))
            except Exception as e:
                # Log error and skip builder in case of an issue
                print(f"Error generating quote for {builder.name}: {e}")
        return quotes

    def display_quotes(self):
        """
        Display all quotes in a user-friendly format.
        """
        quotes = self.get_quotes()
        quotes.sort(key=lambda x: x[1])  # Sort quotes by price (ascending)

        print("Competitive Bidding Results:")
        print("---------------------------")
        for name, price in quotes:
            print(f"{name}: ${price}")
        print("\nBest Option: ", quotes[0][0], " - $",quotes[0].
