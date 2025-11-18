"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Create a chatbot script that can answer questions about Homefoods Ghana's product categories, such as "Chicken Seasoning" or "Hausa Kooko Cinnamon Flavored."
Generated: DETERMINISTIC_b18532115148d728
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class HomefoodsChatbot:
    def __init__(self):
        # Initialize product categories with their descriptions
        self.products = {
            "Chicken Seasoning": "A savory blend of spices designed to enhance the flavor of chicken dishes.",
            "Hausa Kooko Cinnamon Flavored": "A deliciously spiced drink made with high-quality cinnamon for a warm, aromatic experience."
            # Add more products as needed
        }

    def get_product_info(self, product_name):
        """
        Retrieves the information for the specified product.
        
        :param product_name: str: Name of the product to retrieve information for.
        :return: str: Description of the product or an error message if the product is not found.
        """
        try:
            # Normalize the product name for case-insensitive matching
            normalized_name = product_name.strip().title()
            if normalized_name in self.products:
                return self.products[normalized_name]
            else:
                return f"Sorry, I don't have information about '{product_name}'. Please check the product name."
        except Exception as e:
            return f"An error occurred while retrieving product information: {str(e)}"

    def chat(self):
        """
        Starts a chat session with the user to answer product-related queries.
        """
        print("Welcome to the Homefoods Ghana Chatbot!")
        print("You can ask me about our products, like 'Chicken Seasoning' or 'Hausa Kooko Cinnamon Flavored'.")
        print("Type 'exit' to end the chat.")

        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            # Get and display product information
            response = self.get_product_info(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Create an instance of the chatbot and start the chat
    chatbot = HomefoodsChatbot()
    chatbot.chat()
```
