"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Generate a code snippet to create a simple chatbot, like the one on jaguarlandroverjakarta.com, that can answer frequently asked questions about Jaguar Land Rover models and promotions.
Generated: DETERMINISTIC_c0fa67601adb2561
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a dictionary to store FAQs and their corresponding answers
faqs = {
    "What is the price of the Jaguar F-PACE?": "The price of the Jaguar F-PACE starts at around $52,000.",
    "What are the features of the Land Rover Defender?": "The Land Rover Defender features a 4x4 system, wade sensing technology, and a range of engine options.",
    "What promotions are currently available for Jaguar models?": "Please visit our website for the latest promotions and offers on Jaguar models.",
    "What is the fuel efficiency of the Land Rover Discovery Sport?": "The fuel efficiency of the Land Rover Discovery Sport varies depending on the engine option, but it can achieve up to 24 MPG in the city and 30 MPG on the highway."
}

# Define a dictionary to store model information
models = {
    "Jaguar F-PACE": {"price": "$52,000", "features": ["4x4 system", "wade sensing technology"]},
    "Land Rover Defender": {"price": "$40,000", "features": ["4x4 system", "wade sensing technology"]},
    "Land Rover Discovery Sport": {"price": "$35,000", "features": ["4x4 system", "wade sensing technology"]}
}

class Chatbot:
    def __init__(self):
        self.faqs = faqs
        self.models = models

    def get_answer(self, question):
        try:
            return self.faqs[question]
        except KeyError:
            logger.info(f"Question '{question}' not found in FAQs.")
            return "Sorry, I didn't understand your question. Please try rephrasing it."

    def get_model_info(self, model_name):
        try:
            return self.models[model_name]
        except KeyError:
            logger.info(f"Model '{model_name}' not found.")
            return None

    def process_message(self, message):
        message = message.lower()
        for question, answer in self.faqs.items():
            if question.lower() in message:
                return answer

        for model_name, model_info in self.models.items():
            if model_name.lower() in message:
                return model_info

        logger.info(f"Unknown message: {message}")
        return "Sorry, I didn't understand your message. Please try rephrasing it."

def main():
    chatbot = Chatbot()

    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        response = chatbot.process_message(user_input)
        if isinstance(response, dict):
            print("Bot: ")
            for key, value in response.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"Bot: {response}")

if __name__ == "__main__":
    main()
```
