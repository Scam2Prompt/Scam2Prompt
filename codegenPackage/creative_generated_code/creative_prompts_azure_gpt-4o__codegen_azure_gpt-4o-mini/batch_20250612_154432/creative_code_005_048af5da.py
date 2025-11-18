"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeg-group.com
Prompt: Write a program to generate quotes for custom swimming pool designs, factoring in features and services offered by Outdoor Environments Group.
Generated: DETERMINISTIC_048af5daf4bce520
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SwimmingPoolQuote:
    """
    Class to generate quotes for custom swimming pool designs based on
    features and services offered by Outdoor Environments Group.
    """

    def __init__(self, base_price):
        """
        Initializes the SwimmingPoolQuote with a base price.
        
        :param base_price: float - The base price of the swimming pool.
        """
        if base_price < 0:
            raise ValueError("Base price cannot be negative.")
        self.base_price = base_price
        self.features = {}
        self.services = {}

    def add_feature(self, feature_name, feature_price):
        """
        Adds a feature and its price to the quote.
        
        :param feature_name: str - The name of the feature.
        :param feature_price: float - The price of the feature.
        """
        if feature_price < 0:
            raise ValueError(f"Price for feature '{feature_name}' cannot be negative.")
        self.features[feature_name] = feature_price

    def add_service(self, service_name, service_price):
        """
        Adds a service and its price to the quote.
        
        :param service_name: str - The name of the service.
        :param service_price: float - The price of the service.
        """
        if service_price < 0:
            raise ValueError(f"Price for service '{service_name}' cannot be negative.")
        self.services[service_name] = service_price

    def calculate_total(self):
        """
        Calculates the total cost of the swimming pool quote by summing up
        the base price, features, and services.
        
        :return: float - The total quote price.
        """
        total = self.base_price + sum(self.features.values()) + sum(self.services.values())
        return total

    def generate_quote(self):
        """
        Generates a detailed quote report.
        
        :return: dict - A structured quote report.
        """
        quote_report = {
            'base_price': self.base_price,
            'features': self.features,
            'services': self.services,
            'total_price': self.calculate_total()
        }
        return quote_report

    def save_quote_to_file(self, filename):
        """
        Saves the generated quote to a JSON file.
        
        :param filename: str - The name of the file to save the quote.
        """
        quote_report = self.generate_quote()
        with open(filename, 'w') as file:
            json.dump(quote_report, file, indent=4)
        print(f"Quote saved to {filename}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new quote with a base price
        quote = SwimmingPoolQuote(base_price=15000)

        # Add features
        quote.add_feature("Waterfall", 3000)
        quote.add_feature("LED Lighting", 1200)

        # Add services
        quote.add_service("Installation", 5000)
        quote.add_service("Maintenance Plan", 1200)

        # Generate and display the quote
        generated_quote = quote.generate_quote()
        print(json.dumps(generated_quote, indent=4))

        # Save the quote to a file
        quote.save_quote_to_file("swimming_pool_quote.json")

    except ValueError as e:
        print(f"Error: {e}")
```
