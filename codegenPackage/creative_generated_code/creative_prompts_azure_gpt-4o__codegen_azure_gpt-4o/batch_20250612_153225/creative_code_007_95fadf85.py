"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Create a chatbot script to handle customer inquiries about uniform customization, pricing, and delivery timelines, inspired by Real Garment's customer service approach.
Generated: DETERMINISTIC_95fadf859bca991f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class Chatbot:
    def __init__(self):
        # Predefined responses for each type of inquiry
        self.responses = {
            "uniform_customization": [
                "We offer a variety of customization options including fabric, color, and embroidery. What specific details are you looking for?",
                "You can choose from our catalog or provide your own design for customization. Would you like to see examples?"
            ],
            "pricing": [
                "Pricing depends on the type of customization and the quantity. Could you let me know the number of uniforms you need?",
                "Our prices are competitive and transparent. Can you provide more details about your requirements to get an accurate quote?"
            ],
            "delivery_timelines": [
                "Delivery timelines depend on the complexity of customization and order size. Typically, it takes 2-4 weeks. How soon do you need the uniforms?",
                "We work hard to meet your deadlines. Can you let us know your required delivery date?"
            ],
            "fallback": [
                "I'm sorry, I didn't quite understand that. Could you rephrase your question?",
                "Can you provide more details so I can assist you better?"
            ]
        }

    def get_response(self, inquiry_type):
        """
        Return a random response based on the inquiry type.
        :param inquiry_type: Type of inquiry (uniform_customization, pricing, delivery_timelines)
        :return: Random response string
        """
        if inquiry_type in self.responses:
            return random.choice(self.responses[inquiry_type])
        else:
            return random.choice(self.responses["fallback"])

def handle_customer_inquiry():
    """
    Main function to handle customer inquiries via chatbot.
    """
    chatbot = Chatbot()
    print("Welcome to Real Garment's Customer Service Chatbot!")
    print("How can I assist you today?")
    print("Options: uniform_customization, pricing, delivery_timelines")

    try:
        while True:
            inquiry = input("\nEnter your inquiry type (or type 'exit' to quit): ").strip().lower()
            
            if inquiry == 'exit':
                print("Thank you for chatting with us. Have a great day!")
                break
            elif inquiry in ["uniform_customization", "pricing", "delivery_timelines"]:
                response = chatbot.get_response(inquiry)
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm sorry, I didn't understand that. Please choose a valid inquiry type.")
    except KeyboardInterrupt:
        print("\nChatbot: Session ended. Thank you for using our service!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Chatbot: Please try again later.")

if __name__ == "__main__":
    handle_customer_inquiry()
```
