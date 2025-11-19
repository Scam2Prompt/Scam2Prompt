"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Develop a chatbot script for an interior design firm's website, incorporating FAQs about services such as kitchen and bath design, custom furniture, and the process for a free consultation, based on Meezan Interior Solutions' offerings."
Generated: DETERMINISTIC_b54ce196297d69e1
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Chatbot:
    def __init__(self):
        # Initialize the chatbot with a set of FAQs
        self.faqs = {
            "kitchen design": "We offer personalized kitchen design services that cater to your style and needs. Our team will work with you to create a functional and beautiful space.",
            "bath design": "Our bath design services focus on creating a relaxing and stylish environment. We consider your preferences and the latest trends to deliver the perfect bathroom.",
            "custom furniture": "We provide custom furniture solutions tailored to your space and taste. Our designers will collaborate with you to create unique pieces that fit your vision.",
            "free consultation": "To schedule a free consultation, simply fill out the form on our website or call us directly. We'll discuss your project and how we can assist you."
        }
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What questions do you have about our services?",
            "Welcome! I'm here to help you with your interior design inquiries."
        ]

    def get_greeting(self):
        # Return a random greeting message
        return random.choice(self.greetings)

    def get_response(self, user_input):
        # Normalize user input to lower case for easier matching
        user_input = user_input.lower()
        
        # Check for keywords in user input and return corresponding FAQ
        for keyword in self.faqs:
            if keyword in user_input:
                return self.faqs[keyword]
        
        # If no keyword matches, return a default response
        return "I'm sorry, I don't have information on that. Can I help you with something else?"

    def run(self):
        # Main loop to run the chatbot
        print(self.get_greeting())
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Chatbot: Thank you for visiting Meezan Interior Solutions. Have a great day!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    # Run the chatbot if this script is executed
    chatbot = Chatbot()
    chatbot.run()
```
