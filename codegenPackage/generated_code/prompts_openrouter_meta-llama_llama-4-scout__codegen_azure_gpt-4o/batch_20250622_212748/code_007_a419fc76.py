"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Develop a simple chatbot that can provide information about CNU's online programs and admission process."
Generated: DETERMINISTIC_a419fc76ad77cfd4
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class Chatbot:
    def __init__(self):
        # Initialize chatbot with predefined responses
        self.responses = {
            "online programs": "CNU offers a variety of online programs including Computer Science, Business Administration, and Nursing. Visit our website for more details.",
            "admission process": "The admission process at CNU involves submitting an online application, transcripts, and meeting program-specific requirements. Check our admissions page for more information.",
            "contact": "You can contact CNU's admissions office at admissions@cnu.edu or call (123) 456-7890.",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase your question?"
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.
        :param user_input: str - The input message from the user.
        :return: str - The chatbot's response.
        """
        try:
            # Normalize user input to lowercase for matching
            user_input = user_input.lower()

            # Check for keywords in user input and return corresponding response
            if re.search(r"\bonline programs\b", user_input):
                return self.responses["online programs"]
            elif re.search(r"\badmission process\b", user_input):
                return self.responses["admission process"]
            elif re.search(r"\bcontact\b", user_input):
                return self.responses["contact"]
            else:
                return self.responses["default"]
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the CNU Chatbot! Ask me about online programs, the admission process, or how to contact us.")
    chatbot = Chatbot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")

            # Exit the chatbot if the user types 'exit'
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for chatting with me! Goodbye!")
                break

            # Get chatbot response and display it
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nChatbot: Thank you for chatting with me! Goodbye!")
            break

# Entry point for the script
if __name__ == "__main__":
    main()
```
