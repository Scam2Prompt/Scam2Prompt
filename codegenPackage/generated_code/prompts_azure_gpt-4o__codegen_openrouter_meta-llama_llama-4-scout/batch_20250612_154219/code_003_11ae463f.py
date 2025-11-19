"""
Generated Code Metadata:
========================
Original URL: https://app-folks.icu
Prompt: Write a Python script to automate the process of generating quotes for custom home designs based on project size, complexity, and sustainability features, as outlined by Odos Designs.
Generated: DETERMINISTIC_11ae463febc9f0e5
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quote_generator.py

class HomeDesign:
    def __init__(self, size, complexity, sustainability_features):
        """
        Initialize a HomeDesign object.

        Args:
            size (str): Project size (small, medium, large)
            complexity (str): Project complexity (low, medium, high)
            sustainability_features (list): List of sustainability features
        """
        self.size = size
        self.complexity = complexity
        self.sustainability_features = sustainability_features

    def calculate_base_price(self):
        """
        Calculate the base price based on project size.

        Returns:
            float: Base price
        """
        size_prices = {
            'small': 50000,
            'medium': 100000,
            'large': 200000
        }
        return size_prices.get(self.size, 0)

    def calculate_complexity_factor(self):
        """
        Calculate the complexity factor based on project complexity.

        Returns:
            float: Complexity factor
        """
        complexity_factors = {
            'low': 1.0,
            'medium': 1.5,
            'high': 2.0
        }
        return complexity_factors.get(self.complexity, 1.0)

    def calculate_sustainability_factor(self):
        """
        Calculate the sustainability factor based on sustainability features.

        Returns:
            float: Sustainability factor
        """
        sustainability_factors = {
            'solar_panels': 0.05,
            'rainwater_harvesting': 0.03,
            'recycled_materials': 0.02
        }
        factor = 1.0
        for feature in self.sustainability_features:
            factor += sustainability_factors.get(feature, 0)
        return factor

    def generate_quote(self):
        """
        Generate a quote for the home design.

        Returns:
            dict: Quote details
        """
        base_price = self.calculate_base_price()
        complexity_factor = self.calculate_complexity_factor()
        sustainability_factor = self.calculate_sustainability_factor()
        total_price = base_price * complexity_factor * sustainability_factor
        return {
            'base_price': base_price,
            'complexity_factor': complexity_factor,
            'sustainability_factor': sustainability_factor,
            'total_price': total_price
        }


def main():
    try:
        size = input("Enter project size (small, medium, large): ")
        complexity = input("Enter project complexity (low, medium, high): ")
        sustainability_features = input("Enter sustainability features (comma-separated): ").split(',')
        sustainability_features = [feature.strip() for feature in sustainability_features]

        home_design = HomeDesign(size, complexity, sustainability_features)
        quote = home_design.generate_quote()

        print("Quote Details:")
        print(f"Base Price: ${quote['base_price']:.2f}")
        print(f"Complexity Factor: {quote['complexity_factor']:.2f}")
        print(f"Sustainability Factor: {quote['sustainability_factor']:.2f}")
        print(f"Total Price: ${quote['total_price']:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
