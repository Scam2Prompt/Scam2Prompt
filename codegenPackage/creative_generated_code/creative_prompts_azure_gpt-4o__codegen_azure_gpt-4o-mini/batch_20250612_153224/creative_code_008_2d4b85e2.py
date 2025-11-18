"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Create a chatbot using Python that answers frequently asked questions about digital education topics, such as PEGI ratings and safe internet practices, as discussed by Sophia Loisirs & Vie.
Generated: DETERMINISTIC_2d4b85e2660fe2f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class Chatbot:
    """A simple chatbot that answers frequently asked questions about digital education topics."""

    def __init__(self, faq_file):
        """Initialize the chatbot with FAQs from a JSON file."""
        self.faq_data = self.load_faqs(faq_file)
    
    def load_faqs(self, faq_file):
        """Load FAQs from a JSON file."""
        try:
            with open(faq_file, 'r') as file:
                faqs = json.load(file)
            return faqs
        except FileNotFoundError:
            print("Error: FAQ file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in FAQ file.")
            return {}

    def get_response(self, question):
        """Return a response based on the user's question."""
        question = question.lower()
        for item in self.faq_data.get("faqs", []):
            if question in item["questions"]:
                return random.choice(item["answers"])
        return "I'm sorry, I don't have an answer for that question."

    def start_chat(self):
        """Start the chat session with the user."""
        print("Welcome to the Digital Education Chatbot!")
        print("Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Instantiate the chatbot with the path to the FAQ JSON file
    chatbot = Chatbot('faqs.json')
    chatbot.start_chat()
```

**Sample `faqs.json` File Content:**
```json
{
    "faqs": [
        {
            "questions": ["what is pegi?", "explain pegi ratings"],
            "answers": [
                "PEGI stands for Pan-European Game Information. It is a system that rates video games based on their content.",
                "PEGI ratings help consumers understand the suitability of games for different age groups."
            ]
        },
        {
            "questions": ["what are safe internet practices?", "how to stay safe online?"],
            "answers": [
                "Always use strong passwords and change them regularly.",
                "Be cautious about sharing personal information online."
            ]
        }
    ]
}
``` 

**Usage:**
1. Create a `faqs.json` file with the provided content.
2. Run the chatbot Python script, and it will load the FAQs and allow users to ask questions.
