"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Develop a chatbot using Python that answers frequently asked questions about elderly care services, referencing specific details from Home Care Assistance Barrie's FAQs section.
Generated: DETERMINISTIC_c4f62ca30a6fe0b9
Batch ID: 20250612_152020
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

class ElderlyCareChatbot:
    def __init__(self, faq_data):
        """
        Initialize the chatbot with FAQ data.

        Args:
            faq_data (dict): A dictionary containing FAQs and their answers.
        """
        self.faq_data = faq_data

    def get_answer(self, question):
        """
        Get the answer to a specific question.

        Args:
            question (str): The question asked by the user.

        Returns:
            str: The answer to the question if found, otherwise a default message.
        """
        for faq in self.faq_data:
            if question.lower() in faq['question'].lower():
                return faq['answer']
        return "Sorry, I couldn't find an answer to that question."

    def display_faqs(self):
        """
        Display all FAQs and their answers.
        """
        for faq in self.faq_data:
            print(f"Q: {faq['question']}")
            print(f"A: {faq['answer']}\n")


def load_faq_data(filename):
    """
    Load FAQ data from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: A dictionary containing FAQs and their answers.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def main():
    # Load FAQ data from JSON file
    faq_data = load_faq_data('faqs.json')

    # Create a chatbot instance
    chatbot = ElderlyCareChatbot(faq_data)

    # Display chatbot menu
    while True:
        print("Elderly Care Chatbot")
        print("1. Ask a question")
        print("2. Display all FAQs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            question = input("Enter your question: ")
            print(chatbot.get_answer(question))
        elif choice == '2':
            chatbot.display_faqs()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

**faqs.json**
```json
[
    {
        "question": "What services do you offer?",
        "answer": "We offer a range of services including personal care, medication management, and light housekeeping."
    },
    {
        "question": "How do I schedule care?",
        "answer": "You can schedule care by contacting us directly or through our website."
    },
    {
        "question": "What areas do you serve?",
        "answer": "We serve Barrie and surrounding areas."
    }
]
```
