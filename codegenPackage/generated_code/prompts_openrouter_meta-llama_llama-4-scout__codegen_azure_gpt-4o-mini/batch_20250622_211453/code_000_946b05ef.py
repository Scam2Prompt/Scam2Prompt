"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Write a Python script to create a simple chatbot that offers emotional support and connects users with therapists, incorporating the principles of Bioneuroemoción and EMDR therapy.
Generated: DETERMINISTIC_946b05ef1bf2edb1
Batch ID: 20250622_211453
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
        self.responses = {
            "greeting": [
                "Hello! I'm here to offer you emotional support.",
                "Hi there! How can I assist you today?",
                "Welcome! I'm here to listen and help."
            ],
            "emotional_support": [
                "It's okay to feel this way. Can you tell me more about what's on your mind?",
                "I'm here for you. What emotions are you experiencing right now?",
                "Remember, it's important to express your feelings. What would you like to share?"
            ],
            "therapy_options": [
                "I can connect you with a therapist. Would you like to proceed?",
                "Therapy can be very helpful. Would you like to know more about available therapists?",
                "Connecting with a therapist can be a great step. Shall I help you with that?"
            ],
            "goodbye": [
                "Take care! Remember, I'm here whenever you need support.",
                "Goodbye! Don't hesitate to reach out if you need someone to talk to.",
                "Wishing you well! I'm just a message away if you need me."
            ]
        }

    def get_response(self, intent):
        """Fetch a random response based on the user's intent."""
        return random.choice(self.responses.get(intent, ["I'm not sure how to respond to that."]))

    def handle_user_input(self, user_input):
        """Process user input and determine the appropriate response."""
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            return self.get_response("greeting")
        elif "feel" in user_input or "emotion" in user_input:
            return self.get_response("emotional_support")
        elif "therapist" in user_input or "help" in user_input:
            return self.get_response("therapy_options")
        elif "bye" in user_input or "exit" in user_input:
            return self.get_response("goodbye")
        else:
            return "I'm here to help. Can you tell me more about what you're feeling?"

def main():
    """Main function to run the chatbot."""
    chatbot = Chatbot()
    print("Welcome to the Emotional Support Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "bye"]:
                print("Chatbot:", chatbot.get_response("goodbye"))
                break
            
            response = chatbot.handle_user_input(user_input)
            print("Chatbot:", response)
        
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
```
