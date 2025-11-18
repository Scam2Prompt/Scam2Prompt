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

class Chatbot:
    def __init__(self):
        """
        Constructor initializes the chatbot with product categories.
        """
        self.product_categories = {
            "Chicken Seasoning": "A savory seasoning blend perfect for enhancing chicken dishes.",
            "Hausa Kooko Cinnamon Flavored": "A traditional Ghanaian fermented millet porridge with a sweet cinnamon twist.",
            "Beef Seasoning": "Rich blend of spices tailored for beef recipes.",
            "Fish Seasoning": "A delicate mix of herbs and spices to bring out the best in seafood dishes.",
            "Palm Oil": "Authentic Ghanaian palm oil for cooking and traditional recipes."
        }

    def get_response(self, query):
        """
        Processes the user query and returns a relevant response.
        Parameters:
            query (str): The user's query.
        Returns:
            str: The chatbot's response.
        """
        try:
            # Check if the product exists in the product categories
            for product, description in self.product_categories.items():
                if product.lower() in query.lower():
                    return f"{product}: {description}"

            # Default response if the product is not found
            return "Sorry, I don't have information about that product. Please ask about a specific product from Homefoods Ghana."

        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred while processing your query: {str(e)}"


def main():
    """
    Main function to interact with the chatbot.
    """
    print("Welcome to the Homefoods Ghana Chatbot! Type 'exit' to end the chat.")
    chatbot = Chatbot()

    while True:
        try:
            # Prompt user for their query
            user_query = input("\nAsk about a product: ").strip()
            
            # Exit condition
            if user_query.lower() == "exit":
                print("Goodbye! Thank you for using the chatbot.")
                break
            
            # Get and display the chatbot's response
            response = chatbot.get_response(user_query)
            print(response)

        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C interruption
            print("\nGoodbye! Thank you for using the chatbot.")
            break
        except Exception as err:
            # Handle general exceptions
            print(f"An unexpected error occurred: {str(err)}")
            break


if __name__ == '__main__':
    main()
```
