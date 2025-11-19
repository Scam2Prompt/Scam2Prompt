"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: "Develop a chatbot to answer common questions about renting properties in Bucaramanga based on Dominguez Parra's FAQs."
Generated: DETERMINISTIC_49e3b20df023b2fd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class PropertyRentalChatbot:
    def __init__(self, faq_file):
        """
        Initialize the chatbot with FAQs loaded from a JSON file.
        
        :param faq_file: Path to the JSON file containing FAQs.
        """
        self.faq_data = self.load_faqs(faq_file)

    def load_faqs(self, faq_file):
        """
        Load FAQs from a JSON file.
        
        :param faq_file: Path to the JSON file containing FAQs.
        :return: Dictionary containing FAQs.
        """
        try:
            with open(faq_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: FAQ file '{faq_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: FAQ file '{faq_file}' contains invalid JSON.")
            return {}

    def get_response(self, user_input):
        """
        Get a response based on user input by matching it to FAQs.
        
        :param user_input: The user's question or input.
        :return: A response string.
        """
        user_input = user_input.lower()
        for question, answer in self.faq_data.items():
            if user_input in question.lower():
                return answer
        return "I'm sorry, I couldn't find an answer to your question. Please try rephrasing or ask something else."

    def start_chat(self):
        """
        Start the chatbot interaction loop.
        """
        print("Welcome to the Bucaramanga Property Rental Chatbot!")
        print("Ask me anything about renting properties in Bucaramanga.")
        print("Type 'exit' to end the chat.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using the chatbot. Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    # Path to the FAQ JSON file
    faq_file_path = "dominguez_parra_faqs.json"

    # Example FAQ file structure:
    # {
    #     "What are the requirements to rent a property?": "You need a valid ID, proof of income, and a security deposit.",
    #     "Are pets allowed in rental properties?": "It depends on the property. Please check with the landlord.",
    #     "What is the average rental price in Bucaramanga?": "The average rental price varies between $500,000 and $1,500,000 COP depending on the location and property size."
    # }

    chatbot = PropertyRentalChatbot(faq_file_path)
    chatbot.start_chat()
```

### Notes:
- Ensure the `dominguez_parra_faqs.json` file exists in the same directory as the script or provide the correct path.
- The JSON file should contain FAQs in the format: `{ "question": "answer", ... }`.
- This code includes error handling for file operations and JSON parsing.
