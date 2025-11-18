"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Create a chatbot script to answer FAQs about investment plans, refunds, and referrals, based on the FAQ section of New World Trade.
Generated: DETERMINISTIC_9e7f3832b8197cfe
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class FAQChatbot:
    def __init__(self, faq_data_file):
        """
        Initializes the chatbot with a set of FAQs loaded from a JSON file.

        :param faq_data_file: Path to the JSON file containing FAQ data.
        """
        self.faqs = self.load_faqs(faq_data_file)

    def load_faqs(self, file_path):
        """
        Loads FAQs from a JSON file.
        
        :param file_path: Path to the JSON file.
        :return: A dictionary of FAQs.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
            return {}

    def get_response(self, question):
        """
        Retrieves a response based on the user's question.

        :param question: The user's question as a string.
        :return: A string with the response or a fallback message.
        """
        for key, responses in self.faqs.items():
            if key.lower() in question.lower():
                return random.choice(responses)
        return "I'm sorry, I don't have an answer for that. Please contact support for assistance."

    def chat(self):
        """
        Starts a chat session with the user, allowing them to ask questions until they decide to exit.
        """
        print("Welcome to the New World Trade FAQ Chatbot! Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using the FAQ Chatbot. Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Replace 'faq_data.json' with the path to your actual FAQ JSON file
    chatbot = FAQChatbot('faq_data.json')
    chatbot.chat()
```

### Sample FAQ JSON Structure (faq_data.json):
```json
{
    "investment plans": [
        "We offer various investment plans tailored to your needs. Please visit our website for more details.",
        "Our investment plans include short-term, medium-term, and long-term options. You can find more information on our investment page."
    ],
    "refunds": [
        "Refund requests can be submitted through our support portal. Please provide your order number.",
        "Our refund policy allows for refunds within 30 days of purchase. Check our refund policy for more details."
    ],
    "referrals": [
        "You can refer a friend by using your unique referral link found in your account dashboard.",
        "For every successful referral, you earn rewards! Check the referral program details in your account."
    ]
}
```
