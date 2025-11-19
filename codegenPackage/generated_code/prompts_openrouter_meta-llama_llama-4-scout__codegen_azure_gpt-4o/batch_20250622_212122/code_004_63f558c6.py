"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop a chatbot script to handle wholesale inquiries for kitchen utensils, similar to Varejão das Louças' atacado services.
Generated: DETERMINISTIC_63f558c607d0e022
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class WholesaleChatbot:
    def __init__(self):
        """
        Initialize the chatbot with predefined responses and supported actions.
        """
        self.responses = {
            "greeting": "Hello! Welcome to our wholesale kitchen utensils service. How can I assist you today?",
            "product_inquiry": "We offer a wide range of kitchen utensils including pots, pans, cutlery, and more. What specific items are you looking for?",
            "pricing_inquiry": "Our pricing depends on the quantity and type of items. Please provide more details about your requirements.",
            "minimum_order": "Our minimum order quantity is 50 units per item. Let me know if you'd like to proceed.",
            "order_process": "To place an order, please provide your company details, the items you need, and the quantities. We will send you a quote shortly.",
            "thank_you": "Thank you for reaching out! If you have further questions, feel free to ask.",
            "fallback": "I'm sorry, I didn't understand that. Could you please rephrase your question?"
        }

    def handle_message(self, message):
        """
        Process the user's message and return an appropriate response.
        
        Args:
            message (str): The user's input message.
        
        Returns:
            str: The chatbot's response.
        """
        # Normalize the message to lowercase for easier matching
        message = message.lower()

        # Check for keywords in the message and respond accordingly
        if re.search(r"\bhello\b|\bhi\b|\bhey\b", message):
            return self.responses["greeting"]
        elif re.search(r"\bproduct\b|\bitems\b|\bkitchen\b|\butensils\b", message):
            return self.responses["product_inquiry"]
        elif re.search(r"\bprice\b|\bcost\b|\bpricing\b", message):
            return self.responses["pricing_inquiry"]
        elif re.search(r"\bminimum\b|\border\b|\bquantity\b", message):
            return self.responses["minimum_order"]
        elif re.search(r"\bhow\b|\bplace\b|\border\b", message):
            return self.responses["order_process"]
        elif re.search(r"\bthank\b|\bthanks\b", message):
            return self.responses["thank_you"]
        else:
            return self.responses["fallback"]

def main():
    """
    Main function to run the chatbot in a loop for user interaction.
    """
    print("Wholesale Chatbot is now running. Type 'exit' to quit.")
    chatbot = WholesaleChatbot()

    while True:
        try:
            # Get user input
            user_message = input("You: ")
            
            # Exit condition
            if user_message.lower() == "exit":
                print("Chatbot: Goodbye! Have a great day!")
                break
            
            # Get chatbot response
            response = chatbot.handle_message(user_message)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
