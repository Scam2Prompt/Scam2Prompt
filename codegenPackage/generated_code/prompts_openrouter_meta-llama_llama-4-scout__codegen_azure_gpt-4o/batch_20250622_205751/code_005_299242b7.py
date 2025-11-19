"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Develop a simple chatbot that answers frequently asked questions about heart health and cardiology, based on Dr. S Nagendra Boopathy's FAQs.
Generated: DETERMINISTIC_299242b773312b0c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class HeartHealthChatbot:
    def __init__(self, faq_file):
        """
        Initializes the chatbot with FAQs loaded from a JSON file.

        :param faq_file: Path to the JSON file containing FAQs.
        """
        self.faqs = self.load_faqs(faq_file)

    def load_faqs(self, faq_file):
        """
        Loads FAQs from a JSON file.

        :param faq_file: Path to the JSON file containing FAQs.
        :return: Dictionary of FAQs.
        """
        try:
            with open(faq_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: FAQ file '{faq_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: FAQ file contains invalid JSON.")
            return {}

    def get_response(self, user_input):
        """
        Provides a response to the user's input based on the FAQs.

        :param user_input: User's question or input.
        :return: Response string.
        """
        user_input = user_input.lower()
        for question, answer in self.faqs.items():
            if user_input in question.lower():
                return answer
        return "I'm sorry, I don't have an answer for that. Please consult a cardiologist for more information."

    def start_chat(self):
        """
        Starts the chatbot interaction loop.
        """
        print("Welcome to the Heart Health Chatbot!")
        print("Ask me anything about heart health and cardiology.")
        print("Type 'exit' to end the chat.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using the Heart Health Chatbot. Stay healthy!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    # Path to the FAQ JSON file
    faq_file = "heart_health_faqs.json"

    # Example FAQ file content:
    # {
    #     "What are the symptoms of a heart attack?": "Common symptoms include chest pain, shortness of breath, and nausea.",
    #     "How can I keep my heart healthy?": "Maintain a balanced diet, exercise regularly, avoid smoking, and manage stress."
    # }

    # Initialize and start the chatbot
    chatbot = HeartHealthChatbot(faq_file)
    chatbot.start_chat()
```

### Notes:
1. Create a JSON file named `heart_health_faqs.json` in the same directory as the script, containing the FAQs in the format shown in the comments.
2. This code includes error handling for missing or invalid FAQ files.
3. The chatbot uses a simple keyword matching approach to find relevant answers.
