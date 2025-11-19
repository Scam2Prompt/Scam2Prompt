"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Write a Python script to create a simple interior design advisor chatbot that suggests products and decor ideas based on user input, using a dataset of products from websites like origines-decoration.com."
Generated: DETERMINISTIC_f4bf7870b5eab19b
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class InteriorDesignAdvisor:
    def __init__(self, product_data_file):
        """
        Initializes the InteriorDesignAdvisor with a dataset of products.

        :param product_data_file: Path to the JSON file containing product data.
        """
        self.products = self.load_product_data(product_data_file)

    def load_product_data(self, product_data_file):
        """
        Loads product data from a JSON file.

        :param product_data_file: Path to the JSON file.
        :return: List of products.
        """
        try:
            with open(product_data_file, 'r') as file:
                products = json.load(file)
                return products
        except FileNotFoundError:
            print(f"Error: The file {product_data_file} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON.")
            return []

    def suggest_product(self, style):
        """
        Suggests a product based on the user's preferred style.

        :param style: The style input from the user.
        :return: A suggested product or a message if no products are found.
        """
        filtered_products = [product for product in self.products if style.lower() in product['style'].lower()]
        
        if filtered_products:
            suggested_product = random.choice(filtered_products)
            return f"How about this {suggested_product['name']}? It's a great fit for {style} style!"
        else:
            return f"Sorry, I couldn't find any products for the {style} style."

    def run_chatbot(self):
        """
        Runs the chatbot, allowing user interaction.
        """
        print("Welcome to the Interior Design Advisor Chatbot!")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("What style are you interested in? ")
            if user_input.lower() == 'exit':
                print("Thank you for using the Interior Design Advisor. Goodbye!")
                break
            
            suggestion = self.suggest_product(user_input)
            print(suggestion)

if __name__ == "__main__":
    # Path to the JSON file containing product data
    product_data_file = 'products.json'
    
    # Create an instance of the InteriorDesignAdvisor
    advisor = InteriorDesignAdvisor(product_data_file)
    
    # Start the chatbot
    advisor.run_chatbot()
```

**Note:** Ensure that you have a `products.json` file in the same directory as this script, containing a list of products with at least `name` and `style` fields for the chatbot to function correctly. Here is an example of how the `products.json` file might look:

```json
[
    {"name": "Modern Sofa", "style": "modern"},
    {"name": "Vintage Chair", "style": "vintage"},
    {"name": "Rustic Table", "style": "rustic"},
    {"name": "Minimalist Lamp", "style": "minimalist"}
]
```
