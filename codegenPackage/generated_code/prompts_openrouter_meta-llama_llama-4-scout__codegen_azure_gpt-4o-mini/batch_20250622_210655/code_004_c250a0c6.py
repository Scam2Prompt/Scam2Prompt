"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Create a chatbot that answers frequently asked questions about Cartório Justiniano's services, such as the cost of a union stable in Manaus and the required documents.
Generated: DETERMINISTIC_c250a0c663054cc4
Batch ID: 20250622_210655
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
            "cost_union_stable": "The cost of a union stable in Manaus varies. Please contact us for the most accurate pricing.",
            "required_documents": "The required documents for a union stable include: 1. Identification documents (RG, CPF) 2. Proof of residence 3. Birth certificates.",
            "operating_hours": "Our operating hours are Monday to Friday, from 8 AM to 5 PM.",
            "contact_info": "You can contact us at (92) 1234-5678 or visit our website at www.cartoriojustiniano.com."
        }
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What questions do you have about our services?",
            "Welcome! I'm here to help you with your inquiries."
        ]

    def greet_user(self):
        # Greet the user with a random greeting
        return random.choice(self.greetings)

    def get_response(self, question):
        # Provide a response based on the user's question
        question = question.lower()
        if "cost" in question and "union stable" in question:
            return self.faqs["cost_union_stable"]
        elif "documents" in question or "required" in question:
            return self.faqs["required_documents"]
        elif "hours" in question or "operating" in question:
            return self.faqs["operating_hours"]
        elif "contact" in question:
            return self.faqs["contact_info"]
        else:
            return "I'm sorry, I don't have the information you're looking for. Please ask another question."

    def run(self):
        # Main loop to run the chatbot
        print(self.greet_user())
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the chatbot application
    chatbot = Chatbot()
    chatbot.run()
```
