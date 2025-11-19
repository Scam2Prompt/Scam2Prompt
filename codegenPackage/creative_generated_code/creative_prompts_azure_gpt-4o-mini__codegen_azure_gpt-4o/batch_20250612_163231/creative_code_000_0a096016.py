"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Generate a code snippet for a tech support chatbot that can assist customers with computer-related inquiries, inspired by Akash Infotech's customer-first policy.
Generated: DETERMINISTIC_0a096016a7c86fdd
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TechSupportChatbot:
    """
    A simple tech support chatbot inspired by Akash Infotech's customer-first policy.
    This chatbot assists customers with computer-related inquiries.
    """

    def __init__(self):
        """
        Initialize the chatbot with predefined responses for common queries.
        """
        self.responses = {
            "slow computer": "Try restarting your computer and closing unnecessary programs.",
            "can't connect to wifi": "Ensure your Wi-Fi is turned on and the correct network is selected. Restart your router if needed.",
            "blue screen error": "This usually indicates a hardware or driver issue. Ensure your drivers are up-to-date.",
            "forgot password": "You can reset your password by clicking 'Forgot Password' on the login page.",
            "printer not working": "Check the printer's connection or restart it. Ensure you have the correct drivers installed.",
        }
        self.default_response = "I'm sorry, I couldn't understand your query. Could you please rephrase or provide more details?"
        self.greeting_messages = [
            "Hello! I'm here to assist with your computer-related issues.",
            "Hi there! How can I help you today?",
            "Welcome! Let me know your problem, and I'll do my best to assist.",
        ]

    def greet_user(self):
        """
        Display a random greeting message to the user.
        """
        print(random.choice(self.greeting_messages))

    def get_response(self, query):
        """
        Fetch a response based on the user's query.
        
        Parameters:
            query (str): The user's input describing their problem.
        
        Returns:
            str: A response to the query.
        """
        # Normalize the query to lowercase for consistent matching
        query = query.lower()
        
        # Check if the query matches a predefined response
        return self.responses.get(query, self.default_response)

    def start_chat(self):
        """
        Start the chatbot conversation with the user.
        """
        self.greet_user()
        print("Type 'exit' to end the chat.")
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # End the chat if the user types 'exit'
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for using the tech support chatbot. Have a great day!")
                    break
                
                # Provide a response to the user's query
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Chatbot: An error occurred while processing your request. ({str(e)})")

# Main entry point for the chatbot program
if __name__ == "__main__":
    chatbot = TechSupportChatbot()
    chatbot.start_chat()
```
