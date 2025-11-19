"""
Generated Code Metadata:
========================
Original URL: https://dappimport.com
Prompt: Generate a code snippet to create a simple chatbot that provides customer support for an online store like Dapp Imports, handling queries about product availability, shipping, and contact information.
Generated: DETERMINISTIC_b52a1f7b219c294e
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class Chatbot:
    def __init__(self):
        # Predefined responses for common queries
        self.responses = {
            "product_availability": "Our products are available for purchase online. Please visit our website to check the availability of specific items.",
            "shipping_info": "We offer worldwide shipping. Delivery times and costs depend on your location. You can find more details on our shipping policy page.",
            "contact_info": "You can contact us via email at support@dappimports.com or call us at +1-800-555-1234 during business hours."
        }

    def handle_query(self, query):
        """
        Handles customer queries by matching keywords and providing appropriate responses.
        :param query: str - The customer's query
        :return: str - The chatbot's response
        """
        # Normalize the query to lowercase for easier matching
        query = query.lower()

        # Check for keywords in the query and respond accordingly
        if re.search(r'\b(product|availability|stock)\b', query):
            return self.responses["product_availability"]
        elif re.search(r'\b(shipping|delivery|ship)\b', query):
            return self.responses["shipping_info"]
        elif re.search(r'\b(contact|email|phone|support)\b', query):
            return self.responses["contact_info"]
        else:
            return "I'm sorry, I couldn't understand your query. Could you please rephrase or provide more details?"

def main():
    """
    Main function to simulate chatbot interaction with a user.
    """
    print("Welcome to Dapp Imports Customer Support Chatbot!")
    print("Type 'exit' to end the chat.\n")

    chatbot = Chatbot()

    while True:
        # Get user input
        user_query = input("You: ")

        # Exit condition
        if user_query.lower() == 'exit':
            print("Chatbot: Thank you for chatting with us. Have a great day!")
            break

        # Get chatbot response
        try:
            response = chatbot.handle_query(user_query)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: An error occurred while processing your query. Please try again later. (Error: {e})")

# Entry point for the script
if __name__ == "__main__":
    main()
```
