"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Develop a simple chatbot to provide basic support and answer frequently asked questions about י.א. אינסטלציה's services and operating hours.
Generated: DETERMINISTIC_53567a917f4c3ea4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class PlumbingChatbot:
    """
    A simple chatbot to provide basic support and answer frequently asked questions
    about י.א. אינסטלציה's services and operating hours.
    """

    def __init__(self):
        # Define a dictionary of FAQs and their answers
        self.faqs = {
            "services": "We offer plumbing services including pipe repair, leak detection, and installation of fixtures.",
            "hours": "Our operating hours are Sunday to Thursday, 8:00 AM to 6:00 PM.",
            "emergency": "Yes, we provide 24/7 emergency plumbing services. Call us at 123-456-7890.",
            "location": "We are located at 123 Main Street, Tel Aviv.",
            "contact": "You can contact us at 123-456-7890 or email us at info@ya-plumbing.com."
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: The chatbot's response.
        """
        # Normalize user input to lowercase for case-insensitive matching
        user_input = user_input.lower()

        # Check for keywords in the user's input and respond accordingly
        if re.search(r"\bservices\b", user_input):
            return self.faqs["services"]
        elif re.search(r"\bhours\b|\bopen\b|\bclose\b", user_input):
            return self.faqs["hours"]
        elif re.search(r"\bemergency\b", user_input):
            return self.faqs["emergency"]
        elif re.search(r"\blocation\b|\baddress\b", user_input):
            return self.faqs["location"]
        elif re.search(r"\bcontact\b|\bphone\b|\bemail\b", user_input):
            return self.faqs["contact"]
        else:
            return "I'm sorry, I didn't understand your question. Can you please rephrase?"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to י.א. אינסטלציה's support chatbot!")
    print("Type 'exit' to end the conversation.\n")

    chatbot = PlumbingChatbot()

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the chat if the user types 'exit'
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break

        # Get the chatbot's response
        response = chatbot.get_response(user_input)

        # Print the response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```
