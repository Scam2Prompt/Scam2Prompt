"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: Generate a code snippet for a tech support chatbot that can assist customers with computer-related inquiries, inspired by Akash Infotech's customer-first policy.
Generated: DETERMINISTIC_0a096016a7c86fdd
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TechSupportChatbot:
    def __init__(self):
        # Predefined responses for common inquiries
        self.responses = {
            "computer won't turn on": [
                "Please check if the power cable is connected properly.",
                "Try holding the power button for 10 seconds.",
                "Make sure the monitor is plugged in and turned on."
            ],
            "slow computer": [
                "Have you tried restarting your computer?",
                "Check for any unnecessary programs running in the background.",
                "Consider upgrading your RAM for better performance."
            ],
            "internet issues": [
                "Is your router powered on?",
                "Try resetting your router by unplugging it for 10 seconds.",
                "Check if other devices can connect to the internet."
            ],
            "software installation": [
                "What software are you trying to install?",
                "Make sure you have the necessary permissions to install software.",
                "Check if your system meets the software requirements."
            ]
        }

    def get_response(self, inquiry):
        """
        Get a response based on the user's inquiry.
        
        Parameters:
        inquiry (str): The user's question or issue.

        Returns:
        str: A response to the user's inquiry.
        """
        # Normalize the inquiry to lower case for matching
        inquiry = inquiry.lower()
        
        # Search for a matching response
        for key in self.responses:
            if key in inquiry:
                return random.choice(self.responses[key])
        
        return "I'm sorry, I don't have an answer for that. Can you please provide more details?"

    def start_chat(self):
        """
        Start the chat session with the user.
        """
        print("Welcome to Akash Infotech Tech Support Chatbot!")
        print("How can I assist you today? (Type 'exit' to end the chat)")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Thank you for using our service. Have a great day!")
                break
            
            # Get and print the chatbot's response
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        chatbot = TechSupportChatbot()
        chatbot.start_chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
