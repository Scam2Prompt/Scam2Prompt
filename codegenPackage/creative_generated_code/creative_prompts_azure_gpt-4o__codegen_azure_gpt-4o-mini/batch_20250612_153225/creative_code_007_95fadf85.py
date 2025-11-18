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

class Chatbot:
    def __init__(self):
        """Initialize the chatbot with predefined responses."""
        self.responses = {
            'customization': [
                "We offer a variety of customization options including colors, sizes, and logos.",
                "You can customize your uniform by choosing from our available styles and adding your logo.",
                "Customization allows you to express your brand identity through our uniform designs."
            ],
            'pricing': [
                "Our pricing varies based on the type of uniform and customization options selected. Please provide more details.",
                "For a precise quote, let us know the quantity and specific customizations you're interested in.",
                "Pricing typically starts at $50 per uniform, but discounts may apply for bulk orders."
            ],
            'delivery': [
                "Delivery times depend on your location and the complexity of the order. Generally, it takes 2-4 weeks.",
                "We aim to dispatch all orders within 10 business days, but custom orders may take longer.",
                "Please provide your location and order details for a more accurate delivery estimate."
            ],
            'default': [
                "I'm sorry, I didn't understand that. Can you please rephrase your question?",
                "Could you please specify what you're inquiring about regarding our uniforms?",
                "If you could clarify your question, I'd be happy to assist you!"
            ]
        }

    def respond_to_inquiry(self, inquiry):
        """Generate a response based on the customer's inquiry."""
        inquiry_lower = inquiry.lower()
        
        if 'customization' in inquiry_lower:
            return random.choice(self.responses['customization'])
        elif 'pricing' in inquiry_lower:
            return random.choice(self.responses['pricing'])
        elif 'delivery' in inquiry_lower:
            return random.choice(self.responses['delivery'])
        else:
            return random.choice(self.responses['default'])

def main():
    """Main function to run the chatbot interaction."""
    chatbot = Chatbot()
    
    print("Welcome to the Real Garment Customer Service Chatbot!")
    print("You can ask about customization, pricing, or delivery timelines.")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Chatbot: Thank you for reaching out! Have a great day!")
                break
            
            response = chatbot.respond_to_inquiry(user_input)
            print(f"Chatbot: {response}")
    
    except KeyboardInterrupt:
        print("\nChatbot: Thank you for reaching out! Have a great day!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
