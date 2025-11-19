"""
Generated Code Metadata:
========================
Original URL: https://bengonbase-xyz.pages.dev
Prompt: Write a code snippet in a programming language of your choice to create a simple chatbot that answers frequently asked questions about $BENG token, such as "What chain is $BENG on?" and "Why does $BENG look like Pepe?".
Generated: DETERMINISTIC_39f09d1ca17676bd
Batch ID: 20250622_210802
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
        # Dictionary to store frequently asked questions and their answers
        self.faqs = {
            "What chain is $BENG on?": "The $BENG token is built on the Ethereum blockchain.",
            "Why does $BENG look like Pepe?": "The $BENG token features Pepe as a mascot to represent its fun and community-driven nature.",
            "What is the purpose of $BENG?": "The $BENG token aims to foster a vibrant community and support various charitable initiatives.",
            "How can I buy $BENG?": "You can buy $BENG on various decentralized exchanges like Uniswap or through supported wallets.",
            "Is $BENG a good investment?": "As with any investment, please do your own research and consider the risks involved."
        }

    def get_response(self, question):
        """
        Get the response for a given question.
        
        Args:
            question (str): The question asked by the user.
        
        Returns:
            str: The answer to the question or a default response if the question is not found.
        """
        # Normalize the question to improve matching
        normalized_question = question.strip().capitalize()
        
        # Return the answer if the question exists in the FAQs
        if normalized_question in self.faqs:
            return self.faqs[normalized_question]
        else:
            return "I'm sorry, I don't have an answer for that question. Please try asking something else."

    def chat(self):
        """
        Start a simple chat loop with the user.
        """
        print("Welcome to the $BENG FAQ Chatbot! Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            # Get the response from the chatbot
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Create an instance of the Chatbot and start chatting
    try:
        bot = Chatbot()
        bot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
