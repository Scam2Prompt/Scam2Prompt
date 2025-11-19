"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Create a chatbot script that can answer questions about Homefoods Ghana's product categories, such as "Chicken Seasoning" or "Hausa Kooko Cinnamon Flavored."
Generated: DETERMINISTIC_b18532115148d728
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class HomefoodsGhanaChatbot:
    """
    A chatbot that provides information about Homefoods Ghana's product categories.
    """

    def __init__(self, products_data_path: str = "products.json"):
        """
        Initialize the chatbot with product data.

        Args:
            products_data_path (str): Path to JSON file containing product data.
        """
        try:
            with open(products_data_path, 'r') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Product data file not found at {products_data_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {products_data_path}")

    def get_product_categories(self) -> List[str]:
        """
        Get all available product categories.

        Returns:
            List[str]: List of product category names.
        """
        return list(self.products.keys())

    def get_product_info(self, category: str) -> Optional[Dict[str, str]]:
        """
        Get information about a specific product category.

        Args:
            category (str): Name of the product category.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing product information,
                                     or None if category doesn't exist.
        """
        return self.products.get(category.title())

    def handle_query(self, query: str) -> str:
        """
        Process user query and return appropriate response.

        Args:
            query (str): User's question about products.

        Returns:
            str: Response to the user's query.
        """
        query = query.strip().lower()
        
        # Check for greeting
        if any(greeting in query for greeting in ["hi", "hello", "hey"]):
            return "Hello! Welcome to Homefoods Ghana. How can I help you with our products today?"
        
        # Check for help request
        if "help" in query:
            return "I can provide information about Homefoods Ghana products. Try asking about categories or specific products like 'Chicken Seasoning'."
        
        # List all categories if asked
        if "categories" in query or "list" in query:
            categories = self.get_product_categories()
            return f"Our product categories are: {', '.join(categories)}."
        
        # Check for specific product queries
        for category in self.get_product_categories():
            if category.lower() in query:
                product_info = self.get_product_info(category)
                if product_info:
                    return (f"{category}: {product_info.get('description', 'No description available')}. "
                           f"Key features: {product_info.get('features', 'N/A')}. "
                           f"Available in: {product_info.get('availability', 'N/A')}.")
        
        return "I couldn't find information about that product. Please try asking about our product categories or specific items like 'Chicken Seasoning'."

# Example usage
if __name__ == "__main__":
    # Sample product data (in production, this would be in a separate JSON file)
    sample_products = {
        "Chicken Seasoning": {
            "description": "A special blend of spices for perfect chicken dishes",
            "features": "All-natural ingredients, no MSG, gluten-free",
            "availability": "All major supermarkets in Ghana"
        },
        "Hausa Kooko Cinnamon Flavored": {
            "description": "Traditional Hausa porridge with cinnamon flavor",
            "features": "Instant preparation, rich in fiber, vegan-friendly",
            "availability": "Northern region and selected stores nationwide"
        }
    }

    # Save sample data to file for demonstration
    with open("products.json", 'w') as f:
        json.dump(sample_products, f)

    # Initialize and run chatbot
    chatbot = HomefoodsGhanaChatbot()
    
    print("Homefoods Ghana Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.handle_query(user_input)
        print("Bot:", response)
```
