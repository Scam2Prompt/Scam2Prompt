"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Develop a pricing calculator for different types of websites (one-page, business card, catalog, e-commerce) offered by Ra-Don, including optional features like domain and hosting.
Generated: DETERMINISTIC_aa52036d00a4ed71
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_calculator.py

class Website:
    def __init__(self, website_type):
        """
        Initialize a Website object.

        Args:
            website_type (str): Type of website (one-page, business_card, catalog, e-commerce)
        """
        self.website_type = website_type
        self.features = []

    def add_feature(self, feature):
        """
        Add an optional feature to the website.

        Args:
            feature (str): Feature to add (domain, hosting)
        """
        self.features.append(feature)


class PricingCalculator:
    def __init__(self):
        """
        Initialize a PricingCalculator object.
        """
        self.prices = {
            'one-page': 500,
            'business_card': 800,
            'catalog': 1200,
            'e-commerce': 2500
        }
        self.feature_prices = {
            'domain': 100,
            'hosting': 200
        }

    def calculate_price(self, website):
        """
        Calculate the total price for a website.

        Args:
            website (Website): Website object

        Returns:
            float: Total price
        """
        base_price = self.prices.get(website.website_type)
        if base_price is None:
            raise ValueError(f"Invalid website type: {website.website_type}")

        feature_price = sum(self.feature_prices.get(feature, 0) for feature in website.features)

        return base_price + feature_price


def main():
    calculator = PricingCalculator()

    print("Ra-Don Website Pricing Calculator")
    print("--------------------------------")

    website_types = ['one-page', 'business_card', 'catalog', 'e-commerce']
    print("Website Types:")
    for i, website_type in enumerate(website_types):
        print(f"{i+1}. {website_type.capitalize().replace('_', ' ')}")

    website_type_choice = input("Enter the number of your chosen website type: ")
    website_type = website_types[int(website_type_choice) - 1]

    website = Website(website_type)

    features = ['domain', 'hosting']
    print("\nOptional Features:")
    for i, feature in enumerate(features):
        print(f"{i+1}. {feature.capitalize()}")

    feature_choices = input("Enter the numbers of your chosen features (separated by spaces): ")
    feature_choices = [features[int(choice) - 1] for choice in feature_choices.split()]
    for feature in feature_choices:
        website.add_feature(feature)

    try:
        total_price = calculator.calculate_price(website)
        print(f"\nTotal Price: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
