"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Develop a chatbot using Python that can answer customer queries about Akash Infotech's computer products and services.
Generated: DETERMINISTIC_da57748bcec37b48
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ChatBot:
    """
    A simple chatbot for answering customer queries about Akash Infotech's computer products and services.
    """

    def __init__(self):
        """
        Initializes the chatbot with predefined responses.
        """
        self.responses = {
            "products": [
                "We offer a wide range of computers, laptops, and accessories.",
                "Our product range includes gaming PCs, business laptops, and peripherals.",
                "You can find details about our products on our website under the 'Products' section."
            ],
            "services": [
                "We provide computer repair, software installation, and IT consulting services.",
                "Our services include hardware upgrades, virus removal, and cloud solutions.",
                "For detailed information, visit the 'Services' page on our website."
            ],
            "pricing": [
                "Our prices vary depending on the product or service. Please check our website for the latest pricing.",
                "You can contact our sales team for a customized quote.",
                "We offer competitive pricing and seasonal discounts on selected items."
            ],
            "contact": [
                "You can reach us at support@akashinfotech.com or call us at +1-800-123-4567.",
                "Our customer support team is available Monday to Friday, 9 AM to 6 PM.",
                "Feel free to use the contact form on our website for inquiries."
            ],
            "default": [
                "I'm sorry, I didn't understand that. Could you please rephrase your query?",
                "I'm here to help! Please ask about our products, services, pricing, or contact details.",
                "Could you clarify your question? I'd like to assist you better."
            ]
        }

    def get_response(self, user_input):
        """
        Returns a response based on the user's input.

        :param user_input: str, the customer's query
        :return: str, an appropriate response
        """
        # Normalize user input by converting to lowercase
        user_input = user_input.lower()

        # Match user input to predefined categories
        if "product" in user_input or "computer" in user_input or "laptop" in user_input:
            response_category = "products"
        elif "service" in user_input or "repair" in user_input or "consulting" in user_input:
            response_category = "services"
        elif "price" in user_input or "cost" in user_input or "quote" in user_input:
            response_category = "pricing"
        elif "contact" in user_input or "support" in user_input or "reach" in user_input:
            response_category = "contact"
        else:
            response_category = "default"

        # Return a random response from the matched category
        return random.choice(self.responses[response_category])


def main():
    """
    Main function to interact with the chatbot.
    """
    print("Welcome to Akash Infotech ChatBot! How can I assist you today?")
    chatbot = ChatBot()

    try:
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Exit condition
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("ChatBot: Thank you for visiting Akash Infotech. Have a great day!")
                break

            # Get response from the chatbot
            response = chatbot.get_response(user_input)
            print(f"ChatBot: {response}")
    except KeyboardInterrupt:
        print("\nChatBot: Goodbye! Feel free to reach out anytime.")
    except Exception as e:
        print(f"\nChatBot: Sorry, something went wrong. Error: {e}")


if __name__ == "__main__":
    main()
```
