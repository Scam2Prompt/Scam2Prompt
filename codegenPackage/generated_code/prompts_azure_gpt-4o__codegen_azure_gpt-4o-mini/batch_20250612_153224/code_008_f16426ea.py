"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Create a chatbot that educates users on ethical AI practices in journalism, referencing Jusoor International's Geneva seminar.
Generated: DETERMINISTIC_f16426eadcedf37b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EthicalAIChatbot:
    """
    A chatbot that educates users on ethical AI practices in journalism,
    referencing Jusoor International's Geneva seminar.
    """

    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello! I'm here to help you learn about ethical AI practices in journalism.",
                "Hi there! Let's discuss ethical AI in journalism."
            ],
            "seminar": [
                "The Jusoor International seminar in Geneva focused on the importance of ethical AI in journalism.",
                "At the Geneva seminar, experts discussed how AI can be used responsibly in journalism."
            ],
            "ethical_practices": [
                "Ethical AI practices include transparency, accountability, and fairness.",
                "It's crucial to ensure that AI systems do not perpetuate biases in journalism."
            ],
            "resources": [
                "You can find more information on ethical AI practices in journalism on various academic websites.",
                "Consider checking out publications from the Geneva seminar for in-depth insights."
            ],
            "default": [
                "I'm sorry, I didn't quite understand that. Can you ask me something else?",
                "Could you please rephrase your question?"
            ]
        }

    def get_response(self, user_input):
        """
        Get a response based on user input.

        Args:
            user_input (str): The input from the user.

        Returns:
            str: A response from the chatbot.
        """
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.responses["greeting"])
        elif "seminar" in user_input:
            return random.choice(self.responses["seminar"])
        elif "ethical" in user_input or "practice" in user_input:
            return random.choice(self.responses["ethical_practices"])
        elif "resources" in user_input:
            return random.choice(self.responses["resources"])
        else:
            return random.choice(self.responses["default"])

    def run(self):
        """
        Run the chatbot in a loop, allowing user interaction until they choose to exit.
        """
        print("Welcome to the Ethical AI Chatbot! Type 'exit' to end the conversation.")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = EthicalAIChatbot()
    chatbot.run()
```
