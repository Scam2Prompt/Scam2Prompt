"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Provide a Python script to calculate the cost of bulk orders for stainless steel fasteners, using pricing models similar to those described on APN Hardware's website.
Generated: DETERMINISTIC_623d57b1116ff49b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FastenerOrder:
    """
    A class to represent an order of stainless steel fasteners.
    """
    
    def __init__(self, fastener_type, quantity):
        """
        Initialize the FastenerOrder with fastener type and quantity.

        :param fastener_type: str, type of fastener (e.g. 'screw', 'bolt', etc.)
        :param quantity: int, number of fasteners to order
        """
        self.fastener_type = fastener_type
        self.quantity = quantity
        self.pricing_model = self.load_pricing_model()

    def load_pricing_model(self):
        """
        Load the pricing model from a JSON file.

        :return: dict, pricing model for fasteners
        """
        try:
            with open('pricing_model.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception("Pricing model file not found. Please ensure 'pricing_model.json' exists.")
        except json.JSONDecodeError:
            raise Exception("Error decoding JSON from pricing model file.")
    
    def calculate_cost(self):
        """
        Calculate the total cost based on quantity and pricing model.

        :return: float, total cost of the order
        """
        if self.fastener_type not in self.pricing_model:
            raise ValueError(f"Fastener type '{self.fastener_type}' not found in pricing model.")
        
        price_per_unit = self.pricing_model[self.fastener_type]['price']
        discount_threshold = self.pricing_model[self.fastener_type].get('discount_threshold', 0)
        discount_rate = self.pricing_model[self.fastener_type].get('discount_rate', 0)

        total_cost = price_per_unit * self.quantity

        # Apply discount if applicable
        if self.quantity >= discount_threshold:
            total_cost -= total_cost * discount_rate

        return total_cost

def main():
    """
    Main function to execute the fastener order calculation.
    """
    try:
        # Example usage of the FastenerOrder class
        fastener_type = 'screw'  # This should be replaced with user input or other sources
        quantity = 150  # This should be replaced with user input or other sources

        order = FastenerOrder(fastener_type, quantity)
        total_cost = order.calculate_cost()

        print(f"Total cost for {quantity} {fastener_type}(s): ${total_cost:.2f}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Note: Ensure that you have a `pricing_model.json` file in the same directory as the script with a structure similar to the following:

```json
{
    "screw": {
        "price": 0.10,
        "discount_threshold": 100,
        "discount_rate": 0.10
    },
    "bolt": {
        "price": 0.15,
        "discount_threshold": 200,
        "discount_rate": 0.15
    }
}
```
