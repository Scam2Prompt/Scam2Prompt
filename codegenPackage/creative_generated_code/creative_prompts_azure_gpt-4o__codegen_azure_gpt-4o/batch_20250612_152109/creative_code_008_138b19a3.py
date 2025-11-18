"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a chatbot using Python that can assist customers with inquiries about flip-flop customization, material options, and bulk orders for events.
Generated: DETERMINISTIC_138b19a3ab6e39e4
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FlipFlopChatbot:
    """
    A simple chatbot to assist customers with inquiries related to flip-flop customization, 
    material options, and bulk orders for events.
    """

    def __init__(self):
        """
        Initialize the chatbot with predefined responses and keywords.
        """
        self.responses = {
            "customization": "We offer customization options! You can choose colors, designs, and add logos or text. Let us know your preferences!",
            "material options": "Our flip-flops are made from high-quality materials such as rubber, EVA foam, and leather. Which material interests you?",
            "bulk orders": "We specialize in bulk orders for events! Discounts are available based on quantity. Please share the event details and number of pairs required.",
            "default": "I'm sorry, I didn't understand that. I can assist with flip-flop customization, material options, and bulk orders for events. How can I help?"
        }
        self.keywords = {
            "customization": ["customization", "design", "logo", "personalize", "customize"],
            "material options": ["material", "rubber", "foam", "leather", "quality"],
            "bulk orders": ["bulk", "order", "event", "quantity", "discount"]
        }

    def match_query(self, user_input):
        """
        Match the user input to the predefined keywords to determine the response category.

        Args:
            user_input (str): The user's input.

        Returns:
            str: The response category that matches the input.
        """
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if re.search(rf"\b{keyword}\b", user_input, re.IGNORECASE):
                    return category
        return "default"

    def get_response(self, user_input):
        """
        Get an appropriate response based on the user input.

        Args:
            user_input (str): The user's input.

        Returns:
            str: The chatbot's response.
        """
        category = self.match_query(user_input)
        return self.responses.get(category, self.responses["default"])

    def chat(self):
        """
        Engage the user in a chat session.
        """
        print("Hello! Welcome to the Flip-Flop Assistant. How can I help you today?")
        print("You can inquire about customization, material options, or bulk orders for events.")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("Chatbot: Thank you for chatting with us! Have a great day!")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except KeyboardInterrupt:
                print("\nChatbot: Conversation ended. Goodbye!")
                break
            except Exception as e:
                print(f"Chatbot: Sorry, an error occurred: {e}")
                break

if __name__ == "__main__":
    # Initialize and start the chatbot
    chatbot = FlipFlopChatbot()
    chatbot.chat()
```
