"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Develop a simple chatbot in Python to provide customer support for an outdoor gear store, integrating with the content and product information from activesport.cz."
Generated: DETERMINISTIC_7d76b1c142d4525b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional

class OutdoorGearChatbot:
    """
    A simple chatbot for providing customer support for an outdoor gear store.
    Integrates with product information from activesport.cz (simulated).
    """
    
    def __init__(self):
        """
        Initialize the chatbot with greetings and load product data.
        """
        self.greetings = [
            "Hello! Welcome to ActiveSport Outdoor Gear. How can I help you today?",
            "Hi there! Ready for your next adventure? How can I assist you?",
            "Welcome to ActiveSport! What outdoor gear are you looking for today?"
        ]
        self.farewells = [
            "Thank you for visiting ActiveSport! Have a great adventure!",
            "Happy trails! Come back if you need more outdoor gear advice.",
            "Goodbye! Don't hesitate to return if you have more questions."
        ]
        self.products = self._load_product_data()
        self.unknown_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I don't have information on that. Can I help with something else?",
            "Our outdoor gear experts could help with that. Would you like to contact them?"
        ]

    def _load_product_data(self) -> Dict[str, Dict]:
        """
        Load simulated product data (in a real app, this would come from activesport.cz API).
        
        Returns:
            Dict[str, Dict]: Dictionary of product categories and their items.
        """
        # Simulated product data structure
        return {
            "tents": {
                "Marmot Tungsten 2P": {
                    "price": 299.99,
                    "description": "2-person tent with durable construction",
                    "stock": True
                },
                "MSR Hubba Hubba NX": {
                    "price": 449.95,
                    "description": "Lightweight 2-person backpacking tent",
                    "stock": False
                }
            },
            "sleeping_bags": {
                "The North Face Cat's Meow": {
                    "price": 199.00,
                    "description": "20°F synthetic sleeping bag",
                    "stock": True
                },
                "Western Mountaineering UltraLite": {
                    "price": 549.95,
                    "description": "20°F down sleeping bag, ultralight",
                    "stock": True
                }
            },
            "backpacks": {
                "Osprey Atmos AG 65": {
                    "price": 279.95,
                    "description": "65L backpack with anti-gravity suspension",
                    "stock": True
                },
                "Gregory Baltoro 75": {
                    "price": 329.95,
                    "description": "75L backpack for heavy loads",
                    "stock": False
                }
            }
        }

    def get_random_response(self, responses: List[str]) -> str:
        """
        Select a random response from a list of possible responses.
        
        Args:
            responses (List[str]): List of possible responses.
            
        Returns:
            str: Randomly selected response.
        """
        return random.choice(responses)

    def handle_greeting(self) -> str:
        """
        Generate a greeting message.
        
        Returns:
            str: Random greeting message.
        """
        return self.get_random_response(self.greetings)

    def handle_farewell(self) -> str:
        """
        Generate a farewell message.
        
        Returns:
            str: Random farewell message.
        """
        return self.get_random_response(self.farewells)

    def handle_product_inquiry(self, product_name: str) -> str:
        """
        Respond to a product inquiry with product details if available.
        
        Args:
            product_name (str): Name of the product being inquired about.
            
        Returns:
            str: Response with product details or not found message.
        """
        product_name = product_name.lower()
        found_product = None
        category_name = None

        for category, products in self.products.items():
            for name, details in products.items():
                if product_name in name.lower():
                    found_product = details
                    category_name = category
                    product_name = name
                    break
            if found_product:
                break

        if found_product:
            stock_status = "in stock" if found_product["stock"] else "out of stock"
            return (f"The {product_name} is {stock_status}. "
                   f"Price: {found_product['price']} CZK. "
                   f"Description: {found_product['description']}")
        else:
            return self.get_random_response(self.unknown_responses)

    def handle_category_inquiry(self, category: str) -> str:
        """
        Respond to a category inquiry with list of available products.
        
        Args:
            category (str): Name of the category being inquired about.
            
        Returns:
            str: Response with product list or not found message.
        """
        category = category.lower()
        normalized_categories = {
            "tent": "tents",
            "tents": "tents",
            "sleeping bag": "sleeping_bags",
            "sleeping bags": "sleeping_bags",
            "backpack": "backpacks",
            "backpacks": "backpacks"
        }

        if category in normalized_categories:
            category = normalized_categories[category]
            if category in self.products:
                products = self.products[category]
                response = f"We have these {category.replace('_', ' ')} available:\n"
                for name, details in products.items():
                    stock_status = "✓" if details["stock"] else "✗"
                    response += f"- {name} ({stock_status}) {details['price']} CZK\n"
                return response
        return self.get_random_response(self.unknown_responses)

    def process_message(self, message: str) -> str:
        """
        Process user message and generate appropriate response.
        
        Args:
            message (str): User input message.
            
        Returns:
            str: Generated response.
        """
        message = message.lower().strip()
        
        if any(word in message for word in ["hi", "hello", "hey", "greetings"]):
            return self.handle_greeting()
        elif any(word in message for word in ["bye", "goodbye", "exit", "quit"]):
            return self.handle_farewell()
        elif "product" in message or any(word in message for word in ["item", "specific"]):
            # Extract product name (simplified)
            product_name = message.replace("product", "").replace("item", "").strip()
            return self.handle_product_inquiry(product_name)
        elif any(word in message for word in ["category", "type", "kind", "tent", "sleeping bag", "backpack"]):
            # Extract category (simplified)
            category = message.replace("category", "").replace("type", "").strip()
            return self.handle_category_inquiry(category)
        else:
            return self.get_random_response(self.unknown_responses)

def main():
    """
    Main function to run the chatbot interactively.
    """
    chatbot = OutdoorGearChatbot()
    print(chatbot.handle_greeting())
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(chatbot.handle_farewell())
                break
                
            response = chatbot.process_message(user_input)
            print("Bot:", response)
            
        except KeyboardInterrupt:
            print("\n" + chatbot.handle_farewell())
            break
        except Exception as e:
            print("Bot: Sorry, I encountered an error. Please try again.")
            if __debug__:
                print(f"[Debug] Error: {e}")

if __name__ == "__main__":
    main()
```
