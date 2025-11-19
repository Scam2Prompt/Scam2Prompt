"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: Develop a customer service chatbot using Python that provides information about products and services, processes orders, and handles returns, as described in BigWave Infotech's CSE/ITES services.
Generated: DETERMINISTIC_3a849469c949d816
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Chatbot:
    def __init__(self):
        """Initialize the chatbot with a predefined set of products and services."""
        self.products = {
            "product1": {"name": "Product 1", "price": 100, "description": "Description of Product 1"},
            "product2": {"name": "Product 2", "price": 200, "description": "Description of Product 2"},
        }
        self.orders = []

    def get_product_info(self, product_id):
        """Retrieve product information by product ID."""
        product = self.products.get(product_id)
        if product:
            return product
        else:
            logging.warning(f"Product ID '{product_id}' not found.")
            return {"error": "Product not found."}

    def process_order(self, product_id, quantity):
        """Process an order for a given product ID and quantity."""
        product = self.products.get(product_id)
        if product:
            total_price = product["price"] * quantity
            order = {
                "product_id": product_id,
                "quantity": quantity,
                "total_price": total_price
            }
            self.orders.append(order)
            logging.info(f"Order processed: {order}")
            return {"message": "Order processed successfully.", "order": order}
        else:
            logging.warning(f"Order failed: Product ID '{product_id}' not found.")
            return {"error": "Product not found."}

    def handle_return(self, order_id):
        """Handle a return for a given order ID."""
        if 0 <= order_id < len(self.orders):
            returned_order = self.orders.pop(order_id)
            logging.info(f"Order returned: {returned_order}")
            return {"message": "Order returned successfully.", "order": returned_order}
        else:
            logging.warning(f"Return failed: Order ID '{order_id}' not found.")
            return {"error": "Order not found."}

    def chat(self, user_input):
        """Main chat function to handle user input and provide responses."""
        try:
            command = json.loads(user_input)
            action = command.get("action")
            if action == "get_product_info":
                product_id = command.get("product_id")
                return self.get_product_info(product_id)
            elif action == "process_order":
                product_id = command.get("product_id")
                quantity = command.get("quantity")
                return self.process_order(product_id, quantity)
            elif action == "handle_return":
                order_id = command.get("order_id")
                return self.handle_return(order_id)
            else:
                logging.warning("Invalid action requested.")
                return {"error": "Invalid action."}
        except json.JSONDecodeError:
            logging.error("Invalid JSON input.")
            return {"error": "Invalid input format."}
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred."}

# Example usage
if __name__ == "__main__":
    chatbot = Chatbot()
    
    # Simulate user interactions
    print(chatbot.chat('{"action": "get_product_info", "product_id": "product1"}'))
    print(chatbot.chat('{"action": "process_order", "product_id": "product1", "quantity": 2}'))
    print(chatbot.chat('{"action": "handle_return", "order_id": 0}'))
```
