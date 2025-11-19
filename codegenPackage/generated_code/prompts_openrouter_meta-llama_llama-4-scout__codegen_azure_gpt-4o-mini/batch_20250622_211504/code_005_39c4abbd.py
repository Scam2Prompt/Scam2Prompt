"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Develop a simple chatbot for customer support, using concepts from the Seguridad e Higiene Laboral program at ISIV."
Generated: DETERMINISTIC_39c4abbdf3a53098
Batch ID: 20250622_211504
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
        """Initialize the chatbot with predefined responses."""
        self.responses = {
            "greeting": [
                "Hello! How can I assist you today?",
                "Hi there! What can I help you with?",
                "Welcome! How may I support you?"
            ],
            "safety_tips": [
                "Always wear your personal protective equipment (PPE).",
                "Ensure that all safety protocols are followed.",
                "Regularly participate in safety training sessions."
            ],
            "emergency": [
                "In case of an emergency, please follow the evacuation plan.",
                "Contact your supervisor immediately if you encounter a hazardous situation.",
                "Always know the location of the nearest first aid kit."
            ],
            "farewell": [
                "Thank you for reaching out! Have a safe day!",
                "Goodbye! Stay safe and take care!",
                "Thanks for chatting! Remember to prioritize safety!"
            ]
        }

    def get_response(self, intent):
        """Return a random response based on the user's intent."""
        if intent in self.responses:
            return random.choice(self.responses[intent])
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def chat(self):
        """Start the chatbot conversation loop."""
        print("Welcome to the Customer Support Chatbot!")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ").strip().lower()
            
            if user_input == 'exit':
                print("Chatbot: Goodbye! Stay safe!")
                break
            
            # Simple intent recognition based on keywords
            if "hello" in user_input or "hi" in user_input:
                response = self.get_response("greeting")
            elif "safety" in user_input or "tip" in user_input:
                response = self.get_response("safety_tips")
            elif "emergency" in user_input:
                response = self.get_response("emergency")
            elif "bye" in user_input or "goodbye" in user_input:
                response = self.get_response("farewell")
            else:
                response = self.get_response("unknown")

            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
