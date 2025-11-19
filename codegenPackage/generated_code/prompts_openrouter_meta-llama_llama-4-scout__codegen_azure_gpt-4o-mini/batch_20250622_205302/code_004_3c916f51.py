"""
Generated Code Metadata:
========================
Original URL: https://etherkan.com
Prompt: Develop a simple chatbot that provides basic support and answers frequently asked questions (FAQs) related to VSport's services, such as football coaching, fitness courses, and sports psychology.
Generated: DETERMINISTIC_3c916f5165eb791e
Batch ID: 20250622_205302
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
        """Initialize the chatbot with a set of FAQs."""
        self.faqs = {
            "football coaching": "Our football coaching program offers personalized training sessions for all skill levels. You can sign up on our website.",
            "fitness courses": "We provide a variety of fitness courses, including yoga, pilates, and high-intensity interval training (HIIT). Check our schedule for more details.",
            "sports psychology": "Our sports psychology services help athletes improve their mental game through one-on-one sessions and workshops.",
            "contact": "You can contact us via email at support@vsport.com or call us at (123) 456-7890.",
            "hours": "We are open Monday to Friday from 9 AM to 6 PM and Saturday from 10 AM to 4 PM."
        }

    def get_response(self, user_input):
        """Return a response based on user input."""
        user_input = user_input.lower()
        
        # Check for a matching FAQ
        for key in self.faqs:
            if key in user_input:
                return self.faqs[key]
        
        return "I'm sorry, I don't have information on that. Please ask about our football coaching, fitness courses, or sports psychology."

    def chat(self):
        """Start the chat session with the user."""
        print("Welcome to VSport Chatbot! How can I assist you today?")
        print("Type 'exit' to end the chat.")
        
        while True:
            try:
                user_input = input("You: ")
                
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting with us! Have a great day!")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    # Run the chatbot
    chatbot = Chatbot()
    chatbot.chat()
```
