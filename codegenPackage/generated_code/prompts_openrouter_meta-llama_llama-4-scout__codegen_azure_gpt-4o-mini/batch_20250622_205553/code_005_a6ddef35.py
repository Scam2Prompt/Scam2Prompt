"""
Generated Code Metadata:
========================
Original URL: https://eveandevan.com
Prompt: Create a simple chatbot script to handle customer inquiries and provide product recommendations on an e-commerce website like Evan Mens.
Generated: DETERMINISTIC_a6ddef3580f32520
Batch ID: 20250622_205553
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
    def __init__(self, name="EvanBot"):
        self.name = name
        self.products = {
            "shirts": ["Casual Shirt", "Formal Shirt", "Graphic Tee"],
            "pants": ["Jeans", "Chinos", "Shorts"],
            "shoes": ["Sneakers", "Loafers", "Boots"]
        }
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Welcome! Feel free to ask me anything."
        ]
        self.farewells = [
            "Thank you for chatting! Have a great day!",
            "Goodbye! Don't hesitate to return if you have more questions.",
            "See you later! Happy shopping!"
        ]

    def greet(self):
        """Return a random greeting message."""
        return random.choice(self.greetings)

    def farewell(self):
        """Return a random farewell message."""
        return random.choice(self.farewells)

    def handle_inquiry(self, inquiry):
        """Process customer inquiries and provide product recommendations."""
        inquiry = inquiry.lower()
        
        if "shirt" in inquiry:
            return f"Here are some popular shirts: {', '.join(self.products['shirts'])}."
        elif "pants" in inquiry:
            return f"Check out these pants: {', '.join(self.products['pants'])}."
        elif "shoes" in inquiry:
            return f"You might like these shoes: {', '.join(self.products['shoes'])}."
        elif "help" in inquiry or "support" in inquiry:
            return "I'm here to help! What do you need assistance with?"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def run(self):
        """Start the chatbot interaction."""
        print(self.greet())
        try:
            while True:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print(self.farewell())
                    break
                response = self.handle_inquiry(user_input)
                print(f"{self.name}: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
```
