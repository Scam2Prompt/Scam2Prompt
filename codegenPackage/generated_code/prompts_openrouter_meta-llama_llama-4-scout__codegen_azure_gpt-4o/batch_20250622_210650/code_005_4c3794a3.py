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
        # Dictionary to store FAQs and their answers
        self.faqs = {
            "Is the procedure painful?": "Hair transplantation is generally performed under local anesthesia, so the procedure itself is not painful. Some discomfort may occur during recovery.",
            "How long does it take to recover?": "Recovery time varies, but most people can return to work within 1-2 days. Full healing and hair growth may take several months.",
            "Are the results permanent?": "Yes, hair transplantation results are typically permanent as the transplanted hair is resistant to hair loss.",
            "What is the cost of hair transplantation?": "The cost depends on various factors such as the clinic, location, and the extent of the procedure. It's best to consult a specialist for an accurate estimate.",
            "Are there any side effects?": "Side effects are usually minimal, including swelling, redness, or mild discomfort. Serious complications are rare."
        }
        # Default response for unrecognized questions
        self.default_response = "I'm sorry, I don't have information on that. Please consult a specialist for more details."

    def get_response(self, question):
        """
        Fetches a response for the given question.
        If the question is not recognized, returns a default response.
        """
        return self.faqs.get(question, self.default_response)

    def chat(self):
        """
        Starts a simple chatbot session where the user can ask questions.
        """
        print("Welcome to the Hair Transplant Chatbot!")
        print("You can ask me questions like:")
        print(" - Is the procedure painful?")
        print(" - How long does it take to recover?")
        print("Type 'exit' to end the chat.\n")

        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Exit condition
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break
                
                # Fetch and display the response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Chatbot: An error occurred: {e}. Please try again.")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = HairTransplantChatbot()
    chatbot.chat()
```
