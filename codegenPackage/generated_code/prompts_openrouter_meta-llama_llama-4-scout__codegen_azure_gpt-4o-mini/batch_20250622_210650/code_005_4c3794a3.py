"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Generate a Python code snippet to create a simple chatbot that answers frequently asked questions about hair transplantation, such as "Is the procedure painful?" or "How long does it take to recover?"
Generated: DETERMINISTIC_4c3794a3bc11b740
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HairTransplantChatbot:
    def __init__(self):
        # Dictionary to store frequently asked questions and their answers
        self.faqs = {
            "Is the procedure painful?": "Most patients report minimal discomfort during the procedure, as local anesthesia is used.",
            "How long does it take to recover?": "Recovery time varies, but most people can return to normal activities within a week.",
            "What is hair transplantation?": "Hair transplantation is a surgical procedure that moves hair follicles from a donor site to a balding or thinning area.",
            "Are the results permanent?": "Yes, the results are generally permanent, as the transplanted hair follicles are resistant to balding.",
            "How much does it cost?": "The cost can vary widely depending on the clinic and the extent of the procedure, typically ranging from $4,000 to $15,000."
        }

    def get_response(self, question):
        """
        Get a response for a given question.
        
        :param question: str - The question asked by the user.
        :return: str - The answer to the question or a default response if not found.
        """
        # Normalize the question to improve matching
        normalized_question = question.strip().capitalize()
        
        # Return the answer if the question is in the FAQs, else return a default response
        return self.faqs.get(normalized_question, "I'm sorry, I don't have an answer for that question.")

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Welcome to the Hair Transplant Chatbot! Ask me anything about hair transplantation.")
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
    # Create an instance of the chatbot and start the chat
    try:
        chatbot = HairTransplantChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
