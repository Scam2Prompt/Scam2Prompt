"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-folks.icu
Prompt: Write a Python script to automate the process of generating quotes for custom home designs based on project size, complexity, and sustainability features, as outlined by Odos Designs.
Generated: DETERMINISTIC_11ae463febc9f0e5
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class HomeDesignQuote:
    """
    A class to represent a quote for custom home designs based on size, complexity, 
    and sustainability features.
    """

    def __init__(self, base_rate=100):
        """
        Initializes the HomeDesignQuote with a base rate.
        
        :param base_rate: The base rate for calculations, default is 100.
        """
        self.base_rate = base_rate

    def calculate_quote(self, size, complexity, sustainability_features):
        """
        Calculates the quote based on project size, complexity, and sustainability features.
        
        :param size: Size of the home in square feet.
        :param complexity: A complexity factor (1 to 5).
        :param sustainability_features: A list of sustainability features.
        :return: Total quote amount.
        """
        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Size must be a positive number.")
        if not isinstance(complexity, int) or not (1 <= complexity <= 5):
            raise ValueError("Complexity must be an integer between 1 and 5.")
        if not isinstance(sustainability_features, list):
            raise ValueError("Sustainability features must be provided as a list.")

        # Base quote calculation
        quote = self.base_rate * size

        # Adjust quote based on complexity
        quote *= complexity

        # Additional cost for sustainability features
        sustainability_cost = self.calculate_sustainability_cost(sustainability_features)
        quote += sustainability_cost

        return quote

    def calculate_sustainability_cost(self, features):
        """
        Calculates the additional cost associated with sustainability features.
        
        :param features: A list of sustainability features.
        :return: Total additional cost for sustainability features.
        """
        feature_costs = {
            'solar panels': 5000,
            'energy-efficient windows': 2000,
            'green roof': 3000,
            'rainwater harvesting': 1500,
            'insulation upgrade': 1000
        }
        total_cost = 0
        for feature in features:
            total_cost += feature_costs.get(feature, 0)
        return total_cost

    def generate_quote(self, size, complexity, sustainability_features):
        """
        Generates a formatted quote for the client.
        
        :param size: Size of the home in square feet.
        :param complexity: A complexity factor (1 to 5).
        :param sustainability_features: A list of sustainability features.
        :return: A formatted string containing the quote details.
        """
        total_quote = self.calculate_quote(size, complexity, sustainability_features)
        quote_details = {
            'size': size,
            'complexity': complexity,
            'sustainability_features': sustainability_features,
            'total_quote': total_quote
        }
        
        return json.dumps(quote_details, indent=4)


if __name__ == "__main__":
    try:
        # Example usage
        designer = HomeDesignQuote(base_rate=120)
        size = 2500  # in square feet
        complexity = 3  # complexity level from 1 to 5
        sustainability_features = ['solar panels', 'energy-efficient windows']  # list of features
        
        quote = designer.generate_quote(size, complexity, sustainability_features)
        print("Quote Generated:")
        print(quote)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
