"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Develop a chatbot using Python that can answer FAQs about RM’s initiatives, such as the Khud Kafeel project, Food ATM, and psychological health services.
Generated: DETERMINISTIC_3f1b7ae82d5c0407
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RMChatbot:
    def __init__(self, faq_data):
        """
        Initialize the chatbot with FAQ data.

        :param faq_data: Dictionary containing FAQs and their answers.
        """
        self.faq_data = faq_data

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.

        :param user_input: String input from the user.
        :return: String response from the chatbot.
        """
        user_input = user_input.lower().strip()
        for question, answer in self.faq_data.items():
            if user_input in question.lower():
                return answer
        return "I'm sorry, I couldn't find an answer to your question. Please try rephrasing or ask about a different topic."

def load_faq_data(file_path):
    """
    Load FAQ data from a JSON file.

    :param file_path: Path to the JSON file containing FAQs.
    :return: Dictionary of FAQs and answers.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: FAQ file not found. Please provide a valid file path.")
        return {}
    except json.JSONDecodeError:
        print("Error: FAQ file is not a valid JSON. Please check the file content.")
        return {}

def main():
    """
    Main function to run the chatbot.
    """
    faq_file_path = "faq_data.json"  # Replace with your path to the FAQ JSON file
    faq_data = load_faq_data(faq_file_path)

    # Check if FAQ data is loaded successfully
    if not faq_data:
        print("Unable to load FAQ data. Exiting chatbot.")
        return

    chatbot = RMChatbot(faq_data)

    print("Welcome to the RM Initiatives Chatbot! Type 'exit' to end the conversation.")
    print("You can ask about initiatives like Khud Kafeel, Food ATM, and psychological health services.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for using the RM Initiatives Chatbot. Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```

**Sample `faq_data.json`**
```json
{
  "What is Khud Kafeel?": "Khud Kafeel is an initiative aimed at empowering individuals to become self-reliant by offering skill development programs and resources.",
  "What is the Food ATM project?": "The Food ATM project provides meals to those in need, ensuring no one goes hungry.",
  "What psychological health services does RM offer?": "RM offers counseling, therapy sessions, and support groups to help individuals maintain their psychological health."
}
```
