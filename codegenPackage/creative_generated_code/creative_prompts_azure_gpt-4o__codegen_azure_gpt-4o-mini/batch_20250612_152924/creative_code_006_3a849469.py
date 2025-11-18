"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigwaveinfotech.net
Prompt: Develop a customer service chatbot using Python that provides information about products and services, processes orders, and handles returns, as described in BigWave Infotech's CSE/ITES services.
Generated: DETERMINISTIC_3a849469c949d816
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Chatbot:
    def __init__(self):
        # Load product and service data from a JSON file
        self.products = self.load_data("products.json")
        self.services = self.load_data("services.json")

    def load_data(self, filename):
        """
        Loads data from a JSON file.

        :param filename: str, the name of the JSON file to load
        :return: dict, the data loaded from the file
        """
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: The file {filename} is not a valid JSON.")
            return {}

    def get_product_info(self, product_id):
        """
        Retrieves product information based on the product ID.

        :param product_id: str, the ID of the product
        :return: dict, the product information or None if not found
        """
        return self.products.get(product_id, None)

    def get_service_info(self, service_id):
        """
        Retrieves service information based on the service ID.

        :param service_id: str, the ID of the service
        :return: dict, the service information or None if not found
        """
        return self.services.get(service_id, None)

    def process_order(self, product_id, quantity):
        """
        Processes an order for a product.

        :param product_id: str, the ID of the product to order
        :param quantity: int, the quantity of the product to order
        :return: str, order confirmation or error message
        """
        product = self.get_product_info(product_id)
        if product is None:
            return "Error: Product not found."
        if quantity <= 0:
            return "Error: Quantity must be greater than zero."
        
        # Simulate order processing
        return f"Order confirmed for {quantity} of {product['name']}."

    def handle_return(self, order_id):
        """
        Processes a return request.

        :param order_id: str, the ID of the order to return
        :return: str, return confirmation or error message
        """
        # This is a stub implementation for returning an order
        # In a real-world scenario, you would check the order status
        return f"Return request processed for order ID: {order_id}."

    def chat(self):
        """
        Main chat loop for the chatbot.
        """
        print("Welcome to BigWave Infotech Customer Service Chatbot!")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input in ["exit", "quit"]:
                print("Chatbot: Thank you for chatting. Goodbye!")
                break
            
            # Simulated command processing
            if user_input.startswith("info product"):
                product_id = user_input.split()[-1]
                product_info = self.get_product_info(product_id)
                if product_info:
                    print(f"Chatbot: {product_info}")
                else:
                    print("Chatbot: Product not found.")
            elif user_input.startswith("order"):
                _, product_id, quantity = user_input.split()
                quantity = int(quantity)
                response = self.process_order(product_id, quantity)
                print(f"Chatbot: {response}")
            elif user_input.startswith("return"):
                order_id = user_input.split()[-1]
                response = self.handle_return(order_id)
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: Sorry, I didn't understand that. You can ask about products, place an order, or handle returns.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
```

- Ensure to create `products.json` and `services.json` files with appropriate data structures before running the chatbot.
- Example structure for `products.json`:
```json
{
    "101": {"name": "Product A", "price": 29.99},
    "102": {"name": "Product B", "price": 49.99}
}
```

- Example structure for `services.json`:
```json
{
    "201": {"name": "Service A", "description": "Description of Service A"},
    "202": {"name": "Service B", "description": "Description of Service B"}
}
```
