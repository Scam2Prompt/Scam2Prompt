"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Create a chatbot that provides hearing aid support, including cleaning instructions and battery replacement guidance, inspired by Otex's support section.
Generated: DETERMINISTIC_1ee1b98765b80e56
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class HearingAidChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined responses."""
        self.intro_messages = [
            "Hello! I'm here to assist you with hearing aid support.",
            "Hi there! Need help with your hearing aid? Ask me anything!",
            "Welcome! I can provide guidance on cleaning and battery replacement for your hearing aids."
        ]
        self.cleaning_instructions = (
            "To clean your hearing aids, follow these steps:\n"
            "1. Remove the hearing aid from your ear.\n"
            "2. Use a soft, dry cloth to wipe the outer surface.\n"
            "3. For deeper cleaning, use a small brush to clean the microphone and receiver openings.\n"
            "4. Avoid using water or cleaning solutions.\n"
            "5. Regularly inspect wax guards and replace if necessary."
        )
        self.battery_replacement_guidance = (
            "Here are the steps to replace the battery in your hearing aid:\n"
            "1. Locate the battery compartment on your hearing aid.\n"
            "2. Open the compartment gently.\n"
            "3. Remove the old battery, making sure to handle it carefully.\n"
            "4. Take a new battery and ensure the '+' symbol is facing the correct way.\n"
            "5. Insert the new battery and close the compartment.\n"
            "6. Dispose of the old battery properly."
        )

    def get_intro_message(self):
        """Return a random introduction message."""
        return random.choice(self.intro_messages)

    def handle_query(self, user_input):
        """Handle user input and return appropriate responses."""
        user_input = user_input.lower()
        
        if "clean" in user_input or "cleaning" in user_input:
            return self.cleaning_instructions
        elif "battery" in user_input or "replace" in user_input:
            return self.battery_replacement_guidance
        elif "help" in user_input or "support" in user_input:
            return "What specific assistance do you need regarding your hearing aid?"
        else:
            return "I'm sorry, I didn't understand that. I can help with cleaning instructions or battery replacement."

    def run_chatbot(self):
        """Run the chatbot to interact with the user."""
        print(self.get_intro_message())
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            response = self.handle_query(user_input)
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    try:
        chatbot = HearingAidChatbot()
        chatbot.run_chatbot()
    except Exception as e:
        print(f"An error occurred: {e}")
```
