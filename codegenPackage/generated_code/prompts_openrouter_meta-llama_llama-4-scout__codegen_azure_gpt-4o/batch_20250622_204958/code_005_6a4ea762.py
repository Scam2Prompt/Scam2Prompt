"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Develop a chatbot script in Python that can answer common questions about handyman services in Wellington, such as availability and pricing.
Generated: DETERMINISTIC_6a4ea76233399546
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class HandymanChatbot:
    """
    A chatbot for answering common questions about handyman services in Wellington.
    """

    def __init__(self):
        # Predefined responses for common questions
        self.responses = {
            "availability": "Our handyman services are available Monday to Saturday, 8 AM to 6 PM.",
            "pricing": "Our pricing starts at $50 per hour, depending on the type of service required.",
            "services": "We offer plumbing, electrical work, carpentry, painting, and general repairs.",
            "location": "We operate in Wellington and surrounding suburbs.",
            "contact": "You can contact us at 0800-HANDYMAN or email us at info@handymanwellington.co.nz."
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.
        :param user_input: str - The user's question or statement.
        :return: str - The chatbot's response.
        """
        # Normalize user input to lowercase for easier matching
        user_input = user_input.lower()

        # Match user input to predefined keywords
        if re.search(r"\bavailability\b", user_input):
            return self.responses["availability"]
        elif re.search(r"\bpricing\b|\bcost\b|\brate\b", user_input):
            return self.responses["pricing"]
        elif re.search(r"\bservices\b|\boffer\b", user_input):
            return self.responses["services"]
        elif re.search(r"\blocation\b|\barea\b", user_input):
            return self.responses["location"]
        elif re.search(r"\bcontact\b|\bphone\b|\bemail\b", user_input):
            return self.responses["contact"]
        else:
            return "I'm sorry, I didn't understand your question. Could you please rephrase?"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Wellington Handyman Services Chatbot!")
    print("Ask me about our availability, pricing, services, location, or contact information.")
    print("Type 'exit' to end the chat.\n")

    chatbot = HandymanChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for chatting with us! Have a great day!")
                break
            
            # Get chatbot response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
