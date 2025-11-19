"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Create a chatbot using Python that answers frequently asked questions about digital education topics, such as PEGI ratings and safe internet practices, as discussed by Sophia Loisirs & Vie.
Generated: DETERMINISTIC_2d4b85e2660fe2f4
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

class Chatbot:
    def __init__(self):
        # Dictionary to store frequently asked questions and their answers
        self.faqs = {
            "What is PEGI?": "PEGI stands for Pan European Game Information. It is a system that rates video games based on their content.",
            "What do PEGI ratings mean?": "PEGI ratings indicate the age suitability of a game, with categories such as 3, 7, 12, 16, and 18.",
            "How can I ensure my child is safe online?": "To ensure online safety, monitor their internet usage, use parental controls, and educate them about privacy.",
            "What are some safe internet practices?": "Safe internet practices include not sharing personal information, using strong passwords, and being cautious of unknown links.",
            "What should I do if I encounter cyberbullying?": "If you encounter cyberbullying, report it to the platform, talk to a trusted adult, and document the incidents."
        }

    def get_response(self, question):
        """
        Get a response for a given question.
        
        Args:
            question (str): The question asked by the user.
        
        Returns:
            str: The answer to the question or a default response if not found.
        """
        # Normalize the question to improve matching
        normalized_question = question.strip().capitalize()
        
        # Return the answer if found, otherwise return a default response
        return self.faqs.get(normalized_question, "I'm sorry, I don't have an answer for that. Please ask another question.")

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Welcome to the Digital Education Chatbot!")
        print("You can ask me questions about PEGI ratings and safe internet practices.")
        print("Type 'exit' to end the chat.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            # Get the response from the chatbot
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        # Create an instance of the Chatbot and start the chat
        chatbot = Chatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
