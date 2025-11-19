"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Develop a chatbot script for a law firm specializing in family law and criminal law that provides initial guidance on divorce, adoption, or child custody, referencing Majeli Avocat's approach to personalized legal advice.
Generated: DETERMINISTIC_1502884b47ecac5e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class LawFirmChatbot:
    def __init__(self, firm_name):
        self.firm_name = firm_name
        self.responses = {
            "divorce": [
                "Divorce can be a complex process. It's important to understand your rights and options. Would you like to schedule a consultation?",
                "In a divorce, issues such as asset division and child custody are crucial. How can I assist you further?"
            ],
            "adoption": [
                "Adoption is a wonderful way to build a family. There are various types of adoption processes. Would you like more information?",
                "Each adoption case is unique. Please share your situation so I can provide tailored guidance."
            ],
            "child custody": [
                "Child custody arrangements can be challenging. It's essential to prioritize the child's best interests. How can I help you?",
                "Understanding the different types of custody is key. Would you like to discuss your specific case?"
            ]
        }

    def get_response(self, topic):
        """Fetch a random response based on the topic provided."""
        try:
            if topic in self.responses:
                return random.choice(self.responses[topic])
            else:
                raise ValueError("Invalid topic. Please choose from 'divorce', 'adoption', or 'child custody'.")
        except ValueError as e:
            return str(e)

    def start_chat(self):
        """Initiate the chat with the user."""
        print(f"Welcome to {self.firm_name} Chatbot!")
        print("I can provide guidance on the following topics: divorce, adoption, child custody.")
        
        while True:
            user_input = input("Please enter a topic or type 'exit' to end the chat: ").strip().lower()
            if user_input == 'exit':
                print("Thank you for chatting with us. Have a great day!")
                break
            
            response = self.get_response(user_input)
            print(response)

if __name__ == "__main__":
    # Create an instance of the chatbot for Majeli Avocat
    chatbot = LawFirmChatbot("Majeli Avocat")
    # Start the chat
    chatbot.start_chat()
```
